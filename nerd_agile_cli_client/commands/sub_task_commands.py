from datetime import date

import click

from client.SubTaskClient import client
from model import SubTask, Status, ClassMapper

from printer import print_sub_task


@click.group()
def sub_task_commands() -> None:
    pass


@sub_task_commands.command('sub_task:new')
@click.option('--name', prompt='Enter the "sub_task" name', help='The name of the "sub_task"', type=str)
@click.option('--description', prompt='Enter the description for the "sub_task"', help='The description of the "sub_task"', type=str)
@click.option('--task_id', prompt='Enter the task_id for the "sub_task"', help='The task_id of the "sub_task"', type=int)
def update(name: str, description: str, task_id: int) -> None:
    sub_task = client.create(SubTask(name, description, task_id))
    print_sub_task(sub_task)


@sub_task_commands.command('sub_task:show')
@click.argument('id', required=False, type=int)
def show(id: int) -> None:
    if (id is None):
        sub_tasks = client.find_all()
        [print_sub_task(p) for p in sub_tasks]
    else:
        sub_task = client.find_one(id)
        print_sub_task(sub_task)


@sub_task_commands.command('sub_task:update')
@click.option('--id', prompt='Enter the "sub_task" id', help='The id of the "sub_task"', type=str)
@click.option('--name', prompt='Enter the "sub_task" name', help='The name of the "sub_task"', type=str)
@click.option('--description', prompt='Enter the description for the "sub_task"', help='The description of the "sub_task"', type=str)
@click.option('--task_id', prompt='Enter the feature_id for the "sub_task"', help='The feature_id of the "sub_task"', type=int)
def update(id: int, name: str, description: str, task_id: int) -> None:
    sub_task = client.update(SubTask(name, description, task_id), id)
    print_sub_task(sub_task)


@sub_task_commands.command('sub_task:delete')
@click.option('--id', prompt='Enter the id of the "sub_task" to delete', help='The id of the "sub_task"', type=int)
def delete(id: int) -> None:
    client.delete(id)
    print('deleted')
