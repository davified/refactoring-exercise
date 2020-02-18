# clean-code-ml refactoring exercise setup

## Prerequisites

Please ensure you have the following:

- a [GitHub](https://github.com/) account
- a [CircleCI](https://circleci.com) account
- an IDE ([VS Code](https://code.visualstudio.com/Download) or [PyCharm](https://www.jetbrains.com/pycharm/download/))
- [Windows Users only] Install [git bash](https://gitforwindows.org/). We will be using `git bash` as the terminal for the workshop.

## Getting started

1. Fork repo
1. Clone repository: `git clone https://github.com/YOUR_USERNAME/clean-code-ml`
1. Project setup. You can either use docker or conda. Choose whichever you prefer:

- docker ([workshop setup instructions](./setup-docker.md))
- conda ([workshop setup instructions](./setup-conda.md))
  - Mac/Linux users
  - Windows users

If you encounter any errors, please refer to [FAQs](./FAQs.md) for a list of common errors and how to fix them.

## IDE configuration

Configure your IDE to use `~/miniconda3/envs/clean-code-ml/bin/python` as the Python interpreter. Here are the instructions on how to do that in [VS Code](https://code.visualstudio.com/docs/python/environments) and [PyCharm](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html).

Once you've done that, you should be able to:

1. Get helpful auto-complete suggestions in your IDE as you type. If somehow that's not showing up, try restarting your code editor.
1. Let your IDE auto-format your code in a file. We've installed [autopep8](https://github.com/hhatto/autopep8) using conda, and now your IDE can help you with the auto-formatting)
   - To do this in VS Code, hit `Shift` + `⌘` + `F`
1. Use other tools provided by your IDE.
   - For VS Code, hit `F1` and type 'Python Refactor' and you can experiment with any of these commands (e.g. 'Sort Imports')

## Attributions

The notebook which we use for the starting point of our refactoring exercise was adapted/modified from a [Kaggle submission](https://www.kaggle.com/bhaveshsk/getting-started-with-titanic-dataset/data) for the titanic competition.
