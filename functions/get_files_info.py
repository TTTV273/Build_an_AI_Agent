import os


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
