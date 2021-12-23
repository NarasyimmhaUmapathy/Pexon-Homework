
INSTANCE_NAME=postgres-nara
PG_PASS=postgres
FLASK_APP_ENDPOINT=http://localhost:5000/movies
DB=movies.sqlite

init_db:
	bash init_db.sh

create_db:
	python db.py

rm_db:
	rm $(DB)

run_app:
	export FLASK_APP=app.py
	flask run

get_movies:
	curl -X GET $(FLASK_APP_ENDPOINT) | json_pp

post_movies:
	curl -d "@movies.json" -X POST $(FLASK_APP_ENDPOINT) -H 'Content-Type: application/json' | json_pp
 
pg:
	docker exec -it $(INSTANCE_NAME) /bin/bash -c "psql -U $(PG_PASS)"