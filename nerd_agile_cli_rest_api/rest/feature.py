from typing import List

from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI

from nerd_agile_cli_rest_api.rest.auth import AuthBearer
from nerd_agile_cli_rest_api.models import Feature
from nerd_agile_cli_rest_api.rest.helper import apply_autit_create_infos
from nerd_agile_cli_rest_api.schemas import FeatureSchemaIn, FeatureSchemaOut, FeatureSchemaInPatch


def register(api: NinjaAPI) -> None:

    @api.get("feature", response={200: List[FeatureSchemaOut]}, auth=AuthBearer())
    def get_features(request: HttpRequest):
        return Feature.objects.all()

    @api.get("feature/{id}", response={200: FeatureSchemaOut}, auth=AuthBearer())
    def get_feature_by_id(request: HttpRequest, id: int):
        return get_object_or_404(Feature, id=id)

    @api.post("feature", response={201: FeatureSchemaOut}, auth=AuthBearer())
    def create_feature(request: HttpRequest, payload: FeatureSchemaIn):
        payload_dict = apply_autit_create_infos(payload, request)
        feature = Feature.objects.create(**payload_dict)
        return feature

    @api.put("feature/{id}", response={200: FeatureSchemaOut}, auth=AuthBearer())
    def update_feature(request: HttpRequest, id: int, payload: FeatureSchemaIn):
        feature = get_object_or_404(Feature, id=id)
        for attr, value in payload.dict().items():
            setattr(feature, attr, value)
        feature.save()
        return feature

    @api.patch("feature/{id}", response={200: FeatureSchemaOut}, auth=AuthBearer())
    def update_partial_feature(request: HttpRequest, id: int, payload: FeatureSchemaInPatch):
        feature = get_object_or_404(Feature, id=id)
        for attr, value in payload.dict().items():
            if value is not None:
                setattr(feature, attr, value if value != 'null' else None)
        feature.save()
        return feature

    @api.delete("feature/{id}", response={203: None}, auth=AuthBearer())
    def delete_feature(request, id: int):
        feature = get_object_or_404(Feature, id=id)
        feature.delete()
        return 203
