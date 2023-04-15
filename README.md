# Refactoring Exercise - Titanic Survivorship Classification

A hands-on exercise for refactoring a jupyter notebook laden with code smells to a modular, readable, tested codebase.

```shell script
# mac users
scripts/go/go-mac.sh

# linux users
scripts/go/go-linux-ubuntu.sh

# windows
scripts\go\install_choco.ps1
scripts\go\install.bat
```

Configure Docker runtime
```shell
# set up colima (a license-free docker runtime, an alternative to docker desktop)
https://gist.github.com/jcartledge/0ce114e9719a62a4776569e80088511d
```

## Tasks that you can run

```shell script
# start docker runtime
colima start

# install dependencies
./batect --output=all setup

# start jupyter notebook
./batect start-jupyter

# start container (i.e. local dev environment)
./batect start-dev-container

### in the dev container

# run model training smoke tests
scripts/tests/model-metrics-test.sh

# train model
scripts/train-model.sh 
```
