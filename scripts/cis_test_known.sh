#!/bin/sh

echo "Computing Known CIS Ramsey Numbers for testing purposes"
echo "n, k, l, graph_id, graph_bitstring"

./build/ramnum-cis 1 2 2
./build/ramnum-cis 2 2 2

./build/ramnum-cis 2 2 3
./build/ramnum-cis 3 2 3

./build/ramnum-cis 3 2 4
./build/ramnum-cis 4 2 4

./build/ramnum-cis 4 2 5
./build/ramnum-cis 5 2 5

./build/ramnum-cis 5 3 3
./build/ramnum-cis 6 3 3

# ./build/ramnum-cis 8 3 4
# ./build/ramnum-cis 9 3 4
#
# ./build/ramnum-cis 13 3 5
# ./build/ramnum-cis 14 3 5
