# schwiftydjango 😏

A REST api that serves **Rick & Morty** characters. It is written in python using [django rest framework](http://www.django-rest-framework.org).

It is deployed at [schwiftydjango.herokuapp.com](https://schwiftydjango.herokuapp.com) using **[Heroku Container Registry](https://devcenter.heroku.com/articles/container-registry-and-runtime)** which allows you to deploy your **Docker** based app to Heroku.

Data is stored in a PostgreSQL database using the [Heroku Postgres Addon](https://www.heroku.com/postgres).

Images are stored in an **Amazon S3 bucket** with the help of [boto3](https://github.com/boto/boto3) and [django-storages](https://github.com/jschneier/django-storages).

![Time to get Schwifty](/art/logo.png)

## Running locally 👨‍💻

You will need your own **[Amazon S3 Bucket](https://aws.amazon.com/s3)**. It's very simple to have one up and running in no time.

Thanks to [django-environ](https://github.com/joke2k/django-environ) you only have to create a `.env`file inside the app folder and set these environment variables:

```
DEBUG=on
SECRET_KEY=YOUR_OWN_SECRET_KEY
AWS_ACCESS_KEY_ID=YOUR_OWN_AWS_ACCESS_KEY_ID
AWS_STORAGE_BUCKET_NAME=USE_YOUR_OWN_BUCKET
DATABASE_URL=postgres://postgres:postgres@db:5432/postgres
```

You will also need **Doker and Docker Compose**. On Mac and Windows Docker already includes Compose but on Linux you will have to follow the [official installation guide](https://docs.docker.com/compose/install).


```bash
# Build the images
docker-compose build

# Create the database migrations
docker-compose run web python manage.py migrate

# Start the containers
docker-compose up
```

Check that everything is ok. In another terminal window list the running Docker processes with the `docker ps` command:

```
CONTAINER ID        IMAGE             
1ece04b3958d        schwiftydjango_web
c5245a076a9c        postgres          
```

And you can even access the app running container:

```
docker exec -ti 1ece04b3958d bash
```

## Documentation 📃

The base url is: [schwiftydjango.herokuapp.com](schwiftydjango.herokuapp.com)

### Origins 🌍

Sample **GET** request for listing Origins to `/origins`:

```js
{
    "count": 8,
    "next": "https://schwiftydjango.herokuapp.com/origins/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "Earth (Replacement Dimension)"
        },
        {
            "id": 2,
            "name": "Earth (C-137)"
        }
    ]
}
```

Sample **GET** request for listing one Origin to `/origins/{id}`:

```js
{
    "id": 1,
    "name": "Earth (Replacement Dimension)"
}
```

Sample **POST** request for creating Origins to `/origins`:

```js
{
    "name": "Earth (C-137)"
}
```

### Characters 👽

Sample **GET** request for listing Characters to `/characters`:

```js
{
    "count": 15,
    "next": "https://schwiftydjango.herokuapp.com/origins/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "Rick Sánchez",
            "origin": {
                "id": 2,
                "name": "Earth (C-137)"
            },
            "image": "https://schwifty-media.s3.amazonaws.com/media/characters/rick-sanchez",
            "date_created": "2018-06-03T18:06:23.278544Z",
            "date_modified": "2018-06-03T18:06:23.278917Z"
        }
    ]
}
```

Sample **GET** request for listing one Character to `/characters/{id}`:

```js
{
    "id": 1,
    "name": "Rick Sánchez",
    "origin": {
        "id": 2,
        "name": "Earth (C-137)"
    },
    "image": "https://schwifty-media.s3.amazonaws.com/media/characters/rick-sanchez",
    "date_created": "2018-06-03T18:06:23.278544Z",
    "date_modified": "2018-06-03T18:06:23.278917Z"
}
```

### Pagination 📄

You can access different pages with the `page` parameter. If you don't specify any page, the first page will be shown. The default size is 5.
