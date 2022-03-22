import pathlib
import pandas as pd
from clumper import Clumper

if __name__ == "__main__":
    paths = pathlib.Path().glob("**/*.txt")

    blob = (Clumper(list(paths))
     .map(lambda p: {"words": p.read_text().split("\n"), "path": str(p)})
     .explode("words")
     .collect())

    pd.DataFrame(blob).to_csv("wordlist.csv", index=False)
