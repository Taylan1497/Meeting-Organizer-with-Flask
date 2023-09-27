from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'secret_key'

# Dummy data to store meetings (you can replace this with a database)
#meetings = []

#from flask import Flask, render_template, request, redirect, url_for, flash



meetings = [
    {'id': 1, 'title': 'Meeting 1', 'date': '2023-09-26', 'time': '10:00', 'Participants':'Person1-Person2'},
    {'id': 2, 'title': 'Meeting 2', 'date': '2023-09-27', 'time': '12:00', 'Participants':'Person1-Person2'},
]


@app.route('/')
def index():
    return render_template('index.html', meetings=meetings)

@app.route('/add_meeting', methods=['GET', 'POST'])
def add_meeting():
    if request.method == 'POST':
        new_meeting = {
            'id': len(meetings) + 1,
            'title': request.form['title'],
            'date': request.form['date'],
            'time': request.form['time'],
            'Participants':request.form['Participants']
        }
        meetings.append(new_meeting)
        flash('Meeting added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('add_meeting.html')

@app.route('/edit_meeting/<int:id>', methods=['GET', 'POST'])
def edit_meeting(id):
    meeting = next((m for m in meetings if m['id'] == id), None)
    if meeting is None:
        flash('Meeting not found!', 'danger')
        return redirect(url_for('index'))

    if request.method == 'POST':
        meeting['title'] = request.form['title']
        meeting['date'] = request.form['date']
        meeting['time'] = request.form['time']
        meeting['Participants'] = request.form['Participants']
        flash('Meeting updated successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('edit_meeting.html', meeting=meeting)

@app.route('/delete_meeting/<int:id>')
def delete_meeting(id):
    global meetings
    meetings = [m for m in meetings if m['id'] != id]
    flash('Meeting deleted successfully!', 'success')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

