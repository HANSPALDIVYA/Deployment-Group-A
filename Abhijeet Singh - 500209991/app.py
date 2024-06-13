from flask import Flask, request, jsonify
import pandas as pd
import dill

app = Flask(__name__)

# loading models and pre-processing
with open('preprocessor.pkl', 'rb') as f:
    preprocessor = dill.load(f)
with open('scaler.pkl', 'rb') as f:
    scaler = dill.load(f)
with open('svd.pkl', 'rb') as f:
    svd = dill.load(f)
with open('model.pkl', 'rb') as file:
    model = dill.load(file)
    
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    df = pd.DataFrame(data)

    data_imputed = preprocessor.transform(df)
    data_imputed = pd.DataFrame(data_imputed, columns=df.columns)
    data_transformed = scaler.transform(data_imputed)
    data_reduced = svd.transform(data_transformed)
    predictions = model.predict(data_reduced)
    return jsonify(predictions.tolist())


# def predict():
#     data = request.get_json(force = True)
#     features = data['features']  # Assuming features are sent in JSON body
    
#     rf_prediction = model.predict([features])
    
#     return jsonify({
#         'rf_prediction': rf_prediction[0],
#     })

if __name__ == '__main__':
    app.run(debug=True)
