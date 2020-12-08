import unittest

from main import parse_rule
from main import Edge
from main import Graph

class TestParseRule(unittest.TestCase):
    def test_none_contained(self):
        edges = parse_rule('faded blue bags contain no other bags.')
        self.assertEqual(len(edges), 1)
        self.assertEqual(edges, [Edge('faded blue', None, 0)])

    def test_one_contained(self):
        edges = parse_rule('bright white bags contain 1 shiny gold bag.')
        self.assertEqual(len(edges), 1)
        self.assertEqual(edges, [Edge('bright white', 'shiny gold', 1)])

    def test_multiple_contained(self):
        edges = parse_rule('light red bags contain 1 bright white bag, 2 muted yellow bags.')
        self.assertEqual(len(edges), 2)
        self.assertEqual(edges[0], Edge('light red', 'bright white', 1))
        self.assertEqual(edges[1], Edge('light red', 'muted yellow', 2))

class TestGraph(unittest.TestCase):
    def test_ancestors(self):
        graph = Graph()
        graph.add_edges([
            Edge('a', 'b', 1),
            Edge('a', 'c', 1),
            Edge('c', 'd', 1)])
        self.assertCountEqual(graph.ancestors('a'), ['a'])
        self.assertCountEqual(graph.ancestors('b'), ['a', 'b'])
        self.assertCountEqual(graph.ancestors('c'), ['a', 'c'])
        self.assertCountEqual(graph.ancestors('d'), ['a', 'c', 'd'])

    def test_ancestors_with_crossing_paths(self):
        graph = Graph()
        graph.add_edges([
            Edge('a', 'b', 1),
            Edge('a', 'c', 1),
            Edge('c', 'd', 1),
            Edge('b', 'd', 1)])
        self.assertCountEqual(graph.ancestors('d'), ['a', 'b', 'c', 'd'])