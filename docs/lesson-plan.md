# clean-code-ml lesson plan

Target audience:

- Data scientists / data science enthusiasts

Pre-requisites for attendees:

- Some basic experience with Python, Jupyter notebook, `scikit-learn`, and `pandas`

## Rules of thumb

- Remember the [Two Hats](https://www.martinfowler.com/articles/workflowsOfRefactoring/#2hats)
- Keep tests in watch mode. Test continuously during each refactoring
- Make small and frequent commits

## Session outline

- Temperature check
  - Python, jupyter, ML, unit testing
  - Shuffle seats if necessary
- Why this session? What's wrong with jupyter notebooks (Answer: change and complexity)
  - Jargon:
    - code smells ("if it stinks, change it", Grandma Beck)
      - go through [cheat-sheet.md](./cheat-sheet.md)
    - refactoring
- Code smell #1 (print statements)
  - First, show the titanic dataset and what the notebook is doing
  - Starter code: [notebook-0](../notebooks/titanic-notebook-0.ipynb)
    - Look at this, and call out the first code smell that comes to your mind
  - Refactored code: [notebook-1](../notebooks/titanic-notebook-1.ipynb)
  - Task: Remove code that is only for printing (e.g. `print(...)`, `df.head()`, etc.)
  - Task: Remove dead code (e.g. `df[['IsAlone', 'Survived']].groupby(['IsAlone'], as_index=False).mean()`)
- Code smell #2 (exposed internals)
  - Starter code: [notebook-1](../notebooks/titanic-notebook-1.ipynb)
  - Refactored code: [notebook-2](../notebooks/titanic-notebook-2.ipynb)
  - Use [train.py](https://github.com/davified/clean-code-ml/blob/master/src/train.py) to show the value of functions / abstractions
  - Task: None
- Code smell #3 (Duplication)
  - DEMO + EXERCISE 1: How to refactor to functions - train_model()
  - Starter code: [notebook-2](../notebooks/titanic-notebook-2.ipynb)
  - Refactored code: [notebook-3](../notebooks/titanic-notebook-3.ipynb)
- Break
  - If you cannot run nosetests or start jupyter notebook, please ask us for help.
- Code smell #4 (No unit tests):
  - Starter code: [notebook-3](../notebooks/titanic-notebook-3.ipynb). What are any other code smells?
  - Demo + codealong: How to write a unit test + arrange/act/assert
  - Demo + codealong: How to write a unit test with dataframes
  - Demo + exercise 1.5: How to write a characterisation test + metrics test
  - Demo + exercise 2
  - Exercise 3
- Conclusion
  - Show [titanic-notebook-solution](https://github.com/davified/clean-code-ml/blob/master/notebooks/titanic-notebook-solution.ipynb) and [`src/train.py`](https://github.com/davified/clean-code-ml/blob/master/src/train.py)
  - Full list of [code smells](../README.md)
  - Take-home reading: [refactoring process](./refactoring-process.md)
- Bonus: CI

## Note to self (david)

- Set up split screen to reduce toggling
- Write session plan (with time) on the wall and track progress as we go
- Share google doc scratchpad with class: https://tinyurl.com/y42xa86r
- Get feedback on
  - code smells in clean-code-ml
  - refactoring notebook kata
  - workshop (any general feedback)
