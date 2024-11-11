from matplotlib.ticker import LogLocator
import matplotlib.pyplot as plt
import seaborn as sns
import polars as pl

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
])

with sns.axes_style("whitegrid"):
    fig, axes = plt.subplots(ncols=3, figsize=(15,5))

for i, alg in enumerate(["Linear", "Bintree", "Reduced-Bintree"]):
    filtered_algorithms = algorithms_df.filter(pl.col("Algorithm") == alg)
    _ = sns.scatterplot(
        filtered_algorithms.to_pandas(), 
        x="Graph Order", 
        y="Duration (s)", 
        palette="Set2", 
        hue=filtered_algorithms.to_pandas()[["Clique Order", "ISet Order"]].apply(tuple, axis=1),
        legend=False,
        ax=axes[i]
    )
    _ = sns.lineplot(
        filtered_algorithms.to_pandas(),
        x="Graph Order",
        y="Duration (s)",
        palette="Set2", 
        hue=filtered_algorithms.to_pandas()[["Clique Order", "ISet Order"]].apply(tuple, axis=1),
        legend=True, 
        ax=axes[i], 
        estimator='mean'
    )
    axes[i].set_title(f"Runtime performance of {alg}")
    axes[i].set_yscale('log')
    legend = axes[i].legend(title="(k,l)", loc='upper left')
    axes[i].yaxis.set_major_locator(LogLocator(base=10.0, numticks=10))  # Adjust `numticks` as needed
    axes[i].set_ylim(10e-5, 10e4)
    frame = legend.get_frame()

plt.savefig('results/visualizations/cis_algorithm_runtime.pdf')
plt.close()

