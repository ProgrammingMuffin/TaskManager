from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from lists.views import lists


app = Flask(__name__)
app.config.from_pyfile(os.path.join('.', 'config.py'))
db = SQLAlchemy(app)

app.register_blueprint(lists, url_prefix="/lists")

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

