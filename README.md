# wordlist

This project contains a .csv file that represents the data from the [wordlist project](https://github.com/imsky/wordlists). It's merely added for convenience, any credit should go to the other project. This project also hosts a script that was used to parse the seperate text files into a single csv document. 

## Loading 

If you want to load this project from pandas, it's just a one-liner. 

```python
import pandas as pd

url = "https://raw.githubusercontent.com/koaning/wordlist/main/wordlist.csv"
df = pd.read_csv(url, converters = {'word': str, 'path': str})
df
```
