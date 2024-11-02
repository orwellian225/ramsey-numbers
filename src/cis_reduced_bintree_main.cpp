#include <chrono>

#include <fmt/core.h>

#include "graph.h"
#include "ramsey.h"

int main(int argc, char **argv) {
    size_t graph_order, clique_order, indepset_order;
    if (argc != 4) {
        fmt::println("Incorrect Arguments");
        fmt::println("\tArgument 1: Graph order (n) to search in");
        fmt::println("\tArgument 2: Clique order (k) to search for");
        fmt::println("\tArgument 3: Independent Set order (l) to search for");
        return 0;
    }

    graph_order = std::stoi(argv[1]);
    clique_order = std::stoi(argv[2]);
    indepset_order = std::stoi(argv[3]);

    Graph clique = Graph::complete(clique_order);
    Graph indepset = Graph::empty(indepset_order);

    auto start_time = std::chrono::high_resolution_clock::now();
    Graph *resultant_graph = reduced_bintree_ramsey(graph_order, clique, indepset);
    auto end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration = end_time - start_time;

    // Output format is n, k, l, graph_id, graph_string
    if (resultant_graph == nullptr)
        fmt::println("{},{},{},{},/,{}", graph_order, clique_order, indepset_order, "-1", duration.count());
    else {
        fmt::println("{},{},{},{},{},{}", graph_order, clique_order, indepset_order, resultant_graph->as_id(), resultant_graph->as_bitstring(), duration.count());
        delete resultant_graph;
    }

    return 0;
}
