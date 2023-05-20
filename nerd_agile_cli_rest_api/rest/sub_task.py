from typing import List

from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI

from nerd_agile_cli_rest_api.rest.auth import AuthBearer
from nerd_agile_cli_rest_api.models import SubTask
from nerd_agile_cli_rest_api.rest.helper import apply_autit_create_infos
from nerd_agile_cli_rest_api.schemas import SubTaskSchemaIn, SubTaskSchemaOut


def register(api: NinjaAPI) -> None:

    @api.get("sub_task", response={200: List[SubTaskSchemaOut]}, auth=AuthBearer())
    def get_sub_tasks(request: HttpRequest):
        return SubTask.objects.all()

    @api.get("sub_task/{id}", response={200: SubTaskSchemaOut}, auth=AuthBearer())
    def get_sub_task_by_id(request: HttpRequest, id: int):
        return get_object_or_404(SubTask, id=id)

    @api.post("sub_task", response={201: SubTaskSchemaOut}, auth=AuthBearer())
    def create_sub_task(request: HttpRequest, payload: SubTaskSchemaIn):
        payload_dict = apply_autit_create_infos(payload, request)
        sub_task = SubTask.objects.create(**payload_dict)
        return sub_task

    @api.put("sub_task/{id}", response={200: SubTaskSchemaOut}, auth=AuthBearer())
    def update_sub_task(request: HttpRequest, id: int, payload: SubTaskSchemaIn):
        sub_task = get_object_or_404(SubTask, id=id)
        for attr, value in payload.dict().items():
            if attr != "id":
                setattr(sub_task, attr, value)
        sub_task.save()
        return sub_task

    @api.delete("sub_task/{id}", response={203: None}, auth=AuthBearer())
    def delete_sub_task(request, id: int):
        sub_task = get_object_or_404(SubTask, id=id)
        sub_task.delete()
        return 203
