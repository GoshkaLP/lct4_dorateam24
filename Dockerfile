FROM sunpeek/poetry:py3.11-slim as built

WORKDIR /opt/app
COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.in-project true \
    && poetry config virtualenvs.create true \
    && poetry install --no-root --verbose --no-interaction --no-ansi

FROM sunpeek/poetry:py3.11-slim
WORKDIR /opt/app
RUN python -m venv /opt/app/.venv
COPY --from=built /opt/app/.venv /opt/app/.venv

COPY backend/ ./backend
ENV PATH="/opt/app/.venv/bin:$PATH"

EXPOSE 8080

ENTRYPOINT ["python", "-m", "backend"]
