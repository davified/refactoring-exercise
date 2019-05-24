# clean-code-data-science

## Getting started

1. Clone repository: `git clone https://github.com/davified/clean-code-data-science`
1. Install Docker ([Mac](https://docs.docker.com/docker-for-mac/install/), [Linux](https://docs.docker.com/install/linux/docker-ce/ubuntu/))
1. Start Docker on your desktop
1. Build image and start container:

```shell
# build docker image
docker build . -t clean-code-data-science --build-arg user=$(whoami)

docker run -it  -v $(pwd):/home/clean-code-data-science \
                -p 8888:8888 \
                clean-code-data-science bash
```

You're ready to roll! Here are some common commands that you can run in your dev workflow. Run these in the container.

```shell
# run unit tests
nosetests

# run unit tests in watch mode and color output
nosetests --with-watch --rednose --nologcapture

# starting jupyter notebook server on http://localhost:8888
jupyter notebook --ip 0.0.0.0 --no-browser --allow-root
```

Here are some other commands that you may find useful
```shell
# see list of running containers
docker ps

# start a bash shell in a running container
docker exec -it <container-id> bash
```

## IDE configuration

Run `bin/configure_venv_locally.sh`. This will create a virtual environment directory (named `.venv-local`) on your computer (the host). Next, configure your IDE to use `.venv-local/bin/python` as the Python interpreter.
