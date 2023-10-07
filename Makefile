run:
	docker-compose up -d
down:
	docker-compose down
info:
	docker ps -a

delete-app:
	docker rmi app
delete-all:
	docker rmi app && \
	docker rmi postgres:16-alpine && \
	rm -rf db_data

restart:
	docker-compose down && \
	docker rmi app && \
	docker-compose up -d

run-tests:
	pytest -vs app/unit_tests/person.py
	