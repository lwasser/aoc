# Advent of Code - :snake: Edition

aoc 2021 for funzies

## Environment Setup 
Right now the code in here is fairly simple. It uses `numpy`, `pandas` and 
base Python 3.x. The environment below will allow you to create a similar 
environment locally.

```bash
$ conda env create -f environment.yml
$ conda activate aoc
```

## Syntax 
Cause we all love pretty code. I :heart_eyes: `black` and `flak8` so both 
are installed as pre-commit hooks using the code below: 

```bash
$ pip install -r requirements.txt
$ pre-commit install
```

Once this is setup your code will be linted (or checked via flak8) upon each
commit cause we all gotta stay honest about clean code for lyfe. :) 
