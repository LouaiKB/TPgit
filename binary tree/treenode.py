# coding: utf-8
""" @author : Louai KASSA BAGHDOUCHE
"""

class TreeNode:

    """ class for implementing the binary tree"""

    def __init__(self, data):

        """constructor

        Args:
            self (object): for the object
            data (any type of data): the data of the nodes could be of any type
        """
        self.data = data
        self.right_child = None
        self.left_child = None
        self.level = 0

    def __str__(self):

        """string method

        Returns:
            str: a string descritption of the object
        """
        if self.is_leaf():
            return str(self.data)

        return "[" + str(self.left_child) + ";" + str(self.right_child) + "]: " + str(self.data)

    def print_node(self):

        """a method to print nodes of the binary tree

        Args:
            self (object): for the object
        """

        if self.right_child:
            self.right_child.print_node()

        print(self.data)

        if self.left_child:
            self.left_child.print_node()

    def is_leaf(self):

        """this method checks if the treeNode is a leaf or not
        (a leaf means that the tree node have no children!)

        Args:
            self(object):for the object
        """

        return self.right_child is None and self.left_child is None

    def have_one_child(self):

        """this method checks if a tree node have only one child

        Args:
            self(object): for the object
        """
        return self.right_child is None or self.left_child is None

class Tree:

    """class created to manipulate binary tree"""

    def __init__(self, root_node):

        """constructor

        Args:
            self(object):for the object
            rootNode(treeNode): a treeNodes
        """
        self.root_node = root_node

    def traversal_deep(self):

        """this method proceeds the traversel deep process of the binary tree

        Args:
            self (object): for the object
        """
        print(self.root_node)

    def add_node(self, added_node, target_node):

        """a method to add a node at a given position

        Args:
            added_node (node): the added_node
            target_node (could be any type): the target node
        """
        queue = list()

        if self.root_node is None:
            self.root_node = added_node

        queue.append(self.root_node)

        while len(queue) > 0:

            node = queue.pop(0)

            if node.data == target_node:
                if node.left_child is None:
                    node.left_child = added_node
                else:
                    node.right_child = added_node

                break

            if node.left_child:
                queue.append(node.left_child)

            if node.right_child:
                queue.append(node.right_child)

    @staticmethod
    def delete_deepest_node(root, deleted_node):

        """a static method used to serve the delete node method,
            this method search the deepest node (the last one in the right,
            "because we always begin with the left in the binary trees")
            and the node to be deleted. After that this static method replaces the node which
            we want to delete with the deepest node.
            After that it will be easy for us to delete the deepest node
        """

        queue = list()
        queue.append(root)
        while len(queue) > 0:
            elem = queue.pop(0)

            if elem is deleted_node:
                elem = None
                return

            if elem.right_child:
                if elem.right_child is deleted_node:
                    elem.right_child = None
                    return
                else:
                    queue.append(elem.right_child)

            if elem.left_child:
                if elem.left_child is deleted_node:
                    elem.left_child = None
                    return
                else:
                    queue.append(elem.left_child)

    def delete_node(self, target_node):
        """this method deletes a target Node

        Args:
            target_node(could be any type of data): the node tree to be deleted
        """
        if self.root_node is None:
            return None

        if self.root_node.is_leaf():
            if self.root_node.data == target_node:
                return None

            return self.root_node

        key_node = None
        queue = list()
        queue.append(self.root_node)

        while len(queue) > 0:
            elem = queue.pop(0)
            if elem.data == target_node:
                key_node = elem

            if elem.left_child:
                queue.append(elem.left_child)

            if elem.right_child:
                queue.append(elem.right_child)

        if key_node:
            value = elem.data
            Tree.delete_deepest_node(self.root_node, elem)
            key_node.data = value

        return self.root_node


if __name__ == '__main__':

    n0 = TreeNode(5)
    n1 = TreeNode(1)
    n2 = TreeNode(12)
    n3 = TreeNode(4)
    n4 = TreeNode(6)
    n5 = TreeNode(14)
    n6 = TreeNode(15)
    n7 = TreeNode(3)
    n8 = TreeNode(2)
    n9 = TreeNode(10)
    n10 = TreeNode(16)
    n11 = TreeNode(17)

    n0.right_child = n1
    n0.left_child = n2

    n1.right_child = n6
    n1.left_child = n5

    n2.right_child = n4
    n2.left_child = n3

    n6.right_child = n11
    n6.left_child = n10

    n3.right_child = n7
    n3.left_child = n8

    n4.left_child = n9

    print(n0)
    arbre = Tree(n0)
    arbre.add_node(100, 6)
    print(n0)
    arbre.delete_node(6)
