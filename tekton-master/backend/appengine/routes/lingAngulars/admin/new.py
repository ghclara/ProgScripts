# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from lingAngular_app import facade
from routes.lingAngulars import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'lingAngulars/admin/form.html')


def save(_handler, ling_angular_id=None, **ling_angular_properties):
    cmd = facade.save_ling_angular_cmd(**ling_angular_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'ling_angular': cmd.form}

        return TemplateResponse(context, 'lingAngulars/admin/form.html')
    _handler.redirect(router.to_path(admin))

