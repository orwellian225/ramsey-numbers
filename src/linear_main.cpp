#include <fmt/core.h>

#include "graph.h"
#include "ramsey.h"

int main(int argc, char **argv) {
    Graph test = Graph::complete(4);
    Graph test_sub_a = Graph::empty(3);
    Graph test_sub_b = Graph::complete(3);

    test.matrix[{1, 2}] = 0;
    test.matrix[{1, 3}] = 0;
    test.matrix[{2, 1}] = 0;
    test.matrix[{3, 1}] = 0;
    /*test.print();*/
    /*fmt::println("Result for Empty: {}", test.has_subgraph(test_sub_a));*/
    /*fmt::println("Result for Complete: {}", test.has_subgraph(test_sub_b));*/


    Graph F = Graph::complete(3);
    Graph H = Graph::empty(3);
    Graph *G = find_graph_without_subgraphs(5, F, H);
    if (G != nullptr)
        G->print();
    else
        fmt::println("no graph");

    return 0;
}

