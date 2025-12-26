from collections import deque

from task_5.colorizer import lighten
from task_5.tree import Node, draw_tree

START_COLOR = "#0600A1"
END_COLOR = "#ADA6FF"


def dfs_traversal(root, count=0):
    stack = [root]
    node_color = START_COLOR
    current_num = 0
    while stack:
        node = stack.pop()
        current_num += 1
        node.color = node_color
        node_color = lighten(START_COLOR, END_COLOR, count, current_num)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


def get_bfs_path(graph, start, goal):
    visited = set()
    result = []
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            result.append(vertex)
            visited.add(vertex)
            if vertex == goal:
                return result
            queue.extend(set(graph[vertex]) - visited)
    return result


def bfs_traversal(root, count=0):
    queue = deque([root])
    visited = set()
    node_color = START_COLOR
    current_num = 0
    while queue:
        node = queue.popleft()
        if node not in visited:
            current_num += 1
            node.color = node_color
            node_color = lighten(START_COLOR, END_COLOR, count, current_num)

            visited.add(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


def create_tree() -> (Node, int):
    root = Node(0)
    root.left = Node(1)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    return root, 7


def main():
    tree_for_dfs, num_nodes = create_tree()
    dfs_traversal(tree_for_dfs, 7)
    draw_tree(tree_for_dfs)

    tree_for_bfs, num_nodes = create_tree()
    bfs_traversal(tree_for_bfs, num_nodes)
    draw_tree(tree_for_bfs)


if __name__ == "__main__":
    main()
