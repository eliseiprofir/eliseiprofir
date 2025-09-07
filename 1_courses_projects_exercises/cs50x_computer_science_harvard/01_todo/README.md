# PROJECT TITLE: Minimalist to-do list
#### NAME: Elisei Profir
#### GITHUB USERNAME: proelisei
#### EDX USERNAME:    proelisei
#### CITY & COUNTRY: Brasov, Romania
#### RECORDING DATE: 25th of January 2024
#### Video Demo:  https://youtu.be/3U8sO6k5ZCY
#### Description:

# Minimalist To-Do List

## Overview

Welcome to the Minimalist To-Do List project! This simple web application allows users to manage their tasks in a minimalistic and user-friendly interface. The project is built using Flask, a lightweight Python web framework, and consists of three main files: `app.py`, `index.html`, and `style.css`.

## Files and Functionality

### 1. app.py

`app.py` is the heart of the project, containing the Flask application and server logic. Here's a breakdown of its functionalities:

- **Routes:**
  - `/`: The home route renders the main to-do list page, displaying existing tasks.
  - `/add`: This route handles the addition of new tasks via a form submission.
  - `/delete/<int:task_id>`: Allows users to delete tasks by clicking on the "Delete task" link next to each task.

- **Data Storage:**
  - `tasks`: A Python list used to store the user's tasks in memory.

- **Functions:**
  - `index()`: Renders the main page, passing the current tasks to the HTML template.
  - `add()`: Adds a new task to the `tasks` list when the user submits the form.
  - `delete(task_id)`: Deletes a task based on its index when the user clicks the "Delete task" link.

### 2. index.html

The `index.html` file contains the HTML structure for the main page. It utilizes Jinja templating to dynamically render tasks and handle form submissions. Key elements include:

- **Form:**
  - Allows users to input new tasks and submit them to the server.

- **Task List:**
  - Displays existing tasks in an unordered list (`<ul>`).
  - Utilizes Jinja templating to loop through tasks and display each task with a delete link.

### 3. style.css

The `style.css` file provides styling to enhance the user interface. Key styling decisions include:

- **Body and Header:**
  - Sets the background color and font for the entire page.
  - Centers the header text.

- **Form Styling:**
  - Adjusts the appearance of the form, ensuring it is visually appealing and responsive.

- **Task List Items:**
  - Defines the style for each task item, including background color, borders, and padding.

- **Delete Link:**
  - Defines the appearance of the "Delete task" link, with a confirmation prompt.

## Design Choices

### 1. UI and Styling

The project adopts a minimalist design to keep the interface clean and intuitive. The color scheme, font choices, and overall layout contribute to a visually pleasing user experience.

### 2. Code Structure

The code is structured to be modular, with separate files for server logic (`app.py`), HTML templates (`index.html`), and styles (`style.css`). This separation enhances maintainability and readability.

### 3. Confirmation Prompt

The decision to include a confirmation prompt when deleting a task aims to prevent accidental deletions. This user-friendly feature adds a layer of protection against unintentional data loss.

## Conclusion

The Minimalist To-Do List project offers a straightforward and efficient solution for task management. The README.md provides comprehensive documentation on the project's structure, functionality, and design choices.

# THANK YOU CS50
