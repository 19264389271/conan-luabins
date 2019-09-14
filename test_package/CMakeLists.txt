cmake_minimum_required(VERSION 2.8.12)
project(test_package)

set(CMAKE_VERBOSE_MAKEFILE TRUE)

if(APPLE)
set ( CMAKE_EXE_LINKER_FLAGS "-pagezero_size 10000 -image_base 100000000" )
endif()

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(${PROJECT_NAME} test_package.cpp test_api.c)
target_link_libraries(${PROJECT_NAME} ${CONAN_LIBS})
