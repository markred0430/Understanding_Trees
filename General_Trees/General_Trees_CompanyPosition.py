#Benchmarks for this exercise
# Create class for TreeNode
class TreeNode:
    def __init__(self, designation, name):
        self.designation = designation
        self.name = name
        self.children = []
        self.parent = None
# Add method for add child
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

# build method for print tree and get level
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return  level

    def print_tree(self, Property):
        if Property == 'both':
            print()
            value = self.name + " (" + self.designation + ")"
        elif Property == 'name':
            print()
            value = self.name
        else:
            print()
            value = self.designation

        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "•" if self.parent else ""
        print(prefix + value)
        if self.children:
            for child in self.children:
                child.print_tree(Property)

# build management tree
def build_management_tree():
    infra_head = TreeNode("Vishwa","Infrastructure Head")
    infra_head.add_child(TreeNode("Dhaval","Cloud Manager"))
    infra_head.add_child(TreeNode("Abhijit", "App Manager"))

    cto = TreeNode("Chinmay", "CTO")
    cto.add_child(infra_head)
    cto.add_child(TreeNode("Aamir", "Application Head"))

    # HR hierarchy
    hr_head = TreeNode("Gels","HR Head")

    hr_head.add_child(TreeNode("Peter","Recruitment Manager"))
    hr_head.add_child(TreeNode("Waqas", "Policy Manager"))

    ceo = TreeNode("Nilupul", "CEO")
    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo
# execution for the tree.
if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name")
    root_node.print_tree("designation")
    root_node.print_tree("both")
