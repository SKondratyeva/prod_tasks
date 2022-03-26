from src.tree_utils_02.size_tree import SizeTree
from src.tree_utils_02.size_node import FileSizeNode
import os, sys

def test_size_tree_0():
    size = SizeTree()
    current_dir = os.listdir()[-2]
    BLOCK_SIZE = os.path.getsize(current_dir)

    filename = os.path.basename(current_dir)
    fzn = FileSizeNode(
        name=current_dir,
        is_dir=False,
        children=[],
        size=BLOCK_SIZE
    )
    assert fzn == size.construct_filenode(current_dir, False)


def test_size_tree_1():
    size = SizeTree()
    BLOCK_SIZE = 4096
    filename = os.path.basename('test_tree.py')
    fzn = FileSizeNode(
        name='test_tree.py',
        is_dir=True,
        children=[],
        size=BLOCK_SIZE
    )
    assert fzn == size.construct_filenode(r'test_tree.py', True)



def test_update_filenode():
    parentdir = os.path.dirname('test_02/')
    sys.path.insert(0, parentdir)
    size = SizeTree()
    BLOCK_SIZE = 4096
    path = r'test_tree.py'
    filename = os.path.basename(path)
    child = FileSizeNode(
            name=filename,
            is_dir=True,
            children=[],
            size=BLOCK_SIZE
        )

    fzn = FileSizeNode(
        name= filename,
        is_dir=True,
        children=[child],
        size=BLOCK_SIZE*2
    )
    assert fzn == size.update_filenode(fzn)




