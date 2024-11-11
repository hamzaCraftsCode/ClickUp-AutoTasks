# Import necessary libraries
import requests

# Ensure the API_TOKEN and BASE_URL are set
API_TOKEN = "YOUR_API_TOKEN"
BASE_URL = "https://api.clickup.com/api/v2"

def get_spaces(team_id):
    """
    Get all spaces within a specific team.
    """
    url = f"{BASE_URL}/team/{team_id}/space"
    headers = {
        "Authorization": API_TOKEN
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        spaces = response.json().get("spaces", [])
        return {space["name"]: space["id"] for space in spaces}
    except requests.exceptions.RequestException as e:
        print(f"Failed to get spaces: {e}")
        return {}

def create_folder(space_id, folder_name):
    """
    Create a new folder in a specific space.
    """
    url = f"{BASE_URL}/space/{space_id}/folder"
    headers = {
        "Authorization": API_TOKEN,
        "Content-Type": "application/json"
    }
    payload = {
        "name": folder_name
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        created_folder = response.json()
        print(f"Folder '{folder_name}' created with ID: {created_folder['id']}")
        return created_folder
    except requests.exceptions.RequestException as e:
        print(f"Failed to create folder '{folder_name}': {e}")
        return None

def create_list(folder_id, list_name="test_list_api"):
    """
    Create a new list in a specific folder.
    """
    url = f"{BASE_URL}/folder/{folder_id}/list"
    headers = {
        "Authorization": API_TOKEN,
        "Content-Type": "application/json"
    }
    payload = {
        "name": list_name
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        created_list = response.json()
        print(f"List '{list_name}' created in folder '{folder_id}' with ID: {created_list['id']}")
        return created_list
    except requests.exceptions.RequestException as e:
        print(f"Failed to create list '{list_name}' in folder '{folder_id}': {e}")
        return None

def create_task(list_id, task_name="test_task_api"):
    """
    Create a new task in a specific list.
    """
    url = f"{BASE_URL}/list/{list_id}/task"
    headers = {
        "Authorization": API_TOKEN,
        "Content-Type": "application/json"
    }
    payload = {
        "name": task_name
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        created_task = response.json()
        print(f"Task '{task_name}' created in list '{list_id}' with ID: {created_task['id']}")
        return created_task
    except requests.exceptions.RequestException as e:
        print(f"Failed to create task '{task_name}' in list '{list_id}': {e}")
        return None

def main():
    # Define the team ID to fetch spaces from
    TEAM_ID = "YOUR_TEAM_ID"  # Replace with your actual team ID
    
    # Fetch all spaces within the team and populate SPACE_IDS
    global SPACE_IDS
    SPACE_IDS = get_spaces(TEAM_ID)
    print("Fetched spaces:", SPACE_IDS)

    # Folder names to create
    folder_names = [
        "Kanban: 11 Nov - 22 Nov",
        "Scrum: 11 Nov - 22 Nov"
    ]

    # Process each space in SPACE_IDS
    for space_name, space_id in SPACE_IDS.items():
        print(f"\nProcessing space: {space_name} (ID: {space_id})")
        
        # Create each folder, list, and task within the current space
        created_folders = []
        for folder_name in folder_names:
            # Create the folder
            folder = create_folder(space_id, folder_name)
            if folder:
                created_folders.append(folder)
                # Create a list within the created folder
                created_list = create_list(folder["id"])
                if created_list:
                    # Create a task within the created list
                    create_task(created_list["id"])

        # Display the created folders, lists, and tasks
        for folder in created_folders:
            print(f"Folder Name: {folder['name']}, Folder ID: {folder['id']}")

# Run the main function
if __name__ == "__main__":
    main()
