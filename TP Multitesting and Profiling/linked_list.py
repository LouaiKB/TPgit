# coding: utf-8
"""
    author: Olivier Chabrol
    updated by: Louai KB
"""

class Node:
    """ Node of a list """
    def __init__(self, data):
        """constructor

        Args:
            data (float): the data of the node
        """
        self.data = data
        self.next = None

    def __str__(self):
        """string method

        Returns:
            string
        """
        return str(self.data)

    def __repr__(self):
        """representative method

        Returns:
            the data of the object
        """
        return self.data

class LinkedList:

    """ Linked list """

    def __init__(self, nodes=None):
        """constructor

        Args:
            nodes (list, optional): a list of data to be converted into a linked list.
            Defaults to None.
        """
        self.head = None
        if nodes is not None and len(nodes) != 0:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def is_empty(self):
        """method to check if the linked list is empty or not

        Returns:
            a boolean
        """
        return self.head is None


    def get(self, index):
        """method to get the node from the index

        Args:
            index (int): the index of the node

        Raises:
            Exception: if the node is empty

        Returns:
            Node
        """
        if self.is_empty():
            raise Exception('empty node')

        self.recursion(index, self.head)

    def recursion(self, index, node):
        """recursive method to get the node from the index

        Args:
            index (int): the index of the node
            node (Node): the head node

        Returns:
            the searched Node
        """

        if node is None:
            return node

        elif index == 0:
            return node

        return self.recursion(index - 1, node.next)

    def add_after(self, data, new_node):
        """a method to insert a node after a given node

        Args:
            data (float): data of the node which we will insert the new node after it
            new_node (Node): new node to be inserted

        Raises:
            Exception: list is empty
            Exception: Node with data not found
        """
        if not self.head:
            raise Exception("List is empty")

        for node in self:
            if node.data == data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '{}' not found".format(data))

    def add_before(self, data, new_node):
        """a method to insert a node before a given node

        Args:
            data (float): data of the node which we will insert the new node before it
            new_node (Node): the new node to be inserted

        Raises:
            Exception: list is empty
            Exception: Node with data not found

        Returns:
            Node
        """
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == data:
            return self.add_first(new_node)


        prev_node = self.head

        for node in self:
            if node.data == data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '{}' not found".format(data))

    def remove_node(self, data):
        """Method that allows to delete all node(s) where value == data.

        Args:
            data (float): data of the nodes

        Raises:
            Exception: list is empty
            Exception: Node with data not found
        """
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '{}' not found".format(data))



    def add_first(self, node_to_add):
        """Method that inserts a node at the first element of the list.

        Args:
            node_to_add (Node)
        """
        node_to_add.next = self.head
        self.head = node_to_add

    def add_last(self, node_to_add):
        """Method that inserts a node at the last element of the list.

        Args:
            node_to_add (Node)
        """
        if self.head is None:
            self.head = node_to_add
            return

        node = self.head
        # while node.next is not None:*
        while node.next is not None:
            node = node.next
        node.next = node_to_add

    def __repr__(self):
        """representative method

        Returns:
            the data of the object
        """
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        #return "a"
        return "{}".format(nodes)

    def __iter__(self):
        """Iteration method
        """
        node = self.head
        while node is not None:
            yield node
            node = node.next
