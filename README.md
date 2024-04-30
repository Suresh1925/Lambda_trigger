# SmoothGPT Authenticator API

A REST API to handle smooth GPT user authentication

### Python + FastAPI + PostgreSQL + Mangum + AWS Lambda 

A project to enable user verification the AWS Lambda with Python FastAPI framework

### Install dependencies

A requirements file declare all dependencies (Mangum, FastAPI, Uvicorn, ...). Use the following command to install the reuqired dependencies (For Python 3.9)

```
pip install -r ./requirements.txt
```

### Run locally

You can either use the following command :

```
python -m main.py
```

Or deploy on uvicorn :

```
uvicorn fastapi_smoothgpt.main:app --reload --host 0.0.0.0 --port 5000
```

You can test the application by using the following command : 

```
http://localhost:5000/v1/documentation
```

