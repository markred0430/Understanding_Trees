# Making a class for BinarySearch
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
# Addchild method for the class
    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

# make function for search
    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

# Use in order traversal for sorting
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

# build tree for the class
def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

# execution of tree
if __name__ == '__main__':
    # Verifying if the letters are in the name.
    FirstNameLetters = ["M", "A", "R", "K","A", "N", "T", "H", "O", "N", "Y"]
    Letters_tree = build_tree(FirstNameLetters)
    # Letters that are in the list to test if the output is true.
    print("Is A in the list? ", Letters_tree.search("A"))
    print("Is T in the list? ", Letters_tree.search("T"))
    print()
    #Letters that are not in the list to see if the output is otherwise but false.
    print("Is Z in the list? ", Letters_tree.search("Z"))
    print("Is X in the list? ", Letters_tree.search("X"))
    print()
    # Sorting the letters from least to greatest according to the alphabet
    NameLetters_tree = build_tree(["M", "A", "R", "K","A", "N", "T", "H", "O", "N", "Y", "R", "E", "D", "I", "L", "A"])
    print("In order traversal gives this sorted list:", NameLetters_tree.in_order_traversal())
