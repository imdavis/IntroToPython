#!/usr/bin/env python2.7

"""
A class to create node objects
"""

class Node(object):
    def __init__(self, nnode, x_coord, y_coord, z_coord):
        self.node = nnode
        self.x = x_coord
        self.y = y_coord
        self.z = z_coord

    @property
    def node(self):
        return self._node
    @node.setter
    def node(self, node):
        if not isinstance(node, int):
            raise TypeError("Node number must be an integer")
        else:
            self._node = int(node)

    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError("Node x coordinate must be an int or float")
        else:
            self._x = float(x)

    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, y):
        if not isinstance(y, (int, float)):
            raise TypeError("Node y coordinate must be an int or float")
        else:
            self._y = float(y)

    @property
    def z(self):
        return self._z
    @z.setter
    def z(self, z):
        if not isinstance(z, (int, float)):
            raise TypeError("Node z coordinate must be an int or float")
        else:
            self._z = float(z)

if __name__ == '__main__':
    node = {1:Node(1, -2.34, 1.34, 15.367), 2:Node(2, -12.234, 14.52, -6.78), 3:Node(3, 5.78, -12.34, -15.678)}
    print node[1].node
    print node[1].x
    print node[2].y
    print node[3].z
    anode = node[2]
    print anode.node
    print anode.x
    print anode.y
    print anode.z

