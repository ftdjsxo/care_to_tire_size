from flask import Flask, jsonify, request
import pandas as pd

# Carica i dati dal file CSV
car_details_df = pd.read_csv('car_details.csv')

app = Flask(__name__)

def get_vendors():
    """Restituisce tutti i produttori unici nel dataset."""
    vendors = car_details_df['Vendor'].unique().tolist()
    return sorted(vendors)

def get_models(vendor):
    """Restituisce i modelli unici per un dato produttore."""
    models = car_details_df[car_details_df['Vendor'] == vendor]['Model'].unique()
    return models.tolist()

def get_years(vendor, model):
    """Restituisce gli anni unici per un dato produttore e modello."""
    years = car_details_df[(car_details_df['Vendor'] == vendor) & (car_details_df['Model'] == model)]['Year'].unique()
    return years.tolist()

def get_versions(vendor, model, year):
    """Restituisce le versioni uniche per un dato produttore, modello e anno."""
    versions = car_details_df[(car_details_df['Vendor'] == vendor) & 
                              (car_details_df['Model'] == model) & 
                              (car_details_df['Year'] == year)]['Version'].unique()
    return versions.tolist()

def get_tires(vendor, model, year, version, rim_size=None):
    """Restituisce i pneumatici per una data selezione di veicolo, 
    con opzionale filtraggio per dimensione del cerchio."""
    selected = car_details_df[(car_details_df['Vendor'] == vendor) & 
                              (car_details_df['Model'] == model) & 
                              (car_details_df['Year'] == year) & 
                              (car_details_df['Version'] == version)]
    
    if rim_size:
        # Assicurarsi che rim_size sia una stringa, poiché la stiamo inserendo in un'altra stringa per il confronto
        rim_size = str(rim_size)
        # Filtrare per dimensione del cerchio, se specificato
        selected = selected[selected['Front Size Designation'].str.contains(f'R\s?{rim_size}') |
                            selected['Rear Size Designation'].str.contains(f'R\s?{rim_size}')]

    # Rimuovere gli zeri iniziali dai campi di indice di carico e velocità
    selected['Front Load Speed Index'] = selected['Front Load Speed Index'].str.lstrip('0')
    selected['Rear Load Speed Index'] = selected['Rear Load Speed Index'].str.lstrip('0')

    # Restituire i dati dei pneumatici
    return selected.to_dict(orient='records')



def get_rim_sizes(vendor, model, year, version):
    """Restituisce le dimensioni del cerchio uniche per una data selezione di veicolo."""
    selected_versions = car_details_df[(car_details_df['Vendor'] == vendor) & 
                                       (car_details_df['Model'] == model) & 
                                       (car_details_df['Year'] == year) & 
                                       (car_details_df['Version'] == version)]
    
    # Aggiornamento dell'espressione regolare per accettare uno spazio facoltativo prima del numero del cerchio
    front_rim_sizes = selected_versions['Front Size Designation'].str.extract(r'R\s?(\d+)')[0].dropna().unique()
    rear_rim_sizes = selected_versions['Rear Size Designation'].str.extract(r'R\s?(\d+)')[0].dropna().unique()

    all_rim_sizes = set(front_rim_sizes).union(set(rear_rim_sizes))
    return sorted(list(all_rim_sizes))

@app.route('/vendors', methods=['GET'])
def vendors_route():
    return jsonify(get_vendors())

@app.route('/models', methods=['GET'])
def models_route():
    vendor = request.args.get('vendor')
    return jsonify(get_models(vendor))

@app.route('/years', methods=['GET'])
def years_route():
    vendor = request.args.get('vendor')
    model = request.args.get('model')
    return jsonify(get_years(vendor, model))

@app.route('/versions', methods=['GET'])
def versions_route():
    vendor = request.args.get('vendor')
    model = request.args.get('model')
    year = request.args.get('year')
    return jsonify(get_versions(vendor, model, year))

@app.route('/rim_sizes', methods=['GET'])
def rim_sizes_route():
    vendor = request.args.get('vendor')
    model = request.args.get('model')
    year = request.args.get('year')
    version = request.args.get('version')
    return jsonify(get_rim_sizes(vendor, model, year, version))

@app.route('/tires', methods=['GET'])
def tires_route():
    vendor = request.args.get('vendor')
    model = request.args.get('model')
    year = request.args.get('year')
    version = request.args.get('version')
    rim_size = request.args.get('rim_size', None)
    return jsonify(get_tires(vendor, model, year, version, rim_size))

if __name__ == '__main__':
    app.run(debug=True)
