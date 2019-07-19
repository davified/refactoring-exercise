# clean-code-ml lesson plan

Target audience:
- Data scientists / data science enthusiasts

Pre-requisites for attendees:
- Some basic experience with Python, Jupyter notebook, `scikit-learn`, and `pandas`

### Session outline
- Temperature check
- Why do we need clean code? (Answer: change and complexity)
- Code smell #1 (print statements)
    - First, show the titanic dataset and what the notebook is doing
    - Compare [exercise-0](../notebooks/titanic-exercise-0.ipynb) with [exercise-1](../notebooks/titanic-exercise-1.ipynb)
- Code smell #2 (exposed internals)
    - Compare [exercise-1](../notebooks/titanic-exercise-1.ipynb) with [exercise-2](../notebooks/titanic-exercise-2.ipynb)
- Code smell #3 (Duplication)
    - DEMO + EXERCISE 1: How to refactor to functions - train_model()
    - Compare [exercise-2](../notebooks/titanic-exercise-2.ipynb) with [exercise-3](../notebooks/titanic-exercise-3.ipynb)
- Break 
    - If you can't run `docker run ...`, please ask us for help.
- Code smell #4 (No unit tests):
    - Demo + codealong: How to write a unit test + arrange/act/assert
    - Demo + codealong: How to write a unit test with dataframes
    - Demo + exercise 2
    - Exercise 3
- Conclusion
    - Show final solution (ask for 1 volunteer) 
    - Show [titanic-exercise-solution](https://github.com/davified/clean-code-ml/blob/master/notebooks/titanic-exercise-solution.ipynb) and [`src/train.py`](https://github.com/davified/clean-code-ml/blob/master/src/train.py)
    - Full list of [code smells](../README.md)?
    - Take-home reading: [refactoring process](./refactoring-process.md)
- Bonus: CI

Questions:
- where to place
    - How to get set up (Docker, run tests, IDE configuration)

### Note to self (david)
- Set up split screen to reduce toggling
- Write session plan (with time) on the wall and track progress as we go
- Share google doc scratchpad with class: https://tinyurl.com/y42xa86r
- Get feedback on 
    - code smells in clean-code-ml
    - refactoring notebook kata
    - workshop (any general feedback)
