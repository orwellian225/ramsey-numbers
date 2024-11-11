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

temp_rbt_df = rbt_df.rename({"Duration (s)": "RBT Duration"})
temp_bt_df = bintree_df.rename({"Duration (s)": "BT Duration"})

joined_df = temp_rbt_df.join(temp_bt_df, on=["Graph Order", "Clique Order", "ISet Order"], how="inner", )

difference_df = joined_df.select(
    pl.col("Graph Order"),
    pl.col("Clique Order"),
    pl.col("ISet Order"),
    (pl.col("BT Duration") - pl.col("RBT Duration")).alias(r"Duration Difference")
)

sns.set_style("whitegrid")

ax = sns.scatterplot(
    difference_df.to_pandas(), 
    x="Graph Order", 
    y=r'Duration Difference', 
    palette="Set2", 
    hue=difference_df.to_pandas()[["Clique Order", "ISet Order"]].apply(tuple, axis=1),
    legend=False
)
_ = sns.lineplot(
    difference_df.to_pandas(),
    x="Graph Order",
    y=r'Duration Difference',
    palette="Set2", 
    hue=difference_df.to_pandas()[["Clique Order", "ISet Order"]].apply(tuple, axis=1),
    legend=True, 
    ax=ax, 
    estimator='mean'
)
ax.set_title(f"Runtime difference of Binary-Tree and Reduced-Binary-Tree")
ax.set_yscale('log')
legend= ax.legend(title="(k,l)")
frame = legend.get_frame()

plt.savefig('results/visualizations/cis_runtime_difference.pdf')