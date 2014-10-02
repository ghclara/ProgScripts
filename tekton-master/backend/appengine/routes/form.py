# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required, permissions, login_required
from permission_app.model import ADMIN, USUARIO
from tekton import router



@login_not_required
@no_csrf
def index():
    contexto = {'save_path': router.to_path(salvar)}
    return TemplateResponse(contexto);

@permissions(USUARIO)
@no_csrf
def salvar(_resp,nome):
    _resp.write(nome)

@login_required
@no_csrf
def usuario(_resp, _logged_user):
    _resp.write('Usuario logado %s' %(_logged_user))
