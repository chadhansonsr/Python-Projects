import os


def find_files(suffix, path):
    matches = []
    for entry in os.listdir(path):
        path_dir = os.path.join(path, entry)
        if os.path.isfile(path_dir) and path_dir.endswith(suffix):
            matches.append(path_dir)
        elif os.path.isdir(path_dir):
            matches.extend(find_files(suffix, path_dir))
    return matches


search1 = find_files(".c", r"\Users\t9349ch\Desktop\SWX\Udacity\Data Structures Project")  # noqa
print("\nHere are the files ending with .c.")
for search in search1:
    print(search)
    # search will return
    # \Users\t9349ch\Desktop\SWX\Udacity\Data Structures Project\testdir\t1.c  # noqa
    # \Users\t9349ch\Desktop\SWX\Udacity\Data Structures Project\testdir\subdir1\a.c  # noqa
    # \Users\t9349ch\Desktop\SWX\Udacity\Data Structures Project\testdir\subdir3\subsubdir1\b.c  # noqa
    # \Users\t9349ch\Desktop\SWX\Udacity\Data Structures Project\testdir\subdir5\a.c  # noqa

search2 = find_files(".jpg", r"\Users\t9349ch\Desktop\SWX\Udacity\Data Structures Project")  # noqa
print("\n\nHere are the files ending with .jpg.")
for search in search2:
    print(search)
    # search will be blank because there are no .jpg files

search3 = find_files(".c", r"\Users\t9349ch\Desktop\SWX\Udacity")  # noqa
print("\n\nHere are the files containing with .c.")
for search in search3:
    print(search)
    # this will search a level above the current folder in the directory  # noqa
    # \Users\t9349ch\Desktop\SWX\Udacity\Data Structures Project\testdir\subdir1\a.c  # noqa
    # \Users\t9349ch\Desktop\SWX\Udacity\Data Structures Project\testdir\subdir3\subsubdir1\b.c  # noqa
    # \Users\t9349ch\Desktop\SWX\Udacity\Data Structures Project\testdir\subdir5\a.c  # noqa
    # \Users\t9349ch\Desktop\SWX\Udacity\Data Structures Project\testdir\t1.c
    # \Users\t9349ch\Desktop\SWX\Udacity\Side Projects\Python\venv\Lib\site-packages\httptools\parser\parser.c  # noqa
    # \Users\t9349ch\Desktop\SWX\Udacity\Side Projects\Python\venv\Lib\site-packages\httptools\parser\url_parser.c  # noqa
    # \Users\t9349ch\Desktop\SWX\Udacity\Side Projects\Python\venv\Lib\site-packages\markupsafe\_speedups.c  # noqa
    # \Users\t9349ch\Desktop\SWX\Udacity\Side Projects\Python\venv\Lib\site-packages\websockets\speedups.c  # noqa
