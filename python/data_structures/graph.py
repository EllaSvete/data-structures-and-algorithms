from data_structures.queue import Queue
class Graph:
    """
    Put docstring here
    """

    def __init__(self):
        self._adjacency_list = {}
        # setting to a dictionary

    def add_node(self, value):
        vertex = Vertex(value)
        # grabbing the value of the vertex
        self._adjacency_list[vertex] = []
        # passing it into the dictionary and saving it to a list

        return vertex

    def size(self):
        return len(self._adjacency_list)
        # grabbing the length of our list


    def get_nodes(self):
        return list(self._adjacency_list.keys())
        # returning the keys of our list, grabbing the nodes

    def add_edge(self, start_vertex, end_vertex, weight=0):
        if start_vertex not in self._adjacency_list or end_vertex not in self._adjacency_list:
            raise KeyError()
        # If our start or end of the vertex is not in the list then raise an error

        edge = Edge(end_vertex, weight)
        # set the variable grabbing the last vertex and the weight

        self._adjacency_list[start_vertex].append(edge)
        # append this to our list

        # still a bit confused about the edges!

    def get_neighbors(self, vertex):
        return self._adjacency_list[vertex]

        # also confused about the neighbors. How is this checking what is next to something? Seems like its returning the whole list

    def breadth_first(self, vertex):
        all_vertices = []
        breadth = Queue()
        checked_vertices = set()
        breadth.enqueue(vertex)
        checked_vertices.add(vertex)

        while not breadth.is_empty():
        # while the queue isnt empty dequeue the front and append the value to the list
            front = breadth.dequeue()
            all_vertices.append(front.value)

            for neighbor in self.get_neighbors(front):
                if neighbor.vertex not in checked_vertices:
                    checked_vertices.add(neighbor.vertex)
                    breadth.enqueue(neighbor.vertex)
        return all_vertices



class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
