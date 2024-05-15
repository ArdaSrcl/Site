from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data store
members_list = []
voting_data = {}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/members', methods=['GET', 'POST'])
def members():
    global members_list, voting_data
    if request.method == 'POST':
        new_member = request.form.get('new_member')
        if new_member and new_member not in members_list:
            members_list.append(new_member)
            voting_data[new_member] = 0  # Initialize vote count for new member
    return render_template('members.html', members=members_list)

@app.route('/vote', methods=['GET', 'POST'])
def vote():
    if request.method == 'POST':
        selected_option = request.form.get('option')
        if selected_option in voting_data:
            voting_data[selected_option] += 1
        return redirect(url_for('results'))
    return render_template('vote.html', options=voting_data.keys())

@app.route('/results')
def results():
    return render_template('results.html', voting_data=voting_data)

if __name__ == '__main__':
    app.run(debug=True)
