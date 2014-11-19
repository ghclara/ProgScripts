# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from lingAngular_app import facade


def index():
    cmd = facade.list_ling_angulars_cmd()
    ling_angular_list = cmd()
    short_form=facade.ling_angular_short_form()
    ling_angular_short = [short_form.fill_with_model(m) for m in ling_angular_list]
    return JsonResponse(ling_angular_short)


def save(**ling_angular_properties):
    cmd = facade.save_ling_angular_cmd(**ling_angular_properties)
    return _save_or_update_json_response(cmd)


def update(ling_angular_id, **ling_angular_properties):
    cmd = facade.update_ling_angular_cmd(ling_angular_id, **ling_angular_properties)
    return _save_or_update_json_response(cmd)


def delete(ling_angular_id):
    facade.delete_ling_angular_cmd(ling_angular_id)()


def _save_or_update_json_response(cmd):
    try:
        ling_angular = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.ling_angular_short_form()
    return JsonResponse(short_form.fill_with_model(ling_angular))

