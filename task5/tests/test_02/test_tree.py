from src.tree_utils_02.tree import Tree
import tempfile, sys, requests, pytest
from src.tree_utils_02.node import FileNode
import os, unittest, pytest
from unittest.mock import patch
from unittest.mock import MagicMock


@pytest.fixture
def temp_file(tmpdir):
    file = tmpdir.mkdir("sub").join("test_file.txt")
    file.write('blah')
    return file


def test_tree_one(temp_file):
    tree = Tree()
    assert tree.construct_filenode(temp_file, is_dir=False) == tree.get(temp_file, False, recurse_call=False)


def test_not_dir():
    while str(os.getcwd())[-5:] != 'task5':
        os.chdir("..")

    with pytest.raises(AttributeError):
        tree = Tree()
        path_to_file = r'main.py'
        tree.get(path_to_file, recurse_call=False, dirs_only=True)


def test_tree_one_attr():
    tree = Tree()

    with pytest.raises(TypeError) as err:
        tree.construct_filenode(25, True)


def test_tree_one_one():
    tree = Tree()
    with pytest.raises(TypeError) as err2:
        tree.construct_filenode(5, is_dir=False) == tree.get(temp_file, False, recurse_call=False)


def test_tree_three():
    tree = Tree()
    with pytest.raises(AttributeError):
        tree.get(22, True, recurse_call=True)


def test_tree_four():
    tree = Tree()
    with pytest.raises(TypeError) as err2:
        requests.get(22, recurse_call=False, dirs_only=False)


def test_tree_two():
    tree = Tree()

    with pytest.raises(AttributeError):
        tree.get('', recurse_call=False, dirs_only=True)


def test_tree_three(temp_file):
    tree = Tree()
    assert None == tree.get(temp_file, True, recurse_call=True)


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
    assert test_node == tree.construct_filenode(current_path, is_dir)


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

    assert None == tree.filter_empty_nodes(test_node, current_path='.')


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
    child = FileNode(
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
