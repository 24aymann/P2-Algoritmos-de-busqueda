import search

# Color codes for terminal output
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

# Search methods
problemas = [
    ('A', 'B'),
    ('O', 'E'),
    ('G', 'Z'),
    ('N', 'D'),
    ('M', 'F')
]

def output_generator(method_name, search_function, problem):
    """Print the searches result in a formatted way."""
    execution_result = search_function(problem)

    if not execution_result:
        print(f"No se ha encontrado solución para: {method_name}")

    else:
        stats = execution_result.stats

        print(f"==========> {method_name} <==========")
        print(f"Nº de nodos generados:  {stats['generated_nodes']}")
        print(f"Nº de nodos visitados:  {stats['visited_nodes']}")
        print(f"Ruta solución:          {execution_result.path()}")
        print(f"Coste total:            {execution_result.path_cost}")
        print(f"Tiempo de ejecución:    {stats['execution_time']:.7f} segundos")
        print("")

for inicio, fin in problemas:
    print(f"\n{RED}{BOLD} *********** Problema {inicio} → {fin} *********** {RESET}")
    prob = search.GPSProblem(inicio, fin, search.romania)

    output_generator("BFS", search.breadth_first_graph_search, prob)
    output_generator("DFS", search.depth_first_graph_search, prob)
    output_generator("Ramificación y Acotación", search.branch_and_bound_graph_search, prob)
    output_generator("Ramificación y Acotación con Subestimación", search.branch_and_bound_subestimation_graph_search, prob)
