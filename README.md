# FlightTracker Pro - Modern Flight Tracking System

## Video Demo: https://youtu.be/yAL5FpeBl5Y?si=X1AQYWCX05ibnBxx

## Description
FlightTracker Pro is a modern web application for tracking flights and monitoring their status in real-time. Built with Flask and modern web technologies, it provides a user-friendly interface for tracking flight information, status updates, and detailed flight data.

This project was developed as a final project for CS50x, focusing on creating a professional and intuitive flight tracking system that helps users stay informed about flight statuses, departures, and arrivals.

## Features
- 🔍 Real-time flight tracking and searching
- ✈️ Detailed flight information display
- 🕒 Live status updates
- 🌓 Dark/Light mode support
- 📱 Responsive design for all devices
- 🖨️ Print-friendly flight details
- 🔄 Real-time data updates
- 🎨 Modern and intuitive UI

## Technologies Used
### Backend
- Flask (Python web framework)
- SQLAlchemy (ORM)
- SQLite (Database)
- Werkzeug
- Jinja2 (Template engine)

### Frontend
- HTML5/CSS3
- JavaScript (ES6+)
- Bootstrap 5
- Font Awesome Icons
- Custom CSS animations
- Responsive design principles

## Project Structure
```bash
flight_tracker/
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
├── templates/
│   ├── layout.html
│   ├── index.html
│   ├── flights.html
│   └── flight_detail.html
├── app.py
├── models.py
├── requirements.txt
└── README.md

Installation

1. Clone the repository:
git clone https://github.com/cilem612/flight-tracker.git
cd flight-tracker

2. Create a virtual environment: python -m venv venv

3. Activate virtual environment: venv\Scripts\activate

4. Install required packages: pip install -r requirements.txt

5. Initialize the database: ⁠python app.py

Visit http://127.0.0.1:5000 in your browser

Key Features Explained
Flight Search

Real-time search functionality
Search by flight number or city
Instant results with debounced API calls

Flight Details

Comprehensive flight information
Visual timeline of flight progress
Status indicators and updates
Service information
Cabin class details

User Interface

Intuitive navigation
Dark/Light mode toggle
Responsive design for all screen sizes
Animated transitions and effects
Print-friendly layouts

Technical Implementations
Database Structure

Flight model with comprehensive attributes
Real-time status tracking
Relationship preparation for future expansion
Automated timestamps for tracking

Frontend Features

Modern CSS with variables
Gradient designs
Smooth animations
Interactive elements
Responsive breakpoints
Dark mode implementation

Performance Optimizations

Debounced search queries
Optimized database queries
Efficient CSS animations
Responsive image handling

Future Improvements

User authentication system
Flight notifications
Mobile app development
Weather integration
Airline integration
Booking system integration

Dependencies
Flask==2.0.1
Flask-SQLAlchemy==2.5.1
SQLAlchemy==1.4.23
Werkzeug==2.0.1
Jinja2==3.0.1
itsdangerous==2.0.1
click==8.0.1
python-dotenv==0.19.0

Author

Created by: Cilem Erdinc
GitHub: cilem612
edX: cilemerdinc

License
This project is released under the MIT License.
Acknowledgments

Thanks to CS50 team for their educational support
Bootstrap team for their excellent UI framework
Font Awesome for the comprehensive icon set