from Flask import Blueprint

list_controller = Blueprint("list_controller", __name__)

@list_controller.route("/", methods=["POST"])
def createList():
	return "created a list"