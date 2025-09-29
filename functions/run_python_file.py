import os
import subprocess


def run_python_file(working_directory, file_path, args=[]):
    absolute_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    wor_dir_abs_path = os.path.abspath(working_directory)

    if not absolute_file_path.startswith(wor_dir_abs_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(absolute_file_path):
        return f'Error: File "{file_path}" not found.'

    if not absolute_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        command_list = ["python", absolute_file_path] + args
        report = subprocess.run(
            command_list,
            timeout=30,
            capture_output=True,
            cwd=wor_dir_abs_path,
            text=True,
        )

        output = ""

        if report.stdout:
            output += f"STDOUT: {report.stdout}\\n"

        if report.stderr:
            output += f"STDERR: {report.stderr}\\n"

        if report.returncode != 0:
            output += f"Process exited with code {report.returncode}\\n"

        if not output:
            return "No output produced."

        return output.strip()

    except Exception as e:
        return f"Error: executing Python file: {e}"
