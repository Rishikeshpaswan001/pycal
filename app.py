from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML template as a string
html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .calculator {
            background: #ffffff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        input[type="text"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 18px;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            border: none;
            border-radius: 4px;
            background-color: #007bff;
            color: white;
        }
        button:hover {
            background-color: #0056b3;
        }
        .result {
            margin-top: 10px;
            font-size: 24px;
            color: #333;
        }
    </style>
</head>
<body>
    <div class="calculator">
        <h2>Flask Calculator</h2>
        <form method="POST">
            <input type="text" name="expression" placeholder="Enter expression (e.g., 2+2)" required>
            <button type="submit">Calculate</button>
        </form>
        {% if result %}
            <div class="result">Result: {{ result }}</div>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""
    if request.method == "POST":
        try:
            expression = request.form["expression"]
            result = eval(expression)
        except Exception:
            result = "Error"

    return render_template_string(html_template, result=result)

if __name__ == "__main__":
    app.run(debug=True)
