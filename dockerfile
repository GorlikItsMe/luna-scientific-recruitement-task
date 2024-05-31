FROM python:3.11-slim-bullseye as base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Install dependencies
RUN apt-get update \
    && apt-get install -y libpq-dev gcc python3-dev musl-dev 

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip --no-cache-dir \
    && pip install -r requirements.txt --no-cache-dir \
    && pip install gunicorn --no-cache-dir


# Production image
FROM python:3.11-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app

RUN apt-get update \
    && apt-get install -y wget

COPY --from=base /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
COPY --from=base /usr/local/bin/ /usr/local/bin/

# Copy application code
COPY . /app

EXPOSE 8000

CMD ["/bin/bash", "/app/entrypoint.sh"]

# HEALTHCHECK --interval=30s --timeout=5s \
#   CMD wget -qO- http://127.0.0.1:8000/health || exit 1