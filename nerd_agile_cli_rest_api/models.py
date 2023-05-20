from django.db import models


class Status(models.TextChoices):
    IN_PLANNING = ('IN_PLANNING', 'in planning')
    PLANNED = ('PLANNED', 'planned')
    IN_PROGRESS = ('IN_PROGRESS', 'in progress')
    BLOCKED = ('BLOCKED', 'blocked')
    CHECKING = ('CHECKING', 'checking')
    RESOLVED = ('RESOLVED', 'resolved')
    WONT_RESOLVE = ('WONT_RESOLVE', 'won\'t resolve')


class FeaturePriority(models.TextChoices):
    MUST = ('MUST', 'must')
    SHOULD = ('SHOULD', 'should')
    COULD = ('COULD', 'could')
    WONT = ('WONT', 'won\'t')


class TaskType(models.TextChoices):
    BUG = ('BUG', 'bug')
    STORY = ('STORY', 'story')
    DEVOPS = ('DEVOPS', 'DevOps')


class Project(models.Model):
    name = models.CharField(max_length=255, blank=False)
    creator = models.CharField(max_length=255, blank=False)
    create_date = models.DateTimeField(blank=False)


class Epic(models.Model):
    name = models.CharField(max_length=255, blank=False)
    tags = models.CharField(max_length=1024, blank=True)
    creator = models.CharField(max_length=255, blank=False)
    create_date = models.DateTimeField(blank=False)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING, blank=False)


class Feature(models.Model):
    name = models.CharField(max_length=255, blank=False)
    priority = models.CharField(blank=False, choices=FeaturePriority.choices)
    creator = models.CharField(max_length=255, blank=False)
    create_date = models.DateTimeField(blank=False)
    tags = models.CharField(max_length=1024, blank=True)
    epic = models.ForeignKey(Epic, on_delete=models.DO_NOTHING, blank=False)


class Sprint(models.Model):
    name = models.CharField(max_length=255, blank=False)
    goal = models.CharField(max_length=255, blank=True)
    start = models.DateField(blank=False)
    end = models.DateField(blank=False)
    creator = models.CharField(max_length=255, blank=False)
    create_date = models.DateTimeField(blank=False)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)


class Task(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=False)
    task_type = models.CharField(blank=False, default=TaskType.choices)
    task_status = models.CharField(blank=False, default=Status.IN_PLANNING, choices=Status.choices)
    tags = models.CharField(max_length=1024, blank=True)
    estimation = models.IntegerField(blank=True, default=9999)
    sprint_order = models.IntegerField(blank=True, default=9999)
    creator = models.CharField(max_length=255, blank=False)
    create_date = models.DateTimeField(blank=False)
    assignee = models.CharField(max_length=255, blank=True)
    sprint = models.ForeignKey(Sprint, on_delete=models.DO_NOTHING, blank=True)
    feature = models.ForeignKey(Feature, on_delete=models.DO_NOTHING, blank=True)


class SubTask(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=False)
    creator = models.CharField(max_length=255, blank=False)
    create_date = models.DateTimeField(blank=False)
    task = models.ForeignKey(Task, on_delete=models.DO_NOTHING, blank=False)


class Comment(models.Model):
    content = models.TextField(blank=False)
    creator = models.CharField(max_length=255, blank=False)
    create_date = models.DateTimeField(blank=False)
    task = models.ForeignKey(Task, on_delete=models.DO_NOTHING, blank=False)
