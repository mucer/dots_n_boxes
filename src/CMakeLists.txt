#cmake_minimum_required(VERSION 3.5)

#project(Arduino LANGUAGES CXX VERSION 0.0.1)
add_subdirectory(lib/Catch2)

add_executable(tests
  test/tests.cpp
  test/GameLogic.test.cpp
)
target_link_libraries(tests PRIVATE Catch2::Catch2WithMain)

# These tests need their own main
#add_executable(custom-main-tests test/tests.cpp)
#target_link_libraries(custom-main-tests PRIVATE Catch2::Catch2)