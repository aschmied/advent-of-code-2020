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
    tokens = tokenize_rule_string(rule_string)

    containing_bag_colour = read_colour(tokens)
    skip_token(tokens, 'contain')
    
    count = read_count(tokens)
    if count == 0:
        return [Edge(containing_bag_colour, None, 0)]

    edges = []
    while True:
        contained_bag_colour = read_colour(tokens)
        edges.append(Edge(containing_bag_colour, contained_bag_colour, count))
        if len(tokens) == 0:
            return edges
        count = read_count(tokens)

def tokenize_rule_string(rule_string):
    tokens_and_blanks = re.split(r'[ ,.]', rule_string)
    return list(filter(lambda s: s != '', tokens_and_blanks))

def read_colour(tokens):
    colour_words = []
    current_token = tokens.pop(0)
    while current_token != 'bag' and current_token != 'bags':
        colour_words.append(current_token)
        current_token = tokens.pop(0)
    return ' '.join(colour_words)

def skip_token(tokens, token_to_skip):
    skipped = tokens.pop(0)
    if skipped != token_to_skip:
        raise RuntimeError(f'Expected {token_to_skip} but found {skipped}')

def read_count(tokens):
    head = tokens.pop(0)
    try:
        return int(head)
    except ValueError:
        pass

    if head != 'no':
        raise RuntimeError(f'Found {head} but expected no')
    skip_token(tokens, 'other')
    skip_token(tokens, 'bags')
    return 0

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
