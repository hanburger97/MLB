cmake_minimum_required(VERSION 3.3)
project(MLB_Tools_FormatGL)

set (CMAKE_CXX_STANDARD 11)
SET(CMAKE_CXX_FLAGS  "${CMAKE_CXX_FLAGS} -pthread -Wall -Wno-switch -std=c++11 -DBUILD_SHARED_LIBS=OFF -Wfatal-errors" )

file(GLOB src
        "./*.cpp"
        "./*.h"
        )


add_executable(mlb_format_gl ${src})