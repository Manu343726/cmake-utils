project(conan-cmake-test)
cmake_minimum_required(VERSION 2.8)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

include(${CONAN_CMAKE-UTILS_ROOT}/conan.cmake)
