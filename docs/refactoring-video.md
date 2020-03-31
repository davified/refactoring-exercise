# Tutorial: How to refactor a jupyter notebook

My refactoring process (use them in the order that works for you)

## Prerequisites
- [] Local dev environment is set up
- [] Run notebook and ensure it works
- [] Make a copy of the notebook (to eliminate any emotional attachment)
- [] Remove print statements
- [] Convert notebook as Python file
- [] Read notebook and list code smells

## Refactoring steps
- [] Run tests in watch mode
- [] Identify a block of code that can be extracted into a pure function
- [] The refactoring cycle
    - [] Write a test
    - [] Create a Python module and define a function. 
    - [] Make the test pass
    - [] In the notebook, replace original code block with the newly defined function
    - [] Restart and run entire notebook
    - (Optional) Refactor function some more
    - [] Commit your changes
- [] Add functional test for ML model
- [] Celebrate 🤘🤘