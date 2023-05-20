from typing import List

from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI

from nerd_agile_cli_rest_api.rest.auth import AuthBearer
from nerd_agile_cli_rest_api.models import Project
from nerd_agile_cli_rest_api.schemas import ProjectSchemaOut, ProjectSchemaIn
from nerd_agile_cli_rest_api.rest.helper import apply_autit_create_infos


def register(api: NinjaAPI) -> None:

    @api.get("project", response={200: List[ProjectSchemaOut]}, auth=AuthBearer())
    def get_projects(request: HttpRequest):
        return Project.objects.all()

    @api.get("project/{id}", response={200: ProjectSchemaOut}, auth=AuthBearer())
    def get_project_by_id(request: HttpRequest, id: int):
        return get_object_or_404(Project, id=id)

    @api.post("project", response={201: ProjectSchemaOut}, auth=AuthBearer())
    def create_project(request: HttpRequest, payload: ProjectSchemaIn):
        payload_dict = apply_autit_create_infos(payload, request)
        project = Project.objects.create(**payload_dict)
        return project

    @api.put("project/{id}", response={200: ProjectSchemaOut}, auth=AuthBearer())
    def update_project(request: HttpRequest, id: int, payload: ProjectSchemaIn):
        project = get_object_or_404(Project, id=id)
        for attr, value in payload.dict().items():
            if attr != "id":
                setattr(project, attr, value)
        project.save()
        return project

    @api.delete("project/{id}", response={203: None}, auth=AuthBearer())
    def delete_project(request, id: int):
        project = get_object_or_404(Project, id=id)
        project.delete()
        return 203

