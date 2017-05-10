import pathlib

cur_path = pathlib.Path()
print("Current path is ", cur_path.cwd())
print("Current path contains ", list(cur_path.iterdir()))
