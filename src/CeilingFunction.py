class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key


n, k = map(int, input().split())
shapes = set()
for _ in range(n):
    crv = list(map(int, input().split()))
    shape = set()
    root = Node(crv[0])
    for c in crv[1:]:
        i = 1
        current_node = root
        while True:
            if c < current_node.val:
                i = i * 2
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = Node(c)
                    break
            else:
                i = i * 2 + 1
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = Node(c)
                    break
        shape.add(i)
    shape = frozenset(shape)
    shapes.add(shape)
unique_shapes = len(shapes)
print(unique_shapes)



