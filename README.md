# Arte e territorio: nuovi approcci e strumenti digitali per una fruizione più accessibile e interattiva al patrimonio culturale

🇺🇸: This project automates the integration of descriptive metadata for the management of a digital archive for Liverani's drawings on WordPress via the Tainacan plugin.

🇮🇹: Questo progetto automatizza l'integrazione di metadati descrittivi per la gestione di un archivio digitale di disegni di Liverani su WordPress tramite il plugin Tainacan.


## 🇺🇸 English version

### Overview
This system processes a collection of drawings. It combines descriptive metadata (downloaded dynamically from Pater's API) with descriptive metadata collected in a separate CSV file.

### Key features
* ***Pater's API interaction***: Downloads JSON data related to a list of drawings from Pater and converts it into a CSV table.
* ***Custom merging***: Merges the CSV obtained via the API calls with another CSV generated manually and containing additional data that are not present in Pater (e.g., latitude and longitude).
* ***Tainacan ready***: Automatically formats column headers using a specific syntax (e.g., `Title|text|status_public`) for the WordPress Tainacan CSV importer.

### Project structure
* `data`: Folder containing the project's data.
* `main.py`: Pipeline orchestrator.
* `config.py`: Centralised configuration file.
* `src/extract.py`: Extraction engine that uses JSONPath.
* `src/merge.py`: Script for merging one full CSV file with a selection of columns extracted from another CSV file.
* `src/prep.py`: Formatting logic for Tainacan integration.

### Usage
This project relies on [uv](https://github.com/astral-sh/uv) for fast and reliable dependency management.

1. **Installing uv**: If you haven't installed it yet, run:

```bash
curl -LsSf https://astral-sh.uv/install.sh | sh
```

2. **Virtual environment creation**: Within the project folder, create the environment with:

```bash
uv init .
```

3. **Project synchronization**: Install dependencies with:

```bash
uv sync
```

4. **Configuration**: Verify directory paths and file paths in `config.py`.

5. **Execution**: Run the processing pipeline using `uv`:

```bash
uv run main.py
```


## 🇮🇹 Versione italiana

### Panoramica
Questo sistema elabora una collezione di disegni. Combina i metadati descrittivi (scaricati dinamicamente dall'API di Pater) con i metadati descrittivi raccolti in un file CSV separato.

### Caratteristiche principali
* ***Interazione con le API di Pater***: Scarica i dati in formato JSON relativi a un elenco di disegni da Pater e li converte in una tabell***a CSV.
* ***Merge personalizzato***: Unisce il CSV ottenuto tramite le chiamate API con un altro CSV generato manualmente contenente dati aggiuntivi non presenti su Pater (ad esempio, latitudine e longitudine).
* ***Preparazione per Tainacan***: Formatta automaticamente le intestazioni delle colonne con una sintassi specifica (es. `Identificativo|text|status_private`) per l'importatore CSV di Tainacan.

### Struttura del progetto
* `main.py`: Orchestratore della pipeline.
* `config.py`: File di configurazione centralizzato.
* `src/extract.py`: Motore di estrazione che utilizza JSONPath.
* `src/merge.py`: Script per l'unione di un file CSV completo con una selezione di colonne estratte da un altro file CSV.
* `src/prep.py`: Logica di formattazione per l'integrazione con Tainacan.

### Uso
Questo progetto utilizza [uv](https://github.com/astral-sh/uv) per una gestione rapida e affidabile delle dipendenze.

1. **Installazione di uv**: Se non lo hai già, installalo con:

```bash
curl -LsSf https://astral-sh.uv/install.sh | sh
```

2. **Creazione dell'ambiente virtuale**: Nella cartella di progetto, inizializza l'ambiente con:

```bash
uv init .
```

3. **Sincronizzazione progetto**: Installa le dipendenze con:

```bash
uv sync
```

4. **Configurazione**: Verifica i percorsi delle directory e dei file in `config.py`.

5. **Esecuzione**: Avvia la pipeline di elaborazione tramite `uv`:

```bash
uv run main.py
```