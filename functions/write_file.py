import os


def write_file(working_directory, file_path, content):
    absolute_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    wor_dir_abs_path = os.path.abspath(working_directory)

    if not absolute_file_path.startswith(wor_dir_abs_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(os.path.dirname(absolute_file_path)):
        os.makedirs(os.path.dirname(absolute_file_path))

    with open(absolute_file_path, "w") as f:
        f.write(content)

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
