# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from linguagem_app import facade
from routes.linguagems import admin


@no_csrf
def index(linguagem_id):
    linguagem = facade.get_linguagem_cmd(linguagem_id)()
    detail_form = facade.linguagem_detail_form()
    context = {'save_path': router.to_path(save, linguagem_id), 'linguagem': detail_form.fill_with_model(linguagem)}
    return TemplateResponse(context, 'linguagems/admin/form.html')


def save(_handler, linguagem_id, **linguagem_properties):
    cmd = facade.update_linguagem_cmd(linguagem_id, **linguagem_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'linguagem': cmd.form}

        return TemplateResponse(context, 'linguagems/admin/form.html')
    _handler.redirect(router.to_path(admin))

