from datetime import datetime  # Standard library imports first
from flask import Flask, render_template, request, redirect, url_for  

# Third-party library imports after

app = Flask(__name__)

# Home route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        dob_str = request.form['dob']  # Date of birth as string
        try:
            # Convert string to date
            dob = datetime.strptime(dob_str, '%d/%m/%Y')
            # Calculate days since birth
            today = datetime.today()
            days_since_birth = (today - dob).days
            # Return results to the UI
            return render_template('result.html', username=username, days=days_since_birth)
        except ValueError:
            # Handle invalid date format
            error = "Invalid date format. Please use DD/MM/YYYY."
            return render_template('index.html', error=error)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
