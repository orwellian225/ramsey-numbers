#!/bin/bash
#SBATCH --job-name=Classical-CIS-Ramsey
#SBATCH --output=./results/classical_cis_ramsey_results.csv
#SBATCH -p
#SBATCH -N 1 ## Number of nodes
#SPATCH -n 4 ## Number of cores per node

test_graph_orders=(2 3 4 5 6 7 8 9 10)
test_clique_order=3
test_iset_order=3


if [ ! -d ./results ]; then
    mkdir -p ./results
fi

if [ ! -f ./results/classical_cis_ramsey_results.csv ]; then
    touch ./results/classical_cis_ramsey_results.csv
    echo "Graph Order,Clique Order,ISet Order,Graph ID,Graph Bitstring,Duration (s)" > ./results/classical_cis_ramsey_results.csv
fi

# 0 -> num_tests - 1
for i in {0..8};
do
    echo "test" $i":" ${test_graph_orders[$i]} "?= R("${test_clique_order}","${test_iset_order}")"
    ./build/ramnum-cis ${test_graph_orders[$i]} ${test_clique_order} ${test_iset_order} | tee -a ./results/classical_cis_ramsey_results.csv
done
