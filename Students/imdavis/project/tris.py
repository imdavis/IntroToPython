#!/usr/bin/env python2.7

"""
A class to create triangle objects
"""

class Tri(object):
    def __init__(self, ntri, node0, node1, node2, neighbor=None):
        self.tri = ntri
        self.node0 = node0
        self.node1 = node1
        self.node2 = node2
        self.neighbor = neighbor

    @property
    def tri(self):
        return self._tri
    @tri.setter
    def tri(self, tri):
        if not isinstance(tri, int):
            raise ValueError("Triangle number must be an int")
        else:
            self._tri = tri

    @property
    def node0(self):
        return self._node0
    @node0.setter
    def node0(self, node0):
        if not isinstance(node0, int):
            raise ValueError("Triangle must be initialized with node0 number which is an int")
        else:
            self._node0 = node0

    @property
    def node1(self):
        return self._node1
    @node1.setter
    def node1(self, node1):
        if not isinstance(node1, int):
            raise ValueError("Triangle must be initialized with node1 number which is an int")
        else:
            self._node1 = node1

    @property
    def node2(self):
        return self._node2
    @node2.setter
    def node2(self, node2):
        if not isinstance(node2, int):
            raise ValueError("Triangle must be initialized with node2 number which is an int")
        else:
            self._node2 = node2

    @property
    def neighbor(self):
        return self._neighbor
    @neighbor.setter
    def neighbor(self, neighbor):
        if not neighbor:
            self._neighbor = []
        elif not (neighbor == "external" or isinstance(neighbor, int) ):
            raise TypeError("Triangle neighbor must be either 'external' or type int")
        else:
            self._neighbor = [neighbor]
