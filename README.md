# Pexon Homework

## General

This exercise uses the [postgres](https://hub.docker.com/_/postgres) image.

## Initialize DB

```bash
make init_db
```

## Create table

```bash
make create_table
```

## Playing with the endpoings

```bash
make post_movies
```

```bash
make get_movies
```

## Notes

- See also this article: they do something similar.
- To change the entrypoint is a better solution to initialize a database in a container.
- See [this article](https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask) for Flask.
- POSTMAN is not necessary imo. Better learn [curl](https://curl.se/).
