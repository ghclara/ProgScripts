# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from lingAngular_app.model import LingAngular

class LingAngularPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = LingAngular
    _include = [LingAngular.descricao]


class LingAngularForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = LingAngular
    _include = [LingAngular.descricao]


class LingAngularDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = LingAngular
    _include = [LingAngular.creation, 
                LingAngular.descricao]


class LingAngularShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = LingAngular
    _include = [LingAngular.creation, 
                LingAngular.descricao]


class SaveLingAngularCommand(SaveCommand):
    _model_form_class = LingAngularForm


class UpdateLingAngularCommand(UpdateNode):
    _model_form_class = LingAngularForm


class ListLingAngularCommand(ModelSearchCommand):
    def __init__(self):
        super(ListLingAngularCommand, self).__init__(LingAngular.query_by_creation())

