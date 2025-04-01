## Event Management System
<p>This is a robust, RESTful backend for an event management system built with Django and Django REST Framework (DRF), containerized using Docker. This API provides endpoints to manage events and categories, designed for integration with any frontend framework</p>

## Features
* Event CRUD: Create, read, update, and delete events with details like name, category, dates, priority, and location.
* Category Management: Full CRUD operations for event categories.
* RESTful API: Exposes endpoints for seamless frontend integration.
* Database: Powered by PostgreSQL for reliable storage.
* Containerization: Dockerized for easy deployment and scalability.

## Tech Stack
* Backend: Django, Django REST Framework
* Database: PostgreSQL
* Containerization: Docker, Docker Compose
* Python Version: 3.10.12

## Prerequisites
* Docker and Docker Compose installed
* Python 3.10+ (for local development outside Docker)
* PostgreSQL (if running locally without Docker)

## Setup and Installation
Using Docker: </Br>
1. CLone the Repo:</br>
`https://github.com/alexander784/Events.git`</br>
`cd Events`</br>
2. Configure Databse Environment:</br>
<p>In your settings file:</p>

 `DATABASES = {`
    `'default': {`
        `'ENGINE': 'django.db.backends.postgresql',`</br>
        `'NAME': 'name',`</br>
        `'PASSWORD':'pass',`</br>
        `'USER':'user',`</br>
        `'HOST':'127.0.0.1',`</br>
        `'PORT':'5432'`
   ` }`
`}`

3. Build and Run::</br>
`docker-compose  --build`:</br>
* Run:</br>
`docker-compose- up`:</br>

* API Available at :</br>`http://localhost:8000`:
4. Appy Migrations::</br>
`docker-compose exec web python manage.py migrate`:</br>
5. Stop APplication::</br>
`docker-compose down`:</br>

## API Endpoints

| Endpoint                          | Method | Description                  |
|--------------------------------   |--------|------------------------------|
| `/events/create/`                 | POST   | Create a new event           |
| `/events/update/<id>/`            | PUT    | Update an existing event     |
| `/Events/categories/`             | GET    | List all categories          |
| `/events/categories/create/`      | POST   | Create a new category        |
| `/events/categories/delete/<id>/` | DELETE | Delete a category            |
| `/events/categories/<id>/events/` | GET    | List events in a category    |
| `/events/events/chart/`           | GET    | Get pending event counts     |

## Usage
* Create an Event: Send a POST request to /events/create/ with JSON data (e.g., `{"name": "Sciencecongress", "category_id": 1, ...}`).

* View Categories: Fetch `/categories/` to retrieve all categories in JSON format.

## Contributing
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License
This project is licensed under MIT License

* Contact - Alexander Nyaga.
           ga.nyaga7@gmail.com








