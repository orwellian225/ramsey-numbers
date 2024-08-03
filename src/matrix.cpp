#include <fmt/core.h>

#include "matrix.h"

Matrix Matrix::new_uniform(size_t n, int8_t value) {
    std::unique_ptr<int8_t> data(new int8_t[n * n]);

    for (size_t i = 0; i < n * n; ++i)
        data.get()[i] = value;

    return (Matrix) { n, std::move(data) };
}

int8_t& Matrix::read(size_t index) const { 
    return data.get()[index]; 
}

int8_t& Matrix::read(std::pair<size_t, size_t> indices) const {
    return data.get()[indices.first * n + indices.second];
}

int8_t& Matrix::operator[](size_t index) const { return read(index); }
int8_t& Matrix::operator[](std::pair<size_t, size_t> indices) const { return read(indices); }

void Matrix::print() const {
    for (size_t i = 0; i < n; ++i) {
        for (size_t j = 0; j < n; ++j)
            fmt::print("{} ", read({i, j}));
        fmt::print("\n");
    }
}
