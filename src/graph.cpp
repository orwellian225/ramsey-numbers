#include <stack>
#include <vector>

#include "graph.h"

Graph Graph::unfinished(size_t n) {
    Graph g = { n, Matrix::new_uniform(n, 0) };

    for (size_t i = 0; i < n; ++i) {
        for (size_t j = 0; j < n; ++j) {
            if (i == j)
                continue;

            g.matrix[{i,j}] = -1;
        }
    }
    
    return g;
}

Graph Graph::complete(size_t n) {
    Graph g = { n, Matrix::new_uniform(n, 0) };

    for (size_t i = 0; i < n; ++i) {
        for (size_t j = 0; j < n; ++j) {
            if (i == j)
                continue;

            g.matrix[{i,j}] = 1;
        }
    }

    return g;
}

Graph Graph::empty(size_t n) {
    Graph g = { n, Matrix::new_uniform(n, 0) };
    return g;
}

void Graph::print() const {
    matrix.print();
}

bool Graph::has_subgraph(const Graph& H) {
    std::stack<std::vector<size_t>> stack;
    stack.push(std::vector<size_t>());

    while (!stack.empty()) {
        auto& item = stack.top();

        if (item.size() != H.order) {

        } else {
            
        }
    }
}
