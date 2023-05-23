from typing import List

from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI

from nerd_agile_cli_rest_api.rest.auth import AuthBearer
from nerd_agile_cli_rest_api.models import Sprint, Task
from nerd_agile_cli_rest_api.schemas import SprintSchemaOut, SprintSchemaIn, SprintSchemaInPatch, \
    SprintSchemaOutWithTask
from nerd_agile_cli_rest_api.rest.helper import apply_autit_create_infos


def register(api: NinjaAPI) -> None:
    @api.get("sprint", response={200: List[SprintSchemaOut]}, auth=AuthBearer())
    def get_sprints(request: HttpRequest):
        return Sprint.objects.all()

    @api.get("sprint/{id}", response={200: SprintSchemaOutWithTask}, auth=AuthBearer())
    def get_sprint_by_id(request: HttpRequest, id: int):
        sprint = get_object_or_404(Sprint, id=id)
        tasks = Task.objects.filter(sprint_id=id).all()
        return {"sprint": sprint, "tasks": list(tasks)}

    @api.post("sprint", response={201: SprintSchemaOut}, auth=AuthBearer())
    def create_sprint(request: HttpRequest, payload: SprintSchemaIn):
        payload_dict = apply_autit_create_infos(payload, request)
        sprint = Sprint.objects.create(**payload_dict)
        return sprint

    @api.put("sprint/{id}", response={200: SprintSchemaOut}, auth=AuthBearer())
    def update_sprint(request: HttpRequest, id: int, payload: SprintSchemaIn):
        sprint = get_object_or_404(Sprint, id=id)
        for attr, value in payload.dict().items():
            setattr(sprint, attr, value)
        sprint.save()
        return sprint

    @api.patch("sprint/{id}", response={200: SprintSchemaOut}, auth=AuthBearer())
    def update_partial_sprint(request: HttpRequest, id: int, payload: SprintSchemaInPatch):
        sprint = get_object_or_404(Sprint, id=id)
        for attr, value in payload.dict().items():
            if value is not None:
                setattr(sprint, attr, value if value != 'null' else None)
        sprint.save()
        return sprint

    @api.delete("sprint/{id}", response={203: None}, auth=AuthBearer())
    def delete_sprint(request, id: int):
        sprint = get_object_or_404(Sprint, id=id)
        sprint.delete()
        return 203
