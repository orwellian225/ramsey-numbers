#include <fmt/core.h>

#include "graph.h"

int main(int argc, char **argv) {
    Graph g = Graph::unfinished(2);
    g.print();
    return 0;
}
