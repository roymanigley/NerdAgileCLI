from django.contrib import admin
from nerd_agile_cli_rest_api.models import Sprint, Project, Epic, Feature, Task, SubTask, Comment

admin.site.register(Project)
admin.site.register(Epic)
admin.site.register(Feature)
admin.site.register(Sprint)
admin.site.register(Task)
admin.site.register(SubTask)
admin.site.register(Comment)
