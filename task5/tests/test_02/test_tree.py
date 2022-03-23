from src.tree_utils_02.tree import Tree
import tempfile
from src.tree_utils_02.node import FileNode


temp = tempfile.TemporaryFile()

def test_tree0():
    tree = Tree()
    assert tree.construct_filenode(temp.name, is_dir=False) == tree.get(temp.name, False, recurse_call=False)

def test_tree1():
    tree = Tree()
    assert None == tree.get(temp.name, True, recurse_call=True)

def test_tree2():
    tree = Tree()
    current_path = 'test_02/'
    assert FileNode(name='', is_dir=True, children=[FileNode(name='__pycache__', is_dir=True, children=[])]) == tree.get(current_path, True, recurse_call=True)