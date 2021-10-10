from flask import Blueprint


lists = Blueprint("list_controller", __name__)

@lists.route("", methods=["POST"])
def createList():
    return "created a list"

