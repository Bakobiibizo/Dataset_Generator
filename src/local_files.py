import os


def save_local_file(data):
    dir_files = os.listdir("tmp")
    dir_path = "tmp/"
    i = [i for i in range(len(dir_files)) if dir_files[i].endswith(".txt")]
    filename = f"{dir_path}temp{i}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(data)

    return filename
