from sys import stderr
from importlib.metadata import version, metadata, PackageNotFoundError


def main() -> None:
    """Demonstrate pip and poetry usage."""
    # define the list of depenedencies
    packages: list[str] = ["pandas", "requests", "matplotlib"]
    packages_installed = True

    # check if all packages are available
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

    import requests
    from pandas import DataFrame
    import matplotlib.pyplot as plt

    file_name: str = "matrix_analysis.png"

    # query the dummyjson api for some dummy json data
    products = requests.get("https://dummyjson.com/products").json()[
        "products"
    ]
    print(f"""
Analyzing Matrix data...
Processing {len(products)} data points...
Generating visualization...

Analysis complete!
Results saved to: {file_name}""")

    # create a pandas datafram from the list of products
    data_fram: DataFrame = DataFrame(products)
    # plot the received data using matplotlib
    data_fram.plot.scatter(x="price", y="rating")
    plt.xlabel("Price")
    plt.xscale("log")
    plt.ylabel("Rating")
    plt.title("Product price vs rating")
    # save the graph to file_name
    plt.savefig(file_name)


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("[Error]:", error, file=stderr)
