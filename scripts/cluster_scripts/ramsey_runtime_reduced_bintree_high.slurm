#!/bin/bash
#SBATCH --job-name=ram-rbt
#SBATCH --output=./results/runtime/reduced_bintree_output.txt
#SBATCH -p stampede
#SBATCH -N 1 ## Number of nodes
#SPATCH -n 1 ## Number of cores per node

if [ ! -d ./results ]; then
    mkdir -p ./results
fi

if [ ! -f ./results/classical_cis_reduced_bintree_ramsey_results.csv ]; then
    touch ./results/classical_cis_reduced_bintree_ramsey_results.csv
    echo "Graph Order,Clique Order,ISet Order,Graph ID,Graph Bitstring,Duration (s)" > ./results/classical_cis_reduced_bintree_ramsey_results.csv
fi

for n in {8..10};
do
    for t in {1..5};
    do
        for i in {3..5};
        do
            echo "trail" $t":" $n "?= R("${i}","${i}")"
            ./build/cis_reduced_bintree $n $i $i
        done
    done
done