# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from linguagem_app import facade
from routes.linguagems import admin
from routes.linguagems.admin import new, edit


@login_not_required
@no_csrf
def index():
    cmd = facade.list_linguagems_cmd()
    linguagems = cmd()
    public_form = facade.linguagem_public_form()
    linguagem_public_dcts = [public_form.fill_with_model(linguagem) for linguagem in linguagems]
    context = {'linguagems': linguagem_public_dcts,'admin_path':router.to_path(admin),'new_path': router.to_path(new)}
    return TemplateResponse(context)

