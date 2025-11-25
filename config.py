# config.py

API_ENDPOINT = "https://bbcc.regione.emilia-romagna.it/samira/api/card/"
FILE = "lista_link_liverani_pater.txt"
BATCH = 50

# --- Values to extract ---
TARGET_VALUES = {
    "type": 'dct["sections"][1]["blocks"][0]["marks"][0]["values"][0]',
    "subject": 'dct["sections"][1]["blocks"][1]["marks"][0]["values"][0]',
    "nation": 'dct["sections"][2]["blocks"][0]["marks"][0]["values"][0]',
    "region": 'dct["sections"][2]["blocks"][0]["marks"][1]["values"][0]',
    "province": 'dct["sections"][2]["blocks"][0]["marks"][2]["values"][0]',
    "conservation_org": 'dct["sections"][2]["blocks"][1]["marks"][2]["values"][0]',
    "collection": 'dct["sections"][2]["blocks"][1]["marks"][4]["values"][0]',
    "inventory_id": 'dct["sections"][3]["blocks"][0]["marks"][0]["values"][0]',
    "author": 'dct["sections"][5]["blocks"][0]["marks"][0]["values"][0]',
    "measure_height": 'dct["sections"][6]["blocks"][0]["marks"][1]["values"][0]',
    "measure_length": 'dct["sections"][6]["blocks"][0]["marks"][2]["values"][0]',
    "measure_unit": 'dct["sections"][6]["blocks"][0]["marks"][0]["values"][0]',
    "begin_date": 'dct["sections"][4]["blocks"][1]["marks"][0]["values"][0]',
    "end_date": 'dct["sections"][4]["blocks"][1]["marks"][2]["values"][0]'
}