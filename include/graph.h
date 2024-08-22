#pragma once

#include "matrix.h"

struct Graph {
    size_t order;
    Matrix matrix;

    static Graph unfinished(size_t n);
    static Graph *heap_unfinished(size_t n);

    static Graph complete(size_t n);
    static Graph empty(size_t n);

    void print() const;
    bool has_subgraph(const Graph& H);

    Graph *clone();
};
