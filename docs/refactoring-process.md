# How to refactor a Jupyter notebook

What is "refactoring"? **Changing code to make it easier to understand and modify without changing its observable behavior** (Adapted from Refactoring (2nd edition) - Martin Fowler)

Refactoring without tests is **hard**. And typically, when we write Jupyter notebooks, we usually just bang out code without writing tests.

Nonetheless, since this is the predicament which we find ourselves in, we need to find a way towards code that is unit-tested and properly abstracted, so that we can have a maintainable, readable and extensible codebase. So that we can remain productive even as we're confronted with new business requirements and new data.

### The refactoring process
Before we start refactoring:
- Ensure that notebooks when run from start to end
    - Even better if you can add an "integration" or "functional" test
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

### Some tips
- When refactoring, don't change the program's observable behaviour.
- Keep tests in watch mode. Test after every refactoring
    - "Testing after each change means that when I make a mistake, I only have a small change to consider in order to spot the error, which makes it far easier to find and fix." (Martin Fowler)
- Make small and frequent commits
- Don't try big bang refactorings. Refactoring isn’t an activity that’s separated from programming. We refactor as we go.
- When to refactor
    - "**Three strikes, then you refactor.** The first time you do something, you just do it. The second time you do something similar, you wince at the duplication, but you do the duplicate thing anyway. The third time you do something similar, you refactor." (Martin Fowler)
