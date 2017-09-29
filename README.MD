## Boilerplate template for Flask

As of now this template is for **Development** use, for production I recommend that you read [this documentation](https://exploreflask.com). Making it ready for production is in my Todo list for this project.

The design pattern looks like this -
```
boilerplate/
        boilerplate/
                static/
                templates/
                __init__.py
                database.py
                forms.py
                models.py
                views.py
        instance/
                config.py   [this is not in git repo, all your SECRET_KEY, DB URI goes here]
        venv/ [pip install -r requirements.txt will create this folder/virtual environment]
        config.py
        createdb.py
        README.MD
        requirements.txt
        run.py
```

Uses following packages -

1. Flask ("**Lego blocks of Web Development**")
2. flask-wtf (WTF FORMS)
3. flask-sqlalchemy (ORM)
4. psycopg2 (PostgreSQL DB)

Screenshot -

![Flask Boilerplate](/Screenshot.png)

### Features -

1. Create records using Contact form (uses WTForms)
2. Fetches records from PostgreSQL DB & displays on HTML via Jinja2 templates

### Todo -

1. Blueprints
2. Update & Delete operations
3. Login & Sessions/cookies
4. OAuth & Social Sign in
5. Flask admin
6. Production proof
7. Dockerise
8. and more...

=======
=====================================================================================

MIT License

Copyright (c) 2017 Nikhil Akki

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
