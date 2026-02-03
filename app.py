from flask import Flask, render_template, redirect, url_for, request, flash

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for flash messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/class')
def classes():
    return render_template('class.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/enrollment')
def enrollment():
    return render_template('enrollment.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/blog/<int:id>')
def blog_detail(id):
    return render_template('blog_detail.html', id=id)

@app.route('/book_seat', methods=['POST'])
def book_seat():
    # Handle form submission
    # You can access form data with: request.form['name'], request.form['email'], etc.
    name = request.form.get('name')
    email = request.form.get('email')
    class_selected = request.form.get('class')
    
    # Here you would typically save to database
    # For now, just flash a success message
    flash(f'Thank you {name}! Your seat for {class_selected} class has been booked.', 'success')
    return redirect(url_for('index'))

@app.route('/subscribe', methods=['POST'])
def subscribe():
    # Handle newsletter subscription
    name = request.form.get('name')
    email = request.form.get('email')
    
    # Here you would typically save to database
    flash(f'Thank you {name}! You have been subscribed to our newsletter.', 'success')
    return redirect(url_for('index'))

@app.route('/send_message', methods=['POST'])
def send_message():
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')

if __name__ == '__main__':
    app.run(debug=True)