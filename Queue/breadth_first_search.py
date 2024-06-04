from collections import deque

# This class represents a directed graph using adjacency list representation


class Graph:
    def __init__(self, V):
        self.V = V  # No. of vertices
        self.adj = [[] for _ in range(V)]  # Adjacency lists

    # Function to add an edge to graph
    def addEdge(self, v, w):
        self.adj[v].append(w)  # Add w to v’s list

    # Prints BFS traversal from a given source s
    def BFS(self, s):
        # Mark all the vertices as not visited
        visited = [False] * self.V

        # Create a queue for BFS
        queue = deque()

        # Mark the current node as visited and enqueue it
        visited[s] = True
        queue.append(s)

        # Create a mapping from integers to characters
        mapping = ['A', 'B', 'C', 'D', 'E', 'F']

        while queue:
            # Dequeue a vertex from queue and print it
            s = queue.popleft()
            # Use the mapping to print the original label
            print(mapping[s], end=" ")

            # Get all adjacent vertices of the dequeued vertex s
            # If an adjacent has not been visited, then mark it visited
            # and enqueue it
            for i in self.adj[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True


if __name__ == "__main__":
    # Create a graph given in the diagram
    #      A
    #     / \
    #    B   C
    #   /   / \
    #  D   E   F
    g = Graph(6)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 4)
    g.addEdge(2, 5)

    print("Breadth First Traversal is: ", end="")
    g.BFS(0)  # Start BFS from A (0)