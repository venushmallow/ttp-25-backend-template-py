# ttp-25-backend-template-py

Ensure that python has been installed by checking it's version:

```cmd
python -V
```

If python has not been installed, install it by checking the link here: https://realpython.com/installing-python/#macos-how-to-check-or-get-python

## Run the project

Install all dependencies listed in `requirements.txt` by running the command:

```cmd
pip install -r requirements.txt
```

Run the project by executing:

```cmd
uvicorn app.main:app --reload
```