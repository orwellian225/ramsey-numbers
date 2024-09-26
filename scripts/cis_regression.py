import matplotlib.pyplot as plt
import seaborn as sns
import polars as pl

df = pl.read_csv(
    "./results/classical_cis_ramsey_results.csv",
    schema={ 
        "Graph Order": pl.Int64, 
        "Clique Order": pl.Int64, 
        "ISet Order": pl.Int64,
        "Graph ID": pl.String,
        "Graph Bitstring": pl.String,
        "Duration (s)": pl.Float64
    }
)

ax = sns.scatterplot(
    df.to_pandas(), 
    x="Graph Order", 
    y="Duration (s)", 
    hue=df.to_pandas()[["Clique Order", "ISet Order"]].apply(tuple, axis=1),
    palette="Set2"
)
ax.set_title("Duration vs Graph Order")
ax.set_yscale("log")

plt.savefig("./results/visualizations/cis_runtime.pdf")
