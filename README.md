# discord-choice-bot

Discord bot that random choice from numbers or a list of strings

## Directory

```shell
(root)
├── .github
│   └── ISSUE_TEMPLATE
├── .gitignore
├── .vscode
│   ├── launch.json
│   └── settings.json
├── LICENSE
├── Procfile            # Heroku run file
├── README.md
├── app.json            # Heroku app setting json
├── discord_choice_bot  # Bot dirs
│   ├── __init__.py
│   └── run.py
├── poetry.lock
├── pyproject.toml
├── requirements.txt    # poetry export requirements file
└── runtime.txt         # Heroku runtime file
```

## Prerequisites

- Installed [Poetry](https://github.com/python-poetry/poetry) (>=1.1.7), [Git](https://git-scm.com/) (>=2.17.1)

## Create repository command memo

```shell
# git clone this repository
git clone https://github.com/neruo/python3-dev-template.git
cd ~/workspace/python3-dev-template

# setup poetry
poetry init -n
poetry env use python # create virtual environment
poetry add --dev flake8 black isort mypy
poetry shell # attach virtual environment

# setup vscode files: launch.json settings.json
git clone https://gist.github.com/278955c697d3788500e77521e57c47bb.git .vscode
rm -r .vscode/.git

# create start files: __init__.py run.py argument.py
git clone https://gist.github.com/c7830fa9d7aa62581b91da6d4a028ae3.git python3-dev-template
rm -r python3-dev-template/.git
```

## Development usage

```shell
# setup poetry
poetry env use python # create virtual environment
poetry install # install packages
poetry shell # attach virtual environment
```
