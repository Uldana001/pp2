import os
def c(path):
    if os.path.exists(path):
        print(f"Path exists: {path}")
        print("Directory: ", os.path.dirname(path))
        print("Filename: ", os.path.basename(path))
    else:
        print(f"Path does not exist: {path}")

path = "/path/tp/check"
c(path)

