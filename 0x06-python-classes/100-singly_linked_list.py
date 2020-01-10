#!/usr/bin/python3
class Node:
    '''Class node
    '''
    def __init__(self, data, next_node=None):
        '''Constructor
        '''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''Getter
        '''
        return self.__data

    @data.setter
    def data(self, value):
        '''Setter
        '''
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        '''Getter
        '''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''Setter
        '''
        if value is not None and not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')
        else:
            self.__next_node = value

class SinglyLinkedList:
    '''Class SinglyLinkedList
    '''
    def __init__(self):
        '''Constructor
        '''
        self.__head = None

    def sorted_insert(self, value):
        '''Function that inserts a new Node into
        the correct sorted position in the list (increasing order)
        '''
        if self.__head is not None:
            n = Node(value)
            n.data = value
            n.next_node = self.__head
            self.__head = n
        else:
            n = Node(value, None)
            n.data = value
            n.next_node = self.__head
            self.__head = n

    def __str__(self):
        tmp = self.__head
        li = []

        while tmp is not None:
            li.append(str(tmp.data))
            tmp = tmp.next_node
        li.sort(key=int)
        return ('\n'.join(li))
