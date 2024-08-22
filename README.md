# Computation Ramsey Numbers

## Building

```bash
git submodule update --recursive --init
mkdir build
cmake -S . -B build/
cd build
make
```

## Clique / Independent-Set

The most common type of Ramsey Number represented as $n = R(k,l)$.

* $n$ - The graph order
* $k$ - The clique order
* $l$ - The independant set order

Finds any graphs of order $n$ that doesn't have either a clique of size $k$ or an independent set of size $l$.

### Running

```bash
cd build
make
./ramnum-cis $n $k $l
```

### Output

The program will output the result of the computation in the following format

`n, k, l, graph_id, graph_bitstring`

* `graph_id` - The numeric identifier unique to a graph of a specified size
* `graph_bitstring` - The upper triangular adjacency matrix concatenated to form a binary string
