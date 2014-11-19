# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from linguagem_app.model import Linguagem

class LinguagemPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Linguagem
    _include = [Linguagem.descricao]


class LinguagemForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Linguagem
    _include = [Linguagem.descricao]


class LinguagemDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Linguagem
    _include = [Linguagem.creation, 
                Linguagem.descricao]


class LinguagemShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Linguagem
    _include = [Linguagem.creation, 
                Linguagem.descricao]


class SaveLinguagemCommand(SaveCommand):
    _model_form_class = LinguagemForm


class UpdateLinguagemCommand(UpdateNode):
    _model_form_class = LinguagemForm


class ListLinguagemCommand(ModelSearchCommand):
    def __init__(self):
        super(ListLinguagemCommand, self).__init__(Linguagem.query_by_creation())

