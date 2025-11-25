# config.py

API_ENDPOINT = "https://bbcc.regione.emilia-romagna.it/samira/api/card/"
FILE = "lista_link_liverani_pater.txt"
BATCH = 50

# --- Values to extract ---
TARGET_VALUES = {
    "type": 'dct["sections"][1]["blocks"][0]["marks"][0]["values"][0]',
    "subject": 'dct["sections"][1]["blocks"][1]["marks"][0]["values"][0]',
    "nation": 'dct["sections"][2]["blocks"][0]["marks"][0]["values"][0]',
    "province": 'dct["sections"][2]["blocks"][0]["marks"][1]["values"][0]',
    "place": 'dct["sections"][2]["blocks"][0]["marks"][2]["values"][0]',
}