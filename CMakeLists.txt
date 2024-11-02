cmake_minimum_required(VERSION 3.16)

project(RR-RamNums DESCRIPTION "Research Report: C++ Impl of the UPPER-RAMSEY algorithms" LANGUAGES CXX)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED On)
set(CMAKE_CXX_EXTENSIONS Off)
add_subdirectory(lib/fmt)

add_executable(ramnum-benchmark
    src/benchmark_main.cpp
    src/ramsey.cpp src/matrix.cpp src/graph.cpp
)
target_include_directories(ramnum-benchmark PUBLIC include PUBLIC lib/fmt/include)
target_link_directories(ramnum-benchmark PRIVATE src lib/fmt/src)
target_link_libraries(ramnum-benchmark fmt)

add_executable(ramnum-cis
    src/cis_main.cpp
    src/ramsey.cpp src/matrix.cpp src/graph.cpp
)
target_include_directories(ramnum-cis PUBLIC include PUBLIC lib/fmt/include)
target_link_directories(ramnum-cis PRIVATE src lib/fmt/src)
target_link_libraries(ramnum-cis fmt)

add_executable(ramnum-linear 
    src/linear_main.cpp
    src/ramsey.cpp src/matrix.cpp src/graph.cpp
)
target_include_directories(ramnum-linear PUBLIC include PUBLIC lib/fmt/include)
target_link_directories(ramnum-linear PRIVATE src lib/fmt/src)
target_link_libraries(ramnum-linear fmt)

add_executable(test
    src/test.cpp
    src/ramsey.cpp src/matrix.cpp src/graph.cpp
)
target_link_libraries(test m)
target_include_directories(test PUBLIC include PUBLIC lib/fmt/include)
target_link_directories(test PRIVATE src lib/fmt/src)
target_link_libraries(test fmt)
