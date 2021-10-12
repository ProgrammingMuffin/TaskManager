from flask import Blueprint, request
from .models import List
from . import list_service
from database import db


lists = Blueprint("list_controller", __name__)


@lists.route("", methods=["POST"])
def createList():
    request_json = request.json
    response = list_service.create_task_list(request_json)
    return response


@lists.route("", methods=["GET"])
def getAllLists():
    return list_service.get_all_lists()
