import click

from client.EpicClient import client
from model import Epic, ClassMapper

from printer import print_epic


@click.group()
def epic_commands() -> None:
    pass


@epic_commands.command('epic:new')
@click.option('--name', prompt='Enter the "epic" name', help='The name of the "epic"', type=str)
@click.option('--project_id', prompt='Enter the project_id for the "epic"', help='The project_id of the "epic"', type=int)
@click.option('--tags', help='The tags of the "epic"', type=str)
def new(name: str, tags: str, project_id: int) -> None:
    epic = client.create(Epic(name, tags, project_id))
    print_epic(epic)


@epic_commands.command('epic:show')
@click.argument('id', required=False, type=int)
def show(id: int) -> None:
    if (id is None):
        epics = client.find_all()
        [print_epic(p) for p in epics]
    else:
        epic = client.find_one(id)
        print_epic(epic)


@epic_commands.command('epic:update')
@click.option('--id', prompt='Enter the "epic" id', help='The id of the "epic"', type=str)
@click.option('--name', help='The name of the "epic"', type=str)
@click.option('--project_id', help='The project_id of the "epic"', type=int)
@click.option('--tags', help='The tags of the "epic"', type=str)
def update(id: int, name: str, tags: str, project_id: int) -> None:
    epic = client.update_partial(Epic(name, tags, project_id), id)
    print_epic(epic)


@epic_commands.command('epic:delete')
@click.option('--id', prompt='Enter the id of the "epic" to delete', help='The id of the "epic"', type=int)
def delete(id: int) -> None:
    client.delete(id)
    print('deleted')
