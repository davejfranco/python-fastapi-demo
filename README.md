# Python FastAPI DEMO

This DEMO API will be used to showcase fastAPI, CICD and more.

## Requirements

python >= 3.9

## Instruction

1. Create virtual environment
```
virtualenv -p python3 .venv
```

2. Install requirements
```
pip install -r requirements.txt
```

3. Test Code
```
pytest test/test.py
```

4. Start API
```
uvicorn app.main:app --reload
```