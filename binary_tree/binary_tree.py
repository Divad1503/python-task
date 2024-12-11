class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def print(self):
        print(self.value)

if __name__ == "__main__":
    right3 = Node(7, None, None)
    left3 = Node(6, None, None)
    right2 = Node(5, None, None)
    left2 = Node(4, None, None)
    right = Node(3, left3, right3)
    left = Node(2, left2, right2)
    node = Node(1, left, right)
    node.print()
    node.left.print()
    node.right.print()
    left.left.print()
    left.right.print()
    right.right.print()