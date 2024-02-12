from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary storage for tickets (in-memory)
tickets = []

@app.route('/')
def index():
    return render_template('index.html', tickets=tickets)

@app.route('/create', methods=['GET', 'POST'])
def create_ticket():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        status = 'Open'
        tickets.append({'title': title, 'description': description, 'status': status})
        return redirect(url_for('index'))
    return render_template('create_ticket.html')

@app.route('/update/<int:ticket_id>', methods=['GET', 'POST'])
def update_ticket(ticket_id):
    ticket = tickets[ticket_id]
    if request.method == 'POST':
        new_status = request.form['status']
        ticket['status'] = new_status
        return redirect(url_for('index'))
    return render_template('update_ticket.html', ticket=ticket)

if __name__ == '__main__':
    app.run(debug=True)
