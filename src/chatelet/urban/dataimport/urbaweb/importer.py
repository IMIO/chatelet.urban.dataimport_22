# -*- coding: utf-8 -*-

from zope.interface import implements

from chatelet.urban.dataimport.urbaweb import valuesmapping
from chatelet.urban.dataimport.interfaces import IChateletDataImporter

from imio.urban.dataimport.mapping import ObjectsMapping, ValuesMapping
from imio.urban.dataimport.access.importer import AccessDataImporter

from chatelet.urban.dataimport.urbaweb import objectsmapping


class LicencesImporter(AccessDataImporter):
    """ """

    implements(IChateletDataImporter)

    def __init__(self, db_name='tab_urba_97.mdb', table_name='URBA', key_column='Cle_Urba', **kwargs):
        super(LicencesImporter, self).__init__(db_name, table_name, key_column, **kwargs)


class LicencesMapping(ObjectsMapping):
    """ """

    def getObjectsNesting(self):
        return objectsmapping.OBJECTS_NESTING

    def getFieldsMapping(self):
        return objectsmapping.FIELDS_MAPPINGS


class LicencesValuesMapping(ValuesMapping):
    """ """

    def getValueMapping(self, mapping_name):

        return valuesmapping.VALUES_MAPS.get(mapping_name, None)
