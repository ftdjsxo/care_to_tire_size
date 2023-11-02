# Car Details API

Questa API fornisce informazioni sui dettagli delle automobili, comprese le specifiche dei pneumatici e le dimensioni dei cerchi in base a vari criteri come produttore, modello, anno e versione.

## API Endpoints

### Get All Vendors

- **URL**: `/vendors`
- **Method**: `GET`
- **Descrizione**: Restituisce un elenco di tutti i produttori di automobili unici.
- **Esempio di richiesta**:
GET http://127.0.0.1:5000/vendors

markdown
Copy code

### Get Models by Vendor

- **URL**: `/models`
- **Method**: `GET`
- **Query Parameters**:
- `vendor`: Il nome del produttore.
- **Descrizione**: Restituisce un elenco di modelli in base al produttore specificato.
- **Esempio di richiesta**:
GET http://127.0.0.1:5000/models?vendor=ALPINE

### Get Years by Vendor and Model

- **URL**: `/years`
- **Method**: `GET`
- **Query Parameters**:
- `vendor`: Il nome del produttore.
- `model`: Il modello dell'auto.
- **Descrizione**: Restituisce un elenco di anni di produzione per un dato produttore e modello.
- **Esempio di richiesta**:
GET http://127.0.0.1:5000/years?vendor=ALPINE&model=A110

### Get Versions by Vendor, Model, and Year

- **URL**: `/versions`
- **Method**: `GET`
- **Query Parameters**:
- `vendor`: Il nome del produttore.
- `model`: Il modello dell'auto.
- `year`: L'anno di produzione dell'auto.
- **Descrizione**: Restituisce un elenco di versioni disponibili per un dato produttore, modello e anno.
- **Esempio di richiesta**:
GET http://127.0.0.1:5000/versions?vendor=ALPINE&model=A110&year=2017%20-%20

### Get Tires by Vehicle Selection

- **URL**: `/tires`
- **Method**: `GET`
- **Query Parameters**:
- `vendor`: Il nome del produttore.
- `model`: Il modello dell'auto.
- `year`: L'anno di produzione dell'auto.
- `version`: La versione dell'auto.
- `rim_size` (opzionale): La dimensione del cerchio per filtrare i pneumatici.
- **Descrizione**: Restituisce un elenco di pneumatici compatibili con la selezione specifica di veicolo. È possibile filtrare ulteriormente per dimensione del cerchio.
- **Esempio di richiesta**:
GET http://127.0.0.1:5000/tires?vendor=ALPINE&model=A110&year=2017%20-%20&version=1.8%20L%20252&rim_size=17

### Get Rim Sizes by Vehicle Selection

- **URL**: `/rim_sizes`
- **Method**: `GET`
- **Query Parameters**:
- `vendor`: Il nome del produttore.
- `model`: Il modello dell'auto.
- `year`: L'anno di produzione dell'auto.
- `version`: La versione dell'auto.
- **Descrizione**: Restituisce le dimensioni dei cerchi disponibili per la selezione specifica di veicolo.
- **Esempio di richiesta**:
GET http://127.0.0.1:5000/rim_sizes?vendor=ALPINE&model=A110&year=2017%20-%20&version=1.8%20L%20252

## Installazione e Avvio

Per utilizzare questa API, clona il repository e installa le dipendenze con:

```bash
pip install -r requirements.txt
