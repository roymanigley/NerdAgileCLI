from datetime import date

import click

from client.SubTaskClient import client
from model import SubTask, Status, ClassMapper

from printer import print_sub_task, print_sub_tasks


@click.group()
def sub_task_commands() -> None:
    pass


@sub_task_commands.command('sub_task:new')
@click.option('--name', prompt='Enter the "sub_task" name', help='The name of the "sub_task"', type=str)
@click.option('--task_id', prompt='Enter the task_id for the "sub_task"', help='The task_id of the "sub_task"', type=int)
def new(name: str, task_id: int) -> None:
    description = click.edit()
    sub_task = client.create(SubTask(name, description, task_id))
    print_sub_task(sub_task)


@sub_task_commands.command('sub_task:show')
@click.argument('id', required=False, type=int)
def show(id: int) -> None:
    if (id is None):
        sub_tasks = client.find_all()
        print_sub_tasks(sub_tasks)
    else:
        sub_task = client.find_one(id)
        print_sub_task(sub_task)


@sub_task_commands.command('sub_task:update')
@click.option('--id', prompt='Enter the "sub_task" id', help='The id of the "sub_task"', type=str)
@click.option('--name', help='The name of the "sub_task"', type=str)
@click.option('--task_id', help='The feature_id of the "sub_task"', type=int)
def update(id: int, name: str, task_id: int) -> None:
    description = click.edit(client.find_one(id).description)
    sub_task = client.update_partial(SubTask(name, description, task_id), id)
    print_sub_task(sub_task)


@sub_task_commands.command('sub_task:delete')
@click.option('--id', prompt='Enter the id of the "sub_task" to delete', help='The id of the "sub_task"', type=int)
def delete(id: int) -> None:
    client.delete(id)
    print('deleted')
