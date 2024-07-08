# Install dependencies
I use `pyenv` to manage my Python versions and `pipenv` to manage my virtual environments. You can use any solution, but I will share the steps for `pyenv` and `pipenv` here.

## Install pyenv
Installation instructions are documented for Linux, MacOS, and Microsoft Windows. Follow the steps here: https://github.com/pyenv/pyenv?tab=readme-ov-file#installation

## Install Python
1. If you followed the steps for install pyenv to the end, you will already have installed the Python build dependencies. If you haven't yet done so, you can follow the steps here: https://github.com/pyenv/pyenv/wiki#suggested-build-environment.
2. After having installed the Python build dependencies, install Python with `pyenv install 3.12.4`.

# Create the virtual environment
1. Install pipenv:
```bash
``~/.pyenv/versions/3.12.4/bin/python -m install pipenv
```
2. Clone the repository:
```bash
git clone git@github.com:adriaanjoubert/uoeo-phonebook.git
```
3. Change directory into the project root directory:
```bash
cd uoeo-phonebook
```
4. Create the virtual environment:
```bash
~/.pyenv/versions/3.12.4/bin/pipenv --python 3.12.4
```
5. Activate the virtual environment:
```bash
~/.pyenv/versions/3.12.4/bin/pipenv shell
```
6. Install the Python dependencies:
```bash
pip install pipenv
pipenv install
```

# Run the Jupyter Notebook
## Start the Jupyter Notebook
```bash
jupyter notebook
```

## Open the Jupyter Notebook
1. Open your browser and navigate to `http://localhost:8888` (if it didn't automatically open).
2. Open the file `Notebook.ipynb` to load and interact with the program.

# Run the program in the command line
```bash
python main.py
```

```python
from main import main


main()
```

# Run unit tests
```bash
python -m unittest
```

# Using the program
The program is implemented as a read-eval-print-loop (REPL). There is a main menu with 6 options:
1. Add a new entry
2. Print all entries
3. Search for an entry by ID
4. Sort entire phonebook by name
5. Delete entry by ID
6. Exit

After each operation, the main menu is displayed again. You can exit the program by selecting option 6.

Insertion is implemented by appending entries to the list of entries. Deletion is implemented by concatenating the
slices of entries before and after the entry to be deleted to form a new list of entries. Searching is implemented by
maintaining a hash table of IDs to indices in the list of entries. Sorting is implemented using the Quicksort algorithm
developed by Hoare (1960) as implemented by Sedgewick (1992). Please refer to the PDF for the full reference list.
