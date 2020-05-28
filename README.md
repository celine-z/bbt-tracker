# BBT Tracker
![drinks](https://user-images.githubusercontent.com/25543099/83160264-fa3c7b00-a0d4-11ea-933f-725be3f95063.png)

![stores](https://user-images.githubusercontent.com/25543099/83159972-9dd95b80-a0d4-11ea-8be9-b60ad125ce8f.png)

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
