# atramentarium
*Python3 prompt with simple command completion.*

atramentarium means "inkpot" in late latin.

## Installation
### Install with pip
```
pip install -U atramentarium
```

## Usage
```
In [1]: import atramentarium

In [2]: prompt(
    command_processing_function=lambda cmd: print(cmd),
    command_list=["ALICE", "BOB"]
    )
> # Hit tab.
ALICE  BOB
>
```
