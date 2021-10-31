#######################
# DTOs are Data Transfer Objects
# They can be serialized to json
# or anything for that matter
#######################

class TaskListsDto:

    def __init__(self, taskListDtos):
        self.lists = taskListDtos


class TaskListDto:

    def __init__(self, id, name, recurring_deadline):
        self.id = id
        self.name = name
        self.recurring_deadline = recurring_deadline


class TasksDto:

    def __init__(self, taskDtos):
        self.tasks = taskDtos


class TaskDto:

    def __init__(self, id, name, status, description):
        self.id = id
        self.name = name
        self.status = status
        self.description = description


