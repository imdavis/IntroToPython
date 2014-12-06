#!/usr/bin/env python2.7

from nodes import Node
from tets import Tet
from tris import Tri
import pytest

# ------------ #
# Node testing
# ------------ #
def test_init_node():
    anode = Node(5, -2.34, 1.34, 15.367)
    assert anode.node == 5
    assert anode.x == -2.34
    assert anode.y == 1.34
    assert anode.z == 15.367

def test_init_node_no_args():
    with pytest.raises(TypeError):
        Node()

def test_node_number_isint():
    with pytest.raises(TypeError):
        Node(1.11, -2.34, 1.34, 15.367)
    with pytest.raises(TypeError):
        Node(-1.11, -2.34, 1.34, 15.367)
    with pytest.raises(TypeError):
        Node("astring", -2.34, 1.34, 15.367)

def test_node_coord():
    with pytest.raises(TypeError):
        Node(3, "astring", 1.34, 15.367)
    with pytest.raises(TypeError):
        Node(3, -2.34, "astring", 15.367)
    with pytest.raises(TypeError):
        Node(3, -2.34, 1.34, "astring")

# define a dict of dummy nodes to use in testing below
node = {1:Node(1, -2.34, 1.34, 15.367), 17:Node(17, -12.234, 14.52, -6.78), 
        34:Node(34, 5.78, -12.34, -15.678), 18:Node(18, 6.98, -1.12, -34.56)}

# ---------------- #
# Triangle testing
# ---------------- #
def test_init_tri():
    atri = Tri(15, 7, 11, 14, "external")
    assert atri.tri == 15
    assert atri.node0 == 7
    assert atri.node1 == 11
    assert atri.node2 == 14
    assert atri.neighbor == ["external"]
    atri = Tri(15, 7, 11, 14, 32)
    assert atri.neighbor == [32]

def test_init_tri2():
    atri = Tri(13, node[17].node, node[34].node, node[18].node, "external")
    assert atri.tri == 13
    assert atri.node0 == 17
    assert atri.node1 == 34
    assert atri.node2 == 18
    assert atri.neighbor == ["external"]

def test_init_tri_no_args():
    with pytest.raises(TypeError):
        atri = Tri()

def test_init_tri_not_node():
    with pytest.raises(ValueError):
        Tri(43.23, node[17].node, node[34].node, node[18].node)
    with pytest.raises(ValueError):
        Tri("astring", node[17].node, node[34].node, node[18].node)
    with pytest.raises(ValueError):
        Tri(13, node[17].x, node[34].node, node[18].node)
    with pytest.raises(ValueError):
        Tri(13, node[17].node, "astring", node[18].node)
    with pytest.raises(ValueError):
        Tri(13, node[17].node, node[34].node, 32.333)
    with pytest.raises(TypeError):
        Tri(13, node[17].node, node[34].node, node[18].node, "blah")
    with pytest.raises(TypeError):
        Tri(13, node[17].node, node[34].node, node[18].node, 2.34)

# define some dummy triangles to use in testing below
triangle0 = Tri(13, node[17].node, node[34].node, node[18].node)
triangle1 = Tri(44, node[1].node, node[17].node, node[18].node)
triangle2 = Tri(72, node[18].node, node[1].node, node[34].node)
triangle3 = Tri(2, node[17].node, node[34].node, node[1].node)

# ------------------- #
# Tetrahedron testing #
# ------------------- #
def test_init_tet():
    atet = Tet(42, node[1], node[17], node[34], node[18], 17)
    assert atet.tet == 42
    assert atet.region == 17
    assert isinstance(atet.node0, Node)
    assert isinstance(atet.node1, Node)
    assert isinstance(atet.node2, Node)
    assert isinstance(atet.node3, Node)
    assert atet.node0.x == -2.34
    assert atet.node1.y == 14.52
    assert atet.node2.z == -15.678
    assert atet.node3.node == 18

def test_init_tet_no_args():
    with pytest.raises(TypeError):
        atet = Tet()

def test_init_tet_not_node():
    with pytest.raises(TypeError):
        Tet(42, 52, node[17], node[34], node[18], 17)
    with pytest.raises(TypeError):
        Tet(42, node[1], "astring", node[34], node[18], 17)
    with pytest.raises(TypeError):
        Tet(42, node[1], node[17], -23.34, node[18], 17)
    with pytest.raises(TypeError):
        Tet(42, node[1], node[17], node[34], 23, 17)

def test_init_tri0_in_tet():
    atet = Tet(42, node[1], node[17], node[34], node[18], 17)
    atet.tri0 = triangle0
    assert atet.tri0.tri == 13
    assert atet.tri0.node0 == 17
    assert atet.tri0.node1 == 34
    assert atet.tri0.node2 == 18
    with pytest.raises(TypeError):
        atet.tri0 = 14.233

def test_init_tri1_in_tet():
    atet = Tet(42, node[1], node[17], node[34], node[18], 17)
    atet.tri1 = triangle1
    assert atet.tri1.tri == 44
    assert atet.tri1.node0 == 1
    assert atet.tri1.node1 == 17
    assert atet.tri1.node2 == 18
    with pytest.raises(TypeError):
        atet.tri1 = "astring"

def test_init_tri2_in_tet():
    atet = Tet(42, node[1], node[17], node[34], node[18], 17)
    atet.tri2 = triangle2
    assert atet.tri2.tri == 72
    assert atet.tri2.node0 == 18
    assert atet.tri2.node1 == 1
    assert atet.tri2.node2 == 34
    with pytest.raises(TypeError):
        atet.tri2 = 104

def test_init_tri3_in_tet():
    atet = Tet(42, node[1], node[17], node[34], node[18], 17)
    atet.tri3 = triangle3
    assert atet.tri3.tri == 2
    assert atet.tri3.node0 == 17
    assert atet.tri3.node1 == 34
    assert atet.tri3.node2 == 1
    with pytest.raises(TypeError):
        atet.tri3 = node[1]
