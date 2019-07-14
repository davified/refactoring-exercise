# clean-code-ml refactoring exercise

## Pre-workshop setup

Please ensure you have the following:
- a [GitHub](https://github.com/) account
- a [CircleCI](https://circleci.com) account
- an IDE ([VS Code](https://code.visualstudio.com/Download) or [PyCharm](https://www.jetbrains.com/pycharm/download/))
- Windows users:
    - Download [Git Bash](https://gitforwindows.org/)
- Docker for Desktop (Install for [Mac](https://docs.docker.com/docker-for-mac/install/), [Linux](https://docs.docker.com/install/linux/docker-ce/ubuntu/), [Windows](https://docs.docker.com/docker-for-windows/install/))
    - If you don't have a dockerhub account, you will be prompted to create one. It's free

## Getting started

1. Fork repo
1. Clone repository: `git clone https://github.com/YOUR_USERNAME/clean-code-ml`
1. Start Docker on your desktop
1. Update your git username and email in `Dockerfile`
1. Build image and start container:

```shell
# build docker image
docker build . -t clean-code-ml

docker run -it  -v $(pwd):/home/clean-code-ml \
                -p 8888:8888 \
                clean-code-ml bash
```

You're ready to roll! Here are some common commands that you can run in your dev workflow. Run these in the container.

#### Run tests

```shell
# run unit tests
nosetests

# run unit tests in watch mode and color output
nosetests --with-watch --rednose --nologcapture
```

#### Start another bash shell in the running container
```shell
# see list of running containers
docker ps

# start a bash shell in a running container
docker exec -it <container-id> bash
```

#### Start jupyter notebook

```shell
# starting jupyter notebook server on http://localhost:8888
jupyter notebook --ip 0.0.0.0 --no-browser --allow-root

# Now you can visit localhost:8888 on your browser. The required token can be found in the output of the `jupyter notebook ...` command
```

## IDE configuration

Run `bin/configure_venv_locally.sh`. This will create a virtual environment directory (named `.venv-local`) on your computer (the host). Next, configure your IDE to use `.venv-local/bin/python` as the Python interpreter. Here are the instructions on how to do that in [VS Code](https://code.visualstudio.com/docs/python/environments) and [PyCharm](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html).


## Attributions

The notebook which we use for the starting point of our refactoring exercise was adapted/modified from a [Kaggle submission](https://www.kaggle.com/bhaveshsk/getting-started-with-titanic-dataset/data) for the titanic competition. 