#include <pybind11/pybind11.h>
#include <pybind11/eigen.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>

#include "do_triwild.h"

namespace py = pybind11;

PYBIND11_MODULE(pytriwild, m)
{
    m.doc() = "Python bindings for TriWild - Robust Triangulation with Curve Constraints";

    m.def("triangulate", [](const Eigen::MatrixXd &vertices_in, const Eigen::MatrixXi &edges_in, py::dict feature_info_dict, double stop_quality = 10.0, int max_iterations = 80, int stage = 1, double epsilon = 1e-3, double feature_epsilon = 1e-3, double target_edge_length = -1.0, double edge_length_ratio = 0.02, double flat_feature_angle = 10.0, bool cut_outside = false, const Eigen::MatrixXd &hole_points = Eigen::MatrixXd(), bool mute_log = false)
          {
        // Convert Python dict to nlohmann::json
        nlohmann::json feature_info = nlohmann::json::parse(
            py::str(feature_info_dict).cast<std::string>()
        );
        
        // Output variables
        Eigen::MatrixXd vertices_out;
        Eigen::MatrixXi faces_out;
        Eigen::MatrixXd nodes;
        std::vector<std::vector<int>> face_nodes;
        
        // Call the main TriWild function
        triwild::do_triwild(
            vertices_in, edges_in, feature_info,
            vertices_out, faces_out, nodes, face_nodes,
            stop_quality, max_iterations, stage,
            epsilon, feature_epsilon, target_edge_length,
            edge_length_ratio, flat_feature_angle,
            cut_outside, hole_points, mute_log
        );
        
        // Return as tuple
        return py::make_tuple(vertices_out, faces_out, nodes, face_nodes); }, "Robust triangulation with curve constraints", py::arg("vertices_in"), py::arg("edges_in"), py::arg("feature_info") = py::dict(), py::arg("stop_quality") = 10.0, py::arg("max_iterations") = 80, py::arg("stage") = 1, py::arg("epsilon") = 1e-3, py::arg("feature_epsilon") = 1e-3, py::arg("target_edge_length") = -1.0, py::arg("edge_length_ratio") = 0.02, py::arg("flat_feature_angle") = 10.0, py::arg("cut_outside") = false, py::arg("hole_points") = Eigen::MatrixXd(), py::arg("mute_log") = false);

    // Expose the global flag
    m.attr("keep_holes") = &triwild::do_triwild_keep_holes;
}