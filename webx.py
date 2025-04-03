import requests
import json
from datetime import datetime, timedelta

acess_token = "ZmZlZTI4MDYtYjg4MS00ZGNkLTg0OTAtYjNhMDk0ZDkxOGI1ZjFlMGNiNjMtMjQw_P0A1_5462e211-b9d5-4e48-af15-7e685ad359c2"

# Function to get all recordings
def getCallsData(use_test_data=True):
    if use_test_data:
        return get_test_recordings()
    
    headers = {
        'Authorization': f'Bearer {acess_token}',
        'Content-Type': 'application/json'
    }
    
    # Set parameters - you can adjust these as needed
    params = {
        'hostEmail': 'user@example.com',
        'from': (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%dT%H:%M:%SZ"),  # last 30 days
        'max': 100  # maximum number of recordings to retrieve
    }
    
    # https://developer.webex.com/docs/api/v1/recordings/list-recordings
    response = requests.get('https://webexapis.com/v1/recordings', headers=headers, params=params)
    
    if response.status_code != 200:
        print(f"Error fetching recordings: {response.status_code}")
        print(response.text)
        return None
        
    recordings = response.json()
    return recordings

# Function to get details of a specific recording
def getRecordingDetails(recording_id, host_email=None, use_test_data=True):
    if use_test_data:
        return get_test_recording_details(recording_id)
    
    headers = {
        'Authorization': f'Bearer {acess_token}',
        'Content-Type': 'application/json'
    }
    
    params = {}
    if host_email:
        params['hostEmail'] = host_email
    
    # https://developer.webex.com/docs/api/v1/recordings/get-recording-details
    response = requests.get(f'https://webexapis.com/v1/recordings/{recording_id}', headers=headers, params=params)
    
    if response.status_code != 200:
        print(f"Error fetching recording details: {response.status_code}")
        print(response.text)
        return None
        
    details = response.json()
    return details

# Function to get transcription of a recording
def getTranscription(recording_id, use_test_data=True):
    if use_test_data:
        return get_test_transcription(recording_id)
    
    headers = {
        'Authorization': f'Bearer {acess_token}',
        'Content-Type': 'application/json'
    }
    
    # Note: This endpoint may vary based on Webex documentation
    response = requests.get(f'https://webexapis.com/v1/recordings/{recording_id}/transcription', headers=headers)
    
    if response.status_code != 200:
        print(f"Error fetching transcription: {response.status_code}")
        print(response.text)
        return None
        
    transcription = response.json()
    return transcription

# Function to get summary of a recording
def getSummary(recording_id, use_test_data=True):
    if use_test_data:
        return get_test_summary(recording_id)
    
    headers = {
        'Authorization': f'Bearer {acess_token}',
        'Content-Type': 'application/json'
    }
    
    # Note: This endpoint may vary based on Webex documentation
    response = requests.get(f'https://webexapis.com/v1/recordings/{recording_id}/summary', headers=headers)
    
    if response.status_code != 200:
        print(f"Error fetching summary: {response.status_code}")
        print(response.text)
        return None
        
    summary = response.json()
    return summary

# Test data functions
def get_test_recordings():
    return {
        "items": [
            {
                "id": "recording_id_1",
                "meetingId": "meeting_id_1",
                "topic": "Weekly Team Meeting",
                "createTime": "2023-11-01T14:00:00Z",
                "hostEmail": "user@example.com",
                "siteUrl": "example.webex.com",
                "size": 256000000,
                "format": "MP4",
                "duration": 3600,
                "timeRecorded": "2023-11-01T14:00:00Z",
                "shareToMe": False
            },
            {
                "id": "recording_id_2",
                "meetingId": "meeting_id_2",
                "topic": "Project Planning Session",
                "createTime": "2023-11-05T10:00:00Z",
                "hostEmail": "user@example.com",
                "siteUrl": "example.webex.com",
                "size": 156000000,
                "format": "MP4",
                "duration": 1800,
                "timeRecorded": "2023-11-05T10:00:00Z",
                "shareToMe": False
            },
            {
                "id": "recording_id_3",
                "meetingId": "meeting_id_3",
                "topic": "Client Presentation",
                "createTime": "2023-11-10T15:30:00Z",
                "hostEmail": "user@example.com",
                "siteUrl": "example.webex.com",
                "size": 320000000,
                "format": "MP4",
                "duration": 4500,
                "timeRecorded": "2023-11-10T15:30:00Z",
                "shareToMe": False
            }
        ]
    }

def get_test_recording_details(recording_id):
    recordings = {
        "recording_id_1": {
            "id": "recording_id_1",
            "meetingId": "meeting_id_1",
            "topic": "Weekly Team Meeting",
            "createTime": "2023-11-01T14:00:00Z",
            "hostEmail": "user@example.com",
            "siteUrl": "example.webex.com",
            "size": 256000000,
            "format": "MP4",
            "duration": 3600,
            "timeRecorded": "2023-11-01T14:00:00Z",
            "shareToMe": False,
            "downloadUrl": "https://example.webex.com/recording/download/recording_id_1",
            "password": "",
            "playbackUrl": "https://example.webex.com/recording/play/recording_id_1",
            "participants": [
                {"email": "user1@example.com", "name": "User One"},
                {"email": "user2@example.com", "name": "User Two"},
                {"email": "user3@example.com", "name": "User Three"}
            ]
        },
        "recording_id_2": {
            "id": "recording_id_2",
            "meetingId": "meeting_id_2",
            "topic": "Project Planning Session",
            "createTime": "2023-11-05T10:00:00Z",
            "hostEmail": "user@example.com",
            "siteUrl": "example.webex.com",
            "size": 156000000,
            "format": "MP4",
            "duration": 1800,
            "timeRecorded": "2023-11-05T10:00:00Z",
            "shareToMe": False,
            "downloadUrl": "https://example.webex.com/recording/download/recording_id_2",
            "password": "",
            "playbackUrl": "https://example.webex.com/recording/play/recording_id_2",
            "participants": [
                {"email": "user1@example.com", "name": "User One"},
                {"email": "user4@example.com", "name": "User Four"}
            ]
        },
        "recording_id_3": {
            "id": "recording_id_3",
            "meetingId": "meeting_id_3",
            "topic": "Client Presentation",
            "createTime": "2023-11-10T15:30:00Z",
            "hostEmail": "user@example.com",
            "siteUrl": "example.webex.com",
            "size": 320000000,
            "format": "MP4",
            "duration": 4500,
            "timeRecorded": "2023-11-10T15:30:00Z",
            "shareToMe": False,
            "downloadUrl": "https://example.webex.com/recording/download/recording_id_3",
            "password": "",
            "playbackUrl": "https://example.webex.com/recording/play/recording_id_3",
            "participants": [
                {"email": "user1@example.com", "name": "User One"},
                {"email": "user2@example.com", "name": "User Two"},
                {"email": "client@example.com", "name": "Client"}
            ]
        }
    }
    
    return recordings.get(recording_id, {"error": "Recording not found"})

def get_test_transcription(recording_id):
    transcriptions = {
        "recording_id_1": {
            "id": "recording_id_1",
            "transcript": [
                {"speaker": "User One", "time": "00:00:05", "text": "Welcome everyone to our weekly team meeting."},
                {"speaker": "User Two", "time": "00:00:12", "text": "Thanks for organizing this. I have a few updates to share."},
                {"speaker": "User Three", "time": "00:00:20", "text": "I've completed the task assigned to me last week."},
                {"speaker": "User One", "time": "00:00:30", "text": "Great progress! Let's discuss the roadmap for next month."}
            ]
        },
        "recording_id_2": {
            "id": "recording_id_2",
            "transcript": [
                {"speaker": "User One", "time": "00:00:03", "text": "Let's plan out the next phase of our project."},
                {"speaker": "User Four", "time": "00:00:10", "text": "I think we should focus on the user interface first."},
                {"speaker": "User One", "time": "00:00:18", "text": "Good idea. We can start with wireframes next week."}
            ]
        },
        "recording_id_3": {
            "id": "recording_id_3",
            "transcript": [
                {"speaker": "User One", "time": "00:00:08", "text": "Thank you for joining our presentation today."},
                {"speaker": "User Two", "time": "00:00:15", "text": "We've prepared a detailed overview of our solution."},
                {"speaker": "Client", "time": "00:00:25", "text": "I'm looking forward to seeing what you've developed."},
                {"speaker": "User One", "time": "00:00:32", "text": "Let's start with the problem statement and then move to our approach."}
            ]
        }
    }
    
    return transcriptions.get(recording_id, {"error": "Transcription not found"})

def get_test_summary(recording_id):
    summaries = {
        "recording_id_1": {
            "id": "recording_id_1",
            "summary": "In this weekly team meeting, the team discussed progress on current projects, shared updates on completed tasks, and planned the roadmap for the upcoming month. Action items were assigned to team members with deadlines for completion.",
            "key_points": [
                "Project A is on track for delivery next week",
                "Team needs to address the bug in the login module",
                "New feature request from marketing team to be evaluated",
                "Budget approval for new tools pending from management"
            ],
            "action_items": [
                {"assignee": "User Two", "action": "Fix login module bug", "deadline": "2023-11-08"},
                {"assignee": "User Three", "action": "Prepare feature evaluation report", "deadline": "2023-11-10"}
            ]
        },
        "recording_id_2": {
            "id": "recording_id_2",
            "summary": "This project planning session focused on determining the next steps for the product development. The team decided to prioritize the user interface improvements based on recent user feedback. A timeline was established for wireframe creation and initial prototyping.",
            "key_points": [
                "User interface needs improvements based on feedback",
                "Wireframes to be created by next week",
                "Performance issues to be addressed in parallel",
                "Testing phase scheduled for late November"
            ],
            "action_items": [
                {"assignee": "User One", "action": "Create wireframes", "deadline": "2023-11-12"},
                {"assignee": "User Four", "action": "Set up testing environment", "deadline": "2023-11-15"}
            ]
        },
        "recording_id_3": {
            "id": "recording_id_3",
            "summary": "The client presentation covered the proposed solution for their business needs. The team presented the problem statement, their approach to solving it, and a demo of the current prototype. The client expressed satisfaction with the progress and provided feedback on specific features they would like to see enhanced.",
            "key_points": [
                "Client is satisfied with the overall approach",
                "Enhanced reporting features requested by client",
                "Timeline for delivery confirmed for Q1 2024",
                "Follow-up meeting scheduled for next month"
            ],
            "action_items": [
                {"assignee": "User Two", "action": "Enhance reporting features", "deadline": "2023-12-01"},
                {"assignee": "User One", "action": "Prepare detailed timeline", "deadline": "2023-11-20"},
                {"assignee": "Client", "action": "Provide access to test data", "deadline": "2023-11-15"}
            ]
        }
    }
    
    return summaries.get(recording_id, {"error": "Summary not found"})

# Function to process and display all data for a recording
def process_recording(recording_id, use_test_data=True):
    # Get recording details
    details = getRecordingDetails(recording_id, use_test_data=use_test_data)
    if not details or "error" in details:
        print(f"Could not get details for recording {recording_id}")
        return
    
    # Get transcription
    transcription = getTranscription(recording_id, use_test_data=use_test_data)
    if not transcription or "error" in transcription:
        print(f"Could not get transcription for recording {recording_id}")
    
    # Get summary
    summary = getSummary(recording_id, use_test_data=use_test_data)
    if not summary or "error" in summary:
        print(f"Could not get summary for recording {recording_id}")
    
    # Display all information
    print("\n" + "="*50)
    print(f"RECORDING: {details.get('topic', 'Unknown')}")
    print("="*50)
    
    print("\nRECORDING DETAILS:")
    print(f"ID: {details.get('id')}")
    print(f"Meeting ID: {details.get('meetingId')}")
    print(f"Date: {details.get('createTime')}")
    print(f"Duration: {details.get('duration')} seconds")
    print(f"Host: {details.get('hostEmail')}")
    
    if details.get('participants'):
        print("\nPARTICIPANTS:")
        for participant in details.get('participants', []):
            print(f"- {participant.get('name')} ({participant.get('email')})")
    
    if summary:
        print("\nSUMMARY:")
        print(summary.get('summary', 'No summary available'))
        
        if summary.get('key_points'):
            print("\nKEY POINTS:")
            for point in summary.get('key_points', []):
                print(f"- {point}")
        
        if summary.get('action_items'):
            print("\nACTION ITEMS:")
            for item in summary.get('action_items', []):
                print(f"- {item.get('assignee')}: {item.get('action')} (Due: {item.get('deadline')})")
    
    if transcription:
        print("\nTRANSCRIPT EXCERPT:")
        for entry in transcription.get('transcript', [])[:5]:  # Show first 5 entries
            print(f"[{entry.get('time')}] {entry.get('speaker')}: {entry.get('text')}")
        
        if len(transcription.get('transcript', [])) > 5:
            print("... (transcript continues)")
    
    print("\n" + "="*50 + "\n")

# Main function
def main():
    # Get all recordings
    recordings = getCallsData(use_test_data=True)
    
    if not recordings or "items" not in recordings:
        print("No recordings found or error in retrieving recordings")
        return
    
    # Display basic info about all recordings
    print("\nALL RECORDINGS:")
    print("-" * 100)
    print(f"{'ID':<20} {'Topic':<40} {'Date':<25} {'Duration':<15}")
    print("-" * 100)
    
    for recording in recordings.get('items', []):
        duration_mins = recording.get('duration', 0) // 60
        print(f"{recording.get('id'):<20} {recording.get('topic'):<40} {recording.get('createTime'):<25} {duration_mins} minutes")
    
    print("\n")
    
    # Process each recording in detail
    for recording in recordings.get('items', []):
        process_recording(recording.get('id'), use_test_data=True)

# This block runs when the script is executed directly
if __name__ == "__main__":
    main()

