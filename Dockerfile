FROM sunpeek/poetry:py3.11-slim
WORKDIR /opt/app
COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root --verbose --no-interaction --no-ansi

COPY backend/ ./backend
ENV PATH="/opt/app/.venv/bin:$PATH"

EXPOSE 8080

ENTRYPOINT ["poetry", "run", "python", "-m", "backend"]
