# Books API

## Backend Challenge to provide the API implementation with Django

A complete implementation of RESTful API to store and consume some structures that it contains, such as users, folders, books, categories and author of projects, which were created using django 3 and django rest_framework.

## Sections

* :scroll: [Patterns](#scroll-patterns) (optional)
* :blue_book: [Requirements and Model](#blue_book-requirements-and-model)
* :postbox: [Testing](#postbox-testing)
* :wrench: [Building App](#wrench-building-app)
* :key: [Authentication](#key-authentication)
* :ticket: [API Consuming](#ticket-api-consuming)
* :exclamation: [Difficulty](#exclamation-difficulty)

## :scroll: Patterns

In order to create the real stage API to consuming I follow some best pratice and concepts of RESTful APIs must has, beside this, I provide the detailed documentation about API with the postman to test endpoints.

### Implemented concepts

* Versioning: All endpoints contains as prefix /api_v1/ that show the version api is first. So when I change some detail or implementation of API I Don't broken any implementation on my API in other application.

* Pagination: As many people can consuming the endpoints I need provide some throughput data. to first version we apply the limit with 5 registries. And implement a custom pagination to categories API.

* Authentication: I make the API visualization with the JWT tokens to Authentication on each endpoints

* Develop methodologies: We use a git-flow method to develop the features.

* Containerization: The project is practical to run both in a virtual environment and in a docker container.

* Throttling: Global per-user limitation policies have been implemented. This concept was implemented globally, however it can be edited in classes.

## :blue_book: Requirements and Model

The system consists of a creator of navedex's API, where you can register using email and password, and then when logging in you will have access to your browsers' database, with information such as: names, birth data, loads, company time and projects who participated.

### Requirements

* Authentication: The user registry himself with the password and email and can be get the token to access any endpoint to create and delete his registry by request.

* User tracked: In order to provide some security and isolation of registry all user only have access to own registry with exception of the dad tables, such as tecnologies and jobs.

* Books Endpoint
    - Create: create new books
    - List: return all values that user have ownership
    - Retrive: return the specific
    - Update: alter books
    - Delete: delete the registry
    - observation: all registry of this model only can accessed by his own owner and this data need authentication.

* Categories Endpoint
    - Create: create new categories
    - List: return all values
    - Retrive: return the specific
    - Update: alter project by JSON information
    - Delete: delete the registry
    - observation: all registry of this model only can accessed by his own owner and this data need authentication.

* Folders Endpoint
    - Create: create new folder that record a book collection
    - List: return all values
    - Retrive: return the specific
    - Update: alter project by JSON information
    - Delete: delete the registry
    - observation: all registry of this model only can accessed by his own owner and this data need authentication.

## :postbox: Testing

Test automation is the use of software to control the execution of the software test, the comparison of the expected results with the actual results, the configuration of the test pre-conditions and other control and test report functions.
In this repository I provide some task to show the knowledge with tests.

## :wrench: Building App

There are two way to build and run this application, first is running with isolate app, second is with docker that separates the context and allows running withou previous dependecies.  

### Normal build

1. Get repository
2. Make the virtualenv
4. Install all dependecies
5. Run test
6. Run migrations
7. Run app

```console

    git clone https://github.com/BrenoOsvaldoFunicheli/books-api.git
    python3 -m venv .env
    source .env/bin/activate
    pip install -r requirements.txt
    python manage.py test
    python manage.py migrate
    python manage.py runserver 0.0.0.0:8002

```

The essencial obs is that we provide virtualenviroment with pipenv to delivery dependecies controll. You can access and user that with pipenv controll method.

### Docker Build

This API was construct with the docker implementation, so you can run without others dependecies and scale after make your implementations, so you need make docker and docker compose in your machine.

#### Docker installation

To install docker follow the instructions in the links below depending on your operating system:

* CentOS: https://docs.docker.com/install/linux/docker-ce/centos/
* Debian: https://docs.docker.com/install/linux/docker-ce/debian/
* Fedora: https://docs.docker.com/install/linux/docker-ce/fedora/
* Ubuntu: https://docs.docker.com/install/linux/docker-ce/ubuntu/
* MacOS: https://docs.docker.com/docker-for-mac/install/
* Windows: https://docs.docker.com/docker-for-windows/install/

#### Step by Step to Set Up

For API build you need some simple steps, download the this repository with the follow command:

``` linux

git clone https://github.com/BrenoOsvaldoFunicheli/naveapi.git

```

before the next step you need create the docker-volume to store the database data.

``` linux

docker volume create nave-pgdata

```

Next, you need setting the app and database containers with the follow command on the folder downloaded, that make(download all dependencies of the project), building(when you don't have container in your machine it downloaded it) and setting containers with docker compose.

``` linux

docker-compose build

docker-compose up

```

After this you need create database on container, because django can't create automatic, the database container is running the postgres. so you need create the database with the name nave.


* Postgres DDL

``` sql

CREATE DATABASE conceptu;

```

Next, you can't press CTRL+C to exit database and set it up again with the docker-compose up, with this you'll have the API running, but you need migrate database changes with follow command:

* migrations

``` linux

docker exec -it [container-name] /bin/sh -c "[ -e /bin/bash ] && /bin/bash || /bin/sh"

python manage.py makemigrations

python manage.py migrate

```

Finally, you can use the API !!!

## :key: Authentication

As the API was implemented with JWT tokens all access on the endpoints are do with the jwt tokens, so you need apply the request and set in the authorization.

### Token duration

So when you access token through the url [uri]/api/v1/[resource] you can get two values on the payload response, first is the access token, with it, you can access the endpoint for 5 minutes, after you need used the refresh endpoint that gives the token to access for 24 hours.  

## :ticket: API Consuming

The API consuming were detailed on the postman collection, that implements all steps to consuming and explain some steps to use. The ordering of steps need to be follow, because you need authentication before consuming. The collection link is https://documenter.getpostman.com/view/8382418/UVypzcqJ

## :exclamation: Obs

We provide this section to comment some errors and things that I guess interrest.

* Commits
    The first point is that there are some commits made in the master, a fact that should be disregarded, as I only made them in order to submit documentation. However, other processes followed the gitFlow scheme.

* Tests
    Another point is the lack of tests, I particularly love implementing them using Pytest and even the schema provided by drf (django rest framework). However, due to some time issues I didn't do it. However, I have the knowledge to implement them.

* Database
    You may notice that I left the default db as sqlite, even though in docker I created a postgres container. I've simplified it for quick use in a local way without docker. However, as you can see I added a dotenv where parameters such as the bank can be changed in the future.

* Hard Delete
    Another point of attention is that the deletion method applied was hard-delete (where the record is actually deleted). Good practices point out that the correct method should be soft. However, as a conceptual example, I am pointing this out to attest to my knowledge on the subject by showing that I could easily implement soft-delete just by adding a deleted flag to the created models.



### Example of the code to create super user

```linux

python manage.py createsuperuser --username django --email django@django.com
put password

```
