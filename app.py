from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__, template_folder='templates')
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print(f"New contact: {name} ({email}) says: {message}")
        return redirect(url_for('index'))
    return render_template('contact.html')

@app.route('/projects/bbc-scraper')
def bbc_scraper():
    return render_template('project1.html')

@app.route('/projects/sales-analysis')
def sales_analysis():
    return render_template('project2.html')

if __name__ == '__main__':
    app.run(debug=True)