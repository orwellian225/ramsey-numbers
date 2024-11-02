#!/bin/bash
#SBATCH --job-name=rh-bt
#SBATCH --output=./results/runtime/bintree_high_output.txt
#SBATCH -p stampede
#SBATCH -N 1 ## Number of nodes
#SPATCH -n 1 ## Number of cores per node

if [ ! -d ./results ]; then
    mkdir -p ./results
fi

if [ ! -f ./results/classical_cis_bintree_ramsey_high_results.csv ]; then
    touch ./results/classical_cis_bintree_ramsey_high_results.csv
    echo "Graph Order,Clique Order,ISet Order,Graph ID,Graph Bitstring,Duration (s)" > ./results/classical_cis_bintree_ramsey_high_results.csv
fi

for n in {8..10};
do
    for t in {1..5};
    do
        for i in {3..5};
        do
            echo "trail" $t":" $n "?= R("${i}","${i}")"
            ./build/cis_bintree $n $i $i | tee -a ./results/classical_cis_bintree_ramsey_high_results.csv
        done
    done
done