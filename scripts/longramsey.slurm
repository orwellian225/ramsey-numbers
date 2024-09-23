#!/bin/bash
#SBATCH --job-name=Classical-CIS-Ramsey
#SBATCH --output=./results/classical_cis_ramsey_results.csv
#SBATCH -p
#SBATCH -N 1 ## Number of nodes
#SPATCH -n 4 ## Number of cores per node

# num_tests=14
# test_graph_orders=(5 6 7 13 14 15 17 18 19 36 37 38 39 40)
# test_clique_orders=(3 3 3 3 3 3 4 4 4 4 4 4 4 4)
# test_iset_orders=(3 3 3 5 5 5 4 4 4 6 6 6 6 6)
#
num_tests=1
test_graph_orders=(5 6)
test_clique_orders=(3 3)
test_iset_orders=(3 3)

if [ ! -d ./results ]; then
    mkdir -p ./results
fi

if [ ! -d ./results/classical_cis_ramsey_results.csv ]; then
    touch ./results/classical_cis_ramsey_results.csv
    echo "Graph Order, Clique Order, ISet Order, Graph ID, Graph Bitstring, Duration (s)" > ./results/classical_cis_ramsey_results.csv
fi

# 0 -> num_tests - 1
for i in {0..1};
do
    echo "test" $i":" ${test_graph_orders[$i]} "?= R("${test_clique_orders[$i]}","${test_iset_orders[$i]}")"
    ./build/ramnum-cis ${test_graph_orders[$i]} ${test_clique_orders[$i]} ${test_iset_orders[$i]} | tee -a ./results/classical_cis_ramsey_results.csv
done
