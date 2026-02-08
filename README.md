![Banner](https://raw.githubusercontent.com/carlosplanchon/atramentarium/refs/heads/master/assets/banner.jpeg)

# atramentarium
*Python CLI minilib to enable simple command completion.*

atramentarium means "inkpot" in late latin.

## Installation
### Install with uv:
```
uv add -U atramentarium
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
