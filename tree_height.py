class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def create_nodes(n, parents):
    nodes = [Node(i) for i in range(n)]
    for i, parent in enumerate(parents):
        if parent == -1:
            continue
        nodes[parent].children.append(nodes[i])
    return nodes

def get_height(node):
    if not node.children:
        return 1
    return 1 + max(get_height(child) for child in node.children)

def compute_height(n, parents):
    nodes = create_nodes(n, parents)
    root = next(node for node in nodes if node.value == parents.index(-1))
    return get_height(root)

def main():
    try:
        n = int(input())
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))

if __name__ == '__main__':
    main()
