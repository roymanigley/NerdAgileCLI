from model import Project, Epic, Feature, Sprint, Task, SubTask, Comment
from rich.markdown import Markdown
from rich.console import Console

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
- description : {task.description}
- type        : {task.task_type}
- status      : {task.task_status}
- tags        : {task.tags}
- estimation  : {task.estimation}
- sprint order: {task.sprint_order}
- sprint 
    - name     : {task.sprint["name"]}
    - id       : {task.sprint["id"]}
- feature 
    - name     : {task.feature["name"]}
    - id       : {task.feature["id"]}
- creator     : {task.creator}
- create_date : {task.create_date}
---
    ''')
    console.print(md)


def print_sub_task(sub_task: SubTask):
    md = Markdown(f'''# Sub-Task: {sub_task.name}
- id          : {sub_task.id}
- name        : {sub_task.name}
- description : {sub_task.description}
- task 
    - name     : {sub_task.task["name"]}
    - id       : {sub_task.task["id"]}
- creator     : {sub_task.creator}
- create_date : {sub_task.create_date}
---
    ''')
    console.print(md)


def print_comment(comment: Comment):
    md = Markdown(f'''# Comment for Task: {comment.task["name"]} (id: {comment.task["id"]})
- id          : {comment.id}
- description : {comment.content}
- task 
    - name     : {comment.task["name"]}
    - id       : {comment.task["id"]}
- creator     : {comment.creator}
- create_date : {comment.create_date}
---
    ''')
    console.print(md)
