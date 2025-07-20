from reconops_dashboard import db, create_app

# Initialize the Flask app context
app = create_app()

with app.app_context():
    db.create_all()
    print("✅ Database initialized and all tables created!")
