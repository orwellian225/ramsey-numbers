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


ax_r33 = sns.scatterplot(algorithms_df.filter(pl.col("Clique Order") == 3), x="Graph Order", y="Duration (s)", palette="Set2", hue="Algorithm", legend=False, ax=axes[0])
_ = sns.lineplot(algorithms_df.filter(pl.col("Clique Order") == 3), x="Graph Order", y="Duration (s)", palette="Set2", hue="Algorithm", legend=True, ax=axes[0], estimator='mean')
ax_r33.legend(loc='upper left')
ax_r33.set_yscale('log')
ax_r33.set_title(r"Runtime performance for $R(3,3)$")
ax_r33.yaxis.set_major_locator(LogLocator(base=10.0, numticks=10))  # Adjust `numticks` as needed
ax_r33.set_ylim(10e-5, 10e4)

ax_r44 = sns.scatterplot(algorithms_df.filter(pl.col("Clique Order") == 4), x="Graph Order", y="Duration (s)", palette="Set2", hue="Algorithm", legend=False, ax=axes[1])
_ = sns.lineplot(algorithms_df.filter(pl.col("Clique Order") == 4), x="Graph Order", y="Duration (s)", palette="Set2", hue="Algorithm", legend=True, ax=axes[1], estimator='mean')
ax_r44.legend(loc='upper left')
ax_r44.set_yscale('log')
ax_r44.set_title(r"Runtime performance for $R(4,4)$")
ax_r44.yaxis.set_major_locator(LogLocator(base=10.0, numticks=10))  # Adjust `numticks` as needed
ax_r44.set_ylim(10e-5, 10e4)

ax_r55 = sns.scatterplot(algorithms_df.filter(pl.col("Clique Order") == 5), x="Graph Order", y="Duration (s)", palette="Set2", hue="Algorithm", legend=False, ax=axes[2])
_ = sns.lineplot(algorithms_df.filter(pl.col("Clique Order") == 5), x="Graph Order", y="Duration (s)", palette="Set2", hue="Algorithm", legend=True, ax=axes[2], estimator='mean')
ax_r55.legend(loc='upper left')
ax_r55.set_yscale('log')
ax_r55.set_title(r"Runtime performance for $R(5,5)$")
ax_r55.yaxis.set_major_locator(LogLocator(base=10.0, numticks=10))  # Adjust `numticks` as needed
ax_r55.set_ylim(10e-5, 10e4)

# plt.show()
# Generating an algorithm comparison across the different cases
plt.savefig('results/visualizations/cis_case_runtimes.pdf')
plt.close()

