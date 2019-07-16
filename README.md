# clean-code-ml

## Table of Contents
- [Introduction](#introduction)
- [Variables](docs/variables.md)
    - Variable names should reveal intent
    - Use meaningful and pronounceable variable names
    - Use the same vocabulary for the same type of variable
    - Avoid magic numbers and magic strings
    - Use variables to keep code "DRY"  ("Don't Repeat Yourself")
    - Use explanatory variables
    - Avoid mental mapping
    - Don't add unneeded context
- [Functions](docs/functions.md)
    - Use functions to keep code "DRY"
    - Functions should do one thing
    - Functions should only be one level of abstraction
    - Function names should say what they do
    - Use type hints to improve readability
    - Avoid side effects
    - Avoid unexpected side effects on values passed as function parameters
    - Function arguments (2 or fewer ideally)
    - Use default arguments instead of short circuiting or conditionals
    - Don't use flags as function parameters
- [Dispensables](docs/dispensables.md)
    - Avoid comments
    - Remove dead code
    - Avoid print statements (even glorified print statements such as df.head(), df.describe(), df.plot())
- [Design](docs/design.md)
    - Set boundaries (Keep implementation details hidden). When implementation details are all laid bare in the notebook without any abstractions (functions), we are forced to understand the how's in order to know what's happening
    - Shotgun surgery. When you want to change one thing, you end up having to make changes in many places

## Introduction

Clean code practices (from [Clean Code](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882) and [Refactoring](https://www.amazon.com/Refactoring-Improving-Existing-Addison-Wesley-Signature/dp/0134757599)) adapted for machine learning / data science workflows in Python. This is not a style guide. It's a guide to producing
readable, reusable, and refactorable software.

If you’ve tried your hand at machine learning or data science, you would know that code can get messy, quickly. 

Unclean code adds to complexity by making code difficult to read and modify. As a consequence, changing code to respond to business needs becomes increasingly difficult, and sometimes even impossible. This has been written about extensively in several languages, and even in Python (e.g. Clean Code, Refactoring, clean-code-python). In this repo, we have adapted these principles for data science / machine learning codebases.

Targets Python3.7+

Inspired by [clean-code-javascript](https://github.com/ryanmcdermott/clean-code-javascript) and forked from [clean-code-python](https://github.com/zedr/clean-code-python).

## Hands-on Exercise

If you'd like to try out these practices, we've created a [refactoring exercise](./docs/refactoring-exercise.md) which you can follow along. Starting with [a jupyter notebook with many code smells](notebooks/titanic-exercise-1.ipynb), you can apply these clean code principles and refactor it to be readable and maintainable. The sample final solution can be found in [`src/train.py`](src/train.py).
