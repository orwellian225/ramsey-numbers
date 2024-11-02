#pragma once

#include "graph.h"

Graph *find_graph_without_subgraphs(size_t n, Graph& F, Graph& H);
Graph *linear_ramsey(size_t n, Graph& F, Graph& H);
Graph *bintree_ramsey(size_t n, Graph& F, Graph& H);
Graph *reduced_bintree_ramsey(size_t, Graph& F, Graph& H);
