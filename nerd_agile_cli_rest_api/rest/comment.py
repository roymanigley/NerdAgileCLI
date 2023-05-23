from typing import List

from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI

from nerd_agile_cli_rest_api.rest.auth import AuthBearer
from nerd_agile_cli_rest_api.models import Comment
from nerd_agile_cli_rest_api.rest.helper import apply_autit_create_infos
from nerd_agile_cli_rest_api.schemas import CommentSchemaIn, CommentSchemaOut, CommentSchemaInPatch


def register(api: NinjaAPI) -> None:

    @api.get("comment", response={200: List[CommentSchemaOut]}, auth=AuthBearer())
    def get_comments(request: HttpRequest):
        return Comment.objects.all()

    @api.get("comment/{id}", response={200: CommentSchemaOut}, auth=AuthBearer())
    def get_comment_by_id(request: HttpRequest, id: int):
        return get_object_or_404(Comment, id=id)

    @api.post("comment", response={201: CommentSchemaOut}, auth=AuthBearer())
    def create_comment(request: HttpRequest, payload: CommentSchemaIn):
        payload_dict = apply_autit_create_infos(payload, request)
        comment = Comment.objects.create(**payload_dict)
        return comment

    @api.put("comment/{id}", response={200: CommentSchemaOut}, auth=AuthBearer())
    def update_comment(request: HttpRequest, id: int, payload: CommentSchemaIn):
        comment = get_object_or_404(Comment, id=id)
        for attr, value in payload.dict().items():
            setattr(comment, attr, value)
        comment.save()
        return comment

    @api.patch("comment/{id}", response={200: CommentSchemaOut}, auth=AuthBearer())
    def update_partial_comment(request: HttpRequest, id: int, payload: CommentSchemaInPatch):
        comment = get_object_or_404(Comment, id=id)
        for attr, value in payload.dict().items():
            if value is not None:
                setattr(comment, attr, value if value != 'null' else None)
        comment.save()
        return comment

    @api.delete("comment/{id}", response={203: None}, auth=AuthBearer())
    def delete_comment(request, id: int):
        comment = get_object_or_404(Comment, id=id)
        comment.delete()
        return 203
