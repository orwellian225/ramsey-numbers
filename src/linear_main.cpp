#include <fmt/core.h>

#include "graph.h"

int main(int argc, char **argv) {
    Graph test = Graph::complete(5);
    Graph test_sub_a = Graph::empty(3);

    test.has_subgraph(test_sub_a);

    return 0;
}

