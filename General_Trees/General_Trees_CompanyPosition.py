#Benchmarks for this exercise
# Create class for TreeNode
class TreeNode:
    def __init__(self, designation):
        self.designation = designation
        self.children = []
        self.parent = None
# Add method for add child
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

# build position tree
    def build_position_tree(self):
        root = TreeNode("CEO")

        cto = TreeNode("CTO")

        cto.add_child(TreeNode("Infrastracture Head"))
        cto.add_child(TreeNode("Application Head"))

        hr_head = TreeNode("HR Head")
        hr_head.add_child(TreeNode("Policy Manager"))

        root.add_child(hr_head)
        root.add_child(cto)

        return root
# execution for the tree
    if __name__ == "__main__":
        build_position_tree()
# build method for print tree and get level