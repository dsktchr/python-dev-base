# FastAPI 開発環境

## .devcontainer


## poetry
`poetry`を利用する場合h、最初に`poetry init`をする必要あり？
<br/>
`poetry new`は`.devcontainer`ディレクトリがあるため、活用できない...

```
poetry add fastapi uviconrn[standard]
poetry add -D black flake8 isort mypy
```
flake8については、別途設定ファイルを用意する必要がある

```
```