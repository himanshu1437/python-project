from flask import Flask

# Create Flask app
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "<h1>Welcome to My Flask Web App</h1>"

# About route
@app.route('/about')
def about():
    return "<h2>This is the About Page</h2>"

# Dynamic route
@app.route('/user/<name>')
def user(name):
    return f"<h3>Hello, {name}!</h3>"

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
