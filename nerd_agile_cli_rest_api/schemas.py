from ninja import Schema
from datetime import date, datetime

from nerd_agile_cli_rest_api.models import FeaturePriority, Status, TaskType


class ProjectSchemaIn(Schema):
    name: str


class ProjectSchemaOut(Schema):
    id: int = None
    name: str
    creator: str
    create_date: datetime


class EpicSchemaIn(Schema):
    name: str
    tags: str
    project_id: int = None


class EpicSchemaOut(Schema):
    id: int = None
    name: str
    tags: str
    creator: str
    create_date: datetime
    project: ProjectSchemaOut = None


class FeatureSchemaIn(Schema):
    name: str
    priority: FeaturePriority
    tags: str
    epic_id: int = None


class FeatureSchemaOut(Schema):
    id: int = None
    name: str
    priority: FeaturePriority
    tags: str
    creator: str
    create_date: datetime
    epic: EpicSchemaOut = None


class SprintSchemaIn(Schema):
    name: str
    goal: str
    start: date
    end: date
    project_id: int = None


class SprintSchemaOut(Schema):
    id: int = None
    name: str
    goal: str
    start: date
    end: date
    creator: str
    create_date: datetime
    project: ProjectSchemaOut = None


class TaskSchemaIn(Schema):
    name: str
    description: str
    task_type: str
    task_status: Status
    tags: str
    estimation: int
    sprint_order: int
    assignee: str
    sprint_id: int
    feature_id: int


class TaskSchemaOut(Schema):
    id: int = None
    name: str
    description: str
    task_type: TaskType
    task_status: Status
    tags: str
    estimation: int
    sprint_order: int
    assignee: str
    creator: str
    create_date: datetime
    sprint: SprintSchemaOut = None
    feature: FeatureSchemaOut = None


class SubTaskSchemaIn(Schema):
    name: str
    description: str
    task_id: int = None


class SubTaskSchemaOut(Schema):
    id: int = None
    name: str
    description: str
    creator: str
    create_date: datetime
    task: TaskSchemaOut = None


class CommentSchemaIn(Schema):
    content: str
    task_id: int = None


class CommentSchemaOut(Schema):
    id: int = None
    content: str
    creator: str
    create_date: datetime
    task: TaskSchemaOut = None
