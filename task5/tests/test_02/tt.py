from src.tree_utils_02.tree import Tree
tree = Tree()
import sys,os
import tempfile
from src.tree_utils_02.node import FileNode
import os, unittest, pytest
from unittest.mock import patch
from unittest.mock import MagicMock
import sys, requests

temp = tempfile.TemporaryFile()




def test_not_dir():
    while str(os.getcwd())[-5:] != 'task5':
        os.chdir("..")

    with pytest.raises(AttributeError):
         path_to_file = r'main.py'
         tree.get(path_to_file, recurse_call=False, dirs_only=True)