import requests
import json
from datetime import datetime, timedelta

access_token = "ZmZlZTI4MDYtYjg4MS00ZGNkLTg0OTAtYjNhMDk0ZDkxOGI1ZjFlMGNiNjMtMjQw_P0A1_5462e211-b9d5-4e48-af15-7e685ad359c2"

# Function to get all recordings
def get_recordings(host_email=None, days=30, max_recordings=100):
   
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
    # Set parameters
    params = {
        'from': (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%dT%H:%M:%SZ"),
        'max': max_recordings
    }
    
    # Add host email if provided
    if host_email:
        params['hostEmail'] = host_email
    
    # https://developer.webex.com/docs/api/v1/recordings/list-recordings
    response = requests.get('https://webexapis.com/v1/recordings', headers=headers, params=params)
    
    if response.status_code != 200:
        print(f"Error fetching recordings: {response.status_code}")
        print(response.text)
        return None
        
    recordings = response.json()
    return recordings

# Function to get details of a specific recording
def get_recording_details(recording_id, host_email=None):
   
    headers = {
        'Authorization': f'Bearer {access_token}',
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
def get_transcription(recording_id):
   
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
    # Note: This endpoint may vary based on Webex documentation
    # Check the latest API documentation for the exact endpoint
    response = requests.get(f'https://webexapis.com/v1/recordings/{recording_id}/transcription', headers=headers)
    
    if response.status_code != 200:
        print(f"Error fetching transcription: {response.status_code}")
        print(response.text)
        return None
        
    transcription = response.json()
    return transcription

# Function to get summary of a recording
def get_summary(recording_id):

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
    # Note: This endpoint may vary based on Webex documentation
    # Check the latest API documentation for the exact endpoint
    response = requests.get(f'https://webexapis.com/v1/recordings/{recording_id}/summary', headers=headers)
    
    if response.status_code != 200:
        print(f"Error fetching summary: {response.status_code}")
        print(response.text)
        return None
        
    summary = response.json()
    return summary

# Function to process and display all data for a recording
def process_recording(recording_id, host_email=None):
  
    # Get recording details
    details = get_recording_details(recording_id, host_email)
    if not details:
        print(f"Could not get details for recording {recording_id}")
        return
    
    # Get transcription
    transcription = get_transcription(recording_id)
    
    # Get summary
    summary = get_summary(recording_id)
    
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
    
    if transcription and 'transcript' in transcription:
        print("\nTRANSCRIPT EXCERPT:")
        transcript_entries = transcription.get('transcript', [])
        for entry in transcript_entries[:5]:  # Show first 5 entries
            print(f"[{entry.get('time')}] {entry.get('speaker')}: {entry.get('text')}")
        
        if len(transcript_entries) > 5:
            print("... (transcript continues)")
    
    print("\n" + "="*50 + "\n")

# Function to save recording data to file
def save_recording_data(recording_id, file_prefix="recording_data", host_email=None):
 
    # Get recording details
    details = get_recording_details(recording_id, host_email)
    if not details:
        print(f"Could not get details for recording {recording_id}")
        return
    
    # Save details
    with open(f"{file_prefix}_{recording_id}_details.json", 'w') as f:
        json.dump(details, f, indent=2)
    
    # Get and save transcription
    transcription = get_transcription(recording_id)
    if transcription:
        with open(f"{file_prefix}_{recording_id}_transcript.json", 'w') as f:
            json.dump(transcription, f, indent=2)
    
    # Get and save summary
    summary = get_summary(recording_id)
    if summary:
        with open(f"{file_prefix}_{recording_id}_summary.json", 'w') as f:
            json.dump(summary, f, indent=2)
    
    print(f"Saved data for recording {recording_id}")

# Main function
def main():
    # Get user input for email
    user_email = input("Enter your Webex email (leave blank to skip): ").strip()
    
    # Get time range
    try:
        days_back = int(input("Enter number of days to look back (default 30): ") or 30)
    except ValueError:
        days_back = 30
        print("Invalid input, using default of 30 days")
    
    # Get recordings
    print(f"\nRetrieving recordings for the past {days_back} days...")
    
    if user_email:
        recordings = get_recordings(host_email=user_email, days=days_back)
    else:
        recordings = get_recordings(days=days_back)
    
    if not recordings or "items" not in recordings:
        print("No recordings found or error in retrieving recordings")
        return
    
    # Display basic info about all recordings
    items = recordings.get('items', [])
    if not items:
        print("No recordings found in the specified time range")
        return
    
    print(f"\nFound {len(items)} recordings")
    print("\nALL RECORDINGS:")
    print("-" * 100)
    print(f"{'#':<5} {'ID':<20} {'Topic':<40} {'Date':<25} {'Duration':<10}")
    print("-" * 100)
    
    for idx, recording in enumerate(items, 1):
        duration_mins = recording.get('duration', 0) // 60
        print(f"{idx:<5} {recording.get('id'):<20} {recording.get('topic'):<40} {recording.get('createTime'):<25} {duration_mins} min")
    
    print("\n")
    
    # Ask user what to do next
    print("What would you like to do?")
    print("1. View details of a specific recording")
    print("2. Download data for a specific recording")
    print("3. Process all recordings")
    print("4. Exit")
    
    choice = input("\nEnter your choice (1-4): ").strip()
    
    if choice == '1':
        # View a specific recording
        try:
            index = int(input("Enter recording number from the list: ")) - 1
            if 0 <= index < len(items):
                recording_id = items[index].get('id')
                process_recording(recording_id, user_email)
            else:
                print("Invalid recording number")
        except ValueError:
            print("Invalid input")
    
    elif choice == '2':
        # Download data for a specific recording
        try:
            index = int(input("Enter recording number from the list: ")) - 1
            if 0 <= index < len(items):
                recording_id = items[index].get('id')
                save_recording_data(recording_id, host_email=user_email)
            else:
                print("Invalid recording number")
        except ValueError:
            print("Invalid input")
    
    elif choice == '3':
        # Process all recordings
        for recording in items:
            process_recording(recording.get('id'), user_email)
    
    else:
        print("Exiting program")

if __name__ == "__main__":
    main()

