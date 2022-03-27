from src.tree_utils_02.tree import Tree
import tempfile
from src.tree_utils_02.node import FileNode
import os, unittest
from unittest.mock import patch
from unittest.mock import MagicMock
import sys

temp = tempfile.TemporaryFile()

class MyTestCase(unittest.TestCase):

    def test_no_path(self):
        with self.assertRaises(AttributeError):
            tree = Tree()
            tree.get('', recurse_call=False, dirs_only = False)


if __name__ == '__main__':
    unittest.main()

class MyTestCase2(unittest.TestCase):
    temp = tempfile.TemporaryFile()
    current_path = temp.name
    def test_no_path(self):

        with self.assertRaises(AttributeError):
            temp = tempfile.TemporaryFile()
            current_path = temp.name
            tree = Tree()
            tree.get(current_path, recurse_call=False, dirs_only = True)

        with self.assertRaises(TypeError):
            tree = Tree()
            tree.construct_filenode(25, True)
            tree.get(1, recurse_call=False, dirs_only=True)


if __name__ == '__main__':
    unittest.main()


def test_tree_one():
    tree = Tree()
    assert tree.construct_filenode(temp.name, is_dir=False) == tree.get(temp.name, False, recurse_call=False)

def test_tree_two():
    tree = Tree()
    assert None == tree.get(temp.name, True, recurse_call=True)

def test_construct_filenode():
    current_path = './'
    filename = os.path.basename(current_path)
    is_dir = True
    tree = Tree()
    test_node = FileNode(
            name=filename,
            is_dir=is_dir,
            children=[]
        )
    assert test_node == tree.construct_filenode( current_path, is_dir)



def test_update_filenode():
    is_dir = True
    tree = Tree()
    current_path = './'
    filename = os.path.basename(current_path)
    test_node = FileNode(
        name=filename,
        is_dir=is_dir,
        children=[]
    )
    assert test_node == tree.update_filenode(test_node)

def test_filter_empty_nodes():
    is_dir = False
    tree = Tree()
    current_path = './'
    filename = os.path.basename(current_path)
    test_node = FileNode(
        name=filename,
        is_dir=is_dir,
        children=[]
    )

    assert None == tree.filter_empty_nodes(test_node, current_path ='.')

def test_none_child():
    is_dir = False
    tree = Tree()
    current_path = './'
    filename = os.path.basename(current_path)
    test_node = FileNode(
        name=filename,
        is_dir=is_dir,
        children=[]
    )

    assert None != tree.get(current_path, True, recurse_call=True)

sys.modules['shutil.rmtree'] = MagicMock()
def test_filter():
    is_dir = True
    tree = Tree()
    current_path = './'
    filename = os.path.basename(current_path)
    test_node = FileNode(
        name=filename,
        is_dir=is_dir,
        children=[]
    )

    assert MagicMock() == tree.filter_empty_nodes(test_node, current_path='./')


@patch('shutil.rmtree')
def test_filter(rm_mock):
    rm_mock.return_value = 'REMOVED'
    is_dir = True
    tree = Tree()
    current_path = './'
    filename = os.path.basename(current_path)
    test_node = FileNode(
        name=filename,
        is_dir=is_dir,
        children=[]
    )

    assert None == tree.filter_empty_nodes(test_node, current_path='./')

@patch('shutil.rmtree')
def test_filter(rm_mock):
    rm_mock.return_value = 'REMOVED'
    is_dir = True
    tree = Tree()
    current_path = './'
    filename = os.path.basename(current_path)
    child =  FileNode(
        name=filename,
        is_dir=is_dir,
        children=[]
    )

    test_node = FileNode(
        name=filename,
        is_dir=is_dir,
        children=[child]
    )

    assert None == tree.filter_empty_nodes(test_node, current_path='./')

