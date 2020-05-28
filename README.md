# BBT Tracker

## Getting Started
#### Requirements
* Python (currently using 3.6.8)
* MySQL database
* venv

#### Virtual Environment
Create a virtual environment. On windows, the command is as follows:

```py -m venv env```

Now run the virtual environment:

```./env/Scripts/activate```

#### Install the dependencies:

```pip install -r requirements.txt```

#### Setup Configuration
- under config.py set the value for `SQLALCHEMY_DATABASE_URI` to the uri of your database

#### Setup Database
In the terminal run:
```
flask shell
from app import db
db.create_all()
exit()
```
this will create the necessary database tables

### 

## Starting the app
To start the app, run the following command:

`flask run`
