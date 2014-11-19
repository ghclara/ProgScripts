# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from lingAngular_app.commands import ListLingAngularCommand, SaveLingAngularCommand, UpdateLingAngularCommand, \
    LingAngularPublicForm, LingAngularDetailForm, LingAngularShortForm


def save_ling_angular_cmd(**ling_angular_properties):
    """
    Command to save LingAngular entity
    :param ling_angular_properties: a dict of properties to save on model
    :return: a Command that save LingAngular, validating and localizing properties received as strings
    """
    return SaveLingAngularCommand(**ling_angular_properties)


def update_ling_angular_cmd(ling_angular_id, **ling_angular_properties):
    """
    Command to update LingAngular entity with id equals 'ling_angular_id'
    :param ling_angular_properties: a dict of properties to update model
    :return: a Command that update LingAngular, validating and localizing properties received as strings
    """
    return UpdateLingAngularCommand(ling_angular_id, **ling_angular_properties)


def list_ling_angulars_cmd():
    """
    Command to list LingAngular entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListLingAngularCommand()


def ling_angular_detail_form(**kwargs):
    """
    Function to get LingAngular's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return LingAngularDetailForm(**kwargs)


def ling_angular_short_form(**kwargs):
    """
    Function to get LingAngular's short form. just a subset of ling_angular's properties
    :param kwargs: form properties
    :return: Form
    """
    return LingAngularShortForm(**kwargs)

def ling_angular_public_form(**kwargs):
    """
    Function to get LingAngular'spublic form. just a subset of ling_angular's properties
    :param kwargs: form properties
    :return: Form
    """
    return LingAngularPublicForm(**kwargs)


def get_ling_angular_cmd(ling_angular_id):
    """
    Find ling_angular by her id
    :param ling_angular_id: the ling_angular id
    :return: Command
    """
    return NodeSearch(ling_angular_id)


def delete_ling_angular_cmd(ling_angular_id):
    """
    Construct a command to delete a LingAngular
    :param ling_angular_id: ling_angular's id
    :return: Command
    """
    return DeleteNode(ling_angular_id)

