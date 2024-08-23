#include <stack>
#include <math.h>

#include <fmt/core.h>

#include "graph.h"
#include "ramsey.h"

struct StackGraph {
    size_t length;
    Graph *graph;
};

Graph *find_graph_without_subgraphs(size_t n, Graph& G, Graph& H) {
    std::stack<StackGraph> stack; 

    for (size_t i = 0; i < n; ++i) {
        Graph *new_graph = Graph::heap_unfinished(n);
        for (size_t j = 1; j < n; ++j) {
            new_graph->matrix[{0, j}] = 0;
            new_graph->matrix[{j, 0}] = 0;
        }

        for (size_t j = i + 1; j < n; ++j) {
            new_graph->matrix[{0, j}] = 1;
            new_graph->matrix[{j, 0}] = 1;
        }

        stack.push({ n - 1, new_graph});
    }

    size_t counter = 0;
    while (!stack.empty()) {
        StackGraph item = stack.top();
        stack.pop();
        /*fmt::println("Graph {}: {}", item.graph->as_id(), item.graph->as_bitstring());*/

        size_t row = (size_t)floor(item.graph->order - 0.5 - sqrt(
            (item.graph->order - 0.5) * (item.graph->order - 0.5) - 2 * item.length
        ));
        size_t col = (size_t)( row + 1 + item.length + 0.5 * row * row - (item.graph->order - 0.5) * row );

        if (item.graph->matrix.has_element(-1)) {
            Graph *right_graph = item.graph->clone();
            right_graph->matrix[{row, col}] = 1;
            right_graph->matrix[{col, row}] = 1;
            if (!(right_graph->has_subgraph(G) || right_graph->has_subgraph(H)))
                stack.push({item.length + 1, right_graph});
            else
                delete right_graph;

            Graph *left_graph = item.graph;
            left_graph->matrix[{row, col}] = 0;
            left_graph->matrix[{col, row}] = 0;
            if (!(left_graph->has_subgraph(G) || left_graph->has_subgraph(H)))
                stack.push({ item.length + 1, left_graph});
            else
                delete left_graph;

        } else {
            if (!item.graph->has_subgraph(G) && !item.graph->has_subgraph(H)) {
                while (!stack.empty()) { // empty the remainder of the stack
                    StackGraph temp = stack.top();
                    stack.pop();
                    delete temp.graph;
                }

                return item.graph;
            }
        }

    }

    return nullptr;
}
