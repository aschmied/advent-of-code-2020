import re

def main():
    with open('input') as f:
        containment_graph = read_containment_graph(f)
    all_containing_bags = containment_graph.ancestors('shiny gold')
    print(f'The number of bags that transitively contain shiny gold is {len(all_containing_bags) - 1}')
    bags_in_shiny_gold = containment_graph.descendants_weight('shiny gold') - 1
    print(f'The number of bags you must carry inside your shiny gold bag is {bags_in_shiny_gold}')

def read_containment_graph(iterable):
    graph = Graph()
    for line in iterable:
        edges = parse_rule(line.strip())
        graph.add_edges(edges)
    return graph

def parse_rule(rule_string):
    match = re.match(r'^(.*) bags contain no other bags.$', rule_string)
    if match:
        groups = match.groups()
        return [Edge(groups[0], None, 0)]

    match = re.match(r'^(.*) bags contain (\d)+ ([a-z ]+) bags?\.$', rule_string)
    if match:
        groups = match.groups()
        return [Edge(groups[0], groups[2], int(groups[1]))]

    match = re.match(r'^(.*) bags contain (\d) ([a-z ]+) bags?, (\d) ([a-z ]+) bags?.$', rule_string)
    if match:
        groups = match.groups()
        return [Edge(groups[0], groups[2], int(groups[1])),
            Edge(groups[0], groups[4], int(groups[3]))]

    raise RuntimeError(f'Failed matching for {rule_string}')

class Graph:
    def __init__(self):
        self._adjacency = {}
        self._ancestry = {}
        self._weights = {}

    def add_edge(self, edge):
        forward_neighbours = self._adjacency.setdefault(edge.src, [])
        forward_neighbours.append(edge.dst)
        backward_neighbours = self._ancestry.setdefault(edge.dst, [])
        backward_neighbours.append(edge.src)
        self._weights[(edge.src, edge.dst)] = edge.weight

    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(edge)

    def ancestors(self, root):
        ancestors = set()
        return self._ancestors(root, ancestors)

    def _ancestors(self, node, ancestors):
        if node in ancestors:
            return
        ancestors.add(node)
        direct_ancestors = self._ancestry.get(node, [])
        for direct_ancestor in direct_ancestors:
            self._ancestors(direct_ancestor, ancestors)
        return ancestors

    def descendants_weight(self, root):
        visited = set()
        return self._descendants_weight(root, visited)

    def _descendants_weight(self, node, visited):
        direct_descendants = self._adjacency.get(node, [])
        descendants_weight = 0
        for direct_descendant in direct_descendants:
            descendants_weight += self._weights[(node, direct_descendant)] * self._descendants_weight(direct_descendant, visited)
        return 1 + descendants_weight

class Edge:
    def __init__(self, src, dst, weight):
        self.src = src
        self.dst = dst
        self.weight = weight

    def __eq__(self, other):
        return (self.src == other.src
            and self.dst == other.dst
            and self.weight == other.weight)

if __name__ == '__main__':
    main()
