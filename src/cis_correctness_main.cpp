#include <array>
#include <chrono>
#include <string>
#include <stddef.h>

#include <fmt/core.h>

#include "graph.h"
#include "ramsey.h"

int main(int argc, char **argv) {

    std::array<size_t, 7> order_cases  = { 4, 5, 6, 3, 4, 4, 5 };
    std::array<size_t, 7> clique_cases = { 3, 3, 3, 2, 2, 2, 2 };
    std::array<size_t, 7> iset_cases   = { 3, 3, 3, 4, 4, 5, 5 };

    for (size_t test_case = 0; test_case < 7; ++test_case) {
        size_t n = order_cases[test_case];
        size_t k = clique_cases[test_case];
        size_t l = iset_cases[test_case];
        
        Graph clique = Graph::complete(k);
        Graph iset = Graph::empty(l);

        Graph *linear_result = linear_ramsey(n, clique, iset);
        Graph *bintree_result = bintree_ramsey(n, clique, iset);
        Graph *reduced_bintree_result = reduced_bintree_ramsey(n, clique, iset);

        std::string linear_result_string = linear_result != nullptr ? linear_result->as_bitstring() : "-1";
        std::string bintree_result_string = bintree_result != nullptr ? bintree_result->as_bitstring() : "-1";
        std::string reduced_bintree_result_string = reduced_bintree_result != nullptr ? reduced_bintree_result ->as_bitstring() : "-1";

        fmt::println("{},{},{},{},{},{}", n, k, l, linear_result_string, bintree_result_string, reduced_bintree_result_string);  
    }
}

