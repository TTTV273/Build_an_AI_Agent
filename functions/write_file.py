import os

from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes or overwrites a file with the specified content, creating directories if needed, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to write to, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file.",
            ),
        },
    ),
)


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
