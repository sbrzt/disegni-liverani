# config.py 

API_ENDPOINT = "https://bbcc.regione.emilia-romagna.it/samira/api/card/"
IMAGE_PREFIX = "https://bbcc.regione.emilia-romagna.it/pater/data"
ID_LIST = "data/lista_link_liverani_pater.txt"
API_OUTPUT = "data/dataset_pater.csv"
DATASET_MANUAL = "data/vedute.csv"
BATCH = 50
COLUMNS = [
    "id",
    "is_existing",
    "directions",
    "link",
    "latitude",
    "longitude"
]
OUTPUT_ARCHIVE = "data/dataset_disegni.csv"
OUTPUT_PUBLISH = "data/db_liverani.csv"
KEY = "id"

# CSV import syntax constants
LABEL_SEPARATOR = "|"
DB_KEY_PARAMETER = 'collection_key_yes'
STATUS_PRIVATE_PARAMETER = 'status_private'
STATUS_PUBLIC_PARAMETER = 'status_public'
RELATIONSHIP_PARAMETER = 'relationship'
NUMERIC_PARAMETER = 'numeric'
DATE_PARAMETER = 'date'
TEXT_PARAMETER = 'text'

# Values to extract
TARGET_VALUES = {
    1: {
        "key": "id",
        "label": "Identificativo",
        "path": "id",
        "type": TEXT_PARAMETER,
        "status": STATUS_PRIVATE_PARAMETER
        },
    2: {
        "key": "type",
        "label": "Tipologia",
        "path": "sections[?(@.cd=='OG')].blocks[*].marks[?(@.cd=='OGTD')].values",
        "type": TEXT_PARAMETER,
        "status": STATUS_PUBLIC_PARAMETER
        },
    3: {
        "key": "subject",
        "label": "Soggetto",
        "path": "sections[?(@.cd=='OG')].blocks[*].marks[?(@.cd=='SGTI')].values",
        "type": TEXT_PARAMETER,
        "status": STATUS_PUBLIC_PARAMETER
        },
    4: {
        "key": "nation",
        "label": "Nazione",
        "path": "sections[?(@.cd=='LC')].blocks[*].marks[?(@.cd=='PVCS')].values",
        "type": TEXT_PARAMETER,
        "status": STATUS_PUBLIC_PARAMETER
        },
    5: {
        "key": "region",
        "label": "Regione",
        "path": "sections[?(@.cd=='LC')].blocks[*].marks[?(@.cd=='PVCR')].values",
        "type": TEXT_PARAMETER,
        "status": STATUS_PUBLIC_PARAMETER
        },
    6: {
        "key": "province",
        "label": "Provincia",
        "path": "sections[?(@.cd=='LC')].blocks[*].marks[?(@.cd=='PVCP')].values",
        "type": TEXT_PARAMETER,
        "status": STATUS_PUBLIC_PARAMETER
        },
    7: {
        "key": "city",
        "label": "Città",
        "path": "sections[?(@.cd=='LC')].blocks[*].marks[?(@.cd=='PVCC')].values",
        "type": TEXT_PARAMETER,
        "status": STATUS_PUBLIC_PARAMETER
        },
    8: {
        "key": "conservation_org",
        "label": "Ente di conservazione",
        "path": "sections[?(@.cd=='LC')].blocks[*].marks[?(@.cd=='LDCN')].values",
        "type": TEXT_PARAMETER,
        "status": STATUS_PUBLIC_PARAMETER
        },
    9: {
        "key": "collection",
        "label": "Collezione",
        "path": "sections[?(@.cd=='LC')].blocks[*].marks[?(@.cd=='LDCM')].values",
        "type": TEXT_PARAMETER,
        "status": STATUS_PUBLIC_PARAMETER
        },
    10: {
        "key": "inventory_id",
        "label": "Numero di inventario",
        "path": "sections[?(@.cd=='UB')].blocks[*].marks[?(@.cd=='INVN')].values",
        "type": TEXT_PARAMETER,
        "status": STATUS_PUBLIC_PARAMETER
        },
    11: {
        "key": "author",
        "label": "Autore",
        "path": "sections[?(@.cd=='AU')].blocks[*].marks[?(@.cd=='AUTN')].values",
        "type": TEXT_PARAMETER,
        "status": STATUS_PUBLIC_PARAMETER
        },
    12: {
        "key": "measure_height",
        "label": "Altezza",
        "path": "sections[?(@.cd=='MT')].blocks[*].marks[?(@.cd=='MISA')].values",
        "type": NUMERIC_PARAMETER,
        "status": STATUS_PUBLIC_PARAMETER
        },
    13: {
        "key": "measure_length",
        "label": "Lunghezza",
        "path": "sections[?(@.cd=='MT')].blocks[*].marks[?(@.cd=='MISL')].values",
        "type": NUMERIC_PARAMETER,
        "status": STATUS_PUBLIC_PARAMETER
        },
    14: {
        "key": "measure_unit",
        "label": "Unità di misura",
        "path": "sections[?(@.cd=='MT')].blocks[*].marks[?(@.cd=='MISU')].values",
        "type": TEXT_PARAMETER,
        "status": STATUS_PRIVATE_PARAMETER
        },
    15: {
        "key": "materials", 
        "label": "Materiali usati",
        "path": "sections[?(@.cd=='MT')].marks[?(@.cd=='MTC')].values",
        "type": TEXT_PARAMETER,
        "status": STATUS_PUBLIC_PARAMETER
        },
    16: {
        "key": "conservation_status",
        "label": "Stato di conservazione",
        "path": "sections[?(@.cd=='CO')].blocks[*].marks[?(@.cd=='STCC')].values",
        "type": TEXT_PARAMETER,
        "status": STATUS_PUBLIC_PARAMETER
        },
    17: {
        "key": "conservation_status_desc",
        "label": "Descrizione di conservazione",
        "path": "sections[?(@.cd=='CO')].blocks[*].marks[?(@.cd=='STCS')].values",
        "type": TEXT_PARAMETER,
        "status": STATUS_PUBLIC_PARAMETER
        },
    18: {
        "key": "description",
        "label": "Descrizione",
        "path": "sections[?(@.cd=='DA')].blocks[*].marks[?(@.cd=='DESO')].values",
        "type": TEXT_PARAMETER,
        "status": STATUS_PUBLIC_PARAMETER
        },
    19: {
        "key": "notes",
        "label": "Note",
        "path": "sections[?(@.cd=='DA')].marks[?(@.cd=='NSC')].values",
        "type": TEXT_PARAMETER,
        "status": STATUS_PUBLIC_PARAMETER
        },
    20: {
        "key": "acquisition_type",
        "label": "Modalità di acquisizione",
        "path": "sections[?(@.cd=='TU')].blocks[*].marks[?(@.cd=='ACQT')].values",
        "type": TEXT_PARAMETER,
        "status": STATUS_PUBLIC_PARAMETER
        },
    21: {
        "key": "acquisition_resp",
        "label": "Responsabile dell'acquisizione",
        "path": "sections[?(@.cd=='TU')].blocks[*].marks[?(@.cd=='ACQN')].values",
        "type": TEXT_PARAMETER,
        "status": STATUS_PUBLIC_PARAMETER
        },
    22: {
        "key": "acquisition_date",
        "label": "Data di acquisizione",
        "path": "sections[?(@.cd=='TU')].blocks[*].marks[?(@.cd=='ACQD')].values",
        "type": TEXT_PARAMETER,
        "status": STATUS_PUBLIC_PARAMETER
        },
    23: {
        "key": "acquisition_place",
        "label": "Luogo di acquisizione",
        "path": "sections[?(@.cd=='TU')].blocks[*].marks[?(@.cd=='ACQL')].values",
        "type": TEXT_PARAMETER,
        "status": STATUS_PUBLIC_PARAMETER
        },
    24: {
        "key": "property",
        "label": "Proprietà",
        "path": "sections[?(@.cd=='TU')].blocks[*].marks[?(@.cd=='CDGS')].values",
        "type": TEXT_PARAMETER,
        "status": STATUS_PUBLIC_PARAMETER
        },
    25: {
        "key": "path_image_verso",
        "label": "Link (verso)",
        "path": "sections[?(@.cd=='DO')].blocks[0].marks[?(@.cd=='FTAZ')].values",
        "type": TEXT_PARAMETER,
        "status": STATUS_PRIVATE_PARAMETER
        },
    26: {
        "key": "path_image_recto",
        "label": "Link (recto)",
        "path": "sections[?(@.cd=='DO')].blocks[1].marks[?(@.cd=='FTAZ')].values",
        "type": TEXT_PARAMETER,
        "status": STATUS_PRIVATE_PARAMETER
        },
    27: {
        "key": "begin_date",
        "label": "Data di creazione (inizio)",
        "path": "sections[?(@.cd=='DT')].blocks[*].marks[?(@.cd=='DTSI')].values",
        "type": TEXT_PARAMETER,
        "status": STATUS_PUBLIC_PARAMETER
        },
    28: {
        "key": "end_date",
        "label": "Data di creazione (fine)",
        "path": "sections[?(@.cd=='DT')].blocks[*].marks[?(@.cd=='DTSF')].values",
        "type": TEXT_PARAMETER,
        "status": STATUS_PUBLIC_PARAMETER
        },
    29: {
        "key": "is_existing",
        "label": "Esiste",
        "type": TEXT_PARAMETER,
        "status": STATUS_PRIVATE_PARAMETER
        },
    30: {
        "key": "directions",
        "label": "Indicazioni",
        "type": TEXT_PARAMETER,
        "status": STATUS_PRIVATE_PARAMETER
        },
    31: {
        "key": "link",
        "label": "Link (Pater)",
        "type": TEXT_PARAMETER,
        "status": STATUS_PUBLIC_PARAMETER
        },
    32: {
        "key": "latitude",
        "label": "Latitudine",
        "type": TEXT_PARAMETER,
        "status": STATUS_PUBLIC_PARAMETER
        },
    33: {
        "key": "longitude",
        "label": "Longitudine",
        "type": TEXT_PARAMETER,
        "status": STATUS_PUBLIC_PARAMETER
        }
}