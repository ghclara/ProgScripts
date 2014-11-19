# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from linguagem_app import facade
from routes.linguagems import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'linguagems/admin/form.html')


def save(_handler, linguagem_id=None, **linguagem_properties):
    cmd = facade.save_linguagem_cmd(**linguagem_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'linguagem': cmd.form}

        return TemplateResponse(context, 'linguagems/admin/form.html')
    _handler.redirect(router.to_path(admin))

