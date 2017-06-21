# -*- coding: utf-8 -*-

from zope.interface import implements

from imio.urban.dataimport.urbaweb.importer import UrbawebDataImporter
from chatelet.urban.dataimport.interfaces import IChateletDataImporter


class ChateletDataImporter(UrbawebDataImporter):
    """ """

    implements(IChateletDataImporter)
