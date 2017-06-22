# -*- coding: utf-8 -*-

from imio.urban.dataimport.urbaweb.settings import UrbawebImporterFromImportSettings


class LicencesImporterFromImportSettings(UrbawebImporterFromImportSettings):
    """ """

    def get_importer_settings(self):
        """
        Return the db name to read.
        """
        settings = super(LicencesImporterFromImportSettings, self).get_importer_settings()

        db_settings = {
            'db_name': 'tab_urba_97.mdb',
        }

        settings.update(db_settings)

        return settings
