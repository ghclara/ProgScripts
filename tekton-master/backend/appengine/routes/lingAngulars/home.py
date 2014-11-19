# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from lingAngular_app import facade
from routes.lingAngulars import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_ling_angulars_cmd()
    ling_angulars = cmd()
    public_form = facade.ling_angular_public_form()
    ling_angular_public_dcts = [public_form.fill_with_model(ling_angular) for ling_angular in ling_angulars]
    context = {'ling_angulars': ling_angular_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

