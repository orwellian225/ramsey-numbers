#pragma once

#include <stddef.h>
#include <stdint.h>
#include <utility>
#include <memory>

struct Matrix {
    size_t n;
    std::unique_ptr<int8_t> data;

    static Matrix new_uniform(size_t n, int8_t value);

    int8_t& read(size_t index) const;
    int8_t& read(std::pair<size_t, size_t> indices) const;
    int8_t& operator[](size_t index) const;
    int8_t& operator[](std::pair<size_t, size_t> indices) const;

    void print() const;
};

