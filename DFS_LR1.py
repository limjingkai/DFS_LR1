import streamlit as st
st.image("LabReport_BSD2513_#1.jpg", caption="Depth-First Search Graph", use_column_width=True)

graph = {
    'A': ['B', 'D'],
    'B': ['C', 'E', 'G'],
    'C': ['A'],
    'D': ['C'],
    'E': ['H'],
    'F': [],
    'G': ['F'],
    'H': ['F','G']
}

def dfs(graph, node, visited=None, traversal_order=None):
    if visited is None:
        visited = set()
    if traversal_order is None:
        traversal_order = []

    if node not in visited:
        visited.add(node)
        traversal_order.append(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited, traversal_order)

    return traversal_order

st.title("Depth-First Search (DFS) Traversal")
st.write("This app performs DFS on the graph shown above.")

start_node = st.text_input("Enter start node (default = 'A'):", "A")

if st.button("Run DFS"):
    if start_node in graph:
        order = dfs(graph, start_node)
        st.success("Following is the Depth-First Search traversal order:")
        st.write(" → ".join(order))
    else:
        st.error("Start node not found in graph.")

st.caption("Lab Report 1 BSD2513 | DFS Traversal Demonstration")
