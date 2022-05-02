# Jorge Jimenez Diaz PortFolio

## Example Photo
![Alt text](public/image.png?raw=true "Ejemplo")

## Init project

Clone repository:

```sh
$ git clone https://github.com/jorgejimenez98/jorgejimenezPortfolio
$ cd jorgejimenezPortfolio

```
Build Docker Images and Init Database:

```sh
$  docker-compose build
$  docker-compose run backend python backend/manage.py makemigrations
$  docker-compose run backend python backend/manage.py migrate
$  docker-compose run backend python backend/manage.py createsuperuser
$  docker-compose run backend python backend/manage.py populate_database
```

Run project:

```sh
$ docker-compose up
```


If you want to drop the database and initialize the data again do the following command:

```sh
$ docker-compose run backend python backend/manage.py clean_database
```

The Admin Page is on url `http://127.0.0.1:5000/admin`

The project will be running on url `http://127.0.0.1:3000`

Click [here](https://jorgejimenez.herokuapp.com) To see live app on HEROKU. 
