# coding: utf-8
""" @author : Louai KASSA BAGHDOUCHE
"""

from node import Node
from chained_list import ChainedList

def test_print_node():
    """function to test the linkd list
    """
    value_one = Node(1)
    value_two = Node(5)
    value_three = Node(902)
    value_four = Node(698)
    value_one.link = value_two
    value_two.link = value_three
    value_three.link = value_four
    print(value_one)

def test_insert_node():
    """function to test the insertion into a linked list
    """
    chained_list = ChainedList([1, 5, 6, 12, 34])
    print("linked list befor insertion: ", chained_list)
    chained_list.insert_node_after(6, Node(1))
    chained_list.insert_node_after(54, Node(14))
    chained_list.insert_node_after(90, Node(13))
    print("linked list after insertion: ", chained_list)

def test_delete_method():
    """function to tesy the deleting of value in a linked list
    """
    chained_list = ChainedList([1, 5, 6, 12, 34])
    print("linked list befor deletion: ", chained_list)
    chained_list.delete_node(1)
    print("linked list after deletion: ", chained_list)



if __name__ == "__main__":
    test_delete_method()
