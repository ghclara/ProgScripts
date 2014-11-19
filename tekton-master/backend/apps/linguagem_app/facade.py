# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from linguagem_app.commands import ListLinguagemCommand, SaveLinguagemCommand, UpdateLinguagemCommand, \
    LinguagemPublicForm, LinguagemDetailForm, LinguagemShortForm


def save_linguagem_cmd(**linguagem_properties):
    """
    Command to save Linguagem entity
    :param linguagem_properties: a dict of properties to save on model
    :return: a Command that save Linguagem, validating and localizing properties received as strings
    """
    return SaveLinguagemCommand(**linguagem_properties)


def update_linguagem_cmd(linguagem_id, **linguagem_properties):
    """
    Command to update Linguagem entity with id equals 'linguagem_id'
    :param linguagem_properties: a dict of properties to update model
    :return: a Command that update Linguagem, validating and localizing properties received as strings
    """
    return UpdateLinguagemCommand(linguagem_id, **linguagem_properties)


def list_linguagems_cmd():
    """
    Command to list Linguagem entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListLinguagemCommand()


def linguagem_detail_form(**kwargs):
    """
    Function to get Linguagem's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return LinguagemDetailForm(**kwargs)


def linguagem_short_form(**kwargs):
    """
    Function to get Linguagem's short form. just a subset of linguagem's properties
    :param kwargs: form properties
    :return: Form
    """
    return LinguagemShortForm(**kwargs)

def linguagem_public_form(**kwargs):
    """
    Function to get Linguagem'spublic form. just a subset of linguagem's properties
    :param kwargs: form properties
    :return: Form
    """
    return LinguagemPublicForm(**kwargs)


def get_linguagem_cmd(linguagem_id):
    """
    Find linguagem by her id
    :param linguagem_id: the linguagem id
    :return: Command
    """
    return NodeSearch(linguagem_id)


def delete_linguagem_cmd(linguagem_id):
    """
    Construct a command to delete a Linguagem
    :param linguagem_id: linguagem's id
    :return: Command
    """
    return DeleteNode(linguagem_id)

