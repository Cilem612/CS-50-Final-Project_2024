from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event

db = SQLAlchemy()

class Flight(db.Model):
    """Flight Model for storing flight related details"""
    __tablename__ = 'flights'

    id = db.Column(db.Integer, primary_key=True)
    flight_number = db.Column(db.String(20), unique=True, nullable=False, index=True)
    departure = db.Column(db.String(100), nullable=False)
    arrival = db.Column(db.String(100), nullable=False)
    departure_time = db.Column(db.DateTime, nullable=False)
    arrival_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), default='Scheduled')
    aircraft_type = db.Column(db.String(50))
    airline = db.Column(db.String(100))
    gate = db.Column(db.String(10))
    terminal = db.Column(db.String(10))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships (for future expansion)
    # airline_id = db.Column(db.Integer, db.ForeignKey('airlines.id'))
    # airline = db.relationship('Airline', backref='flights')

    def __init__(self, flight_number, departure, arrival, departure_time, arrival_time, 
                 status='Scheduled', aircraft_type=None, airline=None, gate=None, terminal=None):
        self.flight_number = flight_number
        self.departure = departure
        self.arrival = arrival
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.status = status
        self.aircraft_type = aircraft_type
        self.airline = airline
        self.gate = gate
        self.terminal = terminal

    def to_dict(self):
        """Convert flight object to dictionary"""
        return {
            'id': self.id,
            'flight_number': self.flight_number,
            'departure': self.departure,
            'arrival': self.arrival,
            'departure_time': self.departure_time.strftime('%Y-%m-%d %H:%M:%S'),
            'arrival_time': self.arrival_time.strftime('%Y-%m-%d %H:%M:%S'),
            'status': self.status,
            'aircraft_type': self.aircraft_type,
            'airline': self.airline,
            'gate': self.gate,
            'terminal': self.terminal
        }

    @property
    def duration(self):
        """Calculate flight duration"""
        if self.departure_time and self.arrival_time:
            duration = self.arrival_time - self.departure_time
            hours = duration.total_seconds() / 3600
            return round(hours, 1)
        return None

    @property
    def is_delayed(self):
        """Check if flight is delayed"""
        return self.status.lower() == 'delayed'

    @property
    def progress(self):
        """Calculate flight progress percentage"""
        now = datetime.utcnow()
        if now < self.departure_time:
            return 0
        elif now > self.arrival_time:
            return 100
        
        total_duration = (self.arrival_time - self.departure_time).total_seconds()
        elapsed = (now - self.departure_time).total_seconds()
        progress = (elapsed / total_duration) * 100
        return min(round(progress, 1), 100)

# Event listeners for model
@event.listens_for(Flight, 'before_insert')
def set_created_at(mapper, connection, target):
    target.created_at = datetime.utcnow()
    target.updated_at = datetime.utcnow()

@event.listens_for(Flight, 'before_update')
def set_updated_at(mapper, connection, target):
    target.updated_at = datetime.utcnow()

# For future expansion, you might want to add more models:

"""
class Airline(db.Model):
    __tablename__ = 'airlines'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(3), unique=True, nullable=False)
    country = db.Column(db.String(100))
    flights = db.relationship('Flight', backref='airline_info')

class Airport(db.Model):
    __tablename__ = 'airports'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(3), unique=True, nullable=False)
    city = db.Column(db.String(100))
    country = db.Column(db.String(100))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
"""