# To do list
A To-Do List application is a useful project that helps users manage and organize their tasks efficiently. This project aims to create a command-line or GUI-based application using Python, allowing users to create, update, and track their to-do lists

## Features for the To-Do List Application
#### * Create Tasks: Users can add new tasks to their to-do list.
#### View Tasks: Users can see all tasks in the list.
#### Update Tasks: Users can mark tasks as completed or update their descriptions.
#### Delete Tasks: Users can remove tasks that are no longer needed.
#### Save and Load Data: Tasks can be saved to a file, so they persist between sessions.
### 1. Command-Line Interface (CLI) To-Do List
The CLI version will be simple and allow users to manage their tasks via a terminal. Here’s an outline of how to build it:

Step 1: Plan the Task Structure
Each task will have the following attributes:
Task Description: A brief description of the task.
Status: Whether the task is "pending" or "completed".
You can store tasks as a list of dictionaries or a list of strings.

Step 2: Create Task Manager Class
Create a class to handle the task operations (add, view, update, delete).

Step 3: Create the User Interface (CLI)
Create a loop to interact with the user and process their commands.

### Features Implemented in the CLI:
#### View Tasks: Displays all tasks in the list.
#### Add Task: Prompts the user to enter a task and adds it.
#### Delete Task: Allows the user to remove a task by number.
#### Update Task: Prompts the user to update a task's description.
#### Mark Task Completed: Marks a task as completed (adding "(Completed)" to the task description).
#### Save and Load Tasks: Saves tasks to a file (tasks.txt) and loads them when the application starts.

### 2. Expanding to a Graphical User Interface (GUI)
If you'd like to turn this into a GUI-based application, you can use Tkinter, which is a built-in Python library for creating simple desktop applications.

### Features Implemented in the GUI:
Task List: Displays tasks in a list box.
Add Task: Allows users to enter a task and add it to the list.
Delete Task: Allows users to delete a selected task.
File I/O: Tasks are saved to and loaded from tasks.txt.

### Summary
CLI Version: Allows tasks to be created, updated, marked as completed, deleted, and saved to a file.
GUI Version: Adds a simple user interface for managing tasks using Tkinter.
With either version, the To-Do List application can help users stay organized and manage their tasks effectively.




