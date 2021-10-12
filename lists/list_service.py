from .models import List
from database import db
from .dtos import TaskListDto, TaskListsDto
import json
import time

global STRP_FORMAT
STRP_FORMAT = "%H:%M:%S"


def create_and_get_list(name, recurring_deadline):
    new_list = List(name=name, recurring_deadline=\
            time.strptime(recurring_deadline, STRP_FORMAT))
    return new_list


def create_task_list(request_dict):
    new_list = create_and_get_list(request_dict["name"],
            request_dict["recurring_deadline"])
    db.session.add(new_list)
    db.session.commit()
    response = dict()
    response["message"] = "created a new list"
    return response


def get_all_lists():
    task_lists = List.query.all()
    task_list_dtos = []
    for task_list in task_lists:
        task_list_dto = TaskListDto()
        task_list_dto.set_name(task_list.name)
        task_list_dto.set_recurring_deadline(
                task_list.recurring_deadline.strftime(STRP_FORMAT))
        task_list_dtos.append(task_list_dto.__dict__)
    task_lists_dto = TaskListsDto()
    task_lists_dto.set_lists(task_list_dtos)
    return json.dumps(task_lists_dto.__dict__)
