# How to refactor a Jupyter notebook

Refactoring without tests is **hard**. And typically, when we write Jupyter notebooks, we usually just bang out code without writing tests.

Nonetheless, since this is the predicament which we find ourselves in, we need to find a way towards code that is unit-tested and properly abstracted, so that we can have a maintainable, readable and extensible codebase. So that we can remain productive even as we're confronted with new business requirements and new data.

### The refactoring process
Before we start refactoring:
- Ensure that notebooks when run from start to end
- Read notebook and list code smells (see next section)
- Make a copy of the original notebook (for comparing the end result later)

The refactoring cycle:
1. Identify a block of code that can be extracted into a pure function
1. Pseudo-TDD (test-driven development)
    - Write a unit test for it and run the unit tests in watch mode
    - Create a Python module and create a function. Cut and paste existing implementation from notebook into that function
    - Make the tests pass
1. Import function back into the notebook
1. Restart and run entire notebook (Unfortunately, until we have sufficient unit tests, we will still need manual “integration” tests for the time being.)
1. [If possible] Refactor function some more
1. Commit your changes
    - git add .
    - git commit -m "your commit message"
1. Rinse and repeat