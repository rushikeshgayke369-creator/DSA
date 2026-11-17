
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def insert(root, x):
    if root is None:
        return Node(x)
    if x < root.data:
        root.left = insert(root.left, x)
    elif x > root.data:
        root.right = insert(root.right, x)
    else:
        print("Duplicate value")
    return root


def search(root, x):
    if root is None:
        return False
    if root.data == x:
        return True
    if x < root.data:
        return search(root.left, x)
    return search(root.right, x)


def delete(root, x):
    if root is None:
        return None

    if x < root.data:
        root.left = delete(root.left, x)
    elif x > root.data:
        root.right = delete(root.right, x)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        temp = root.right
        while temp.left:
            temp = temp.left

        root.data = temp.data
        root.right = delete(root.right, temp.data)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


def depth(root):
    if root is None:
        return 0
    return 1 + max(depth(root.left), depth(root.right))


def copy_tree(root):
    if root is None:
        return None
    new = Node(root.data)
    new.left = copy_tree(root.left)
    new.right = copy_tree(root.right)
    return new


def mirror(root):
    if root is None:
        return None
    new = Node(root.data)
    new.left = mirror(root.right)
    new.right = mirror(root.left)
    return new


def parents(root):
    if root:
        if root.left or root.right:
            print(root.data, "->",
                  root.left.data if root.left else None,
                  root.right.data if root.right else None)
        parents(root.left)
        parents(root.right)


def leaves(root):
    if root:
        if root.left is None and root.right is None:
            print(root.data, end=" ")
        leaves(root.left)
        leaves(root.right)


def level_order(root):
    if root is None:
        print("Tree is empty")
        return

    q = [root]
    while q:
        node = q.pop(0)
        print(node.data, end=" ")
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


root = None

while True:
    print("\n1.Insert  2.Delete  3.Search")
    print("4.Traversal  5.Depth  6.Mirror")
    print("7.Copy  8.Parent-Child  9.Leaf Nodes")
    print("10.Level Order  11.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        root = insert(root, int(input("Enter value: ")))

    elif ch == 2:
        root = delete(root, int(input("Enter value: ")))

    elif ch == 3:
        x = int(input("Enter value: "))
        print("Found" if search(root, x) else "Not Found")

    elif ch == 4:
        print("Inorder: ", end="")
        inorder(root)
        print("\nPreorder: ", end="")
        preorder(root)
        print("\nPostorder: ", end="")
        postorder(root)

    elif ch == 5:
        print("Depth:", depth(root))

    elif ch == 6:
        print("Mirror (Level Order): ", end="")
        level_order(mirror(root))

    elif ch == 7:
        c = copy_tree(root)
        print("Copied Tree: ", end="")
        inorder(c)

    elif ch == 8:
        parents(root)

    elif ch == 9:
        print("Leaf Nodes: ", end="")
        leaves(root)

    elif ch == 10:
        level_order(root)

    elif ch == 11:
        break

    else:
        print("Invalid choice")
