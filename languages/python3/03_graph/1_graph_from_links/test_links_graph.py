import unittest

from links_graph import Node, graph_from_links


class TestLinksGraph(unittest.TestCase):

    def test_line(self):
        links = [
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D'],
        ]
        graph = graph_from_links(links)
        self.assertEqual(4, len(graph))
        a = None
        for n in graph:
            if n.name == 'A':
                a = n
                break
        self.assertIsNotNone(a)
        self.assertEqual(1, len(a.adj_nodes))
        b = a['B']
        self.assertIsNotNone(b)
        self.assertEqual('B', b.name)
        self.assertEqual(1, len(b.adj_nodes))
        c = b['C']
        self.assertIsNotNone(c)
        self.assertEqual('C', c.name)
        self.assertEqual(1, len(c.adj_nodes))
        d = c['D']
        self.assertIsNotNone(d)
        self.assertEqual('D', d.name)
        self.assertEqual(0, len(d.adj_nodes))

    def test_cycle(self):
        links = [
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'A'],
        ]
        graph = graph_from_links(links)
        self.assertEqual(3, len(graph))
        a = None
        for n in graph:
            if n.name == 'A':
                a = n
                break
        self.assertIsNotNone(a)
        self.assertEqual(1, len(a.adj_nodes))
        b = a['B']
        self.assertIsNotNone(b)
        self.assertEqual('B', b.name)
        self.assertEqual(1, len(b.adj_nodes))
        c = b['C']
        self.assertIsNotNone(c)
        self.assertEqual('C', c.name)
        self.assertEqual(1, len(c.adj_nodes))
        a_2 = c['A']
        self.assertIsNotNone(a_2)
        self.assertEqual(a, a_2)
        self.assertEqual(1, len(a_2.adj_nodes))

    def test_bidirectional_tree(self):
        links = [
            ['A', 'B'],
            ['B', 'A'],
            ['A', 'C'],
            ['C', 'A'],
        ]
        graph = graph_from_links(links)
        self.assertEqual(3, len(graph))
        a = None
        for n in graph:
            if n.name == 'A':
                a = n
                break
        self.assertIsNotNone(a)
        self.assertEqual(2, len(a.adj_nodes))
        b = a['B']
        self.assertIsNotNone(b)
        self.assertEqual('B', b.name)
        self.assertEqual(1, len(b.adj_nodes))
        a_2 = b['A']
        self.assertIsNotNone(a_2)
        self.assertEqual(a, a_2)
        self.assertEqual(2, len(a_2.adj_nodes))
        c = a['C']
        self.assertIsNotNone(c)
        self.assertEqual('C', c.name)
        self.assertEqual(1, len(c.adj_nodes))
        a_3 = c['A']
        self.assertIsNotNone(a_3)
        self.assertEqual(a, a_3)
        self.assertEqual(2, len(a_3.adj_nodes))

    def test_bidirectional_kwarg(self):
        links = [
            ['A', 'B'],
            ['A', 'C'],
        ]
        graph = graph_from_links(links, bidirectional=True)
        self.assertEqual(3, len(graph))
        a = None
        for n in graph:
            if n.name == 'A':
                a = n
                break
        self.assertIsNotNone(a)
        self.assertEqual(2, len(a.adj_nodes))
        b = a['B']
        self.assertIsNotNone(b)
        self.assertEqual('B', b.name)
        self.assertEqual(1, len(b.adj_nodes))
        a_2 = b['A']
        self.assertIsNotNone(a_2)
        self.assertEqual(a, a_2)
        self.assertEqual(2, len(a_2.adj_nodes))
        c = a['C']
        self.assertIsNotNone(c)
        self.assertEqual('C', c.name)
        self.assertEqual(1, len(c.adj_nodes))
        a_3 = c['A']
        self.assertIsNotNone(a_3)
        self.assertEqual(a, a_3)
        self.assertEqual(2, len(a_3.adj_nodes))
