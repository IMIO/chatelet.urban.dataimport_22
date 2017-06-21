# -*- coding: utf-8 -*-

from imio.urban.dataimport.browser.controlpanel import ImporterControlPanel
from imio.urban.dataimport.browser.import_panel import ImporterSettings
from imio.urban.dataimport.browser.import_panel import ImporterSettingsForm
from imio.urban.dataimport.urbaweb.settings import UrbawebImporterFromImportSettings


class ChateletImporterSettingsForm(ImporterSettingsForm):
    """ """

class ChateletImporterSettings(ImporterSettings):
    """ """
    form = ChateletImporterSettingsForm


class ChateletImporterControlPanel(ImporterControlPanel):
    """ """
    import_form = ChateletImporterSettings


class ChateletImporterFromImportSettings(UrbawebImporterFromImportSettings):
    """ """

    def get_importer_settings(self):
        """
        Return the db name to read.
        """
        settings = super(ChateletImporterFromImportSettings, self).get_importer_settings()

        db_settings = {
            'db_name': '',
        }

        settings.update(db_settings)

        return settings
