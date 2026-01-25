from sys import base_prefix, executable, prefix
import site
import os


def main():
    if prefix == base_prefix:
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
""")
    else:
        virtual_env: str = os.path.basename(os.environ.get("VIRTUAL_ENV", ""))
        site_packages: str = site.getsitepackages()[0]
        print(f"""
MATRIX STATUS: Welcome to the construct

Current Python: {executable}
Virtual Environment: {virtual_env}
Environment Path: {prefix}

SUCCESS: You're in an isolated environment!
Safe to install packages without affecting
the global system.

Package installation path:
{site_packages}
""")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("[Error]:", error)
