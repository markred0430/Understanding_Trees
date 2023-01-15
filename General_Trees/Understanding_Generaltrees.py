class Treenode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

#adding child in the Treenode
    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return  level

    def print_tree(self):
        spaces = '  ' * self.get_level() * 5
        prefix = spaces + "•" if self.parent else ""
        print(prefix +self.data)

        if self.children:
            for child in self.children:
                child.print_tree()

def build_product_tree():
    root = Treenode("Electronics")

    laptop = Treenode("Laptop")
    macbook = Treenode("Macbook")
    test = Treenode("Test")
    macbook.add_child(test)
    laptop.add_child(macbook)
    laptop.add_child(Treenode("Ms Surface"))
    laptop.add_child(Treenode("Think"))

    cellphones = Treenode("Cellphones")
    cellphones.add_child(Treenode("Iphone"))
    cellphones.add_child(Treenode("Google Pixel"))
    cellphones.add_child(Treenode("Vivo"))

    tv = Treenode("Television")
    tv.add_child(Treenode("Samsung"))
    tv.add_child(Treenode("LG"))
    
    root.add_child(laptop)
    root.add_child(cellphones)
    root.add_child(tv)

    return root
if __name__ == "__main__":
    root = build_product_tree()
    #print(root.get_level())
    root.print_tree()
    pass