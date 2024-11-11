from matplotlib.ticker import LogLocator
import matplotlib.pyplot as plt
import seaborn as sns
import polars as pl
import numpy as np

from scipy.optimize import curve_fit
from scipy.stats import t    

linear_high_df = pl.read_csv("./results/classical_cis_linear_ramsey_high_results.csv")
linear_low_df = pl.read_csv("./results/classical_cis_linear_ramsey_low_results.csv")
linear_df = pl.concat([linear_high_df, linear_low_df]).with_columns(pl.lit("Linear").alias("Algorithm"))

bintree_high_df = pl.read_csv("./results/classical_cis_bintree_ramsey_high_results.csv")
bintree_low_df = pl.read_csv("./results/classical_cis_bintree_ramsey_low_results.csv")
bintree_df = pl.concat([bintree_high_df, bintree_low_df]).with_columns(pl.lit("Bintree").alias("Algorithm"))

rbt_high_df = pl.read_csv("./results/classical_cis_reduced_bintree_ramsey_high_results.csv")
rbt_low_df = pl.read_csv("./results/classical_cis_reduced_bintree_ramsey_low_results.csv")
rbt_df = pl.concat([rbt_high_df, rbt_low_df]).with_columns(pl.lit("Reduced-Bintree").alias("Algorithm"))

algorithms_df = pl.concat([
    linear_df, bintree_df, rbt_df
]).group_by("Graph Order", "Clique Order", "ISet Order", "Algorithm").agg(
    pl.col("Duration (s)").mean(),
).sort("Clique Order", "ISet Order", "Graph Order")


with sns.axes_style("whitegrid"):
    fig, axes = plt.subplots(ncols=3, figsize=(15,5))

reg_params = []
def reg_curve(x, a, b, c):
    return a * x**2 + b * x + c

for i, alg in enumerate(["Linear", "Bintree", "Reduced-Bintree"]):
    filtered_algorithms = algorithms_df.filter(pl.col("Algorithm") == alg)
    min_k = filtered_algorithms.min().item(row=0, column="Clique Order")
    max_k = filtered_algorithms.max().item(row=0, column="Clique Order")

    # _ = sns.scatterplot(
    #     filtered_algorithms.to_pandas(), 
    #     x="Graph Order", 
    #     y="Duration (s)", 
    #     hue=filtered_algorithms.to_pandas()[["Clique Order", "ISet Order"]].apply(tuple, axis=1),
    #     palette="Set2",
    #     sizes=(75,75),
    #     ax=axes[i],
    #     legend=False
    # )

    for j, k in enumerate(range(min_k, max_k + 1)):
        slice_df = filtered_algorithms.filter(pl.col("Clique Order") == k)
        x = np.array(pl.Series(slice_df.select(pl.col("Graph Order"))).to_list())
        y = np.array(pl.Series(slice_df.select(pl.col("Duration (s)"))).to_list())

        params, covariance = curve_fit(reg_curve, x, np.log2(y))
        variance = np.diag(covariance) 
        std_error = np.sqrt(variance)

        test_x = np.arange(1, 20)
        pred_y_log2 = reg_curve(test_x, *params)
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

        sns.set_style("whitegrid")

        axes[i].plot(test_x, pred_y, c=sns.color_palette("Set2")[j], linestyle="dashed", linewidth=2, label=f'({k}, {k})')
        axes[i].fill_between(test_x, lower_bound, upper_bound, color=sns.color_palette("Set2")[j], alpha=0.2)
        axes[i].set_title(r'$2^{n^2}$ regression of ' + alg)
        axes[i].set_ylabel("Duration (s)")
        axes[i].set_xlabel("Graph Order")
        axes[i].set_yscale('log')
        axes[i].set_xticks(test_x[::5])
        axes[i].yaxis.set_major_locator(LogLocator(base=10.0, numticks=10))  # Adjust `numticks` as needed
        axes[i].set_ylim(10e-7, 10e56)
        legend= axes[i].legend(title="(k,l)")
        frame = legend.get_frame()
        reg_params.append(params)

plt.savefig('results/visualizations/cis_algorithm_regressions.pdf')
projected_runtime_seconds = 2**reg_curve(43, *reg_params[-1]) + 2**reg_curve(44, *reg_params[-1]) +2**reg_curve(45, *reg_params[-1]) +2**reg_curve(46, *reg_params[-1])
projected_runtime_centuries = projected_runtime_seconds / 3_155_696_200

print(f"R(5,5) execution time: {projected_runtime_seconds} seconds")
print(f"R(5,5) execution time: {projected_runtime_centuries} centuries")
print(f"R(5,5) parallel execution time on {1e9:.2f} processors: {projected_runtime_centuries / 1e9} centuries")