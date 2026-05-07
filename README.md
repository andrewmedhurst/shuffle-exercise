# Shuffle a Deck of cards

### What this does

This project contains a function called `shuffle_cards` that will randomly shuffle a default deck of 52 cards if no custom list of type `Card` is passed into the function call. The starting deck is printed to the console, followed by a print statement of the shuffled deck after the process completes

This process, should the default list be used upon every execution, technically takes O(1), or constant time. This is because the number of elements never changes, as a standard deck of cards will always consist of 52 card. Should a custom deck of cards be passed into the function instead, this turns the execution time to O(n), as the list could be anywhere between 0 and positive infinity in size.

The space complexity will always be O(1), as the shuffling is mutating the list of cards that is being passed in directly. No new memory space is allocated to handle any of the shuffling internally.

### Prerequisites

Before you can run this exercise, you will need to have Python3 installed onto your system. If using MacOS, install via homebrew with the following Terminal command:

`brew install python`

Then, verify installation:

`python3 --version`

If using a different operating system than MacOS, consult the appropriate documentation for how to install Python3

### How to Run
As the solution uses only libraries internal to Python3, a virtual environment to install additional dependencies should not be needed. If the step below doesn't work, consider constructing a python venv first, and then trying to execute the below command again.

1. From within the `shuffle_exercise` root directory, run: 
```python -m src.main```
2. If you did not pass a custom card deck list to the `shuffle_cards()` call on line 23 of `main.py`, the terminal output should contain 52 items and look something like the following:
```
The Card list before shuffling: 
[2 of Hearts, 3 of Hearts, 4 of Hearts, 5 of Hearts, 6 of Hearts, 7 of Hearts, 8 of Hearts, 9 of Hearts, 10 of Hearts, Jack of Hearts, Queen of Hearts, King of Hearts, Ace of Hearts, 2 of Diamonds, 3 of Diamonds, 4 of Diamonds, 5 of Diamonds, 6 of Diamonds, 7 of Diamonds, 8 of Diamonds, 9 of Diamonds, 10 of Diamonds, Jack of Diamonds, Queen of Diamonds, King of Diamonds, Ace of Diamonds, 2 of Clubs, 3 of Clubs, 4 of Clubs, 5 of Clubs, 6 of Clubs, 7 of Clubs, 8 of Clubs, 9 of Clubs, 10 of Clubs, Jack of Clubs, Queen of Clubs, King of Clubs, Ace of Clubs, 2 of Spades, 3 of Spades, 4 of Spades, 5 of Spades, 6 of Spades, 7 of Spades, 8 of Spades, 9 of Spades, 10 of Spades, Jack of Spades, Queen of Spades, King of Spades, Ace of Spades]

The Card list after shuffling: 
[3 of Diamonds, King of Spades, 8 of Diamonds, 3 of Spades, 10 of Clubs, Ace of Diamonds, Ace of Hearts, Ace of Spades, 6 of Hearts, Queen of Diamonds, 9 of Clubs, 2 of Hearts, 7 of Spades, Ace of Clubs, Queen of Hearts, 4 of Spades, 2 of Clubs, 8 of Hearts, 6 of Diamonds, Jack of Hearts, 3 of Hearts, 9 of Hearts, 4 of Diamonds, 4 of Clubs, Jack of Diamonds, Queen of Clubs, 2 of Spades, Jack of Clubs, 9 of Spades, 9 of Diamonds, 5 of Hearts, 2 of Diamonds, 4 of Hearts, 5 of Diamonds, 6 of Clubs, 8 of Spades, 8 of Clubs, 7 of Clubs, Queen of Spades, King of Clubs, King of Hearts, 5 of Clubs, 7 of Hearts, 7 of Diamonds, 10 of Spades, 3 of Clubs, 6 of Spades, 10 of Diamonds, Jack of Spades, King of Diamonds, 5 of Spades, 10 of Hearts]
```

### How to validate with tests:

1. From the root of the project, run the following:
`python3 -m unittest tests.test_shuffle_deck`

2. This should run all of the tests within `tests/test_shuffledeck.py` and generate the following output if everything is passing.

```
% python3 -m unittest tests.test_shuffle_deck
......
----------------------------------------------------------------------
Ran 6 tests in 0.000s

OK
```

### Things to keep in mind
1. Using the built-in `random` library for Python (and for most all other languages) is deterministic and traceable in some way. This is because of the pseudo-random nature of randomization lacks true entropy due to an initial 'seeding value' which, on a long enough timeline, will result in values to start repeating themselves.
2. Considering the input size of our decks will likely be relatively small, this isn't much of an issue. We further reinforce 'equality of randomness' by leveraging the Fisher-Yates shuffling algorithm, restricting the window of selectable swap elements with each iteration, rather than a naive algorithm which uses a fixed size throughout the whole process. This window reduction forces the pseudo-random number generator to use a different seed on each execution of the for loop (because the range has shrunk), along with the elimination of the tail-most element, to effectively element the possibility of repeat swaps.