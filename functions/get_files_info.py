import os

from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)


def get_files_info(working_directory, directory="."):
    absolute_path = os.path.abspath(os.path.join(working_directory, directory))

    wor_dir_abs_path = os.path.abspath(working_directory)
    if not absolute_path.startswith(wor_dir_abs_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(absolute_path):
        return f'Error: "{directory}" is not a directory'

    try:
        items = os.listdir(absolute_path)
        info_list = []

        for item in items:
            item_path = os.path.join(absolute_path, item)

            item_size = os.path.getsize(item_path)
            item_dir = os.path.isdir(item_path)

            info_string = f"- {item}: file_size = {item_size} bytes, is_dir={item_dir}"

            info_list.append(info_string)

        return "\n".join(info_list)

    except Exception as e:
        return f"Error: {e}"
