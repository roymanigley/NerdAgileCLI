from itertools import zip_longest
from typing import List

from model import Project, Epic, Feature, Sprint, Task, SubTask, Comment, Status, TaskType
from rich.markdown import Markdown
from rich.console import Console
from rich.table import Table

console = Console()


def print_project(project: Project):
    md = Markdown(f'''# Project: {project.name}
- id          : {project.id}
- name        : {project.name}
- creator     : {project.creator}
- create_date : {project.create_date}
---
    ''')
    console.print(md)


def print_projects(projects: List[Project]):
    table = Table(title='Projects', expand=True)
    table.add_column('Id')
    table.add_column('Name')
    table.add_column('Creator')
    table.add_column('Creation date')

    for project in projects:
        table.add_row(str(project.id), project.name, project.creator, project.create_date)

    console.print(table)

def print_epic(epic: Epic):
    md = Markdown(f'''# Epic: {epic.name}
- id          : {epic.id}
- name        : {epic.name}
- tags        : {epic.tags}
- project 
    - name     : {epic.project["name"]}
    - id       : {epic.project["id"]}
- creator     : {epic.creator}
- create_date : {epic.create_date}
---
    ''')
    console.print(md)


def print_epics(epics: List[Epic]):
    table = Table(title='Projects', expand=True)
    table.add_column('Id')
    table.add_column('Name')
    table.add_column('Tags')
    table.add_column('Project')
    table.add_column('Creator')
    table.add_column('Creation date')

    for epic in epics:
        table.add_row(str(epic.id), epic.name, epic.tags, f'[{epic.project["id"]}] {epic.project["name"]}', epic.creator, epic.create_date)

    console.print(table)

def print_feature(feature: Feature):
    md = Markdown(f'''# Feature: {feature.name}
- id          : {feature.id}
- name        : {feature.name}
- tags        : {feature.tags}
- priority    : {feature.priority}
- epic 
    - name     : {feature.epic["name"]}
    - id       : {feature.epic["id"]}
- creator     : {feature.creator}
- create_date : {feature.create_date}
---
    ''')
    console.print(md)


def print_features(features: List[Feature]):
    table = Table(title='Projects', expand=True)
    table.add_column('Id')
    table.add_column('Name')
    table.add_column('Priority')
    table.add_column('Tags')
    table.add_column('Epic')
    table.add_column('Project')
    table.add_column('Creator')
    table.add_column('Creation date')

    for feature in features:
        table.add_row(str(feature.id), feature.name, feature.priority, feature.tags, f'[{feature.epic["id"]}] {feature.epic["name"]}', f'[{feature.epic["project"]["id"]}] {feature.epic["project"]["name"]}', feature.creator, feature.create_date)

    console.print(table)


def print_sprint(sprint: Sprint):
    md = Markdown(f'''# Sprint: {sprint.name}
- id          : {sprint.id}
- name        : {sprint.name}
- goal        : {sprint.goal}
- start       : {sprint.start}
- end         : {sprint.end}
- project 
    - name     : {sprint.project["name"]}
    - id       : {sprint.project["id"]}
- creator     : {sprint.creator}
- create_date : {sprint.create_date}
---
    ''')
    console.print(md)


def print_task(task: Task):
    md = Markdown(f'''# Task: {task.name}
- id          : {task.id}
- name        : {task.name}
- description : 
```
{task.description}
```
- type        : {task.task_type}
- status      : {task.task_status}
- tags        : {task.tags}
- estimation  : {task.estimation}
- sprint order: {task.sprint_order}
- sprint 
    - name     : {task.sprint["name"] if task.sprint is not None else None}
    - id       : {task.sprint["id"] if task.sprint is not None else None}
- feature 
    - name     : {task.feature["name"] if task.feature is not None else None}
    - id       : {task.feature["id"] if task.feature is not None else None}
- creator     : {task.creator}
- create_date : {task.create_date}
---
    ''')
    console.print(md)


def print_tasks(tasks: List[Task]):
    table = Table(title='Projects', expand=True)
    table.add_column('Id')
    table.add_column('Name')
    table.add_column('Status')
    table.add_column('Tags')
    table.add_column('Sprint')
    table.add_column('Feature')
    table.add_column('Project')
    table.add_column('Creator')
    table.add_column('Creation date')

    for task in tasks:
        table.add_row(str(task.id), task.name, task.task_status, task.tags,
                      f'{"[" + str(task.sprint["id"]) + "]" if task.sprint is not None else ""} ' +
                      f'{task.sprint["name"] if task.sprint is not None else ""}',
                      f'{"[" + str(task.feature["id"]) + "]" if task.feature is not None else ""} ' +
                      f'{task.feature["name"] + " - " if task.feature is not None else ""}' +
                      f'{"[" + str(task.feature["epic"]["id"]) + "]" if task.feature is not None else ""} ' +
                      f'{task.feature["epic"]["name"] if task.feature is not None else ""}',
                      f'{"[" + str(task.feature["epic"]["project"]["id"]) + "]" if task.feature is not None else ""} ' +
                      f'{task.feature["epic"]["project"]["name"] if task.feature is not None else ""}',
                      task.creator, task.create_date)

    console.print(table)


