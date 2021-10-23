#######################
# DTOs are Data Transfer Objects
# They can be serialized to json
# or anything for that matter
#######################

class TaskListsDto:

    def __init__(self):
        self.lists = []
    
    def set_lists(self, taskListDtos=[]):
        self.lists = taskListDtos


class TaskListDto:

    def __init__(self):
        self.id = ""
        self.name = ""
        self.recurring_deadline = None

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_recurring_deadline(self, recurring_deadline):
        self.recurring_deadline = recurring_deadline


