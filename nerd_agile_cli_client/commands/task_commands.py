from datetime import date

import click

from client.TaskClient import client
from model import Task, TaskType, Status, ClassMapper

from printer import print_task, print_tasks


@click.group()
def task_commands() -> None:
    pass


@task_commands.command('task:new')
@click.option('--name', prompt='Enter the "task" name', help='The name of the "task"', type=str)
@click.option('--tags', help='The tags of the "task"', type=str)
@click.option('--type', prompt='Enter the task type date for the "task"', help='The task type of the "task"', type=click.Choice([e.value for e in TaskType]))
@click.option('--status', help='The status of the "task"', type=click.Choice([e.value for e in Status]))
@click.option('--estimation', help='The estimation of the "task"', type=int)
@click.option('--sprint_order', help='The sprint order of the "task"', type=int)
@click.option('--assignee', help='The assignee of the "task"', type=str)
@click.option('--sprint_id', help='The sprint_id of the "task"', type=int)
@click.option('--feature_id', help='The feature_id of the "task"', type=int)
def new(name: str, type: TaskType, status: Status, tags: str,
           estimation: int, sprint_order: int, assignee: str, sprint_id: int, feature_id: int) -> None:
    description = click.edit()
    task = client.create(Task(name, description, type, status, tags, estimation, sprint_order, assignee,
                              sprint_id, feature_id))
    print_task(task)


@task_commands.command('task:show')
@click.argument('id', required=False, type=int)
def show(id: int) -> None:
    if (id is None):
        tasks = client.find_all()
        print_tasks(tasks)
    else:
        task = client.find_one(id)
        print_task(task)


@task_commands.command('task:update')
@click.option('--id', prompt='Enter the "task" id', help='The id of the "task"', type=str)
@click.option('--name', help='The name of the "task"', type=str)
@click.option('--tags', help='The tags of the "task"', type=str)
@click.option('--type', help='The task type of the "task"', type=click.Choice([e.value for e in TaskType]))
@click.option('--status', help='The status of the "task"', type=click.Choice([e.value for e in Status]))
@click.option('--estimation', help='The estimation of the "task"', type=int)
@click.option('--sprint_order', help='The sprint order of the "task"', type=int)
@click.option('--assignee', help='The assignee of the "task"', type=str)
@click.option('--sprint_id', help='The sprint_id of the "task"', type=int)
@click.option('--feature_id', help='The feature_id of the "task"', type=int)
def update(id: int, name: str, type: TaskType, status: Status, tags: str,
                 estimation: int, sprint_order: int, assignee: str, sprint_id: int, feature_id: int) -> None:
    description = click.edit(client.find_one(id).description)
    task = client.update_partial(Task(name, description, type, status, tags, estimation, sprint_order, assignee,
                                      sprint_id, feature_id), id)
    print_task(task)


@task_commands.command('task:delete')
@click.option('--id', prompt='Enter the id of the "task" to delete', help='The id of the "task"', type=int)
def delete(id: int) -> None:
    client.delete(id)
    print('deleted')
