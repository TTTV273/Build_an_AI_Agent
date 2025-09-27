import os

MAX_CHARS = 10000


def get_file_content(working_directory, file_path):
    absolute_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    wor_dir_abs_path = os.path.abspath(working_directory)

    if not absolute_file_path.startswith(wor_dir_abs_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(absolute_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(absolute_file_path, "r", encoding="utf-8") as f:
            file_content_string = f.read(MAX_CHARS)

        if len(file_content_string) == MAX_CHARS:
            file_content_string += (
                f'[...File "{file_path}" truncated at 10000 characters]'
            )
        return file_content_string

    except Exception as e:
        return f"Error: {e}"
