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

def test_smth(temp_file):
    print('the string is ',str(temp_file))