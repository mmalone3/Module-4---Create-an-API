from flask import request, jsonify
from models import Activity  # Assuming you have an Activity model
from app import db  # Assuming you're using SQLAlchemy for ORM

def add_activity():
    """
    Adds a new activity to the database.
    
    :return: A JSON response with the newly added activity details or an error message.
    """
    try:
        # Get the JSON payload from the POST request
        data = request.json
        
        # Validate input data
        if not all(key in data for key in ['name', 'start_time', 'end_time', 'duration']):
            return jsonify({"error": "Missing required fields"}), 400
        
        # Create a new Activity instance
        new_activity = Activity(
            name=data['name'],
            start_time=data['start_time'],
            end_time=data['end_time'],
            duration=data['duration']
        )
        
        # Add the new activity to the session
        db.session.add(new_activity)
        
        # Commit the transaction
        db.session.commit()
        
        # Return the newly added activity
        return jsonify({
            "message": "Activity added successfully",
            "activity_id": new_activity.id,
            "name": new_activity.name,
            "start_time": new_activity.start_time,
            "end_time": new_activity.end_time,
            "duration": new_activity.duration
        }), 201
    
    except Exception as e:
        # Roll back the transaction if there's an error
        db.session.rollback()
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500