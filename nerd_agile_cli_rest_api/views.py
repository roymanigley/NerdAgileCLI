from ninja import NinjaAPI

from nerd_agile_cli_rest_api.rest import \
    login as rest_login, \
    project as rest_project, \
    epic as rest_epic, \
    feature as rest_feature, \
    sprint as rest_sprint, \
    task as rest_task, \
    sub_task as rest_sub_task, \
    comment as rest_comment, \
    errors as rest_errors

api = NinjaAPI()

rest_login.register(api)
rest_project.register(api)
rest_epic.register(api)
rest_feature.register(api)
rest_sprint.register(api)
rest_task.register(api)
rest_sub_task.register(api)
rest_comment.register(api)
rest_errors.register(api)