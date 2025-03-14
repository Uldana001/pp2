import os

def c(path):
    print("Directories: ")
    print([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])

    print("\nFiles: ")
    print([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])

    print("\nAll Directories and Files: ")
    print(os.listdir(path))

path = "."
c(path)