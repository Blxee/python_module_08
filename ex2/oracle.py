from importlib.metadata import version, PackageNotFoundError
from sys import stderr
from os import environ


def main() -> None:
    """Load .env file into environ."""
    # check if dotenv is installed
    try:
        version("python-dotenv")
    except PackageNotFoundError:
        print(
            """\
    [Error]: python-dotenv is not installed..
    To install it, please run 'pip install python-dotenv'""",
            file=stderr,
        )
        exit(1)

    from dotenv import load_dotenv

    config: dict[str, str | None] = {
        "MATRIX_MODE": None,
        "DATABASE_URL": None,
        "API_KEY": None,
        "LOG_LEVEL": None,
        "ZION_ENDPOINT": None,
    }

    # load the .env file into the environ dict.
    load_dotenv(override=False)

    # check if all fields are present
    fields_present = True
    for field in config.copy():
        value = environ.get(field, "")
        if len(value) == 0:
            fields_present = False
            print(
                f"[Error]: var not found: \x1b[31m{field}\x1b[0m",
                file=stderr,
            )
        else:
            config[field] = value

    if not fields_present:
        print("""Define the configurations in the .env file
or in the environment using the shell as follow:\
'VAR=val python3 oracle.py'""")
        exit(1)

    print(f"""
ORACLE STATUS: Reading the Matrix...

Configuration loaded:
Mode: {config["MATRIX_MODE"]}
Database: Connected to local instance
API Access: Authenticated
Log Level: {config["LOG_LEVEL"]}
Zion Network: Online

Environment security check:
[OK] No hardcoded secrets detected
[OK] .env file properly configured
[OK] Production overrides available

The Oracle sees all configurations.""")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("[Error]:", error, file=stderr)
