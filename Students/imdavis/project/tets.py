#!/usr/bin/env python2.7

"""
A class to create tetrahedron objects
"""

from nodes import Node
from tris import Tri

class Tet(object):
    def __init__(self, ntet, node0, node1, node2, node3, region_flag, 
                 tri0=None, tri1=None, tri2=None, tri3=None):
        self.tet = ntet
        self.node0 = node0
        self.node1 = node1
        self.node2 = node2
        self.node3 = node3
        self.region = region_flag
        self.tri0 = tri0
        self.tri1 = tri1
        self.tri2 = tri2
        self.tri3 = tri3

    @property
    def tet(self):
        return self._tet
    @tet.setter
    def tet(self, tet):
        if not isinstance(tet, int):
            raise ValueError("Tetrahedron number must be an int")
        else:
            self._tet = tet

    @property
    def node0(self):
        return self._node0
    @node0.setter
    def node0(self, node0):
        if not isinstance(node0, Node):
            raise TypeError('Attempted to initialize Tet with a node0 which is not of type "Node"')
        else:
            self._node0 = node0

    @property
    def node1(self):
        return self._node1
    @node1.setter
    def node1(self, node1):
        if not isinstance(node1, Node):
            raise TypeError('Attempted to initialize Tet with a node1 which is not of type "Node"')
        else:
            self._node1 = node1

    @property
    def node2(self):
        return self._node2
    @node2.setter
    def node2(self, node2):
        if not isinstance(node2, Node):
            raise TypeError('Attempted to initialize Tet with a node2 which is not of type "Node"')
        else:
            self._node2 = node2

    @property
    def node3(self):
        return self._node3
    @node3.setter
    def node3(self, node3):
        if not isinstance(node3, Node):
            raise TypeError('Attempted to initialize Tet with a node3 which is not of type "Node"')
        else:
            self._node3 = node3

    @property
    def tri0(self):
        return self._tri0
    @tri0.setter
    def tri0(self, tri0):
        if tri0 and (not isinstance(tri0, Tri) ):
            raise TypeError('Attempted to initialize Tet with a tri0 which is not of type "Tri"')
        else:
            self._tri0 = tri0

    @property
    def tri1(self):
        return self._tri1
    @tri1.setter
    def tri1(self, tri1):
        if tri1 and (not isinstance(tri1, Tri) ):
            raise TypeError('Attempted to initialize Tet with a tri1 which is not of type "Tri"')
        else:
            self._tri1 = tri1

    @property
    def tri2(self):
        return self._tri2
    @tri2.setter
    def tri2(self, tri2):
        if tri2 and (not isinstance(tri2, Tri) ):
            raise TypeError('Attempted to initialize Tet with a tri2 which is not of type "Tri"')
        else:
            self._tri2 = tri2

    @property
    def tri3(self):
        return self._tri3
    @tri3.setter
    def tri3(self, tri3):
        if tri3 and (not isinstance(tri3, Tri) ):
            raise TypeError('Attempted to initialize Tet with a tri3 which is not of type "Tri"')
        else:
            self._tri3 = tri3

