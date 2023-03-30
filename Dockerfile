FROM python:3.10.6-slim-buster as base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERD=1 \
    # pip
    PIP_NO_CACHE_DIR=off \
    # poerty
    POETRY_VIRTUALENVS_CREATE=fasle

RUN pip install poetry

COPY pyproject.toml poetry.lock /code/

# 開発環境
FROM base as development

WORKDIR /code

RUN poetry install


# 本番環境用の事前準備
FROM development as for-prod-artifact

WORKDIR /tmp

RUN poetry install --no-dev

# # 本番環境
# FROM python:3.10.6 as production
# COPY --from=for-prod-artifact /usr/local/bin/python3.10/site-packages/ /usr/local/bin/python3.10/site-packages/
# RUN poetry install --no-dev

# COPY ../pyproject.toml ../pyproject.lock ./

# 既にプロジェクトが生成されているならライブラリのインストール
# 新規プロジェクトなら、プロジェクトの初期化を行う
# RUN if [-f pyproject.toml]; then poetry install; else poetry new api --name api; fi