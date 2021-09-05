
# FORMPLUS test

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/silvareal/formplus_backend_test.git
$ cd  formplus_backend_test
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv --no-site-packages vnv
$ source vnv/bin/activate
```

Then install the dependencies:

```sh
$ (env) pip install -r requirements.txt
```


**Parse a .env (dotenv) file directly using BASH**
```sh
$ export $(egrep -v '^#' .env | xargs)
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.


## Tests

To run the tests, `cd` into the directory where `manage.py` is:
```sh
(env)$ python manage.py test --verbosity 2
```
## Redis setup
ensure redis is install on your os, for linus os, simply run this command on terminal
```
$ sudo apt-get install redis-server
```
fire up the server:
```
$ redis-server
```
You can test that Redis is working properly by typing this into your terminal:
```
$ redis-cli-ping
```
redis should reply  with PONG 

if you already have redis server running on the default port, and you consider it safe to kill the process run:

```
$ sudo service redis-server stop
```

## Migrate data from remote endpoint to local 
```
$ python manage.py loadtemplate
```
# Data sample response

```json
{
  "count": 1841,
  "next": "http://127.0.0.1:8000/list/",
  "previous": null,
  "results": [
    {
      "name": "tempor elit, dolore",
      "created": "2021-08-28T07:29:47.983354",
      "category": [
        {
          "name": "Health"
        },
        {
          "name": "E-commerce"
        },
        {
          "name": "Education"
        }
      ],
      "description": "dolor irure consequat. veniam, Lorem",
      "link": "https://formpl.us/templates"
    },
    {
      "name": "reprehenderit tempor magna",
      "created": "2021-08-28T07:29:48.025114",
      "category": [
        {
          "name": "Health"
        },
        {
          "name": "E-commerce"
        },
        {
          "name": "Education"
        }
      ],
      "description": "elit, laboris commodo dolor amet,",
      "link": "https://formpl.us/templates"
    },
    {
      "name": "ullamco voluptate tempor",
      "created": "2021-08-28T07:29:48.102948",
      "category": [
        {
          "name": "Health"
        },
        {
          "name": "E-commerce"
        },
        {
          "name": "Education"
        }
      ],
      "description": "exercitation reprehenderit fugiat elit, Lorem",
      "link": "https://formpl.us/templates"
    },
    }
```

- GET all template [{BASE_URL}/list/](#)
- Filter template by any of the three category  [{BASE_URL}/list/?category=Health](#)
- Search through each template within the active category  [{BASE_URL}/list/?category=Health&search=tempor](#)
- Sort template by sorted by either `names` or `created` and order_by `Ascending`, `Decending` and `Default`  [{BASE_URL}/list/?sort_by=name&order_by=Ascending](#)
- `Note:` GET response of template is paginated and max size for each page is 500 [{BASE_URL}/list/?page=2](#)