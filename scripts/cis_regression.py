import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import polars as pl
import numpy as np 

from scipy.optimize import curve_fit
from scipy.special import comb
from scipy.stats import t    

mpl.rcParams['text.color'] = 'white'
mpl.rcParams['axes.labelcolor'] = 'white'
mpl.rcParams['xtick.color'] = 'white' 
mpl.rcParams['axes.edgecolor'] = 'white' 
mpl.rcParams['ytick.color'] = 'white'

df_schema = { 
    "Graph Order": pl.Int64, 
    "Clique Order": pl.Int64, 
    "ISet Order": pl.Int64,
    "Graph ID": pl.String,
    "Graph Bitstring": pl.String,
    "Duration (s)": pl.Float64
}

df_33 = pl.read_csv(
    "./results/classical_cis_ramsey_results_33.csv",
    schema=df_schema
)
df_44 = pl.read_csv(
    "./results/classical_cis_ramsey_results_44.csv",
    schema=df_schema
)
df_55 = pl.read_csv(
    "./results/classical_cis_ramsey_results_55.csv",
    schema=df_schema
)

df = pl.concat([df_33, df_44, df_55])

mean_df = df.group_by("Graph Order", "Clique Order", "ISet Order").agg(
    pl.col("Duration (s)").mean(),
).sort("Clique Order", "ISet Order", "Graph Order")

ax = sns.scatterplot(
    df.to_pandas(), 
    x="Graph Order", 
    y="Duration (s)", 
    hue=df.to_pandas()[["Clique Order", "ISet Order"]].apply(tuple, axis=1),
    palette="Set2",
    sizes=(75,75)
)


regression_params = []
def curve(x, a, b, c):
    return a * x**2 + b * x + c

for i, (k,l) in enumerate([(i, i) for i in range(3,6)]):
    mean_df_slice = mean_df.filter((pl.col("ISet Order") == k) & (pl.col("Clique Order") == l))
    x = np.array(pl.Series(mean_df_slice.select(pl.col("Graph Order"))).to_list())
    y = np.array(pl.Series(mean_df_slice.select(pl.col("Duration (s)"))).to_list())

    params, covariance = curve_fit(curve, x, np.log2(y))
    variance = np.diag(covariance) 
    std_error = np.sqrt(variance)

    test_x = np.arange(3, 13)
    pred_y_log2 = curve(test_x, *params)
    pred_y = 2**pred_y_log2

    alpha = 0.01 # confidence interval
    n = len(y)
    p = len(params)
    dof = max(0, n - p)  # degrees of freedom
    t_value = t.ppf(1.0 - alpha / 2., dof)

    lower_bound_log2 = pred_y_log2 - t_value * std_error[0]
    upper_bound_log2 = pred_y_log2 + t_value * std_error[0]
    lower_bound = 2 ** lower_bound_log2
    upper_bound = 2 ** upper_bound_log2

    ax.plot(test_x, pred_y, c=sns.color_palette("Set2")[i], linestyle="dashed", linewidth=2)
    ax.fill_between(test_x, lower_bound, upper_bound, color=sns.color_palette("Set2")[i], alpha=0.2)
    regression_params.append(params)

ax.patch.set_facecolor('#1b1b1b')
legend= ax.legend(title="(k,l)")
frame = legend.get_frame()
frame.set_facecolor('#1b1b1b')
ax.set_title("Duration vs Graph Order")
ax.set_yscale('log')

print("R(5,5) in centuries:", np.sum(2**curve(np.array([43, 44, 45, 46]), *regression_params[2])) * 3.171e-10)
print("R(6,6) in centuries:", np.sum(2**curve(np.arange(102, 161), *regression_params[2]) * 3.171e-10))

plt.gcf().patch.set_facecolor('#1b1b1b')
plt.tight_layout()
plt.savefig("./results/visualizations/cis_runtime.pdf")
plt.close()

plt.plot(np.arange(1, 47), 2**curve(np.arange(1, 47), *regression_params[2]) * 3.171e-10, color=sns.color_palette("Set2")[2], linewidth=2)
plt.gcf().patch.set_facecolor('#1b1b1b')
plt.gca().patch.set_facecolor('#1b1b1b')
plt.yscale("log")
plt.ylabel(r'number of centuries')
plt.xlabel(r'$n$')
plt.title(r'Regression Curve of $R(5,5)$')
plt.savefig('results/visualizations/r55_regression.pdf')