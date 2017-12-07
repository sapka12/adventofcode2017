from functools import reduce


class Node:
    def __init__(self, name, val, child_names):
        self.name = name
        self.val = val
        self.child_names = child_names

    def by_name(name, all_nodes):
        for n in all_nodes:
            if n.name == name:
                return n

    def from_(line):
        arr = line.replace(" ", "").split("->")

        def get_children():
            if (len(arr) > 1):
                return arr[1].split(",")
            else:
                return []

        node = arr[0].split("(")

        return Node(
            node[0],
            int(node[1].replace(")", "")),
            get_children()
        )

    def parent(self, all_nodes):
        for node in all_nodes:
            if self.name in node.child_names:
                return node
        return None

    def has_parent(self, all_nodes):
        return self.parent(all_nodes) != None

    def weight(self, all_nodes):
        return self.val + sum(
            [
                Node.by_name(child_name, all_nodes).weight(all_nodes)
                for child_name in self.child_names
            ]
        )

    def balanced(self, all_nodes):
        if not self.child_names:
            return True

        default_weight = Node.by_name(self.child_names[0], all_nodes).weight(all_nodes)
        return all([Node.by_name(child_name, all_nodes).weight(all_nodes) == default_weight for child_name in
                    self.child_names])


def objects(input_file):
    with open(input_file) as f:
        return [Node.from_(line) for line in [x.strip() for x in f.readlines()]]


def task1(input_file):
    nodes = objects(input_file)

    node = nodes[0]
    while node.has_parent(nodes):
        node = node.parent(nodes)

    return node.name


def unbalance_nodes(all_nodes):
    return [node for node in all_nodes if not node.balanced(all_nodes)]


def optimal_weight(children, all_nodes):
    weights = [child.weight(all_nodes) for child in children]
    avg = sum(weights) / len(weights)

    def closer_to_avg(x, y, avg):
        diff_x = abs(x - avg)
        diff_y = abs(y - avg)
        if diff_x > diff_y:
            return y
        else:
            return x

    return reduce(lambda x, y: closer_to_avg(x, y, avg), weights, weights[0])


def task2(input_file):
    nodes = objects(input_file)
    unbalanced_nodes = unbalance_nodes(nodes)

    result = []

    for unbalanced in unbalanced_nodes:
        children = [Node.by_name(child_name, nodes) for child_name in unbalanced.child_names]

        optimal = optimal_weight(children, nodes)

        for child in children:
            weight = child.weight(nodes)
            if weight != optimal:
                diff = weight - optimal
                result.append([child.val - diff, child.val, weight, optimal, child.name])
    return result[len(result) - 1][0]