# Workshop Setup (Using Docker)

## Prerequisites

1. [For Windows users] Docker Desktop requires Windows 10 Pro or Enterprise version 15063 to run. If your laptop is neither of these, please use [conda](./setup-conda.md) instead of Docker.
1. Install Docker

- [for Mac](https://docs.docker.com/docker-for-mac/install/)
- [for Linux](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
- [for Windows](https://docs.docker.com/docker-for-windows/install/)
- **Important things to note**:
  - You will be prompted to create a DockerHub account. Follow the instructions in order to download Docker
  - Follow the installation prompts (go with the default options) **until you have successfully started Docker**
  - [Windows users] When prompted to enable Hyper-V and Containers features, click 'Ok' and let computer restart again.
  - You may have to restart your computer 2-3 times.

2. Start Docker on your desktop (Note: Wait for Docker to complete startup before running the subsequent commands. You'll know when startup is completed when the docker icon in your taskbar stops animating)

## Setup (Mac / Linux)

```shell
# ensure you are in clean-code-ml directory

# build docker image
docker build . -t clean-code-ml

# start bash shell in a docker container
docker run -it -v $(pwd):/code -p 8888:8888 clean-code-ml bash
```

## Setup (Windows)

```shell
# ensure you are in clean-code-ml directory

# build docker image
MSYS_NO_PATHCONV=1 docker build . -t clean-code-ml

# start bash shell in a docker container
winpty docker run -it -v C:\\Users\\path\\to\\your\\clean-code-ml:/code -p 8888:8888 clean-code-ml bash
# Note: to find the path, you can run `pwd` in git bash, and manually replace forward slashes (/) with double backslashes (\\)
```

## Let's roll

Now that your docker container is up and running, you're ready to run the commands that we'll use in this workshop

```shell
# run unit tests
nosetests

# run unit tests in watch mode and color output
nosetests --with-watch --rednose --nologcapture

# open a new terminal and start jupyter notebook server
jupyter notebook --ip 0.0.0.0 --no-browser --allow-root

# To stop a process in the docker container, hit Ctrl + C
```

Now you're ready to roll!

## Other useful docker commands

To run 2 commands/processes in the same container (e.g. run jupyter notebook and nosetests at the same time), you can start a second process in a running container by doing the following:

```shell
# See list of running containers
docker ps

# Start a bash shell in a running container when it’s running
docker exec -it <container-id> bash
# Now you can run your second command (e.g. start jupyter notebook)
```

## Configure your IDE for better intellisense

1. install dependencies locally (i.e. outside of Docker image): `bin/install_deps_locally.sh`

2. Select Python interpreter. In VS Code:

- Open command palette: Press `F1`
- Type: "Python: Select Interpreter"
- Choose or type: `./.venv/bin/python`

## Bonus: running test coverage

We've installed a python library ([`coverage`](https://coverage.readthedocs.io/en/coverage-5.0.3/)) that tells you which lines of code are tested/not tested. To do use, run:

- `coverage run -m nose`
- `coverage html`
- Open `clean-code-ml/htmlcov/index.html` in your browser
