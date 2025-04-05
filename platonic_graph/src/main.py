import networkx as nx
from visualization import draw_graph

# Define the Platonic solids and their corresponding notes
platonic_solids = {
    "Tetrahedron": "C",
    "Cube": "D", 
    "Octahedron": "E",
    "Dodecahedron": "G",
    "Icosahedron": "A"
}

def create_platonic_graph():
    """Create and return a graph of Platonic solids with pentatonic scale mapping"""
    G = nx.Graph()
    
    # Add nodes with note attributes
    for solid, note in platonic_solids.items():
        G.add_node(solid, note=note)
    
    # Define relationships between solids
    relationships = [
        ("Tetrahedron", "Cube"),
        ("Tetrahedron", "Octahedron"),
        ("Cube", "Octahedron"),
        ("Cube", "Dodecahedron"),
        ("Octahedron", "Icosahedron"),
        ("Dodecahedron", "Icosahedron")
    ]
    
    G.add_edges_from(relationships)
    return G

if __name__ == "__main__":
    graph = create_platonic_graph()
    draw_graph(graph)