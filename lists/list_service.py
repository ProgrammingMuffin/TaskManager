from .models import List, Task
from database import db
from .dtos import TaskListDto, TaskListsDto,\
    TaskDto, TasksDto
from .constants import TaskStatus
import json
import time
from flask import make_response, abort

global STRP_FORMAT
STRP_FORMAT = "%H:%M:%S"


def create_and_get_list(name, recurring_deadline):
    new_list = List(name=name, recurring_deadline=\
            time.strptime(recurring_deadline, STRP_FORMAT))
    return new_list


def create_and_get_task(name, status, description, list_id):
    new_task = Task(name=name, status=status,
            description=description, list_id=list_id)
    return new_task


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
        task_list_dto = TaskListDto(task_list.id, task_list.name,
                task_list.recurring_deadline.strftime(STRP_FORMAT))
        task_list_dtos.append(task_list_dto.__dict__)
    task_lists_dto = TaskListsDto(task_list_dtos)
    return json.dumps(task_lists_dto.__dict__)


def delete_task_list(list_id):
    response = dict()
    task_list = List.query.get(list_id)
    if task_list:
        db.session.delete(task_list)
        db.session.commit()
        response["message"] = "List deleted"
        return response
    response["message"] = "List not found"
    abort(make_response(json.dumps(response), 404))


def create_task(request_dict):
    new_task = create_and_get_task(request_dict["name"], TaskStatus.NOT_DONE.value,
            request_dict["description"], request_dict["list_id"])
    db.session.add(new_task)
    db.session.commit()
    response = dict()
    response["message"] = "created a new task for list" +\
        str(request_dict["list_id"])
    return response


def getListTasks(list_id):
    list_tasks = Task.query.filter_by(list_id=list_id).all()
    taskDtos = []
    for list_task in list_tasks:
        task_dto = TaskDto(list_task.id, list_task.name,
                list_task.status, list_task.description)
        taskDtos.append(task_dto.__dict__)
    tasksDto = TasksDto(taskDtos)
    return json.dumps(tasksDto.__dict__)

