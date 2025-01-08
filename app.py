from flask import Flask, render_template, request, redirect, url_for, flash
from models.models import Database

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Initialize the database
db = Database()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/rooms')
def rooms():
    rooms = db.get_all_rooms()
    return render_template('rooms.html', rooms=rooms)

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        customer_name = request.form['name']
        room_id = request.form['room_id']
        days = int(request.form['days'])
        if db.book_room(customer_name, room_id, days):
            flash("Room booked successfully!", "success")
            return redirect(url_for('rooms'))
        else:
            flash("Booking failed. Room might be unavailable.", "danger")
    return render_template('booking.html', rooms=db.get_available_rooms())

@app.route('/admin')
def admin():
    bookings = db.get_all_bookings()
    return render_template('admin.html', bookings=bookings)

@app.route('/invoice/<int:booking_id>')
def invoice(booking_id):
    invoice = db.get_invoice(booking_id)
    return render_template('invoice.html', invoice=invoice)

if __name__ == '__main__':
    app.run(debug=True)
