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
    if re.match(r'^([a-z ]+) bags contain no other bags.$', rule_string):
        return []

    match = re.match(r'^([a-z ]+) bags contain ', rule_string)
    groups = match.groups()
    src_colour = groups[0]
    start_index = len(match.group(0))
    rule_string = rule_string[start_index:]

    edges = []
    while len(rule_string) > 0:
        match = re.match(r'^(\d)+ ([a-z ]+) bags?[,.] ?', rule_string)
        groups = match.groups()
        count = int(groups[0])
        dst_colour = groups[1]
        edges.append(Edge(src_colour, dst_colour, count))
        start_index = len(match.group(0))
        rule_string = rule_string[start_index:]

    return edges

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
