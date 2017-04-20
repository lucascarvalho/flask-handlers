# flask-handlers

## How to install?
```bash
$ pip install flask_handlers
```

## How to use?
```python
from flask import Flask
from flask_handlers import set_json_error_handler

app = Flask(__name__)
set_json_error_handler(app)
```
