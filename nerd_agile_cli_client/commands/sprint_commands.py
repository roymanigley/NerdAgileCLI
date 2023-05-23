from datetime import date

import click

from client.SprintClient import client
from model import Sprint, ClassMapper

from printer import print_sprint


@click.group()
def sprint_commands() -> None:
    pass


@sprint_commands.command('sprint:new')
@click.option('--name', prompt='Enter the "sprint" name', help='The name of the "sprint"', type=str)
@click.option('--start', prompt='Enter the start date for the "sprint"', help='The start date of the "sprint"', type=click.DateTime(formats=["%Y-%m-%d"]))
@click.option('--end', prompt='Enter the end date for the "sprint"', help='The end date of the "sprint"', type=click.DateTime(formats=["%Y-%m-%d"]))
@click.option('--project_id', prompt='Enter the project_id for the "sprint"', help='The project_id of the "sprint"', type=int)
@click.option('--goal', help='The goal of the "sprint"', type=str)
def update(name: str, goal: str, start: date, end: date, project_id: int) -> None:
    sprint = client.create(Sprint(name, goal, start, end, project_id))
    print_sprint(sprint)


@sprint_commands.command('sprint:show')
@click.argument('id', required=False, type=int)
def show(id: int) -> None:
    if (id is None):
        sprints = client.find_all()
        [print_sprint(p) for p in sprints]
    else:
        sprint = client.find_one(id)
        print_sprint(sprint)


@sprint_commands.command('sprint:update')
@click.option('--id', prompt='Enter the "sprint" id', help='The id of the "sprint"', type=str)
@click.option('--name', help='The name of the "sprint"', type=str)
@click.option('--goal', help='The goal of the "sprint"', type=str)
@click.option('--start', help='The start date of the "sprint"', type=click.DateTime(formats=["%Y-%m-%d"]))
@click.option('--end', help='The end date of the "sprint"', type=click.DateTime(formats=["%Y-%m-%d"]))
@click.option('--project_id', help='The project_id of the "sprint"', type=int)
def update(id: int, name: str, goal: str, start: date, end: date, project_id: int) -> None:
    sprint = client.update_partial(Sprint(name, goal, start, end, project_id), id)
    print_sprint(sprint)


@sprint_commands.command('sprint:delete')
@click.option('--id', prompt='Enter the id of the "sprint" to delete', help='The id of the "sprint"', type=int)
def delete(id: int) -> None:
    client.delete(id)
    print('deleted')
