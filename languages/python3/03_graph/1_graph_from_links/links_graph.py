

class Node(object):
    def __init__(self, name=None):
        self._name = name
        self.adj_nodes = []
        self.adj_nodes_by_name = {}

    @property
    def name(self):
        if self._name:
            return self._name
        return super().__repr__()

    def link(self, node, bidirectional=False):
        self.adj_nodes.append(node)
        self.adj_nodes_by_name[node.name] = node
        if bidirectional:
            node.link(self, bidirectional=False)

    def __str__(self):
        return self.name

    def __repr__(self):
        clazz = type(self).__name__
        adj_node_str = ', '.join([str(n) for n in self.adj_nodes])
        self_repr = clazz + (f' {self._name}' if self._name else '')
        return f'<{self_repr}({adj_node_str})>'

    def __getitem__(self, name):
        return self.adj_nodes_by_name[name]

    def __delitem__(self, node):
        if isinstance(node, str):
            node = self.adj_nodes_by_name[node]
        assert(isinstance(node, Node))
        self.adj_nodes.remove(node)
        del(self.adj_nodes_by_name[node.name])

    def remove(self, node):
        self.__delitem__(node)


def graph_from_links(links, bidirectional=False):
    graph = {}
    for a, b in links:
        if a not in graph:
            A = Node(name=a)
            graph[a] = A
        else:
            A = graph[a]
        if b not in graph:
            B = Node(name=b)
            graph[b] = B
        else:
            B = graph[b]
        A.link(B, bidirectional=bidirectional)
    return graph.values()
