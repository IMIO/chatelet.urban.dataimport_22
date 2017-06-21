# -*- coding: utf-8 -*-

from zope.interface import implements

from chatelet.urban.dataimport.interfaces import IChateletDataImporter, IChateletAcropoleImportSource
from chatelet.urban.dataimport.acropole import valuesmapping

from imio.urban.dataimport.acropole.importer import AcropoleDataImporter, AcropoleImportSource
from imio.urban.dataimport.acropole.importer import AcropoleValuesMapping

from sqlalchemy import and_, or_


class LicencesImporter(AcropoleDataImporter):
    """ """

    implements(IChateletDataImporter)

    def __init__(self, db_name='chatelet_20160829', table_name='wrkdossier', key_column='WRKDOSSIER_ID', savepoint_length=0):
        super(AcropoleDataImporter, self).__init__(db_name, table_name, key_column, savepoint_length)


class LicencesImportSource(AcropoleImportSource):
    implements(IChateletAcropoleImportSource)

    def __init__(self, importer):
        super(LicencesImportSource, self).__init__(importer)

    def iterdata(self):
        # iterate on Chatelet database
        result = self.session.query(self.main_table)
        wrkdossier = self.importer.datasource.get_table('wrkdossier')

        folderIdToImport = [
            -67348, # EnvClassTwo Permis d’environnement classe 2
            -62737, # Permis d'urbanisation
            # -53925, permis unique, en cours d'implémentation
            -49306, # Article 127
            -46623, # EnvClassThree CL3 Déclaration environnementale de classe 3
            -42575, # Permis d'urbanisme
            -37624, # EnvClassTwo Permis d’environnement  classe 2
            # -36624, # Infractions, implémentation prévue dans le futur
            -34766, # TODO Lettre notariale (art 85) : fix applicant
            -15200, # Déclaration
            -14179, # Division
        ]

        # default:
        # Remove Urbaweb folders, infraction, 'permis unique'
        records = result.filter(and_(wrkdossier.columns['DOSSIER_TDOSSIERID'].in_(folderIdToImport), ~wrkdossier.columns['DOSSIER_NUMERO'].like('PU%'))).order_by(wrkdossier.columns['WRKDOSSIER_ID'].desc()).all()
        # records = result.filter(and_(wrkdossier.columns['DOSSIER_TDOSSIERID'].in_(folderIdToImport), wrkdossier.columns['DOSSIER_NUMERO'].like('HIST%'), ~wrkdossier.columns['DOSSIER_NUMERO'].like('PU%'))).order_by(wrkdossier.columns['WRKDOSSIER_ID'].desc()).all()
        # records = result.filter(and_(wrkdossier.columns['DOSSIER_TDOSSIERID'].in_(folderIdToImport), ~wrkdossier.columns['DOSSIER_NUMERO'].like('HIST%'), ~wrkdossier.columns['DOSSIER_NUMERO'].like('PU%'), or_(wrkdossier.columns['WRKDOSSIER_ID'] == 2249879, wrkdossier.columns['WRKDOSSIER_ID'] == 1757419, wrkdossier.columns['WRKDOSSIER_ID'] == 1746906))).order_by(wrkdossier.columns['WRKDOSSIER_ID'].desc()).slice(0,100).all()
        # records = result.filter(and_(wrkdossier.columns['DOSSIER_TDOSSIERID'].in_(folderIdToImport), ~wrkdossier.columns['DOSSIER_NUMERO'].like('HIST%'), ~wrkdossier.columns['DOSSIER_NUMERO'].like('PU%'))).order_by(wrkdossier.columns['WRKDOSSIER_ID'].desc()).slice(0,10).all()

        return records


class LicencesValuesMapping(AcropoleValuesMapping):
    """ """

    def getValueMapping(self, mapping_name):
        return valuesmapping.VALUES_MAPS.get(mapping_name)
