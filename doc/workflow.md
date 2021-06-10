# Make workflow

## Install require packages

```sh
pip install -r deploy/requirements.txt
```

Need create file (.env) in directory base_app/base_app.

For example use terminal in linux.

```sh
touch base_app/base_app/.env
```

[Site when can generate key online](https://djecrety.ir/) or you can create key youself. 
And paste this key in file .env. 
File should look like.

```
SECRET_KEY=<here was your key>
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

