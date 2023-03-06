import sys
import numpy 
import threading

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
    openfile = input()
    if "I" in openfile or "i" in openfile:
        n = int(input())
        parents = list(map(int, input().split()))
        print(compute_height(n, parents))
    elif "F" in openfile or "f" in openfile:
        file=input()
        if "a" not in file:
            with open("test/" + file, 'r')as f:
                n = int(f.readline())
                parents = list(map(int, f.readline().split()))
                print(compute_height(n, parents))
    pass

#if __name__ == '__main__':
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
    

