#include <chrono>

#include <fmt/core.h>

#include "ramsey.h"
#include "graph.h"

void benchmark_subgraph_isomorphism(size_t max_g_n, size_t h_n, size_t trials);

int main(int argc, char **argv) {
    
    // Benchmark Types
    // * 1 -> Subgraph Isomorphism
    uint8_t benchmark_type = 0;
    if (argc > 2)
        benchmark_type = std::stoi(argv[1]);
    else {
        fmt::println(stderr, "Invalid Arguments");
        return 0;
    }

    if (benchmark_type == 1 && argc == 5) {
        size_t max_g_n = std::stoull(argv[2]);
        size_t h_n = std::stoull(argv[3]);
        size_t trials = std::stoull(argv[4]);
        benchmark_subgraph_isomorphism(max_g_n, h_n, trials);
    } else if (benchmark_type == 1) {
        fmt::println(stderr, "Invalid Arguments for SIP benchmark");
        return 0;
    }

}

/**
 *  Testing the worst case complexity of the subgraph isomorphism search
 *  - Worst case is when subgraph H is not in the graph G
 *
 *  Output format:
 *  G order, H order, duration (s)
 */
void benchmark_subgraph_isomorphism(size_t max_g_n, size_t h_n, size_t trials) {
    Graph H = Graph::empty(h_n);
    for (size_t n = 0; n < max_g_n; ++n) {
        Graph G = Graph::complete(n);
        for (size_t t = 0; t < trials; ++t) {
            auto start_time = std::chrono::high_resolution_clock::now();
            G.has_subgraph(H);
            auto end_time = std::chrono::high_resolution_clock::now();

            std::chrono::duration<double> duration = end_time - start_time;
            fmt::println("{}, {}, {}", n, h_n, duration.count());
        }
    }
}
