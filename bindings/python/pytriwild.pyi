"""
Type stubs for pytriwild - Python bindings for TriWild

This stub file provides type hints for the compiled pytriwild extension module.
"""

from typing import Dict, List, Tuple, Any, Optional
import numpy as np
from numpy.typing import NDArray

def triangulate(
    vertices_in: NDArray[np.floating],
    edges_in: NDArray[np.integer],
    feature_info: Dict[str, Any] = {},
    stop_quality: float = 10.0,
    max_iterations: int = 80,
    stage: int = 1,
    epsilon: float = 1e-3,
    feature_epsilon: float = 1e-3,
    target_edge_length: float = -1.0,
    edge_length_ratio: float = 0.02,
    flat_feature_angle: float = 10.0,
    cut_outside: bool = False,
    hole_points: Optional[NDArray[np.floating]] = None,
    mute_log: bool = False
) -> Tuple[NDArray[np.floating], NDArray[np.integer], NDArray[np.floating], List[List[int]]]:
    """
    Robust triangulation with curve constraints.
    
    Args:
        vertices_in: Input vertices as Nx2 array of coordinates
        edges_in: Input edges as Mx2 array of vertex indices
        feature_info: Dictionary containing feature information (default: {})
        stop_quality: Quality threshold for stopping optimization (default: 10.0)
        max_iterations: Maximum number of optimization iterations (default: 80)
        stage: Processing stage (default: 1)
        epsilon: General epsilon tolerance (default: 1e-3)
        feature_epsilon: Feature-specific epsilon tolerance (default: 1e-3)
        target_edge_length: Target edge length, -1 for automatic (default: -1.0)
        edge_length_ratio: Edge length ratio parameter (default: 0.02)
        flat_feature_angle: Angle threshold for flat features in degrees (default: 10.0)
        cut_outside: Whether to cut outside regions (default: False)
        hole_points: Points defining holes to be removed (default: None)
        mute_log: Whether to suppress log output (default: False)
    
    Returns:
        Tuple containing:
        - vertices_out: Output vertices as Nx2 array
        - faces_out: Output triangle faces as Mx3 array of vertex indices
        - nodes: Node coordinates for curved elements
        - face_nodes: List of node indices for each face (for curved triangles)
    """
    ...

# Global flag for controlling hole behavior
keep_holes: bool
