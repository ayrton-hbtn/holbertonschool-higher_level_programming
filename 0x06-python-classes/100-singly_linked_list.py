#!/usr/bin/python3
''' Node class '''


class Node:
    ''' Node initializer '''
    def __init__(self, data, next_node=None):

        if isinstance(data, int):
            self.data = data
        else:
            raise TypeError("data must be an integer")
        if isinstance(next_node, Node) or next_node is None:
            self.next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")

    ''' data getter '''
    @property
    def data(self):
        return self.__data

    ''' data setter to private '''
    @data.setter
    def data(self, value):
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    ''' next_node getter '''
    @property
    def next_node(self):
        return self.__next_node

    ''' next_node setter to private '''
    @next_node.setter
    def next_node(self, value):
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")

''' class SinglyLinkedList '''


class SinglyLinkedList:
    ''' initializer for list '''
    def __init__(self):
        self.__head = None

    ''' insert node in sorted crescent place '''
    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value, None)
        elif value <= self.__head.data:
            new = Node(value, self.__head)
            self.__head = new
        else:
            tmp = self.__head
            while tmp.next_node is not None and tmp.next_node.data <= value:
                tmp = tmp.next_node
            nex = tmp.next_node
            tmp.next_node = Node(value, nex)

    ''' makes list printable '''
    def __str__(self):
        tmp = self.__head
        p = ''
        while tmp is not None:
            p = p + str(tmp.data) + '\n'
            tmp = tmp.next_node
        return p[:-1]
