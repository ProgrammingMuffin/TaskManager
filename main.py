from flask import Flask
from controller.list_controller import list_controller


app = Flask(__name__)

app.register_blueprint(list_controller, url_prefix="/lists")

if __name__=='__main__':
	app.run(host='0.0.0.0', debug=True)