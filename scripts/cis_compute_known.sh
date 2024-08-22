#!/bin/sh

echo "Computing Known CIS Ramsey Numbers for testing purposes"
echo "n, k, l, graph_id, graph_bitstring" > ./results/cis_results.csv

echo "R(2,2)"
echo "* n = 1"
./build/ramnum-cis 1 2 2 >> ./results/cis_results.csv
echo "* n = 2"
./build/ramnum-cis 2 2 2 >> ./results/cis_results.csv

echo "R(2,3)"
echo "* n = 2"
./build/ramnum-cis 2 2 3 >> ./results/cis_results.csv
echo "* n = 3"
./build/ramnum-cis 3 2 3 >> ./results/cis_results.csv

echo "R(2,4)"
echo "* n = 3"
./build/ramnum-cis 3 2 4 >> ./results/cis_results.csv
echo "* n = 4"
./build/ramnum-cis 4 2 4 >> ./results/cis_results.csv

echo "R(2,5)"
echo "* n = 4"
./build/ramnum-cis 4 2 5 >> ./results/cis_results.csv
echo "* n = 5"
./build/ramnum-cis 5 2 5 >> ./results/cis_results.csv

echo "R(3,3)"
echo "* n = 5"
./build/ramnum-cis 5 3 3 >> ./results/cis_results.csv
echo "* n = 6"
./build/ramnum-cis 6 3 3 >> ./results/cis_results.csv

echo "R(3,4)"
echo "* n = 8"
./build/ramnum-cis 8 3 4 >> ./results/cis_results.csv
echo "* n = 9"
./build/ramnum-cis 9 3 4 >> ./results/cis_results.csv

echo "R(3,5)"
echo "* n = 13"
./build/ramnum-cis 13 3 5 >> ./results/cis_results.csv
echo "* n = 14"
./build/ramnum-cis 14 3 5 >> ./results/cis_results.csv
