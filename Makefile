run:
	docker-compose up -d
down:
	docker-compose down
info:
	docker ps -a

delete-app:
	docker rmi dips-app
delete-all:
	docker rmi dips-app && \
	docker rmi postgres:16-alpine && \
	rm -rf db_data

restart:
	docker-compose down && \
	docker rmi dips-app && \
	docker-compose up -d && \
	docker ps -a
