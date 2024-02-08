#!/usr/bin/python3
""" Node and SinglyLinkedList Classes Module """


class Node:
    """ Node Class """
    def __init__(self, data, next_node=None):
        """ Initialization method """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Retrieve the data value """
        return (self.__data)

    @data.setter
    def data(self, value):
        """ Update the data value """
        if type(value) is not int:
            raise ValueError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Retrieve the next_node value """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """ Update the next_node value """
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ SinglyLinkedList Class """
    def __init__(self):
        """ Initialization method """
        self.__head = None

    def sorted_insert(self, value):
        """ Insert a new node """
        if self.__head is None:
            new = Node(value)
            new.next_node = self.__head
            self.__head = new
        else:
            new = Node(value)
            new.data = value
            new.next_node = self.__head
            self.__head = new

    def __str__(self):
        """ Represents objects as strings method """
        temp = self.__head
        node = []

        while temp:
            node.sort()
            node.append(str(temp.data))
            temp = temp.next_node

        node.sort(key=int)

        return ("\n".join(node))
