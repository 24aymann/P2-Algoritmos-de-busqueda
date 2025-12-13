import search
# Search methods

ab = search.GPSProblem('A', 'B', search.romania)

print(f"Búsqueda en anchura:        {search.breadth_first_graph_search(ab).path()}")
print(f"Búsqueda en profundidad:    {search.depth_first_graph_search(ab).path()}")
print(f"Ramificación y acotación:   {search.branch_and_bound_graph_search(ab).path()}")
print(f"Ramificación y acotación con subestimación: {search.branch_and_bound_subestimation_graph_search(ab).path()}")
