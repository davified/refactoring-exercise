# Workshop Setup (Using Conda)

## Setup instructions (Mac / Linux)

1. Run `bin/setup.sh`. This will install miniconda3 if it's not already installed, and install project-level dependencies specified in `./environment.yml`

You're ready to roll! Here are some common commands that you can run in your dev workflow.

```shell
# initialize conda shell
conda init <SHELL_NAME> # SHELL_NAME options: bash, zsh, fish, powershell

# close and open your shell/terminal

# activate virtual environment
conda activate clean-code-ml

# run unit tests
nosetests

# run unit tests in watch mode and color output
nosetests --with-watch --rednose --nologcapture

# open a new terminal and start jupyter notebook server
jupyter notebook
# Now you can visit localhost:8888 on your browser.

# at the end of the session, deactivate virtual environment
conda deactivate

```

## Setup instructions (Windows)

### Install Anaconda (if you haven't installed it before)

- Visit: https://docs.conda.io/en/latest/miniconda.html
- Click on Miniconda3 Windows 64-bit to download the installer
- Run the installer. Go with the defaults, but **make sure to check 'Make Anaconda the default Python'"**

### Install project-level dependencies

Note: If you get an error (`bash: conda: command not found`), please run the steps in the **Troubleshooting** section below and try these steps again:

```shell
# install create conda environment and install dependencies
conda create -f ./environment.yml

# activate virtual environment
conda activate clean-code-ml

# run unit tests
nosetests

# run unit tests in watch mode and color output
nosetests --with-watch --rednose --nologcapture

# open a new terminal and start jupyter notebook server
jupyter notebook
# Now you can visit localhost:8888 on your browser.

# at the end of the session, deactivate virtual environment
conda deactivate
```

## Troubleshooting `conda: command not found` error

1. Find full path to conda executable:

- search for conda.exe in Windows Search bar
- In the file that is found, click on 'Open file location'
- Step back to the Miniconda3 folder
- Navigate into Miniconda3/Scripts folder
- Copy full path to your git bash terminal, and replace Windows backslashes with Unix forward slashes. Example:
  - `C:\Users\myname\Miniconda3\Scripts\conda.exe` -> `/c/Users/myname/Miniconda3/Scripts/conda.exe`
- Use `/c/Users/myname/Miniconda3/Scripts/conda.exe` instead of the `conda` shorthand:

2. Configure `conda` to be a command that you can use in your terminal

```shell
# verify if conda can be used directly. If you see 'which: no conda in ...', fix it using the steps below
which conda

# initialize conda shell
/c/Users/myname/Miniconda3/Scripts/conda.exe init bash # we choose bash because gitbash is a bash shell

# reload the shell for conda init to take effect
source ~/.bash_profile

```

3. **Important**: If you get the same `conda: command not found` error again in any new shell (e.g. in VS Code), simply run `source ~/.bash_profile` again

## Bonus: running test coverage

We've installed a python library ([`coverage`](https://coverage.readthedocs.io/en/coverage-5.0.3/)) that tells you which lines of code are tested/not tested. To do use, run:

- `coverage run -m nose`
- `coverage html`
- Open `clean-code-ml/htmlcov/index.html` in your browser
