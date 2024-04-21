# Pokeberries API

This is a Flask-based API for Pokeberries statistics.

## Getting Started

To run this API, follow these steps:

1. Install Python (if you haven't already).

2. Install the required dependencies:

   ```sh
   pip install -r requirements.txt
   ```

   > You can first create a virtual environment to install the dependencies.

3. Run the Flask application:

   ```sh
   python app.py
   ```

4. Access the API at http://localhost:5000.

## Endpoints

- GET "/": The index endpoint with a welcome message.

- GET "/allBerryStats": Returns Pokeberry object class info from all the berries.

## Technologies Used

- Flask
- Python
