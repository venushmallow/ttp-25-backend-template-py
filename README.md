# ttp-25-backend-template-py

Ensure that python has been installed by checking it's version:

```cmd
python -V
```

If python has not been installed, install it by checking the link here: https://realpython.com/installing-python/#macos-how-to-check-or-get-python

Create a python virtual environment for easier package management:

```pwsh
python -m venv venv
```

And activate the virtual environment:

```bash
venv\Scripts\activate # for Powershell
source\bin\activate # for CommandPrompt
source ./venv/bin/activate # for MacOS
```
Your terminal should be prefixed with `(venv)` when the virtual environment is activated.

## Run the project

Install all dependencies listed in `requirements.txt` by running the command:

```cmd
pip install -r requirements.txt
```

Run the project by executing:

```cmd
uvicorn app.main:app --reload
```