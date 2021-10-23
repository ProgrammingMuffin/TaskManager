from database import db
from datetime import datetime


class Audited: 
    created_at = db.Column("created_at",
            db.DateTime, nullable=False, default=datetime.now())
    modified_at = db.Column("modified_at",
            db.DateTime, nullable=False, default=datetime.now())


class List(db.Model, Audited):
    ''' This class represents a list '''
    __tablename__ = "lists"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String, nullable=False)
    recurring_deadline = db.Column("recurring_deadline", 
            db.Time, nullable=False)
    tasks = db.relationship("Task", backref="task_list")
    list_properties = db.relationship("ListProperty", backref="task_list")


class Task(db.Model, Audited):
    ''' This class represents a task '''
    __tablename__ = "tasks"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String, nullable=False)
    status = db.Column("status", db.String, nullable=False)
    description = db.Column("description", db.String)
    list_id = db.Column("list_id", db.ForeignKey(List.id),
            nullable=False)
    soft_deleted = db.Column("soft_deleted", db.BOOLEAN, nullable=False)


class ListProperty(db.Model, Audited):
    ''' This class represents list properties'''
    __tablename__ = "list_properties"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String, nullable=False)
    value = db.Column("value", db.String, nullable=False)
    list_id = db.Column("list_id", db.ForeignKey(List.id),
            nullable=False)
