from flask import Flask, render_template_string, request
import joblib

app = Flask(__name__)

# Loading the trained model here
model = joblib.load('credit_card_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def predict():
    prediction = None
    if request.method == 'POST':
        features = [float(request.form[f'feature{i}']) for i in range(1, 30)]
        pred = model.predict([features])[0]
        prediction = "Fraudulent Transaction" if pred == 1 else "Normal Transaction"
    
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Credit Card Fraud Detection</title>
        <style>
            /* General Settings */
            body {
                font-family: 'Arial', sans-serif;
                background-color: #1b1b1b;
                color: #f5f5f5;
                margin: 0;
                padding: 0;
                line-height: 1.6;
            }

            /* Navbar */
            .navbar {
                background-color: #333;
                padding: 1rem;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            
            .navbar h1 {
                color: #f5f5f5;
                margin: 0;
            }

            .navbar ul {
                list-style: none;
                padding: 0;
                margin: 0;
                display: flex;
            }

            .navbar ul li {
                margin-left: 20px;
            }

            .navbar ul li a {
                color: #f5f5f5;
                text-decoration: none;
                padding: 5px 10px;
                transition: background-color 0.3s ease-in-out;
            }

            .navbar ul li a:hover {
                background-color: #555;
                border-radius: 5px;
            }

            /* Container */
            .container {
                max-width: 1200px;
                margin: 30px auto;
                padding: 20px;
                background-color: #2b2b2b;
                border-radius: 10px;
                box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.5);
            }

            /* Forms */
            form {
                margin: 0 auto;
                padding: 1rem;
            }

            form label {
                display: block;
                margin-bottom: 10px;
                font-weight: bold;
            }

            form input[type="text"],
            form input[type="number"],
            form input[type="email"],
            form select {
                width: 100%;
                padding: 10px;
                margin-bottom: 20px;
                border: 1px solid #ddd;
                border-radius: 5px;
                background-color: #333;
                color: #f5f5f5;
            }

            form input[type="submit"] {
                background-color: #f39c12;
                color: #fff;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                transition: background-color 0.3s ease-in-out;
            }

            form input[type="submit"]:hover {
                background-color: #e67e22;
            }

            /* Footer */
            .footer {
                text-align: center;
                padding: 2px;
                background-color: #333;
                color: #f5f5f5;
                position: fixed;
                bottom: 0;
                width: 100%;
            }
        </style>
    </head>
    <body>
        <div class="navbar">
            <h1>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp Credit Card Fraud Detection</h1>
            <img src="{{ url_for('static', filename='img2.jpg') }}" height="60" width="190" >                    
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/connect">Connect</a></li>
            </ul>
        </div>
 
        <div class="container">
            <h2>Enter Transaction Data</h2>
            <form action="/" method="post">
                {% for i in range(1, 30) %}
                    <label for="feature{{ i }}">Feature {{ i }}:</label>
                    <input type="text" id="feature{{ i }}" name="feature{{ i }}">
                {% endfor %}
                <input type="submit" value="Predict">
            </form>

            {% if prediction %}
                <h2>Prediction Result:</h2>
                <p>{{ prediction }}</p>
            {% endif %}
        </div>

        <div class="footer">
            <p>&copy; 2024 Credit Card Fraud Detection. All Rights Reserved.</p>
        </div>
    </body>
    </html>
    ''', prediction=prediction)

@app.route('/connect', methods=['GET', 'POST'])
def connect():
    alert_script = """
    <script>
        function showAlert() {
            alert("Thank you for reaching out! We will get back to you soon.");
        }
    </script>
    """
    return render_template_string(f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Connect with Us</title>
        <style>
            /* General Settings */
            body {{
                font-family: 'Arial', sans-serif;
                background-color: #1b1b1b;
                color: #f5f5f5;
                margin: 0;
                padding: 0;
                line-height: 1.6;
            }}

            /* Navbar */
            .navbar {{
                background-color: #333;
                padding: 1rem;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }}

            .navbar h1 {{
                color: #f5f5f5;
                margin: 0;
            }}

            .navbar ul {{
                list-style: none;
                padding: 0;
                margin: 0;
                display: flex;
            }}

            .navbar ul li {{
                margin-left: 20px;
            }}

            .navbar ul li a {{
                color: #f5f5f5;
                text-decoration: none;
                padding: 5px 10px;
                transition: background-color 0.3s ease-in-out;
            }}

            .navbar ul li a:hover {{
                background-color: #555;
                border-radius: 5px;
            }}

            /* Container */
            .container {{
                max-width: 1200px;
                margin: 30px auto;
                padding: 20px;
                background-color: #2b2b2b;
                border-radius: 10px;
                box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.5);
            }}

            /* Form */
            form {{
                display: flex;
                flex-direction: column;
            }}

            form label {{
                margin-top: 10px;
            }}

            form input[type="text"],
            form input[type="email"],
            form textarea {{
                padding: 10px;
                margin-top: 5px;
                background-color: #333;
                color: #f5f5f5;
                border: 1px solid #555;
                border-radius: 5px;
            }}

            form input[type="submit"] {{
                margin-top: 20px;
                padding: 10px;
                background-color: #555;
                color: #f5f5f5;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                transition: background-color 0.3s ease-in-out;
            }}

            form input[type="submit"]:hover {{
                background-color: #777;
            }}

            /* Footer */
            .footer {{
                text-align: center;
                padding: 3px;
                background-color: #333;
                color: #f5f5f5;
                position: fixed;
                bottom: 0;
                width: 100%;
            }}
        </style>
        {alert_script}
    </head>
    <body>
        <div class="navbar">
            <h1>Credit Card Fraud Detection</h1>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/connect">Connect</a></li>
            </ul>
        </div>

        <div class="container">
            <h2>Connect with Us</h2>
            <p>If you have any questions, feedback, or just want to get in touch, feel free to reach out!</p>
            <form onsubmit="showAlert()">
                <label for="name">Your Name:</label>
                <input type="text" id="name" name="name" placeholder="Enter your name" required>

                <label for="email">Your Email:</label>
                <input type="email" id="email" name="email" placeholder="Enter your email" required>

                <label for="message">Your Message:</label>
                <textarea id="message" name="message" rows="4" placeholder="Enter your message" required></textarea>

                <input type="submit" value="Send Message">
            </form>
        </div>

        <div class="footer">
            <p>&copy; 2024 Credit Card Fraud Detection. All Rights Reserved.</p>
        </div>
    </body>
    </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
