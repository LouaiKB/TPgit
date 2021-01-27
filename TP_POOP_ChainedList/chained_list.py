# coding: utf-8
""" @author : Louai KASSA BAGHDOUCHE
"""

from node import Node

class ChainedList:

    """a class to generate linked list"""

    def __init__(self, list_of_nodes):
        """constructor

        Args:
            self (object): for the object
            list_of_nodes (list): input list that will be converted into linked list
        """

        self.head = Node(list_of_nodes[0])
        current_node = self.head

        for item in list_of_nodes[1:]:
            current_node.link = Node(item)
            current_node = current_node.link

    def __str__(self):
        """string method

        Args:
            self (object): for the object

        Returns:
            str: representation of a linked list
        """
        return str(self.head)


    def insert_node_after(self, value, new_node):

        """ method to insert a Node in a linked list

        Args:
            self (object): [for the object]
            value (float): [the value of the node to be inserted]
            new_node (object of the Node class) : [the node to be inserted]
        """

        current_node = self.head

        while current_node is not None:
            if current_node.data == value:
                break

            current_node = current_node.link

        new_node.link = current_node.link
        current_node.link = new_node

    def delete_node(self, value):

        """ method to delete a Node where the node data equal to value

        Args:
            self (object): [for the object]
            value (float): [the value of the node to be deleted]
        """

        if self.head.data == value:
            self.head = self.head.link

        current_node = self.head

        while current_node.link is not None:
            if current_node.link.data == value:
                current_node.link = current_node.link.link
            current_node = current_node.link
