from flask import Flask, request, render_template
import joblib
import numpy as np
import sklearn

app = Flask(__name__)

# Load the model
model = joblib.load('phishing_model.pkl')

@app.route('/')
def home():
    return render_template('index.html', prediction=None, url=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract URL from form data
        url = request.form['url']
        
        # Extract features based on provided mapping
        features = extract_features(url)

        # Make a prediction
        prediction = model.predict([features])[0]

        # Map prediction to a user-friendly message
        if prediction == 1:
            prediction_text = 'Prediction says phishing URL'
        elif prediction == 0:
            prediction_text = 'Prediction says safe browsing URL'
        else:
            prediction_text = 'broken url'

        return render_template('index.html', prediction=prediction_text, url=url)
    except Exception as e:
        return render_template('index.html', prediction='Error processing URL', url=None)

# Feature extraction logic
def extract_features(url):
    # Replace this placeholder with actual logic to generate feature values based on the URL
    # For now, returning all features set to 1 as per the provided mapping
    features = {
        "qty_dot_url": 1,
            "qty_hyphen_url": 1,
            "qty_slash_url": 1,
            "qty_questionmark_url": 1,
            "qty_equal_url": 1,
            "qty_at_url": 1,
            "qty_and_url": 1,
            "qty_exclamation_url": 1,
            "qty_space_url": 0,
            "qty_tilde_url": 0,
            "qty_comma_url": 0,
            "qty_plus_url": 1,
            "qty_dot_domain": 1,
            "qty_hyphen_domain": 1,
            "qty_underline_domain": 0,
            "qty_slash_domain": 0,
            "qty_questionmark_domain": 0,
            "qty_equal_domain": 0,
            "qty_at_domain": 0,
            "qty_and_domain": 0,
            "qty_exclamation_domain": 0,
            "qty_space_domain": 0,
            "qty_tilde_domain": 0,
            "qty_comma_domain": 0,
            "qty_plus_domain": 0,
            "qty_asterisk_domain": 0,
            "qty_hashtag_domain": 0,
            "qty_dollar_domain": 0,
            "qty_percent_domain": 0,
            "domain_length": 1,
            "qty_vowels_domain": 1,
            "domain_in_ip": 1,
            "server_client_domain": 0,
            "qty_dot_directory": 1,
            "qty_slash_directory": 1,
            "qty_comma_directory": 0,
            "qty_plus_directory": 0,
            "qty_dot_file": 1,
            "qty_hyphen_file": 1,
            "qty_comma_file": 0,
            "qty_plus_file": 0,
            "qty_dot_params": 1,
            "qty_questionmark_params": 1,
            "qty_equal_params": 1,
            "qty_params": 1,
            "email_in_url": 1,
            "time_response": 1,
            "domain_spf": 0,
            "asn_ip": 0,
            "qty_nameservers": 0,
            "ttl_hostname": 1,
            "tls_ssl_certificate": 1,
            "qty_redirects": 1,
            "url_google_index": 0,
            "domain_google_index": 0,
            "url_shortened": 1
    }
    return list(features.values())

if __name__ == '__main__':
    app.run(port=5000, debug=True)
