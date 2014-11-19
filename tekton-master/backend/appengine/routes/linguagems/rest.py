# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.json_middleware import JsonUnsecureResponse
from linguagem_app import facade

@login_not_required
@no_csrf
def index():
    cmd = facade.list_linguagems_cmd()
    linguagem_list = cmd()
    short_form=facade.linguagem_short_form()
    linguagem_short = [short_form.fill_with_model(m) for m in linguagem_list]
    return JsonUnsecureResponse(linguagem_short)

@login_not_required
@no_csrf
def save(_resp,**linguagem_properties):
    cmd = facade.save_linguagem_cmd(**linguagem_properties)
    return _save_or_update_json_response(_resp, cmd)

@login_not_required
@no_csrf
def update(_resp, linguagem_id, **linguagem_properties):
    cmd = facade.update_linguagem_cmd(linguagem_id, **linguagem_properties)
    return _save_or_update_json_response(_resp, cmd)


@login_not_required
@no_csrf
def delete(linguagem_id):
    facade.delete_linguagem_cmd(linguagem_id)()

@login_not_required
@no_csrf
def _save_or_update_json_response(_resp, cmd):
    try:
        linguagem = cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonUnsecureResponse(cmd.errors)
        #return JsonUnsecureResponse({'errors': cmd.errors})
    short_form=facade.linguagem_short_form()
    return JsonUnsecureResponse(short_form.fill_with_model(linguagem))

