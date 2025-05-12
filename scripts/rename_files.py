import os

run_dir = os.path.abspath(os.getcwd())

for file in os.listdir(run_dir):
    filename, fileext = os.path.splitext(file)
    print(filename)
    print(fileext)
    print(os.path.isdir(file))
