FROM python:3.11.1-slim AS dev

WORKDIR /code

RUN apt-get update && apt-get -y install gcc

RUN pip install poetry
ADD pyproject.toml /code/
RUN poetry config installer.max-workers 10
RUN poetry config virtualenvs.create false

ARG VENV_PATH
ENV VENV_PATH=$VENV_PATH
ENV PATH="$VENV_PATH/bin:$PATH"

CMD ["bash"]
