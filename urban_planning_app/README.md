# Urban Planning Report Generator

This web application assists in urban plan development by utilizing Large Language Model (LLM) tools to compile planning documentation and reports based on various inputs.

## Project Structure

- `urban_planning_app/`: Root directory of the Flask application.
  - `app/`: Contains the core application logic.
    - `__init__.py`: Initializes the Flask application and blueprints.
    - `main.py`: Entry point to run the Flask development server.
    - `routes.py`: Defines application routes and request handlers.
    - `models.py`: (Placeholder) For data models if needed.
    - `services/`: For business logic, including LLM interactions.
      - `llm_service.py`: Contains placeholder functions for LLM tool integration and report compilation.
  - `templates/`: HTML templates for the web interface.
    - `index.html`: Main page with the input form and report display area.
  - `static/`: (Placeholder) For static files like CSS and JavaScript.
  - `tests/`: (Placeholder) For application tests.
  - `config.py`: (Placeholder) For application configuration.
  - `requirements.txt`: Lists Python dependencies for the project.
  - `README.md`: This file.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd urban_planning_app
    ```

2.  **Create a virtual environment:**
    It's recommended to use a virtual environment to manage project dependencies.
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    -   On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```
    -   On Windows:
        ```bash
        venv\Scripts\activate
        ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1.  **Ensure you are in the `urban_planning_app` directory** where `main.py` (inside the `app` folder) and `requirements.txt` are located.

2.  **Run the Flask development server:**
    ```bash
    python -m app.main
    ```

3.  **Open your web browser** and navigate to:
    [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

You should see the main page of the Urban Planning Report Generator. You can fill in the form fields and submit to see placeholder outputs.
