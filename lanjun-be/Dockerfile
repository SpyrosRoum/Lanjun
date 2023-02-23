FROM python:3.10.8-slim as deps
WORKDIR /tmp
RUN pip install --no-cache-dir 'poetry~=1.2' \
    && poetry config virtualenvs.create false
COPY ./pyproject.toml ./poetry.lock* /tmp/
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential=12.9 && \
    rm -rf /var/lib/apt/lists/*
RUN poetry install --no-root

FROM python:3.10.8-slim-bullseye AS prod
COPY --from=deps /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY --from=deps /usr/local/bin/ /usr/local/bin/
RUN adduser worker --disabled-password
USER worker
WORKDIR /home/worker/app
COPY --chown=worker:worker . .
ENV PATH="/home/worker/.local/bin:${PATH}"
