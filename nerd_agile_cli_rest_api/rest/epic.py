from typing import List

from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI

from nerd_agile_cli_rest_api.rest.auth import AuthBearer
from nerd_agile_cli_rest_api.models import Epic
from nerd_agile_cli_rest_api.rest.helper import apply_autit_create_infos
from nerd_agile_cli_rest_api.schemas import EpicSchemaOut, EpicSchemaIn, EpicSchemaInPatch


def register(api: NinjaAPI) -> None:

    @api.get("epic", response={200: List[EpicSchemaOut]}, auth=AuthBearer())
    def get_epics(request: HttpRequest):
        return Epic.objects.all()

    @api.get("epic/{id}", response={200: EpicSchemaOut}, auth=AuthBearer())
    def get_epic_by_id(request: HttpRequest, id: int):
        return get_object_or_404(Epic, id=id)

    @api.post("epic", response={201: EpicSchemaOut}, auth=AuthBearer())
    def create_epic(request: HttpRequest, payload: EpicSchemaIn):
        payload_dict = apply_autit_create_infos(payload, request)
        epic = Epic.objects.create(**payload_dict)
        return epic

    @api.put("epic/{id}", response={200: EpicSchemaOut}, auth=AuthBearer())
    def update_epic(request: HttpRequest, id: int, payload: EpicSchemaIn):
        epic = get_object_or_404(Epic, id=id)
        for attr, value in payload.dict().items():
            setattr(epic, attr, value)
        epic.save()
        return epic

    @api.patch("epic/{id}", response={200: EpicSchemaOut}, auth=AuthBearer())
    def update_partial_epic(request: HttpRequest, id: int, payload: EpicSchemaInPatch):
        epic = get_object_or_404(Epic, id=id)
        for attr, value in payload.dict().items():
            if value is not None:
                setattr(epic, attr, value if value != 'null' else None)
        epic.save()
        return epic

    @api.delete("epic/{id}", response={203: None}, auth=AuthBearer())
    def delete_epic(request, id: int):
        epic = get_object_or_404(Epic, id=id)
        epic.delete()
        return 203
