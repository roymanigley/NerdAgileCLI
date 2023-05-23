from datetime import date

import click

from client.CommentClient import client
from model import Comment, Status, ClassMapper

from printer import print_comment


@click.group()
def comment_commands() -> None:
    pass


@comment_commands.command('comment:new')
@click.option('--task_id', prompt='Enter the task_id for the "comment"', help='The task_id of the "comment"', type=int)
def create(task_id: int) -> None:
    content = click.edit()
    comment = client.create(Comment(content, task_id))
    print_comment(comment)


@comment_commands.command('comment:show')
@click.argument('id', required=False, type=int)
def show(id: int) -> None:
    if (id is None):
        comments = client.find_all()
        [print_comment(p) for p in comments]
    else:
        comment = client.find_one(id)
        print_comment(comment)


@comment_commands.command('comment:update')
@click.option('--id', prompt='Enter the "comment" id', help='The id of the "comment"', type=str)
@click.option('--task_id', help='The task_id of the "comment"', type=int)
def update(id: int, task_id: int) -> None:
    content = click.edit(client.find_one(id).content)
    comment = client.update_partial(Comment(content, task_id), id)
    print_comment(comment)


@comment_commands.command('comment:delete')
@click.option('--id', prompt='Enter the id of the "comment" to delete', help='The id of the "comment"', type=int)
def delete(id: int) -> None:
    client.delete(id)
    print('deleted')
