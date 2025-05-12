import os
import uuid

run_dir = os.path.abspath(os.getcwd())
allowed_extensions = (".png", ".heic", ".jpg", ".jpeg")


def run_rename(dir=run_dir):
    print(dir)
    for file in os.listdir(dir):
        path = dir + "/" + file
        if os.path.isdir(path):
            run_rename(path)
            continue

        file_name, file_extension = os.path.splitext(file)
        if file_extension in allowed_extensions:
            new_name = dir + "/" + str(uuid.uuid4().hex) + file_extension
            rename_file(path, new_name)
        else:
            print("skipped, unsupported file ext: " + file)


def rename_file(file, new_name):
    os.rename(file, new_name)


run_rename()
