# BillSplitter
Are you tired of the hassle and awkwardness of splitting the bill when dining out with friends? We've got the perfect solution for you! With BillSplitter, you can say goodbye to the headache of manual calculations and ensure everyone pays their fair share effortlessly.

## Installation

```
# clone the repo
$ git clone https://github.com/bltomlin/BillSplitter

# change the working directory to BillSplitter
$ cd BillSplitter

# run from CLI
$ python billsplitter.py
```

## Examples

```
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1: The feature is used

Enter the number of friends joining (including you):
> 5

Enter the name of every friend (including you), each on a new line:
> Marc
> Jem
> Monica
> Anna
> Jason

Enter the total bill value:
> 100

Do you want to use the "Who is lucky?" feature? Write Yes/No:
> Yes

Jem is the lucky one!

{'Marc': 25, 'Jem': 0, 'Monica': 25, 'Anna': 25, 'Jason': 25}

Example 2: The feature is skipped

Enter the number of friends joining (including you):
> 5

Enter the name of every friend (including you), each on a new line:
> Marc
> Jem
> Monica
> Anna
> Jason

Enter the total bill value:
> 100

Do you want to use the "Who is lucky?" feature? Write Yes/No:
> No

No one is going to be lucky

{'Marc': 20, 'Jem': 20, 'Monica': 20, 'Anna': 20, 'Jason': 20}

Example 3: Invalid input

Enter the number of friends joining (including you):
> 0

No one is joining for the party
```
