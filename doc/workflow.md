# Make workflow

## Install require packages

```sh
pip install -r deploy/requirements.txt
```

## Testing 

After install requirements you should run tets.

```
cd base_app
pytest
```

# Run using gunicorn 

```sh
cd base_app
gunicorn -w 3 -b 0.0.0.0:8000 base_app.wsgi:application 
```
