class Node:
    def __init__(self, name, val, child_names):
        self.name = name
        self.val = val
        self.child_names = child_names

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


def get_lines(input_file):
    with open(input_file) as f:
        return [x.strip() for x in f.readlines()]


def objects(input_file):
    return [Node.from_(line) for line in get_lines(input_file)]


def task1(input_file):
    nodes = objects(input_file)

    node = nodes[0]
    while node.has_parent(nodes):
        node = node.parent(nodes)

    return node.name


def task2(arr):
    return False
