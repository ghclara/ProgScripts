# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaeforms.ndb.form import ModelForm
from gaegraph.model import Node
from linguagem_app.model import Linguagem
from tekton import router
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index():
    query = Codigo.query(Codigo.ativo==1).order(Codigo.problema)
    codigo_lista = query.fetch()
    form_codigo = CodigoForm()
    codigo_lista = [form_codigo.fill_with_model(codigo) for codigo in codigo_lista]
    edit_path = router.to_path(editar_form)
    delete_path = router.to_path(delete)
    for cod in codigo_lista:
        cod['edit_path'] = '%s/%s'%(edit_path, cod['id'])
        cod['delete_path'] = '%s/%s'%(delete_path, cod['id'])



    contexto = {'codigos': codigo_lista,
                'form_path': router.to_path(form)}
    return TemplateResponse(contexto)

@no_csrf
def form():
    query = Linguagem.query().order(Linguagem.descricao)
    query.fetch()
    contexto = {'salvar_path': router.to_path(salvar),
                'linguagens': query}
    return TemplateResponse(contexto, 'codigo/form.html')

def delete(codigo_id):
    codigo_id = int(codigo_id)
    codigo = Codigo.get_by_id(codigo_id)
    codigo.ativo = 0
    codigo.put()
    return RedirectResponse(router.to_path(index))


@no_csrf
def editar_form(codigo_id):
    query = Linguagem.query().order(Linguagem.descricao)
    query.fetch()

    codigo_id = int(codigo_id)
    codigo = Codigo.get_by_id(codigo_id)
    codigo_form = CodigoForm()
    codigo_form.fill_with_model(codigo)
    contexto = {'salvar_path': router.to_path(editar, codigo_id),
                'codigo': codigo_form,
                'linguagens': query}
    return TemplateResponse(contexto, 'codigo/form.html')

def editar(codigo_id ,**propriedades):
    codigo_id = int(codigo_id)
    codigo = Codigo.get_by_id(codigo_id)

    codigo_form = CodigoForm(**propriedades)
    erros = codigo_form.validate()

    if erros:
        contexto = {'salvar_path': router.to_path(salvar),
                    'erros': erros,
                    'codigo': codigo_form,
                    'linguagens': propriedades['linguagens']}
        return TemplateResponse(contexto, 'codigo/form.html')

    codigo_form.fill_model(codigo)
    codigo.put()
    return RedirectResponse(router.to_path(index))

class Codigo(Node):
    linguagem = ndb.StringProperty(required=True)
    problema = ndb.StringProperty(required=True)
    codigo = ndb.StringProperty(required=True)
    ativo = ndb.IntegerProperty(default=1)

class CodigoForm(ModelForm):
    _model_class = Codigo
    _include = (Codigo.problema, Codigo.codigo, Codigo.linguagem)

class CodigoFormTable(ModelForm):
    _model_class = Codigo
    _include = (Codigo.problema, Codigo.codigo, Codigo.ativo, Codigo.creation)


def salvar(**propriedades):
    codigo_form = CodigoForm(**propriedades)
    erros = codigo_form.validate()

    if erros:
        contexto = {'salvar_path': router.to_path(salvar),
                    'erros': erros,
                    'codigo': codigo_form}
        return TemplateResponse(contexto, 'codigo/form.html')

    codigo = codigo_form.fill_model()
    codigo.put()
    return RedirectResponse(router.to_path(index))