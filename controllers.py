from flask import jsonify
from models import Activity, AdvancedActivity
from serializers import serialize_to_json, serialize_to_xml, serialize_to_soap

activities = []

class ActivityController:
    def get_activities(format='json'):
        if format == 'xml':
            return serialize_to_xml(activities)
        elif format == 'soap':
            return serialize_to_soap(activities)
        else:
            return jsonify(serialize_to_json(activities))

    def get_activity(id):
        activity = next((a for a in activities if a.id == id), None)
        if activity:
            return jsonify(activity.__dict__)
        return jsonify({'error': 'Activity not found'}), 404

    def create_activity(data):
        activity = Activity(len(activities) + 1, data['name'], data['duration_minutes'], data['activity_type'])
        activities.append(activity)
        return jsonify(activity.__dict__), 201

    def update_activity(id, data):
        activity = next((a for a in activities if a.id == id), None)
        if activity:
            activity.name = data['name']
            activity.duration_minutes = data['duration_minutes']
            activity.activity_type = data['activity_type']
            return jsonify(activity.__dict__)
        return jsonify({'error': 'Activity not found'}), 404

    def delete_activity(id):
        global activities
        activities = [a for a in activities if a.id != id]
        return '', 204

activity_controller = ActivityController()