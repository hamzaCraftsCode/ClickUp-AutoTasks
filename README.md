# ClickUp-AutoTasks#

Automate folder, list, and task creation in ClickUp spaces with ease. This script interacts with the ClickUp API to help teams quickly set up their project structures with predefined folders, lists, and tasks.

## Features

- Fetches all spaces within a specified ClickUp team.
- Creates folders, lists, and tasks in each space automatically.
- Customizable folder names, list names, and task names.
- Error handling and timeout settings for stable API interactions.

## Prerequisites

- Python 3.x
- `requests` library for handling HTTP requests

## Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/ClickUp-Automator.git
   cd ClickUp-Automator

## Get ClickUp API Token
- Obtain your ClickUp API token from your ClickUp profile
- Replace the **API_TOKEN** variable in the script with your token.

## Find Your Team ID
- You can find your team ID in the ClickUp URL. Just hit the ClickUp icon on top left. You will see a number in the URL. That number is your team ID.
- Replace the TEAM_ID variable in the script with your team ID.

## Usage
- Update the script with your **TEAM_ID** and **API_TOKEN**.
- Run the script:
- ```bash
  python clickup_automation.py

## Script Objective
The script will:
- Fetch all spaces in the specified team.
- Create customiseable folders, lists, and tasks in each space.

## Code Overview
### Main Functions
- `get_spaces(team_id)`: Fetches all spaces for the given team ID and returns a dictionary of space names and IDs.
- `create_folder(space_id, folder_name)`: Creates a folder in the specified space.
- `create_list(folder_id, list_name="test_list_api")`: Creates a list within the specified folder.
- `create_task(list_id, task_name="test_task_api")`: Creates a task within the specified list.

### Customization
- Modify `folder_names` in the `main()` function to specify which folders you want to create in each space.
- Adjust the default list and task names in the `create_list` and `create_task` functions, if desired.

## Example Output
After running the script, the output will display:
- The names and IDs of the created folders, lists, and tasks for verification.
  ```bash
  Processing space: Data Tram (ID: 90090412347)
  Folder 'Kanban: 11 Nov - 22 Nov' created with ID: 123456789
  List 'test_list_api' created in folder '123456789' with ID: 987654321
  Task 'test_task_api' created in list '987654321' with ID: 555555555

## Notes
- Make sure your ClickUp account has the necessary permissions to create folders, lists, and tasks in the specified spaces.
- The script includes timeout settings to avoid hanging indefinitely if the API is unresponsive.
