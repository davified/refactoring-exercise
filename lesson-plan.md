# clean-code-ml lesson plan

Target audience:
- Data scientists / data science enthusiasts

Pre-requisites for attendees:
- Some basic experience with Python and Jupyter notebook
- Some basic experience with scikit-learn / pandas

Pre-workshop setup:
- Load link to google doc (snippets will be shared here)
- GitHub account
- Fork and clone repo
- CircleCI account
- windows users:
    - Download git bash
- setup: follow instructions in README

Demo:
- how to write a unit test
- how to write a unit test with dataframes
- how to refactor 1 thing (use add_derived_title as demo)

Note:
- Commit your code after each exercise

### outline
- Temperature check
- Why do we need clean code? (A: change and complexity)
    - Demo: pain of refactoring when code is dirty
    - 2 hats: data scientist (exploration) and software dev (production-ready and extensible codebase)
- Context: titanic dataset
    - What the Jupyter notebook does
    - Show data and dataframe 

- What are code smells? (go through list of What does bad code / clean code look like?)
    - Explicitly call out code smells by name
- How do we clean up code in an existing data science / ml codebase?
    - go through refactoring process below
- Hands-on exercise in refactoring titanic notebook)
    - Technical crash course:
        - How to get set up
        - How to write unit tests (Python syntax + arrange act assert)
- How do we write clean code in a new project?

### Refactoring process (for an existing notebook)

My process for refactoring the titanic notebook
- Ensure that notebooks when run from start to end
- Read notebook and list code smells (see next section)
- Make a copy of the original notebook (for comparing the end result later)
- Start refactoring 
    - Identify a block of code that can be extracted into a pure function
    - Pseudo-TDD
        - Write a unit test for it and run the unit tests in watch mode
        - Create a Python module and create a function. Cut and paste existing implementation from notebook into that function
        - Make the tests pass
    - Import function back into the notebook
    - Restart and run entire notebook (Unfortunately, until we have sufficient unit tests, we will still need manual “integration” tests for the time being.)
    - [Optional] Refactor function some more
    - Make a git commit
    - Rinse and repeat

### Code smells
- too many comments
- bad variable names
    - train_df and test_df could be better named (without type information)
    - combine
- too many print statements
    - df.info(), df.head(), df.describe(), etc. - is there any other way that we can get feedback on the data?
- no tests for data transformations (e.g. cell 17 onwards)
- cell 18, 19 (mutation to `dataset` outside of a function)
- duplication in model training code. Can extract to a function.
- duplication in EDA code. Can extract to a function.
- duplication in how test_df and train_df are joined. Why not just join it once, and use the combined df for all data transformations?

### Changelog
- [titanic-exercise-0](https://github.com/davified/clean-code-ml/blob/master/notebooks/titanic-exercise-0.ipynb): Original notebook
- [titanic-exercise-1](https://github.com/davified/clean-code-ml/blob/master/notebooks/titanic-exercise-1.ipynb): Removed most print statements
    - Participants should use this notebook to list code smells
- [titanic-exercise-2](https://github.com/davified/clean-code-ml/blob/master/notebooks/titanic-exercise-2.ipynb): Add exercises for refactoring
    - Participants should refactor this notebook
- [titanic-exercise-solution](https://github.com/davified/clean-code-ml/blob/master/notebooks/titanic-titanic-exercise-solution.ipynb): Final state of notebook after refactoring
- [final code](https://github.com/davified/clean-code-ml/blob/master/src/train.py): Move code from jupyter notebook to plain Python file/module.

### How do we write clean code in a new project?
- It's ok to use notebooks if you need the feedback that it gives. But try to get rid of it (or keep it just for reference and stop adding new code to it) as soon as it has served its purpose of giving us feedback
- TDD
- Demo: tackle a new ML problem using TDD and clean code practices

### Note to self (david)
- Set up split screen to reduce toggling
- Write session plan (with time) on the wall and track progress as we go

### Bonus
- Set up CI pipeline on CircleCI (run unit tests + run jupyter notebook and ensure no errors)


### reading list
- ...