# Inventory Management System API

[![Black Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

This is a simple inventory management system API built with Flask and Flask-RESTful. It allows users to create, delete, update and retrieve products. It also allows users to add products to cart and purchase products.

- [Link to API Documentation](https://documenter.getpostman.com/view/15138887/2s8YzUw1vw)

## Key Features

1. Product creation, deletion, update and retrieval.
2. Adding product to cart and purchasing product
3. Keeping track of product quantity in regards to purchase or add to cart functions, i.e the product quantity should reduce when a purchase is made, or when it is added to the "user's" cart; users should be informed when a product is "out of stock"
4. Products should have (name, category, labels(e.g size, colour etc), quantity, price) A product can have one or more labels.

## Technologies

- [Python 3.10](https://python.org): Base programming language for development
- [Flask](https://flask.palletsprojects.com/en/2.0.x/): Web framework for development
- [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/): Provides API development tools for easy API development
- [PostgreSQL](https://www.postgresql.org/): Application relational databases for development, staging and production environments
- [Adminer](https://www.adminer.org/): Database management tool
- [Docker Engine and Docker Compose](https://www.docker.com/) : Containerization of the application and services orchestration
- [AWS](https://aws.amazon.com/): Deployment of the application

## Testing

Two user accounts have been created for testing purposes. The details are as follows:

- John Doe
  - email: johndoe@example.com
  - password: TestPassword
- Jane Doe
  - email: janedoe@example.com
  - password: TestPassword

- Adminer is used for database management. The details are as follows:
  - System: PostgreSQL
  - Server: db
  - Username: postgres (the value of POSTGRES_USER in the .env file)
  - Password: TestPassword (the value of POSTGRES_PASSWORD in the .env file)
  - Database: inventory (the value of POSTGRES_DB in the .env file)

- The API documentation is available on `https://documenter.getpostman.com/view/15138887/2s8YzUw1vw` on your browser.

## How To Start App

- Clone the Repository
- create a .env file with the variables in the .env.example file
  - `cp env.example .env`

- Run `make build`

  - Running the above command for the first time will download all docker-images and third party packages needed for the app.
  - **NB: This will take a few minutes for the first build**

- Run `make up`

  - Running the above command will Start up the following Servers:
    - API Server --> http://localhost:8000
    - Adminer Server --> http://localhost:8080

- Run `make down` to stop the servers

- Other commands can be found in the Makefile
