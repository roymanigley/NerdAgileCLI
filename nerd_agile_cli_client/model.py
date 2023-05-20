from datetime import date, datetime
from enum import Enum
from typing import TypeVar, Generic

class Status(Enum):
    IN_PLANNING = 'IN_PLANNING'
    PLANNED = 'PLANNED'
    IN_PROGRESS = 'IN_PROGRESS'
    BLOCKED = 'BLOCKED'
    CHECKING = 'CHECKING'
    RESOLVED = 'RESOLVED'
    WONT_RESOLVE = 'WONT_RESOLVE'


class FeaturePriority(Enum):
    MUST = 'MUST'
    SHOULD = 'SHOULD'
    COULD = 'COULD'
    WONT = 'WONT'


class TaskType(Enum):
    BUG = 'BUG'
    STORY = 'STORY'
    DEVOPS = 'DEVOPS'


class Project(object):

    def __init__(self, name: str):
        self.id: int
        self.name: str = name
        self.creator: str
        self.create_date: datetime


class Epic(object):

    def __init__(self, name: str, tags: str, project_id: int):
        self.id: int = None
        self.name: str = name
        self.tags: str = tags
        self.creator: str
        self.create_date: datetime
        self.project: Project = None
        self.project_id: int = project_id


class Feature(object):

    def __init__(self, name: str, tags: str, priority: FeaturePriority, epic_id: int):
        self.id: int
        self.name: str = name
        self.tags: str = tags
        self.priority = priority
        self.creator: str
        self.create_date: datetime
        self.epic: Epic
        self.epic_id = epic_id


class Sprint(object):

    def __init__(self, name: str, goal: str, start: date, end: date, project_id: int):
        self.id: int
        self.name: str = name
        self.goal: str = goal
        self.start: date = start.isoformat()[:10]
        self.end: date = end.isoformat()[:10]
        self.creator: str
        self.create_date: datetime
        self.project: Project
        self.project_id = project_id


class Task(object):

    def __init__(self, name: str, description: str, task_type: TaskType, task_status: Status, tags: str,
                 estimation: int, sprint_order: int, assignee: str, sprint_id: int, feature_id: int):
        self.id: int
        self.name: str = name
        self.description: str = description
        self.task_type: TaskType = task_type
        self.task_status: Status = task_status
        self.tags: str = tags
        self.estimation: int = estimation
        self.sprint_order: int = sprint_order
        self.assignee: str = assignee
        self.creator: str
        self.create_date: datetime
        self.sprint: Sprint
        self.sprint_id = sprint_id
        self.feature: Feature
        self.feature_id = feature_id


class SubTask(object):

    def __init__(self, name: str, description: str, task_id: int):
        self.id: int = None
        self.name: str = name
        self.description: str = description
        self.creator: str
        self.create_date: datetime
        self.task: Task = None
        self.task_id: int = task_id


class Comment(object):

    def __init__(self, content: str, task_id: int):
        self.id: int
        self.content: str = content
        self.creator: str
        self.create_date: datetime
        self.task: Task
        self.task_id: int = task_id


T = TypeVar('T')


class ClassMapper(Generic[T]):

    def __init__(self, dictionary: dict):
        for key in dictionary.keys():
            self.__setattr__(key, dictionary[key])

    def to_class(self) -> T:
        return self
