# Ecommerce Backend

## Local Development Setup
### Create Virtual environment
```bash
python -m venv .venv
```

### Activate Virtual Environment (Bash)
```bash
source .venv/Scripts/Activate
```

### Install Dev Dependencies
```bash
pip install -r requirements-dev.txt
```
### Install Dependencies
```bash
pip install -r requirements.txt
```

### Format Code
```bash
black . --config ./pyproject.toml
```

### Start Backend Server
```bash
python -m flask --app main run
```

### Start Backend Server in Dev Mode
```bash
python -m flask --app main --debug run
```

### Format Code
```bash
black . --config pyproject.toml
```