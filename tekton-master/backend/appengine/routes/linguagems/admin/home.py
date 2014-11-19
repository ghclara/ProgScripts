# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from linguagem_app import facade
from routes.linguagems.admin import new, edit


def delete(_handler, linguagem_id):
    facade.delete_linguagem_cmd(linguagem_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    context = {'new_path': router.to_path(new)}
    return TemplateResponse(context)

    # cmd = facade.list_linguagems_cmd()
    # linguagems = cmd()
    # edit_path = router.to_path(edit)
    # delete_path = router.to_path(delete)
    # short_form = facade.linguagem_short_form()
    #
    # def short_linguagem_dict(linguagem):
    #     linguagem_dct = short_form.fill_with_model(linguagem)
    #     linguagem_dct['edit_path'] = router.to_path(edit_path, linguagem_dct['id'])
    #     linguagem_dct['delete_path'] = router.to_path(delete_path, linguagem_dct['id'])
    #     return linguagem_dct
    #
    # short_linguagems = [short_linguagem_dict(linguagem) for linguagem in linguagems]
    # context = {'linguagems': short_linguagems,
    #            'new_path': router.to_path(new)}
    # return TemplateResponse(context)

