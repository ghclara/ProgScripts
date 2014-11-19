# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from lingAngular_app import facade
from routes.lingAngulars.admin import new, edit


def delete(_handler, ling_angular_id):
    facade.delete_ling_angular_cmd(ling_angular_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_ling_angulars_cmd()
    ling_angulars = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.ling_angular_short_form()

    def short_ling_angular_dict(ling_angular):
        ling_angular_dct = short_form.fill_with_model(ling_angular)
        ling_angular_dct['edit_path'] = router.to_path(edit_path, ling_angular_dct['id'])
        ling_angular_dct['delete_path'] = router.to_path(delete_path, ling_angular_dct['id'])
        return ling_angular_dct

    short_ling_angulars = [short_ling_angular_dict(ling_angular) for ling_angular in ling_angulars]
    context = {'ling_angulars': short_ling_angulars,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

