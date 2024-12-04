from flask import Flask, jsonify, request, render_template_string
import datetime

app = Flask(__name__)

# Sample data to demonstrate dynamic content
daily_quotes = [
    "Every day is a second chance.",
    "Keep pushing, success is just around the corner.",
    "Consistency is the key to progress.",
    "One step at a time, you’ll get there.",
    "Great things never come from comfort zones."
]

# Advanced HTML template with Bootstrap and JavaScript
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Advanced Flask App</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(135deg, #f8f9fa, #e0e0e0);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }
        .container {
            margin-top: 50px;
            flex-grow: 1;
        }
        .quote-card {
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            transition: 0.3s ease-in-out;
        }
        .quote-card:hover {
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
            transform: scale(1.05);
        }
        .navbar-brand {
            font-weight: bold;
            color: #fff !important;
        }
        footer {
            background-color: #343a40;
            color: #fff;
            padding: 15px 0;
            text-align: center;
        }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">🚀 Flask Advanced App</a>
        </div>
    </nav>

    <div class="container text-center">
        <h1 class="my-4 text-primary">Welcome to Our Advanced Flask App 🚀</h1>
        <p class="lead">Let’s make every day count with a little inspiration!</p>
        <div class="quote-card p-4 bg-white rounded">
            <h3>Daily Quote 🌟</h3>
            <p class="fst-italic">{{ quote }}</p>
            <small class="text-muted">Updated at: {{ current_time }}</small>
        </div>
        <hr>
        <h4>Interact with our API:</h4>
        <a class="btn btn-success mt-3" href="/api/quotes">View Quotes API</a>
        
        <button class="btn btn-primary mt-3" data-bs-toggle="modal" data-bs-target="#addQuoteModal">Add a New Quote</button>
    </div>

    <!-- Modal for Adding Quotes -->
    <div class="modal fade" id="addQuoteModal" tabindex="-1" aria-labelledby="addQuoteModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="addQuoteModalLabel">Add a New Quote</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form id="quoteForm">
                        <div class="mb-3">
                            <label for="quoteInput" class="form-label">Your Quote</label>
                            <input type="text" class="form-control" id="quoteInput" required>
                        </div>
                        <button type="submit" class="btn btn-primary">Submit</button>
                    </form>
                </div>
            </div>
        </div>
    </div>

    <footer>
        <p>&copy; {{ current_year }} Flask Advanced App. All Rights Reserved.</p>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        document.getElementById('quoteForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            const quote = document.getElementById('quoteInput').value;
            const response = await fetch('/api/quotes', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ quote })
            });
            const result = await response.json();
            if (response.ok) {
                alert('Quote added successfully!');
                window.location.reload();
            } else {
                alert('Error: ' + result.error);
            }
        });
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    current_year = datetime.datetime.now().year
    daily_quote = daily_quotes[datetime.datetime.now().day % len(daily_quotes)]
    return render_template_string(html_template, quote=daily_quote, current_time=current_time, current_year=current_year)

@app.route('/api/quotes', methods=['GET'])
def get_quotes():
    return jsonify({"quotes": daily_quotes})

@app.route('/api/quotes', methods=['POST'])
def add_quote():
    new_quote = request.json.get('quote')
    if new_quote:
        daily_quotes.append(new_quote)
        return jsonify({"message": "Quote added successfully!", "quotes": daily_quotes}), 201
    else:
        return jsonify({"error": "Quote text is required!"}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