def print_sub_task(sub_task: SubTask):
    md = Markdown(f'''# Sub-Task: {sub_task.name}
- id          : {sub_task.id}
- name        : {sub_task.name}
- description : 
```
{sub_task.description}
```
- task 
    - name     : {sub_task.task["name"]}
    - id       : {sub_task.task["id"]}
- creator     : {sub_task.creator}
- create_date : {sub_task.create_date}
---
    ''')
    console.print(md)


def print_sub_tasks(sub_tasks: List[SubTask]):
    table = Table(title='Projects', expand=True)
    table.add_column('Id')
    table.add_column('Name')
    table.add_column('Task')
    table.add_column('Sprint')
    table.add_column('Creator')
    table.add_column('Creation date')

    for sub_task in sub_tasks:
        table.add_row(str(sub_task.id), sub_task.name,
                      f'[{sub_task.task["id"]}] {sub_task.task["name"]}',
                      f'{"[" + str(sub_task.task["sprint"]["id"]) + "] - " if sub_task.task["sprint"] is not None else ""} ' +
                      f'{sub_task.task["sprint"]["name"] if sub_task.task["sprint"] is not None else ""}',
                      sub_task.creator, sub_task.create_date)

    console.print(table)


def print_comment(comment: Comment):
    md = Markdown(f'''# Comment for Task: {comment.task["name"]} (id: {comment.task["id"]})
- id          : {comment.id}
- content : 
```
{comment.content}
```
- task 
    - name     : {comment.task["name"]}
    - id       : {comment.task["id"]}
- creator     : {comment.creator}
- create_date : {comment.create_date}
---
    ''')
    console.print(md)


def print_comments(comments: List[Comment]):
    table = Table(title='Projects', expand=True)
    table.add_column('Id')
    table.add_column('Content')
    table.add_column('Task')
    table.add_column('Creator')
    table.add_column('Creation date')

    for comment in comments:
        table.add_row(str(comment.id), comment.content,
                      f'[{comment.task["id"]}] {comment.task["name"]}',
                      comment.creator, comment.create_date)

    console.print(table)


def to_table_data(task):
    data = ''
    if task is not None:
        if task["task_type"] == TaskType.BUG.value:
            data += '🐛'
        if task["task_type"] == TaskType.STORY.value:
            data += '💫'
        if task["task_type"] == TaskType.DEVOPS.value:
            data += '👷'
        data += f' [{task["id"]:>3}] [bold]@{task["assignee"]} {task["name"]}[/bold]\n         {task["task_status"]}'
    return data


def print_sprint_with_task(sprintWithTask):


    md = Markdown(f'''# Sprint: {sprintWithTask.sprint["name"]} [{sprintWithTask.sprint["project"]["name"]}]
    ''')
    notStartedTasks = list(filter(lambda task: task["task_status"] in [Status.IN_PLANNING.value, Status.PLANNED.value], sprintWithTask.tasks))
    runningTasks = list(filter(lambda task: task["task_status"] in [Status.IN_PROGRESS.value, Status.BLOCKED.value], sprintWithTask.tasks))
    checkingTasks = list(filter(lambda task: task["task_status"] in [Status.CHECKING.value], sprintWithTask.tasks))

    closedTasks = list(filter(lambda task: task["task_status"] in [Status.RESOLVED.value, Status.WONT_RESOLVE.value], sprintWithTask.tasks))
    table = Table(title=f'🥅 {sprintWithTask.sprint["goal"]} {sprintWithTask.sprint["start"]} - {sprintWithTask.sprint["end"]}', expand=True)
    table.add_column("📋 Not started")
    table.add_column("🏃 In progress")
    table.add_column("📊 In checking")

    table.add_column("[green]✔[/green] Closed")


    for notStartedTask, runningTask, checkingTask, closedTask in list(zip_longest(notStartedTasks, runningTasks, checkingTasks, closedTasks)):
        table.add_row(
            to_table_data(notStartedTask),
            to_table_data(runningTask),
            to_table_data(checkingTask),
            to_table_data(closedTask)
        )

    console.print(md)
    console.print(table)