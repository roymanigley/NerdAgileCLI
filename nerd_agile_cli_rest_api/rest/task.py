from typing import List

from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI

from nerd_agile_cli_rest_api.rest.auth import AuthBearer
from nerd_agile_cli_rest_api.models import Task
from nerd_agile_cli_rest_api.rest.helper import apply_autit_create_infos
from nerd_agile_cli_rest_api.schemas import TaskSchemaOut, TaskSchemaIn


def register(api: NinjaAPI) -> None:

    @api.get("task", response={200: List[TaskSchemaOut]}, auth=AuthBearer())
    def get_tasks(request: HttpRequest):
        return Task.objects.all()

    @api.get("task/{id}", response={200: TaskSchemaOut}, auth=AuthBearer())
    def get_task_by_id(request: HttpRequest, id: int):
        return get_object_or_404(Task, id=id)

    @api.post("task", response={201: TaskSchemaOut}, auth=AuthBearer())
    def create_task(request: HttpRequest, payload: TaskSchemaIn):
        payload_dict = apply_autit_create_infos(payload, request)
        task = Task.objects.create(**payload_dict)
        return task

    @api.put("task/{id}", response={200: TaskSchemaOut}, auth=AuthBearer())
    def update_task(request: HttpRequest, id: int, payload: TaskSchemaIn):
        task = get_object_or_404(Task, id=id)
        for attr, value in payload.dict().items():
            if attr != "id":
                setattr(task, attr, value)
        task.save()
        return task

    @api.delete("task/{id}", response={203: None}, auth=AuthBearer())
    def delete_task(request, id: int):
        task = get_object_or_404(Task, id=id)
        task.delete()
        return 203
