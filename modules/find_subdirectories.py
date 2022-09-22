import sys
from pathlib import Path


file_list = [dir_object for dir_object in Path(sys.argv[1]).glob('**/*')]

