# Find Python and pybind11
find_package(Python COMPONENTS Interpreter Development REQUIRED)
find_package(pybind11 CONFIG REQUIRED)

# Create the Python module
pybind11_add_module(pytriwild
    src/pytriwild.cpp
)

# Link against the main TriWild library and pybind11_json
target_link_libraries(pytriwild PRIVATE triwild_lib pybind11_json)

# Set properties
target_compile_definitions(pytriwild PRIVATE VERSION_INFO="${PROJECT_VERSION}")
target_compile_features(pytriwild PRIVATE cxx_std_11)

# Install the compiled module directly
install(TARGETS pytriwild DESTINATION .)

# Install type hints alongside the module
install(FILES
    ${CMAKE_CURRENT_SOURCE_DIR}/pytriwild.pyi
    DESTINATION .
)