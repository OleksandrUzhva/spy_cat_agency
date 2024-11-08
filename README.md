# Spy Cat Agency Management System

## Project Overview

The Spy Cat Agency (SCA) Management System is designed to help manage spy cats, missions, and targets efficiently. The application allows SCA to handle the hiring, mission assignments, and target tracking for their spy cats. Key functionalities include creating missions with specific targets, assigning missions to cats, tracking notes on targets, and validating the breed of each cat using TheCatAPI.

## Features

- **Spy Cat Management**:
  - Add, update, and remove spy cats, with details including name, years of experience, breed (validated via TheCatAPI), and salary.
  - List all cats or view individual cat details.

- **Mission Management**:
  - Create missions with targets in one request.
  - Assign missions to cats and manage mission status.
  - Mark targets as complete, freeze notes once complete, and track mission progress.

- **Target Management**:
  - Add and update notes on targets.
  - Mark targets as complete and restrict further updates on completed targets.

## Technology Stack

- **Backend Framework**: Django, Django REST Framework
- **Database**: SQLite
- **API for Breed Validation**: [TheCatAPI](https://thecatapi.com)
- **Testing and Documentation**: Postman

### 1. Clone the Repository

```bash
git clone https://github.com/OleksandrUzhva/spy_cat_agency
cd spy-cat-agency

    2. Install Dependencies

```bash
pip install -r requirements.txt

    3. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate

    4. Start the Development Server

```bash
python manage.py runserver


API Endpoints
The API is accessible at http://localhost:8000/api/. Here are the main endpoints:

Spy Cats
GET /api/cats/ – List all spy cats.
POST /api/cats/ – Add a new spy cat.
GET /api/cats/{id}/ – Retrieve details of a specific cat.
PUT /api/cats/{id}/ – Update specific fields of a cat (e.g., salary).
DELETE /api/cats/{id}/ – Remove a spy cat.
Missions
GET /api/missions/ – List all missions.
POST /api/missions/ – Create a new mission with associated targets.
GET /api/missions/{id}/ – Retrieve details of a specific mission.
PUT /api/missions/{id}/ – Update mission status or target information.
DELETE /api/missions/{id}/ – Delete a mission (if not assigned to a cat).
Target Notes
PUT /api/missions/{mission_id}/targets/{target_id}/notes – Update notes on a target (restricted if target is completed).
