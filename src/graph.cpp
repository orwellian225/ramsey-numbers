#include <stack>
#include <vector>

#include <fmt/core.h>

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

Graph *Graph::heap_unfinished(size_t n) {
    Graph *g = new Graph; 
    g->order = n;
    g->matrix = Matrix::new_uniform(n, 0);

    for (size_t i = 0; i < n; ++i) {
        for (size_t j = 0; j < n; ++j) {
            if (i == j)
                continue;

            g->matrix[{i,j}] = -1;
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
    std::stack<std::vector<size_t>*> stack;
    stack.push(new std::vector<size_t>());

    while (!stack.empty()) {
        std::vector<size_t>* item = stack.top();
        stack.pop();

        if (item->size() == H.order) {
            bool local_result = true;
            for (size_t vertex_a_in_H = 0; vertex_a_in_H < item->size(); ++vertex_a_in_H) {
                size_t vertex_a_in_G = item->at(vertex_a_in_H);

                for (size_t vertex_b_in_H = vertex_a_in_H; vertex_b_in_H < item->size(); ++vertex_b_in_H) {
                    size_t vertex_b_in_G = item->at(vertex_b_in_H);

                    if (vertex_a_in_G == vertex_b_in_G || H.matrix[{vertex_a_in_H, vertex_b_in_H}] == -1)
                        continue;
                    local_result = local_result && (this->matrix[{vertex_a_in_G, vertex_b_in_G}] == H.matrix[{vertex_a_in_H, vertex_b_in_H}]);
                }

            }

            if (local_result) {
                while (!stack.empty()) { // Freeing all the items that still exist
                    std::vector<size_t>* temp = stack.top();
                    stack.pop();
                    delete temp;
                }
                return true;
            }
        } else {
            for (size_t i = (item->size() > 0 ? item->at(item->size() - 1) + 1 : 0); i < this->order; ++i) {
                std::vector<size_t>* new_item = new std::vector<size_t>(*item);
                new_item->push_back(i);
                stack.push(new_item);
            }

            delete item;
        }
    }

    return false;
}

Graph *Graph::clone() {
    Graph *new_graph = new Graph;
    new_graph->order = this->order;
    new_graph->matrix = Matrix::new_uniform(this->order, 0);

    for (size_t i = 0; i < this->order; ++i)
        for (size_t j = 0; j < this->order; ++j)
            new_graph->matrix[{i, j}] = this->matrix[{i, j}];

    return new_graph;
}