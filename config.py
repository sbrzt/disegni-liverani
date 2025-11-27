# config.py 

API_ENDPOINT = "https://bbcc.regione.emilia-romagna.it/samira/api/card/"
FILE = "lista_link_liverani_pater.txt"
BATCH = 50
IMAGE_URL = "https://bbcc.regione.emilia-romagna.it/pater/data"


# --- Values to extract ---
TARGET_VALUES = {
    "id":                           "id",
    "type":                         "sections[?(@.cd=='OG')].blocks[*].marks[?(@.cd=='OGTD')].values",
    "subject":                      "sections[?(@.cd=='OG')].blocks[*].marks[?(@.cd=='SGTI')].values",
    "nation":                       "sections[?(@.cd=='LC')].blocks[*].marks[?(@.cd=='PVCS')].values",
    "region":                       "sections[?(@.cd=='LC')].blocks[*].marks[?(@.cd=='PVCR')].values",
    "province":                     "sections[?(@.cd=='LC')].blocks[*].marks[?(@.cd=='PVCP')].values",
    "città":                        "sections[?(@.cd=='LC')].blocks[*].marks[?(@.cd=='PVCC')].values",
    "conservation_org":             "sections[?(@.cd=='LC')].blocks[*].marks[?(@.cd=='LDCN')].values",
    "collection":                   "sections[?(@.cd=='LC')].blocks[*].marks[?(@.cd=='LDCM')].values",
    "inventory_id":                 "sections[?(@.cd=='UB')].blocks[*].marks[?(@.cd=='INVN')].values",
    "author":                       "sections[?(@.cd=='AU')].blocks[*].marks[?(@.cd=='AUTN')].values",
    "measure_height":               "sections[?(@.cd=='MT')].blocks[*].marks[?(@.cd=='MISA')].values",
    "measure_length":               "sections[?(@.cd=='MT')].blocks[*].marks[?(@.cd=='MISL')].values",
    "measure_unit":                 "sections[?(@.cd=='MT')].blocks[*].marks[?(@.cd=='MISU')].values",
    "materials":                    "sections[?(@.cd=='MT')].marks[?(@.cd=='MTC')].values",
    "conservation_status":          "sections[?(@.cd=='CO')].blocks[*].marks[?(@.cd=='STCC')].values",
    "conservation_status_desc":     "sections[?(@.cd=='CO')].blocks[*].marks[?(@.cd=='STCS')].values",
    "description":                  "sections[?(@.cd=='DA')].blocks[*].marks[?(@.cd=='DESO')].values",
    "notes":                        "sections[?(@.cd=='DA')].marks[?(@.cd=='NSC')].values",
    "acquisition_type":             "sections[?(@.cd=='TU')].blocks[*].marks[?(@.cd=='ACQT')].values",
    "acquisition_resp":             "sections[?(@.cd=='TU')].blocks[*].marks[?(@.cd=='ACQN')].values",
    "acquisition_date":             "sections[?(@.cd=='TU')].blocks[*].marks[?(@.cd=='ACQD')].values",
    "acquisition_place":            "sections[?(@.cd=='TU')].blocks[*].marks[?(@.cd=='ACQL')].values",
    "property":                     "sections[?(@.cd=='TU')].blocks[*].marks[?(@.cd=='CDGG')].values",
    "path_image":                   "sections[?(@.cd=='DO')].blocks[*].marks[?(@.cd=='FTAZ')].values",                           # +
    "begin_date":                   "sections[?(@.cd=='DT')].blocks[*].marks[?(@.cd=='DTSI')].values",
    "end_date":                     "sections[?(@.cd=='DT')].blocks[*].marks[?(@.cd=='DTSF')].values"                        # ~
}