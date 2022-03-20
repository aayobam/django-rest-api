# Todo webapp rest Api
- A Todo API endpoints with django rest framework that performs the CRUD operations.
- Security is based on default django authentication and use of jwt token authentication.
- Auto documentation using drf-yasg.

## Technologies used are

- Python.
- Django framework
- Django rest framework
- drf-yasq for documentation
- django-rest-framework-simplejwt
- Database(sqlite3)


## To work on this project:

- Fork the repo to your repo
- Clone the repo to your system with the below command
```
git clone "repo link"
```

## Installation instructions for backend

- Make sure docker and docker-compose are installed on your system (linux/mac/windows10>>).
- After cloning the repository to your system, type the below to build the database and install all dependencies.
```
docker-compose up --build -d
```
- To run the project type the below command
```
docker-compose up
```
- To stop the project, type the below command
```
docker-compose down
```
- To run pytest, type the below command
```
docker-compose exec app pytest
```
