def get_response(session_json: dict):
    session_json["session_messages"].append({
        "message_id": len(session_json['session_messages']),
        "message_sender": "robot",
        "message_time": "",
        "message_text": "ζδΈιε"
    })
    return session_json