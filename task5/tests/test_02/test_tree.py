from src.tree_utils_02.tree import Tree
import tempfile
from src.tree_utils_02.node import FileNode
import os, unittest, pytest
from unittest.mock import patch
from unittest.mock import MagicMock
import sys, requests

temp = tempfile.TemporaryFile()

def test_tree_one():
    tree = Tree()

    with pytest.raises(TypeError) as err:
         tree.construct_filenode(25, True)

    assert tree.construct_filenode(temp.name, is_dir=False) == tree.get(temp.name, False, recurse_call=False)

def test_tree_two():
    tree = Tree()

    with pytest.raises(AttributeError):
        tree.get('', recurse_call=False, dirs_only = False)

    with pytest.raises(TypeError) as err2:
        requests.get(22, recurse_call=False, dirs_only=False)

    assert None == tree.get(temp.name, True, recurse_call=True)

def test_construct_filenode():
    current_path = './'

    with pytest.raises(TypeError) as err2:
         os.path.basename(2)

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

