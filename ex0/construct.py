from sys import prefix, base_prefix, executable
from os import environ, path
from site import getsitepackages
from sys import stderr


def main() -> None:
    """Entry point of the script."""
    # if prefix is different than the base_prefix,
    # we are inside a virual environment.
    if prefix == base_prefix:
        # excutable return the path of the excutable
        print(f"""
MATRIX STATUS: You're still plugged in

Current Python: {executable}
Virtual Environment: None detected

WARNING: You're in the global environment!
The machines can see everything you install.

To enter the construct, run:
python -m venv matrix_env
source matrix_env/bin/activate # On Unix
matrix_env
Scripts
activate # On Windows

Then run this program again.""")
    else:
        # get the name of the env using the env variable "VIRTUAL_ENV"
        environment_name: str = path.basename(environ.get("VIRTUAL_ENV", ""))
        # getsitepackages() return a list of site packages locations
        print(f"""
MATRIX STATUS: Welcome to the construct

Current Python: {executable}
Virtual Environment: {environment_name}
Environment Path: {prefix}

SUCCESS: You're in an isolated environment!
Safe to install packages without affecting
the global system.

Package installation path:
{getsitepackages()[0]}""")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(error, stderr)
