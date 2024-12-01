from app import app, db, Flight
from datetime import datetime, timedelta

# Create sample flight data
def create_sample_flights():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()
        
        # Current time for reference
        now = datetime.utcnow()
        
        # Sample flights
        flights = [
            # Frankfurt - Istanbul routes
            Flight(
                flight_number='TK1957',
                departure='Frankfurt',
                arrival='Istanbul',
                departure_time=now + timedelta(hours=2),
                arrival_time=now + timedelta(hours=5),
                status='On Time'
            ),
            Flight(
                flight_number='LH1300',
                departure='Frankfurt',
                arrival='Istanbul',
                departure_time=now + timedelta(hours=4),
                arrival_time=now + timedelta(hours=7),
                status='Scheduled'
            ),
            
            # Munich - Antalya routes
            Flight(
                flight_number='TK1958',
                departure='Munich',
                arrival='Antalya',
                departure_time=now + timedelta(hours=1),
                arrival_time=now + timedelta(hours=4),
                status='On Time'
            ),
            Flight(
                flight_number='XQ123',
                departure='Munich',
                arrival='Antalya',
                departure_time=now + timedelta(hours=3),
                arrival_time=now + timedelta(hours=6),
                status='Delayed'
            ),
            
            # Berlin - Istanbul routes
            Flight(
                flight_number='TK1959',
                departure='Berlin',
                arrival='Istanbul',
                departure_time=now + timedelta(hours=2, minutes=30),
                arrival_time=now + timedelta(hours=5, minutes=30),
                status='On Time'
            ),
            Flight(
                flight_number='LH1302',
                departure='Berlin',
                arrival='Istanbul',
                departure_time=now + timedelta(hours=5),
                arrival_time=now + timedelta(hours=8),
                status='Scheduled'
            ),
            
            # Additional popular routes
            Flight(
                flight_number='TK1960',
                departure='Hamburg',
                arrival='Antalya',
                departure_time=now + timedelta(hours=3),
                arrival_time=now + timedelta(hours=6),
                status='On Time'
            ),
            Flight(
                flight_number='TK1961',
                departure='Düsseldorf',
                arrival='Istanbul',
                departure_time=now + timedelta(hours=4),
                arrival_time=now + timedelta(hours=7),
                status='Scheduled'
            ),
            Flight(
                flight_number='TK1962',
                departure='Stuttgart',
                arrival='Izmir',
                departure_time=now + timedelta(hours=2),
                arrival_time=now + timedelta(hours=5),
                status='On Time'
            ),
            Flight(
                flight_number='TK1963',
                departure='Cologne',
                arrival='Antalya',
                departure_time=now + timedelta(hours=1),
                arrival_time=now + timedelta(hours=4),
                status='Delayed'
            )
        ]
        
        # Add all flights to the database
        for flight in flights:
            db.session.add(flight)
        
        # Commit the changes
        db.session.commit()
        print("Sample flight data has been successfully added to the database!")

if __name__ == '__main__':
    create_sample_flights()