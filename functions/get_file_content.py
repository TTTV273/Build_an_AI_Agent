import os

from google.genai import types

MAX_CHARS = 10000

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the content of a specified file, truncated at 10,000 characters, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to read from, relative to the working directory.",
            ),
        },
    ),
)


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
