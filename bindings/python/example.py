import numpy as np
import pytriwild

# Example: Simple square with constraints
vertices_in = np.array([
    [0.0, 0.0],
    [1.0, 0.0],
    [1.0, 1.0],
    [0.0, 1.0]
])

edges_in = np.array([
    [0, 1],
    [1, 2],
    [2, 3],
    [3, 0]
])

# Run triangulation
vertices_out, faces_out, nodes, face_nodes = pytriwild.triangulate(
    vertices_in=vertices_in,
    edges_in=edges_in,
    feature_info={},
    stop_quality=10.0,
    max_iterations=80
)

print(f"Input vertices: {vertices_in.shape}")
print(f"Output vertices: {vertices_out.shape}")
print(f"Output faces: {faces_out.shape}")