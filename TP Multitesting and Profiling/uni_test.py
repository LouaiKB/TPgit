# coding: utf-8
"""
    author: Louai KB

"""

import unittest
from linked_list import Node
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):

    """ Class created to proceed tests on the linked list """
    def setUp(self):
        self.new_list = LinkedList()

    def test_new_linked_list_is_empty(self):
        """
        A method to test if the new linked list created is empty or not.
        The head of a new linked list is None!
        """
        self.assertIsNone(self.new_list.head)

    def test_not_empty_after_insertion(self):
        """
        A method to test if after the insertion wether the linked list is empty or not
        """
        self.new_list.add_first(Node(5))
        self.assertIsNotNone(self.new_list)

    def test_unchangement(self):
        """
        A method to test if after an adding and deleting node the linked list is unchanged.
        Original list is created to compare it with the linked list
        after the insertion and the deletion.
        """

        original_list = self.new_list

        self.new_list.add_last(Node(6))
        self.new_list.remove_node(6)
        self.assertEqual(self.new_list, original_list)

    def test_head(self):
        """
        A method to test if after the insertion of a data in the head, then the head == data
        """
        new_head = "i'm the new head!!"
        self.new_list.add_first(Node(new_head))
        self.assertEqual(self.new_list.head.data, new_head)

if __name__ == "__main__":
    unittest.main()
