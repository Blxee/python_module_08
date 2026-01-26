from sys import stderr
from importlib.metadata import version, metadata, PackageNotFoundError

def main() -> None:
    """"""
    packages: list[str] = ["pandas", "requests", "matplotlib"]
    packages_installed = True

    for package in packages:
        try:
            ver = version(package)
            desc = metadata(package).get("Summary")
            print(f"[\x1b[32mOK\x1b[0m] {package} ({ver}) - {desc} ready")
        except PackageNotFoundError:
            packages_installed = False
            print(f"[\x1b[31mKO\x1b[0m] {package} is not installed")

    if not packages_installed:
        print("""\
To install the missing dependencies, you can either:
\t* Use Poetry:
\t\t- Make sure poetry is installed.
\t\t- Run: "poetry install" inside ex1/ to install the dependencies.
\t\t- Then to run the script use: "poetry run python3 loading.py".
\t* Use pip:
\t\t- Install the requirements using: "pip install -r requirements.txt"
\t\t- Then run the program using: "python3 loading.py"\
        """)
        exit(1)

    print("all packages are installed")

    file_name: str = "matrix_analysis.png"

if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("[Error]:", error, file=stderr)

"""
$> python loading.py

LOADING STATUS: Loading programs...
 
Checking dependencies:
[OK] pandas (2.1.0) - Data manipulation ready
[OK] requests (2.31.0) - Network access ready
[OK] matplotlib (3.7.2) - Visualization ready

Analyzing Matrix data...
Processing 1000 data points...
Generating visualization...

Analysis complete!
Results saved to: matrix_analysis.png
"""
