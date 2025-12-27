import alchemy

if __name__ == "__main__":
    print("=== Sacred Scroll Mastery ===")

    print("\nTesting direct module access:")

    print("alchemy.elements.create_fire():", alchemy.elements.create_fire())
    print("alchemy.elements.create_water():", alchemy.elements.create_water())
    print("alchemy.elements.create_earth():", alchemy.elements.create_earth())
    print("alchemy.elements.create_air():", alchemy.elements.create_air())

    print("\nTesting package-level access (controlled by __init__.py):")

    print("alchemy.create_fire():", alchemy.create_fire())
    print("alchemy.create_water():", alchemy.create_water())

    try:
        print("alchemy.create_earth(): ", end="")
        alchemy.create_earth()
    except AttributeError as error:
        print("AttributeError - not exposed")

    try:
        print("alchemy.create_air(): ", end="")
        alchemy.create_air()
    except AttributeError as error:
        print("AttributeError - not exposed")

    version = alchemy.__version__
    author = alchemy.__author__
    print("\nPackage metadata:")
    print("Version:", version)
    print("Author:", author)
