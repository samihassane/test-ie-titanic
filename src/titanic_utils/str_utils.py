import pandas as pd


def extract_titles(name):
    # if name.contains("."):
    # if pd.Series(name).str.contains(".", regex=False)[0]:
    if "." in name:
        return name.split()[0]
    else:
        raise ValueError()


print(__name__)

if __name__ == "__main__":
    print("Script ran successfull")
else:
    print("Thank you for importing str_utils")
