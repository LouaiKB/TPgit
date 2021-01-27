# coding: utf-8
""" @author : Louai KASSA BAGHDOUCHE
"""

class Node:

    """This is a Node class"""

    def __init__(self, data, link=None):

        """constructor

        Args:
            self (object): [for the object]
            data (float): [the data value of the node]
            link (object): [the link for the next node]
        """

        self.data = data
        self.link = link

    def __str__(self):

        """string methode

        Args:
            self (object): [description]

        Returns:
            str: [description]
        """

        liste = []
        node = self
        while node.link is not None:
            liste.append(node.data)
            node = node.link
        liste.append(node.data)
        return str(liste)
