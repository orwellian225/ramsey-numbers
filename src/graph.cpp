#include <stack>
#include <vector>
#include <string>
#include <cstring>

#include <fmt/core.h>
#include <fmt/ranges.h>

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

Graph *Graph::heap_empty(size_t n) {
    Graph *g = new Graph;
    g->order = n;
    g->matrix = Matrix::new_uniform(n, 0);

    return g;
}

std::string Graph::as_bitstring() const {
    std::string result = "";

    for (size_t r = 0; r < order; ++r) {
        for (size_t c = r + 1; c < order; ++c) {
            result += std::to_string(matrix[{r, c}]);
        }
    }

    return result;
}

size_t Graph::as_id() const {
    std::string bitstring = as_bitstring();
    return (size_t)std::strtoll(bitstring.c_str(), NULL, 2);
}

void Graph::print() const {
    matrix.print();
}

bool Graph::has_subgraph(const Graph& H) {
    std::stack<std::vector<size_t>*> stack;
    stack.push(new std::vector<size_t>());

    size_t counter = 0;
    while (!stack.empty()) {
        ++counter;
        std::vector<size_t>* item = stack.top();
        stack.pop();

        if (item->size() == H.order) {
            // bool local_result = true;
            // for (size_t vertex_a_in_H = 0; vertex_a_in_H < item->size(); ++vertex_a_in_H) {
            //     size_t vertex_a_in_G = item->at(vertex_a_in_H);

            //     for (size_t vertex_b_in_H = vertex_a_in_H; vertex_b_in_H < item->size(); ++vertex_b_in_H) {
            //         size_t vertex_b_in_G = item->at(vertex_b_in_H);

            //         if (vertex_a_in_G == vertex_b_in_G || H.matrix[{vertex_a_in_H, vertex_b_in_H}] == -1)
            //             continue;

            //         local_result = local_result && (this->matrix[{vertex_a_in_G, vertex_b_in_G}] == H.matrix[{vertex_a_in_H, vertex_b_in_H}]);
            //     }

            // }

            // if (local_result) {
                while (!stack.empty()) { // Freeing all the items that still exist
                    std::vector<size_t>* temp = stack.top();
                    stack.pop();
                    delete temp;
                }

                delete item;
                return true;
            // }
            // delete item;
        } else {
            for (size_t i = (item->size() > 0 ? item->at(item->size() - 1) + 1 : 0); i < this->order; ++i) {
                std::vector<size_t>* new_item = new std::vector<size_t>(*item);
                new_item->push_back(i);

                if (new_item->size() > 1) {
	                // fmt::println("current item: {}", fmt::join(*new_item, " "));
	                bool should_add = true;
	                // for (size_t vertex_a_in_H = 0; vertex_a_in_H < new_item->size(); ++vertex_a_in_H) {
	                    size_t vertex_a_in_H = new_item->size() - 1;
	                    size_t vertex_a_in_G = new_item->at(vertex_a_in_H);

	                    // for (size_t vertex_b_in_H = vertex_a_in_H; vertex_b_in_H < new_item->size(); ++vertex_b_in_H) {
	                    for (size_t vertex_b_in_H = 0; vertex_b_in_H < new_item->size() - 1; ++vertex_b_in_H) {
	                        size_t vertex_b_in_G = new_item->at(vertex_b_in_H);

	                        if (vertex_a_in_G == vertex_b_in_G || H.matrix[{vertex_a_in_H, vertex_b_in_H}] == -1)
	                            continue;

	                        should_add = should_add && (this->matrix[{vertex_a_in_G, vertex_b_in_G}] == H.matrix[{vertex_a_in_H, vertex_b_in_H}]);
	                   	}
					// }

				    if(should_add) {
					    stack.push(new_item);
				    } else {
						delete new_item;
					}

	            } else {
					stack.push(new_item);
				}
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
