from src.tree_utils_02.size_tree import SizeTree
from src.tree_utils_02.size_node import FileSizeNode
import os
from src.tree_utils_02.tree import Tree

def test_size_tree0():
    size = SizeTree()
    BLOCK_SIZE = 2
    fzn = FileSizeNode(
        name='test_tree.py',
        is_dir=False,
        children=[],
        size=BLOCK_SIZE
    )
    assert fzn == size.construct_filenode( r'test_02/test_tree.py', False)


def test_size_tree1():
    size = SizeTree()
    BLOCK_SIZE = 4096
    fzn = FileSizeNode(
        name='test_tree.py',
        is_dir=True,
        children=[],
        size=BLOCK_SIZE
    )
    assert fzn == size.construct_filenode(r'test_02/test_tree.py', True)


def test_update_filenode():
    size = SizeTree()
    BLOCK_SIZE = 4096
    fzn = FileSizeNode(
        name='test_tree.py',
        is_dir=True,
        children=[],
        size=BLOCK_SIZE
    )
    assert fzn == size.update_filenode(fzn)




