import click

from client.FeatureClient import client
from model import Feature, FeaturePriority, ClassMapper

from printer import print_feature


@click.group()
def feature_commands() -> None:
    pass


@feature_commands.command('feature:new')
@click.option('--name', prompt='Enter the "feature" name', help='The name of the "feature"', type=str)
@click.option('--priority', prompt='Enter the priority for the "feature"', help='The priority of the "feature"', type=click.Choice([e.value for e in FeaturePriority]))
@click.option('--epic_id', prompt='Enter the epic_id for the "feature"', help='The epic_id of the "feature"', type=int)
@click.option('--tags', help='The tags of the "feature"', type=str)
def new(name: str, tags: str, priority: str, epic_id: int) -> None:
    feature = client.create(Feature(name, tags, priority, epic_id))
    print_feature(feature)


@feature_commands.command('feature:show')
@click.argument('id', required=False, type=int)
def show(id: int) -> None:
    if (id is None):
        features = client.find_all()
        [print_feature(p) for p in features]
    else:
        feature = client.find_one(id)
        print_feature(feature)


@feature_commands.command('feature:update')
@click.option('--id', prompt='Enter the "feature" id', help='The id of the "feature"', type=str)
@click.option('--name', help='The name of the "feature"', type=str)
@click.option('--epic_id', help='The epic_id of the "feature"', type=int)
@click.option('--tags', help='The tags of the "feature"', type=str)
def update(id: int, name: str, tags: str, epic_id: int) -> None:
    feature = client.update_partial(Feature(name, tags, epic_id), id)
    print_feature(feature)


@feature_commands.command('feature:delete')
@click.option('--id', prompt='Enter the id of the "feature" to delete', help='The id of the "feature"', type=int)
def delete(id: int) -> None:
    client.delete(id)
    print('deleted')
