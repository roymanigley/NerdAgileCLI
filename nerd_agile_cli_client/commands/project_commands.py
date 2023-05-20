import click

from client.ProjectClient import client
from model import Project, ClassMapper

from printer import print_project


@click.group()
def project_commands() -> None:
    pass


@project_commands.command('project:new')
@click.option('--name', prompt='Enter the "project" name', help='The name of the "project"', type=str)
def new(name: str) -> None:
    project = client.create(Project(name))
    print_project(project)


@project_commands.command('project:show')
@click.argument('id', required=False, type=int)
def show(id: int) -> None:
    if (id is None):
        projects = client.find_all()
        [print_project(p) for p in projects]
    else:
        project = client.find_one(id)
        print_project(project)


@project_commands.command('project:update')
@click.option('--id', prompt='Enter the id of the "project" to update', help='The id of the "project"', type=int)
@click.option('--name', prompt='Enter the "project" name', help='The name of the "project"', type=str)
def update(id: int, name: str) -> None:
    project = client.update(Project(name), id)
    print_project(project)


@project_commands.command('project:delete')
@click.option('--id', prompt='Enter the id of the "project" to delete', help='The id of the "project"', type=int)
def delete(id: int) -> None:
    client.delete(id)
    print('deleted')
