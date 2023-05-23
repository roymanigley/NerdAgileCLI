from typing import Optional

from ninja import Schema
from datetime import date, datetime

from nerd_agile_cli_rest_api.models import FeaturePriority, Status, TaskType


class ProjectSchemaIn(Schema):
    name: str


class ProjectSchemaInPatch(Schema):
    name: Optional[str]


class ProjectSchemaOut(Schema):
    id: int
    name: str
    creator: str
    create_date: datetime


class EpicSchemaIn(Schema):
    name: str
    tags: Optional[str]
    project_id: int


class EpicSchemaInPatch(Schema):
    name: Optional[str]
    tags: Optional[str]
    project_id: Optional[int]


class EpicSchemaOut(Schema):
    id: int
    name: str
    tags: Optional[str]
    creator: str
    create_date: datetime
    project: ProjectSchemaOut


class FeatureSchemaIn(Schema):
    name: str
    priority: FeaturePriority
    tags: Optional[str]
    epic_id: int


class FeatureSchemaInPatch(Schema):
    name: Optional[str]
    priority: Optional[FeaturePriority]
    tags: Optional[str]
    epic_id: Optional[int]


class FeatureSchemaOut(Schema):
    id: int
    name: str
    priority: FeaturePriority
    tags: Optional[str]
    creator: str
    create_date: datetime
    epic: EpicSchemaOut


class SprintSchemaIn(Schema):
    name: str
    goal: Optional[str]
    start: date
    end: date
    project_id: int


class SprintSchemaInPatch(Schema):
    name: Optional[str]
    goal: Optional[str]
    start: Optional[date]
    end: Optional[date]
    project_id: Optional[int]


class SprintSchemaOut(Schema):
    id: int
    name: str
    goal: Optional[str]
    start: date
    end: date
    creator: str
    create_date: datetime
    project: ProjectSchemaOut


class TaskSchemaIn(Schema):
    name: str
    description: str
    task_type: str
    task_status: Optional[Status]
    tags: Optional[str]
    estimation: Optional[int]
    sprint_order: Optional[int]
    assignee: Optional[str]
    sprint_id: Optional[int]
    feature_id: Optional[int]


class TaskSchemaInPatch(Schema):
    name: Optional[str]
    description: Optional[str]
    task_type: Optional[str]
    task_status: Optional[Status]
    tags: Optional[str]
    estimation: Optional[int]
    sprint_order: Optional[int]
    assignee: Optional[str]
    sprint_id: Optional[int]
    feature_id: Optional[int]


class TaskSchemaOut(Schema):
    id: int
    name: str
    description: str
    task_type: TaskType
    task_status: Optional[Status]
    tags: Optional[str]
    estimation: Optional[int]
    sprint_order: Optional[int]
    assignee: Optional[str]
    creator: str
    create_date: datetime
    sprint: Optional[SprintSchemaOut]
    feature: Optional[FeatureSchemaOut]


class SubTaskSchemaIn(Schema):
    name: str
    description: str
    task_id: int


class SubTaskSchemaInPatch(Schema):
    name: Optional[str]
    description: Optional[str]
    task_id: Optional[int]


class SubTaskSchemaOut(Schema):
    id: int
    name: str
    description: str
    creator: str
    create_date: datetime
    task: TaskSchemaOut


class CommentSchemaIn(Schema):
    content: str
    task_id: int


class CommentSchemaInPatch(Schema):
    content: Optional[str]
    task_id: Optional[int]


class CommentSchemaOut(Schema):
    id: int
    content: str
    creator: str
    create_date: datetime
    task: TaskSchemaOut
