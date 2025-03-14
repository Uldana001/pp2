import os

def c(path):
    print(f"Path: {path}")
    print("Exists: ", os.path.exists(path))
    print("Readable: ", os.access(path, os.R_OK))
    print("Writable: ", os.access(path, os.W_OK))
    print("Executable: ", os.access(path, os.X_OK))

path = "/path/to/check"

c(path)