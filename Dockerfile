FROM python:3.11-slim-bullseye

WORKDIR /bot

RUN pip install poetry

# This is for disnake-ext-plugins
RUN apt update && apt install git -y && apt clean

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root --without=dev

COPY . .

CMD ["poetry", "run", "task", "start"]