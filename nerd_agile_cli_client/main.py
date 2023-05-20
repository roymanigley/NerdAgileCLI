import click

from commands.project_commands import project_commands
from commands.epic_commands import epic_commands
from commands.feature_commands import feature_commands
from commands.sprint_commands import sprint_commands
from commands.task_commands import task_commands
from commands.sub_task_commands import sub_task_commands
from commands.comment_commands import comment_commands

if __name__ == '__main__':
    commands = click.CommandCollection(sources=[
        project_commands,
        epic_commands,
        feature_commands,
        sprint_commands,
        task_commands,
        sub_task_commands,
        comment_commands
    ])
    commands()
    # CREATE PROJECT
    # LIST PROJECTS (show epics and features)
    # UPDATE PROJECT (change name)
    # DELETE PROJECT

    # CREATE EPIC
    # LIST EPIC (by project: show features and tasks)
    # UPDATE EPIC (change name, change project, change tags, add feature, remove feature)
    # DELETE Epic

    # CREATE FEATURE
    # LIST FEATURES (by project: show name, tasks)
    # UPDATE FEATURE (change name, change priority, change tags, add task, remove task, change tags)
    # DELETE FEATURE

    # CREATE SPRINT
    # UPDATE SPRINT (start, end, goal)
    # LIST SPRINTS (by project, tag optional: show name, goal, start, end, tasks and subtasks)
    # LIST SINGLE SPRINT (TASKS in KANBAN STYLE)
    # DELETE SPRINT

    # CREATE TASK
    # LIST TASK (by sprint or (tag and project): show name description, subtasks)
    # UPDATE TASK (
    #   change name, change description, change estimation, change sprint_sort, change sprint,
    #   change tags, add sub_task, add comment
    # )
    # DELETE TASK

    # UPDATE SUBTASK (change name, change description)
    # DELETE SUBTASK

    # UPDATE COMMENT (change description => only by creator)
    # DELETE COMMENT (=> only by creator)
    pass
