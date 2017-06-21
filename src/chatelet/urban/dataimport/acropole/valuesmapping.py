# -*- coding: utf-8 -*-

from imio.urban.dataimport.mapping import table

VALUES_MAPS = {
    'type_map': table({
        'header': ['portal_type', 'foldercategory'],
        -67348: ['EnvClassTwo', ''],  # Permis d’environnement classe 2
        -62737: ['ParcelOutLicence', 'lap'],
        -53925: ['', ''],  # Permis unique, ne pas reprendre pour l'instant
        -49306: ['Article127', ''],
        -46623: ['EnvClassThree', ''],  # permis d'environnement classe 3
        -42575: ['BuildLicence', 'uap'],
        -37624: ['EnvClassTwo', ''],  # permis d'environnement classe 2
        -36624: ['', 'infraction'],  # infractions, implémentation prévue dans le futur
        -34766: ['NotaryLetter', ''],  # lettre de notaire (art 85)
        -15200: ['Declaration', ''],
        -14179: ['Division', ''],
    }),

    # pour la reférence, virer le 'RA' ou 'RG'
    # pour la référence, reprendre la colonne DOSSIER_REFCOM

    # Main dictionaries

    # octroi/refus
    'state_map': {
        -58L: 'refuse',  # irrecevable (validé par chatelet)
        -49L: 'accept',  # -49 = octroyé
        -46L: 'refuse',  # -46 = annulé par le FD
        -30L: 'accept',  # recevable (validé par chatelet)
        -27L: 'accept',  # recevable avec condition (validé par chatelet)
        -26L: 'accept',  # -26 = octroyé
        -20L: 'refuse',  # refus, ministre sur recours (validé par chatelet)
        -19L: 'retire',  # -19 = périmé
        -17L: 'refuse',  # refus (FT) (validé par chatelet)
        -15L: 'accept',  # accepté (FT) (validé par chatelet)
        -14L: 'accept',  # -14 = octroyé
        -12L: 'accept',  # -12 = octroyé (validé par Fl)
        -11L: 'retire',  # -11 = retiré
        -10L: 'retire',  # -10 = retiré (validé par Fl)
        -8L: 'refuse',   # irrecevable (validé par chatelet)
        -7L: 'accept',   # recevable (validé par chatelet)
        -6L: 'accept',  # -6 = octroyé (validé par Fl)
        -5L: 'refuse',  # -5 = refusé
        -4L: 'retire',  # -4 = suspendu
        -3L: 'accept',  # -3 = octroyé
        -2L: 'retire',  # -2 = abandonné
        -1L: '',  # -1 = en cours
        0L: 'refuse',  # -1 = refusé
        1L: 'accept',  # 1 = octroyé
    },

    'division_map': {
        '01': '52012',
        '02': '52013',
        '03': '52502',
        '04': '52007',
    },

    'eventtype_id_map': table({
        'header': ['decision_event', 'folder_complete', 'deposit_event', 'send_licence_applicant_event', 'send_licence_fd_event', 'first_folder_transmitted_to_rw_event'],
        'BuildLicence': ['delivrance-du-permis-octroi-ou-refus', 'accuse-de-reception', 'depot-de-la-demande', 'envoi-du-permis-au-demandeur', 'envoi-du-permis-au-fd', 'transmis-1er-dossier-rw'],
        'ParcelOutLicence': ['delivrance-du-permis-octroi-ou-refus', 'accuse-de-reception', 'depot-de-la-demande', 'envoi-du-permis-au-demandeur', 'envoi-du-permis-au-fd', 'transmis-1er-dossier-rw'],
        'Declaration': ['deliberation-college', '', 'depot-de-la-demande', '', '', ''],
        'Division': ['decision-octroi-refus', '', 'depot-de-la-demande', '', '', ''],
        'MiscDemand': ['deliberation-college', '', 'depot-de-la-demande', '', '', ''],
        'UrbanCertificateOne': ['octroi-cu1', '', 'depot-de-la-demande', '', '', ''],
        'UrbanCertificateTwo': ['octroi-cu2', '', 'depot-de-la-demande', '', '', ''],
        'NotaryLetter': ['octroi-lettre-notaire', '', 'depot-de-la-demande', '', '', ''],
        'Article127': ['delivrance-du-permis-octroi-ou-refus', '', 'depot-de-la-demande', '', '', ''],
        'EnvClassTwo': ['decision', '', 'depot-de-la-demande', '', '', ''],
        'EnvClassThree': ['acceptation-de-la-demande', '', 'depot-de-la-demande', '', '', ''],
    }),

    'titre_map': {
        -1000: 'mister',
        21607: 'misters',
        -1001: 'madam',
        171280: 'ladies',
        -1002: 'miss',
        -1003: 'madam_and_mister',
        676263: 'madam_and_mister',
        850199: 'madam_and_mister',
        89801: 'master',
    },

    # event name map dictionaries
    'event_deposit_name_map': {
        'BuildLicence': [u'récépissé'],
        'ParcelOutLicence': [u'récépissé', u'introduction de la demande'],
        'Article127': [u'Début du dossier', u'dépôt dossier', u'réception de la demande du FD', u'dossier complet'],  # dossier complet asked by Florennes
        'NotaryLetter': [u'Réception demande'],
        'UrbanCertificateOne': [u'réception demande'],
        'UrbanCertificateTwo': [u'réception demande'],
        'Declaration': [u'dépôt ou envoi de la déclaration'],
        'Division': [u'récépissé', u"réception avis de division du notaire"],
        'MiscDemand': [u'Accusé de réception', u'réception demande'],
        'EnvClassTwo': [u'accusé de réception', u'réception demande', u'récépissé'],
        'EnvClassThree': [u'Accusé de réception', u'réception demande', u'récépissé'],
    },

    'event_decision_date_map': {
        'BuildLicence': [u'délivrance permis'],
        'ParcelOutLicence': [u'délivrance permis', u"délivrance permis d'urbanisation", u"délivrance modification permis d'urbanisation"],
        'Article127': [u'délivrance du permis par le FD ou le Gvt wallon', u'Délivrance permis'],
        'NotaryLetter': '',
        'UrbanCertificateOne': [u'CU1'],
        'UrbanCertificateTwo': [u'CU2'],
        'Declaration': [u'délivrance permis', u"rapport collège"],
        'Division': [u'délivrance permis'],
        'MiscDemand': [u'Délivrance autorisation'],
        'EnvClassTwo': [u'délivrance permis', u"Date délivrance permis"],
        'EnvClassThree': [u'Date déclaration recevable'],
    },

    'event_decision_map': {
        'BuildLicence': [u'Octroi du permis'],
        'ParcelOutLicence': [u'Octroi du permis', u"octroi modif Purb"],
        'Article127': [u'Octroi du permis', u'OctroiPermis',  u'octroi permis'],
        'NotaryLetter': '',
        'UrbanCertificateOne': [u'CU1'],
        'UrbanCertificateTwo': [u'CU2'],
        'Declaration': [u'délivrance permis', u"dossier recevable ?"],
        'Division': [u'délivrance permis'],
        'MiscDemand': [u'Délivrance autorisation'],
        'EnvClassTwo': [u'octroi du permis', u"dossier recevable ?", u"dossier recevable"],
        'EnvClassThree': [u'date de décision exécutoire'],
    },

    'event_college_report_date_map': {
        'BuildLicence': [u'rapport Collège avant décision du FD'],
        'Article127': [u'rapport Collège'],
        'Declaration': [u'rapport collège'],
        'MiscDemand': [u'rapport collège', u'Décision du Collège'],  # Demande de principe, others
    },

    'event_envclass_ok_date_map': {
        'EnvClassThree': [u'Déclaration recevable'],
    },

    'event_envclass_ko_date_map': {
        'EnvClassThree': [u'Déclaration irrecevable'],
    },

    'event_envclass_ok_cond_date_map': {
            'EnvClassThree': [u'Déc. recevable avec cond. compl.'],
        },

    'declaration_record': {'dossier recevable ?', 'dossier recevable',},

    # Misc. dictionaries

    'solicitOpinionDictionary': {
        u"stp_eau": "stp",
        u"stp": "stp",
        u"stp_voirie": "stp",
        u"base aérienne": "ba",
        u"ddr": "ddr",
        u"sri": "sri",
        u"direction des routes": "spw-dgo1",
        u"x4": "x4",
        u"défense": "defense",
        u"fluxys": "fluxys",
        u"asbl bois du roi": "asblbdr",
        u"cwedd": "cwedd",  # Conseil wallon de l'Environnement pour le Développement durable
        u"elia": "elia",
        u"police": "Police",
        u"tec": "tec",
        u"égouts": "egouts",
        u"ores": "ores",
        u"inasep": "inasep",
        u"dnf": "dnf",
        u"sncb": "sncb",
        u"ccatm": "ccatm",
        u"dgrne": "dgrne",
        u"belgacom": "belgacom",
        u"autres": "autres",

        # u"Administration des mines" : "",
        # u"Belgacom" : "",
        # u"Brutele" : "",
        # u"CCATM" : "",
        # u"Cellule Ram" : "",
        # u"Commissaire voyer" : "",
        # u"Conseiller en mobilité" : "",
        # u"Conseiller en énergie" : "",
        # u"DGO01" : "",
        # u"DGRNE division de l'eau" : "",
        # u"DGRNE office wallon des déchets" : "",
        # u"Direction des routes de Charleroi" : "",
        # u"division de la police d'environnement" : "",
        # u"DNF" : "",
        # u"Logis châtelettain" : "",
        # u"Ministère de l'Agriculture" : "",
        # u"ORES" : "",
        # u"Service d'intervention incendie" : "",
        # u"service environnement" : "",
        # u"Service travaux" : "",
        # u"SNCB" : "",
        # u"SPW service patrimoine" : "",
        # u"SWDE" : "",
        # u"TEC" : "",
        # u"zone de police" : "",
    },

    'zoneDictionary': {
        # déjà présentes
        u"zone d'habitat": "zh",
        u"zone d'habitat à caractère rural": "zhrc",
        u"zone d’habitat à caractère rural sur +/- 50 m et le surplus en zone agricole": "zhrcza",
        u"zone de services publics et d'équipements communautaires": "zspec",
        u"zone de centre d'enfouissement technique": "zcet",
        u"zone de loisirs": "zl",
        u"zones d'activité économique mixte": "zaem",
        u"zones d'activité économique industrielle": "zaei",
        u"zones d'activité économique spécifique agro-économique": "zaesae",
        u"zones d'activité économique spécifique grande distribution": "zaesgd",
        u"zone d'extraction": "ze",
        u"zone d'aménagement différé à caractère industriel": "zadci",
        u"zone agricole": "za",
        u"zone forestière": "zf",
        u"zone d'espaces verts": "zef",
        u"zone naturelle": "zn",
        u"zone de parc": "zp",
        u"zone Natura 2000": "znatura2000",

        u"Zone d'habitat": "zh",
        u"fonction centrale (2)": "fc",
        u"zone urbaine centrale": "zuc",
        u"zone d'habitat de forte densité": "zhfd",
        u"aire à fonction centrale (2)": "afc",
        u"zone d'habitat de densité moyenne à faible": "zhdmf",
        u"aire de bâtisses semi-agglomérées (4)": "absa",
        u"centre ancien de Châtelet (1A)": "cadc",
        u"Zone d'espaces verts": "zev",
        u"aire d'espaces verts et forestière (8)": "zevf",
        u"zone d'intérêt paysager": "zipa",
        u"aire de bâtisses agglomérées (3)": "aba",
        u"Zone de services publics et d'équipements communautaires": "zspec",
        u"aire de grandes bâtisses en milieu isolé non accessibles au public (6B)": "agbminap",
        u"zone d'équipements communautaires et de services publics": "zecsp",
        u"aire de bâtisses pavillonnaires (5)": "abp",
        u"aire rurale de périphérie (7)": "ardp",
        u"Zone agricole": "za",
        u"zone rurale": "zr",
        u"zone d'application automatique de l'article 186 du CWATUPE": "zaaa186",
        u"aire de bâtisses semi-agglomérées avec un périmètre de bâtisses répétitives": "absapbr",
        u"aire d'espaces verts et forestière avec un périmètre de protection particulière": "aevfppp",
        u"zone d'espace vert": "zef",
        u"zone de constructions résidentielles en ordre continu": "zdcroc",
        u"zone de commerce de détail facultatif": "zdcddf",
        u"zone de construction en ordre contigü (hauteur sous corniche 7m max)": "zdcoc",
        u"aire de bâtisses agglomérées avec un périmètre de bâtisses répétitives": "adbaapdbr",
        u"Zone d'activité économique industrielle": "zaei",
        u"zone industrielle": "zi",
        u"grandes bâtisses en milieu isolé non accessibles au public + périmètre protection particulière": "gbeminapppp",
        u"zone de recul": "zdr",
        u"zone d'activité économique de type mixte (artisanat et PME)": "zaetm",
        u"zone de dépôt et de développement artisanal et de PME": "zdddapme",
        u"aire de grandes bâtisses en milieu isolé accessibles au public (6A)": "adgbmiap",
        u"Zone de loisirs": "zdl",
        u"Zone d'aménagement communal concerté": "zacc",
        u"zone de voirie publique": "zdvp",
        u"zone de construction en ordre contigü (hauteur max 24 m)": "zdcoc24",
        u"zone de constructions résidentielles secondaires": "zdcrs",
        u"zone de cours et jardins": "zdcj",
        u"Zone forestière": "zf",
        u"centre ancien de Bouffioulx (1B)": "cadbouf",
        u"aire rurale de périphérie avec un périmètre de protection particulière": "arpappp",
        u"Zone d'ext. d'habitat à caractère rural": "zehacr",
        u"zone d'extension d'habitat": "zeh",
        u"zone de constructions résidentielles": "zdcr",
        u"Zone d'activité économique mixte": "zaem",
        u"zone d'implantation d'entreprises de services, à proportion importante d'espaces verts, ceinturant d": "",
        u"zone d'accès privé à la voirie": "zapv",
        u"aire de bâtisses semi-agglomérées avec un périmètre de valorisation naturelle": "absapvn",
        u"zone à rénover": "zar",
        u"zone de réservation": "zdres",
        u"zone de construction en ordre contigü (hauteur sous corniche entre 10m et 13m)": "zdcoc1013",
        u"zone de construction en ordre contigü (hauteur sous corniche de 10m max)": "zdcoc10max",
        u"Zone d'aménagement différé à caractère industriel": "zadci",
        u"aire d'espaces verts et forestière avec périmètre de valorisation naturelle et protection paysagère": "aevfapvnp",
        u"zone d'assainissement collectif": "zac",
        u"Zone d'activité économique spécifique - Agro-économique": "zaesae",
        u"zone d’activité économique mixte": "zaem",
        u"Identique au Plan de secteur": "ipds",
        u"aire rurale de périphérie avec un périmètre de valorisation naturelle": "arppvn",
        u"zone mixte habitat, commerce et service": "zmhces",
        u"zone de constructions commerciales et de services secondaires": "zdccss",
        u"zone d'isolement (ou de protection, tampon)": "ziso",
        u"zone de parcage arborée": "zpa",
        u"zone pévue pour une piscine": "zpp",
        u"zone d'immeubles commerciaux suivant prescriptions spéciales": "zicsps",
        u"zone d'aménagement différé": "zad",
        u"zone de commerce de détail obligatoire": "zdcddo",
        u"aire d'espaces verts et forestière avec un périmètre de valorisation naturelle": "aevfpvn",
        u"aire de bâtisses semi-agglomérées avec un périmètre de grandes bâtisses en milieu intégré": "adbsaapgbmi",
        u"aire de bâtisses agglomérées avec un périmètre de grandes bâtisses en milieu intégré": "adbaapdgbmi",
        u"Périmètre de réservation": "pdr",
        u"Zone de non aedificandi": "zdnaedi",
        u"zone de constructions publique ou à destination publique": "zdcpodp",
        u"Aire de grande batisse en milieu isolé accessible au public": "adgbmiaap",
        u"Zone d'implantation d'immeuble commerciaux": "ziic",
        u"périmètre de protection particulière": "ppp",
        u"zone de constructions résidentielles en ordre ouvert": "zdcreoo",
        u"Périmètre d'intérêt paysager": "pip",
        u"Aire de grandes bâtisses en milieu intégré": "adgbmi",
        u"Zone réservée à l'implantation de logements à caractère social": "zridlacs",
        u"Zone naturelle d'intérêts scientifiques ou réserve naturelle": "znisorn",
        u"zone d'annexes artisanales ou commerciales": "zaaoc",
        u"zone de blocs de constructions (hauteur sous corniche 23m max)": "zdbc23max",
        u"zone publique (trottoir)": "zpt",
        u"zone de construction en hauteur": "zdceh",
        u"zone de parking": "zdp",
        u"zone d'activité économique": "zae",
        u"zone de captage": "zdc",
        u"zone commerciale avec bureaux ou appartements aux étages": "zcabaae",
        u"zone de construction en annexe": "zdcea",
        u"zone de parc privé (voirie autorisée)": "zdppva",
    },

    'pcaZoneDictionary' : {
        # déjà présentes
        u"Zone de construction d'habitation fermée": "zone-de-construction-d-habitation-fermee",
        u"Zone de construction d'habitation semi ouverte": "zone-de-construction-d-habitation-semi-ouverte",
        u"Zone de construction d'habitation ouverte": "zone-de-construction-d-habitation-ouverte",
        u"Zone de construction en annexe": "zone-de-construction-en-annexe",
        u"Zone de recul": "zone-de-recul",
        u"Zone artisanale": "zone-artisanale",
        u"Zone de voirie": "zone-de-voirie",
        u"Zone affectée à l'eau": "zone-affectee-a-l-eau",
        u"Zone de construction à destination publique indifférenciée": "zone-de-construction-a-destination-publique-indifferenciee",
        u"Zone agricole indiférenciée": "zone-agricole-indiferenciee",

        u"aire de faible densité": "afad",
        u"aire de forte densité": "afod",
        u"aire de moyenne densité": "amd",
        u"dans un périmètre d'intérêt culturel, historique ou esthétique": "dupiche",
        u"dans un périmètre d'intérêt paysager": "dupip",
        u"dans un périmètre de réservation": "dupdr",
        u"déclaré inhabitable": "di",
        u"dossier en cours": "dec",
        u"eau": "eau",
        u"élevé": "eleve",
        u"éloignée": "eloi",
        u"en partie dans un périmètre de réservation": "epdupdr",
        u"faible": "fai",
        u"infraction relevée mais sans pv": "irmspv",
        u"moyen": "moy",
        u"parcs résidentiels": "pres",
        u"périmètre de réservation sur 75 m de profondeur à partir de l'axe de la voirie": "pdrs75mdpapdadlv",
        u"périmètre de zones protégées": "pdzp",
        u"plan d'eau": "peau",
        u"pv de constat d'infraction": "pvdci",
        u"rapprochée": "rapp",
        u"sans affectation": "saffec",
        u"travaux imposés": "timp",
        u"très faible": "tfai",
        u"voirie": "voirie",
        u"zone agricole": "za",
        u"zone agricole dans un périmètre d'intérêt paysager": "zadupip",
        u"zone agricole dans un périmètre d'intérêt paysager pour le surplus": "zadupippsur",
        u"zone agricole et zone de bâtisses agricoles": "zaezba",
        u"zone agricole et zone forestière": "zaezf",
        u"zone agricole pour le surplus": "zaplsur",
        u"zone agricole pour partie": "zapp",
        u"zone artisanale": "zart",
        u"zone boisée": "zb",
        u"zone d'activité économique industrielle": "zaei",
        u"zone d'activité économique mixte": "zaem",
        u"zone d'activités économiques et commerciales": "zaeec",
        u"zone d'aménagement communal concerté": "zacc",
        u"zone d'aménagement communal concerté mise en oeuvre": "zaccmeo",
        u"zone d'assainissement autonome": "zaa",
        u"zone d'assainissement collectif": "zac",
        u"zone d'entreprise commerciale de grande dimension": "zecdgd",
        u"zone d'équipement communautaire": "zec",
        u"zone d'équipements communautaires et de services publics": "zecedsp",
        u"zone d'espaces verts": "zev",
        u"zone d'ext d'industrie": "zexti",
        u"zone d'ext. d'habitat": "zexth",
        u"zone d'ext. d'habitat à caractère rural": "zexthacr",
        u"zone d'ext.. de parcs résidentiels": "zextdpr",
        u"zone d'extension pour bâtisses  espacées": "zexpbe",
        u"zone d'extension pour bâtisses espacées": "zexpbe",
        u"zone d'extraction": "zextract",
        u"zone d'habitat": "zha",
        u"zone d'habitat à caractère rural": "zhaacr",
        u"zone d'habitat à caractère rural sur une profondeur de 40 mètres": "zhaacrsp40",
        u"zone d'habitat à caractère rural sur une profondeur de 50 mètres": "zhaacrsp50",
        u"zone d'habitat dans un périmètre d'intérêt culturel, historique ou esthétique": "zhadupiche",
        u"zone d'habitat sur 50 m de profondeur": "zhas50dp",
        u"zone d'habitation": "zhation",
        u"zone d'habitation, annexes, abris": "zhaaa",
        u"zone de bâtisses agricoles": "zdba",
        u"zone de construction d'habitation fermée": "zdchaf",
        u"zone de construction d'habitation ouverte": "zdchao",
        u"zone de construction d'habitation semi-ouverte": "zdchaso",
        u"zone de construction en annexe": "zdcea",
        u"zone de cours et jardins": "zdcej",
        u"zone de loisirs": "zdl",
        u"zone de parc": "zdparc",
        u"zone de parc ou d'espaces verts": "zdparcev",
        u"zone de prévention en matière de prises d'eau souterraines, zones éloignées.": "zdpemdpeausoutze",
        u"zone de recul": "zdrec",
        u"zone de recul et de voirie": "zdrecedv",
        u"zone de recul, zone de construction d'habitation fermée et zone de cours et jardins": "zdreczdchafeezdcej",
        u"zone de service": "zdserv",
        u"zone de voirie réservée aux piétons": "zdvoirap",
        u"zone de voiries et d'espaces publics": "zdveep",
        u"zone faiblement habitée": "zfaiha",
        u"zone forestière": "zforest",
        u"zone forestière d'intérêt paysager": "zforestip",
        u"zone industrielle": "zi",
        u"zone réservée aux annexes": "zresaa",
        u"zone réservée aux constructions à un étage": "zresacaue",
        u"zone réservée aux constructions principales": "zresacprinc",
        u"zone réservée aux constructions principales, en zone de cours et jardins et en voirie": "zresacprincezcejeev",
    },

    'raw_pca_List': {
        u"pca1": u"pca1",
        u"pca2": u"pca2",
        u"pca3": u"pca3",
        u"pca4": u"pca4",
    },

    'contact_Proprietary_List': {
        'UrbanCertificateOne', 'UrbanCertificateTwo', 'Division', 'NotaryLetter'
    },

    # Simple keys by locality
    'pcaLikeType': 'PCA%',
    'avisPrealableDuFD': u'%avis préalable du FD%',

    'architects_cpsn_type': {-47146, -1003},
    'architects_cpsn_type_like': '%architect%',

    'notaire_cpsn_type': {996050, 917942, -47148},
    'notaire_cpsn_type_like': '%notaire%',

    'investigation_object_key': u"objet enquête",
}
