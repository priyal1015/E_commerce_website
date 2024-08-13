from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/about_us')
def about_us():
    return render_template('aboutus.html')

@app.route('/contact_us', methods=['GET', 'POST'])
def contact_us():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        # Process the form data (e.g., save to database, send email, etc.)
        # For demonstration, we'll just print it
        print(f"Name: {name}, Email: {email}, Phone: {phone}, Message: {message}")
        return 'Form submitted successfully!'
    return render_template('contactus.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        # Process the registration data (e.g., save to database)
        print(f"Register: Name: {name}, Email: {email}, Password: {password}")
        return 'Registration successful!'
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        # Process the login data (e.g., authenticate user)
        print(f"Login: Email: {email}, Password: {password}")
        return 'Login successful!'
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
