# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from plone.theme.interfaces import IDefaultPloneLayer
from imio.urban.dataimport.MySQL.interfaces import IMySQLImportSource

from imio.urban.dataimport.interfaces import IUrbanDataImporter


class IChateletUrbanDataimportLayer(IDefaultPloneLayer):
    """ Marker interface that defines a Zope 3 browser layer."""


class IChateletDataImporter(IUrbanDataImporter):
    """ Marker interface for IChatelet urbaweb importer """

class IChateletAcropoleImportSource(IMySQLImportSource):
    """ Marker interface for IChatelet agorawin importer """