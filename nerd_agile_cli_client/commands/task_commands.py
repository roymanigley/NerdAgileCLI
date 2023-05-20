from datetime import date

import click

from client.TaskClient import client
from model import Task, TaskType, Status, ClassMapper

from printer import print_task


@click.group()
def task_commands() -> None:
    pass


@task_commands.command('task:new')
@click.option('--name', prompt='Enter the "task" name', help='The name of the "task"', type=str)
@click.option('--description', prompt='Enter the description for the "task"', help='The description of the "task"', type=str)
@click.option('--tags', prompt='Enter the tags for the "task"', help='The tags of the "task"', type=str)
@click.option('--type', prompt='Enter the task type date for the "task"', help='The task type of the "task"', type=click.Choice([e.value for e in TaskType]))
@click.option('--status', prompt='Enter the status for the "task"', help='The status of the "task"', type=click.Choice([e.value for e in Status]))
@click.option('--estimation', prompt='Enter the estimation for the "task"', help='The estimation of the "task"', type=int)
@click.option('--sprint_order', prompt='Enter the sprint order for the "task"', help='The sprint order of the "task"', type=int)
@click.option('--assignee', prompt='Enter the assignee for the "task"', help='The assignee of the "task"', type=str)
@click.option('--sprint_id', prompt='Enter the sprint_id for the "task"', help='The sprint_id of the "task"', type=int)
@click.option('--feature_id', prompt='Enter the feature_id for the "task"', help='The feature_id of the "task"', type=int)
def update(name: str, description: str, type: TaskType, status: Status, tags: str,
           estimation: int, sprint_order: int, assignee: str, sprint_id: int, feature_id: int) -> None:
    task = client.create(Task(name, description, type, status, tags, estimation, sprint_order, assignee,
                              sprint_id, feature_id))
    print_task(task)


@task_commands.command('task:show')
@click.argument('id', required=False, type=int)
def show(id: int) -> None:
    if (id is None):
        tasks = client.find_all()
        [print_task(p) for p in tasks]
    else:
        task = client.find_one(id)
        print_task(task)


@task_commands.command('task:update')
@click.option('--id', prompt='Enter the "task" id', help='The id of the "task"', type=str)
@click.option('--name', prompt='Enter the "task" name', help='The name of the "task"', type=str)
@click.option('--description', prompt='Enter the description for the "task"', help='The description of the "task"', type=str)
@click.option('--tags', prompt='Enter the tags for the "task"', help='The tags of the "task"', type=str)
@click.option('--type', prompt='Enter the task type date for the "task"', help='The task type of the "task"', type=click.Choice([e.value for e in TaskType]))
@click.option('--status', prompt='Enter the status for the "task"', help='The status of the "task"', type=click.Choice([e.value for e in Status]))
@click.option('--estimation', prompt='Enter the estimation for the "task"', help='The estimation of the "task"', type=int)
@click.option('--sprint_order', prompt='Enter the sprint order for the "task"', help='The sprint order of the "task"', type=int)
@click.option('--assignee', prompt='Enter the assignee for the "task"', help='The assignee of the "task"', type=str)
@click.option('--sprint_id', prompt='Enter the sprint_id for the "task"', help='The sprint_id of the "task"', type=int)
@click.option('--feature_id', prompt='Enter the feature_id for the "task"', help='The feature_id of the "task"', type=int)
def update(id: int, name: str, description: str, type: TaskType, status: Status, tags: str,
                 estimation: int, sprint_order: int, assignee: str, sprint_id: int, feature_id: int) -> None:
    task = client.update(Task(name, description, type, status, tags, estimation, sprint_order, assignee,
                              sprint_id, feature_id), id)
    print_task(task)


@task_commands.command('task:delete')
@click.option('--id', prompt='Enter the id of the "task" to delete', help='The id of the "task"', type=int)
def delete(id: int) -> None:
    client.delete(id)
    print('deleted')
