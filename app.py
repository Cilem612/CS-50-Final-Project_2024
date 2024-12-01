from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import os

app = Flask("_name_")

# Database configuration
basedir = os.path.abspath(os.path.dirname("_file_"))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'flights.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Flight Model
class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flight_number = db.Column(db.String(20), nullable=False)
    departure = db.Column(db.String(100), nullable=False)
    arrival = db.Column(db.String(100), nullable=False)
    departure_time = db.Column(db.DateTime, nullable=False)
    arrival_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), default='On Time')

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/flights')
def flights():
    all_flights = Flight.query.all()
    return render_template('flights.html', flights=all_flights)

@app.route('/flight/<int:id>')
def flight_detail(id):
    flight = Flight.query.get_or_404(id)
    return render_template('flight_detail.html', flight=flight, now=datetime.utcnow())

@app.route('/search')
def search():
    query = request.args.get('q', '').strip()
    print(f"Search query: {query}")  # Debug print
    
    if not query:
        return jsonify([])

    # Search in all relevant fields
    flights = Flight.query.filter(
        db.or_(
            Flight.flight_number.ilike(f'%{query}%'),
            Flight.departure.ilike(f'%{query}%'),
            Flight.arrival.ilike(f'%{query}%')
        )
    ).all()
    
    print(f"Found {len(flights)} flights")  # Debug print
    
    results = []
    for flight in flights:
        results.append({
            'id': flight.id,
            'flight_number': flight.flight_number,
            'departure': flight.departure,
            'arrival': flight.arrival,
            'departure_time': flight.departure_time.strftime('%H:%M'),
            'arrival_time': flight.arrival_time.strftime('%H:%M'),
            'status': flight.status
        })
    
    return jsonify(results)

# Create sample data
def create_sample_flights():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()
        
        # Current time
        now = datetime.utcnow()
        
        # Sample flights
        flights = [
            Flight(
                flight_number='TK1957',
                departure='Frankfurt',
                arrival='Istanbul',
                departure_time=now + timedelta(hours=2),
                arrival_time=now + timedelta(hours=5),
                status='On Time'
            ),
            Flight(
                flight_number='TK1958',
                departure='Munich',
                arrival='Antalya',
                departure_time=now + timedelta(hours=1),
                arrival_time=now + timedelta(hours=4),
                status='On Time'
            ),
            Flight(
                flight_number='TK1959',
                departure='Berlin',
                arrival='Istanbul',
                departure_time=now + timedelta(hours=3),
                arrival_time=now + timedelta(hours=6),
                status='Scheduled'
            ),
            # Add more sample flights here
        ]
        
        for flight in flights:
            db.session.add(flight)
        
        db.session.commit()
        print("Sample data added successfully!")

if "_name_" == '_main_':
    # Create tables and add sample data if they don't exist
    with app.app_context():
        if not os.path.exists('flights.db'):
            create_sample_flights()
    
    app.run(debug=True)