# clean-code-ml refactoring exercise

## Pre-workshop setup

Please ensure you have the following:
- a [GitHub](https://github.com/) account
- a [CircleCI](https://circleci.com) account
- an IDE ([VS Code](https://code.visualstudio.com/Download) or [PyCharm](https://www.jetbrains.com/pycharm/download/))
- Windows users:
    - Download [Git Bash](https://gitforwindows.org/)

## Getting started

1. Fork repo
1. Clone repository: `git clone https://github.com/YOUR_USERNAME/clean-code-ml`
1. Run `bin/setup.sh`. This will install miniconda3 if it's not already installed, and install project-level dependencies specified in `./environment.yml`

You're ready to roll! Here are some common commands that you can run in your dev workflow.

#### Run tests

```shell
# run unit tests
nosetests

# run unit tests in watch mode and color output
nosetests --with-watch --rednose --nologcapture
```

#### Start jupyter notebook

```shell
# starting jupyter notebook server on http://localhost:8888
jupyter notebook

# Now you can visit localhost:8888 on your browser.
```

## IDE configuration

Run `bin/configure_venv_locally.sh`. This will create a virtual environment directory (named `.venv-local`) on your computer (the host). Next, configure your IDE to use `.venv-local/bin/python` as the Python interpreter. Here are the instructions on how to do that in [VS Code](https://code.visualstudio.com/docs/python/environments) and [PyCharm](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html).


## Attributions

The notebook which we use for the starting point of our refactoring exercise was adapted/modified from a [Kaggle submission](https://www.kaggle.com/bhaveshsk/getting-started-with-titanic-dataset/data) for the titanic competition. 