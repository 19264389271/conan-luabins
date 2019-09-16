cmake_minimum_required(VERSION 3.14)
project(luabins)

if(EXISTS "${CMAKE_BINARY_DIR}/conanbuildinfo.cmake")
	include("${CMAKE_BINARY_DIR}/conanbuildinfo.cmake")
else()
	include("conanbuildinfo.cmake")
endif()
conan_basic_setup()

set(LUABINS_BASIC_SOURCES 
    src/luainternals.c
    src/fwrite.c
    src/luabins.c
	src/lualess.c
    src/savebuffer.c
    src/save.c
    src/load.c
    src/write.c)
    
add_compile_definitions(LUAI_BITSINT=32)

add_library(luabins ${LUABINS_BASIC_SOURCES})
target_link_libraries(luabins ${CONAN_LIBS})

set_target_properties(luabins PROPERTIES PUBLIC_HEADER "src/luabins.h")
install(TARGETS luabins
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib
        PUBLIC_HEADER DESTINATION include
)
