import matplotlib.pyplot as plt
import networkx as nx
from sound import play_solid_note

def on_node_click(event):
    """Handle node click events to play sounds"""
    if event.inaxes is None:
        return
        
    for node, (x, y) in pos.items():
        if ((x - event.xdata)**2 + (y - event.ydata)**2) < 0.01:  # Click radius
            play_solid_note(node)
            break

def draw_graph(G):
    """Visualize the Platonic solids graph with interactive sound"""
    global pos
    pos = nx.spring_layout(G, seed=42)
    labels = nx.get_node_attributes(G, 'note')
    
    fig, ax = plt.subplots(figsize=(10, 8))
    nx.draw(G, pos, 
           ax=ax,
           with_labels=True,
           node_color='skyblue',
           node_size=2000,
           font_size=12,
           font_weight='bold')
    
    nx.draw_networkx_labels(G, pos,
                          labels=labels,
                          font_color='darkred',
                          font_size=14)
    
    plt.title("Click on solids to play pentatonic blues notes", fontsize=16)
    fig.canvas.mpl_connect('button_press_event', on_node_click)
    plt.tight_layout()
    plt.show()
