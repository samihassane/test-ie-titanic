import pandas as pd

def extract_titles(name):
    return name.split()[0]


print(__name__)

if __name__ == "__main__":
    print("Script ran successfull")
else:
    print("Thank you for importing str_utils")