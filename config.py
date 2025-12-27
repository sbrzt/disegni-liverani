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

# Tainacan CSV import syntax constants
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
        0: "id",
        1: "Identificativo",
        2: "id"
        },
    2: {
        0: "type",
        1: "Tipologia",
        2: "sections[?(@.cd=='OG')].blocks[*].marks[?(@.cd=='OGTD')].values"
        },
    3: {
        0: "subject",
        1: "Soggetto",
        2: "sections[?(@.cd=='OG')].blocks[*].marks[?(@.cd=='SGTI')].values"
        },
    4: {
        0: "nation",
        1: "Nazione",
        2: "sections[?(@.cd=='LC')].blocks[*].marks[?(@.cd=='PVCS')].values"
        },
    5: {
        0: "region",
        1: "Regione",
        2: "sections[?(@.cd=='LC')].blocks[*].marks[?(@.cd=='PVCR')].values"
        },
    6: {
        0: "province",
        1: "Provincia",
        2: "sections[?(@.cd=='LC')].blocks[*].marks[?(@.cd=='PVCP')].values"
        },
    7: {
        0: "city",
        1: "Città",
        2: "sections[?(@.cd=='LC')].blocks[*].marks[?(@.cd=='PVCC')].values"
        },
    8: {
        0: "conservation_org",
        1: "Ente di conservazione",
        2: "sections[?(@.cd=='LC')].blocks[*].marks[?(@.cd=='LDCN')].values"
        },
    9: {
        0: "collection",
        1: "Collezione",
        2: "sections[?(@.cd=='LC')].blocks[*].marks[?(@.cd=='LDCM')].values"
        },
    10: {
        0: "inventory_id",
        1: "Numero di inventario",
        2: "sections[?(@.cd=='UB')].blocks[*].marks[?(@.cd=='INVN')].values"
        },
    11: {
        0: "author",
        1: "Autore",
        2: "sections[?(@.cd=='AU')].blocks[*].marks[?(@.cd=='AUTN')].values"
        },
    12: {
        0: "measure_height",
        1: "Altezza",
        2: "sections[?(@.cd=='MT')].blocks[*].marks[?(@.cd=='MISA')].values"
        },
    13: {
        0: "measure_length",
        1: "Lunghezza",
        2: "sections[?(@.cd=='MT')].blocks[*].marks[?(@.cd=='MISL')].values"
        },
    14: {
        0: "measure_unit",
        1: "Unità di misura",
        2: "sections[?(@.cd=='MT')].blocks[*].marks[?(@.cd=='MISU')].values"
        },
    15: {
        0: "materials", 
        1: "Materiali usati",
        2: "sections[?(@.cd=='MT')].marks[?(@.cd=='MTC')].values"
        },
    16: {
        0: "conservation_status",
        1: "Stato di conservazione",
        2: "sections[?(@.cd=='CO')].blocks[*].marks[?(@.cd=='STCC')].values"
        },
    17: {
        0: "conservation_status_desc",
        1: "Descrizione di conservazione",
        2: "sections[?(@.cd=='CO')].blocks[*].marks[?(@.cd=='STCS')].values"
        },
    18: {
        0: "description",
        1: "Descrizione",
        2: "sections[?(@.cd=='DA')].blocks[*].marks[?(@.cd=='DESO')].values"
        },
    19: {
        0: "notes",
        1: "Note",
        2: "sections[?(@.cd=='DA')].marks[?(@.cd=='NSC')].values"
        },
    20: {
        0: "acquisition_type",
        1: "Modalità di acquisizione",
        2: "sections[?(@.cd=='TU')].blocks[*].marks[?(@.cd=='ACQT')].values"
        },
    21: {
        0: "acquisition_resp",
        1: "Responsabile dell'acquisizione",
        2: "sections[?(@.cd=='TU')].blocks[*].marks[?(@.cd=='ACQN')].values"
        },
    22: {
        0: "acquisition_date",
        1: "Data di acquisizione",
        2: "sections[?(@.cd=='TU')].blocks[*].marks[?(@.cd=='ACQD')].values"
        },
    23: {
        0: "acquisition_place",
        1: "Luogo di acquisizione",
        2: "sections[?(@.cd=='TU')].blocks[*].marks[?(@.cd=='ACQL')].values"
        },
    24: {
        0: "property",
        1: "Proprietà",
        2: "sections[?(@.cd=='TU')].blocks[*].marks[?(@.cd=='CDGS')].values"
        },
    25: {
        0: "path_image_verso",
        1: "Link (verso)",
        2: "sections[?(@.cd=='DO')].blocks[0].marks[?(@.cd=='FTAZ')].values"
        },
    26: {
        0: "path_image_recto",
        1: "Link (recto)",
        2: "sections[?(@.cd=='DO')].blocks[1].marks[?(@.cd=='FTAZ')].values"
        },
    27: {
        0: "begin_date",
        1: "Data di creazione (inizio)",
        2: "sections[?(@.cd=='DT')].blocks[*].marks[?(@.cd=='DTSI')].values"
        },
    28: {
        0: "end_date",
        1: "Data di creazione (fine)",
        2: "sections[?(@.cd=='DT')].blocks[*].marks[?(@.cd=='DTSF')].values"
        },
    29: {
        0: "is_existing",
        1: "Esiste"
        },
    30: {
        0: "directions",
        1: "Indicazioni"
        },
    31: {
        0: "link",
        1: "Link (Pater)"
        },
    32: {
        0: "latitude",
        1: "Latitudine"
        },
    33: {
        0: "longitude",
        1: "Longitudine"
        }
}