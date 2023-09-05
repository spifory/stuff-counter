FROM python:3.11-slim-bullseye

WORKDIR /bot

RUN pip install poetry==1.5.1

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.in-project true

RUN poetry install --no-root --only=main --no-interaction

COPY . .

ENTRYPOINT [ "poetry", "run" ]
CMD [ "task", "start" ]
