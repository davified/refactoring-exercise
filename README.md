# Refactoring Exercise - Titanic Survivorship Classification

A hands-on exercise for refactoring a jupyter notebook laden with code smells to a modular, readable, tested codebase.

## Setup

Run the go script to install pre-requisite dependencies. 
The go script will install Python 3 and Poetry, and create a virtual environment on the host. 
This will make it easier to configure our IDE to know about the Python interpreter for this project.   


```shell script
# mac users
scripts/go/go-mac.sh

# linux users
scripts/go/go-linux-ubuntu.sh

# windows
# 1. Download and install Python3 if not installed: https://www.python.org/downloads/release/python-31011/
#    - During installation, when prompted, select "Add Python to PATH"
# 2. In Windows explorer/Search, go 'Manage App Execution Aliases' and turn off 'App Installer' for python. This resolves the issue where the `python` executable is not found in the PATH
# 3. Run the go script in the Powershell or Command Prompt Terminal
.\scripts\go\go-windows.bat
# Note: if you see a HTTPSConnectionPool read timed out error, just run this command a few more times until poetry install succeeds
```

Configure your IDE to use the python virtual environment created in the go script. 
- [PyCharm instructions](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#existing-environment)
- [VS Code instructions](https://code.visualstudio.com/docs/python/environments)

## Tasks that you can run

```shell script
# Activate virtual environment
poetry shell

# Start jupyter notebook
jupyter notebook

# Run model training smoke tests
scripts/tests/model-metrics-test.sh

# Train model
scripts/train-model.sh 
```
