#!/usr/bin/env python2.7

from nodes import Node
from tets import Tet
from tris import Tri

def make_tet_tri_list(atet):
    """
    This will make a list of lists of node numbers composing each 
    triangle face for a given tet such that 'tris[0]' is triangle0 for
    the cannonical tetrahedron (triangle0 = node1, node2, node3), etc.
    """
    tris = [[atet.node1.node, atet.node2.node, atet.node3.node]]
    tris.append([atet.node0.node, atet.node2.node, atet.node3.node])
    tris.append([atet.node0.node, atet.node1.node, atet.node3.node])
    tris.append([atet.node0.node, atet.node1.node, atet.node2.node])
    return tris

def make_sorted_tri_nodes_set(tri_nodes):
    """
    Function which takes a list of node numbers, sorts them,
    and returns a set containing a tuple of the sorted nodes.  This 
    can then be used with 'known_tri_nodes' and issubset to test if the
    triangle has been defined yet or not.
    """
    tri_nodes.sort()
    return tuple(tri_nodes)

def new_tri_obj(triangles, tri_nodes):
    for known_tri_num, known_tri_nodes in triangles.items():
        if (tri_nodes == known_tri_nodes):
            tri_num = known_tri_num
            break
    return Tri(tri_num, tri_nodes[0], tri_nodes[1], tri_nodes[2])

# create a test node
nodes = {2:Node(2, -2.5, 2.5, 2.5), 3:Node(3, -2.5, -2.5, 2.5),
         4:Node(4, -7.5, -2.5, 2.5), 7:Node(7, -2.5, -2.5, -2.5),
         8:Node(8, -7.5, -2.5, -2.5), 17:Node(17, -5.0, 0.0, 0.0)}

# create some test tets
tetrahedron = {}
tetrahedron[9] = Tet(9, nodes[3], nodes[2], nodes[17], nodes[7], 2)
tetrahedron[10] = Tet(10, nodes[8], nodes[3], nodes[7], nodes[17], 2)
tetrahedron[11] = Tet(11, nodes[4], nodes[8], nodes[17], nodes[3], 3)

# create the empty triangle dictionary
triangles = {}
known_tri_nodes = set(triangles.values())
new_tri_num = 0

for tet in tetrahedron.keys():
    tet_tri_list = make_tet_tri_list(tetrahedron[tet])
    tet_tri_obj = [tetrahedron[tet].tri0, tetrahedron[tet].tri1,
                   tetrahedron[tet].tri2, tetrahedron[tet].tri3]

    for tet_tri, tri_nodes in enumerate(tet_tri_list):
        test_tri = make_sorted_tri_nodes_set(tri_nodes)
        # test to see if triangle is already defined
        if (test_tri in known_tri_nodes):
            # if the triangle is known, set it for the current tet tri
            tet_tri_obj[tet_tri] = new_tri_obj(triangles, tuple(tri_nodes))
        else:
            # if the triangle is not known, update the triangle list, and 
            # set the triangle for the current tet tri
            tet_tri_obj[tet_tri] = Tri(new_tri_num, tri_nodes[0], 
                                       tri_nodes[1], tri_nodes[2])
            triangles[new_tri_num] = tuple(tri_nodes)
            known_tri_nodes = set(triangles.values())
            new_tri_num += 1

print triangles




