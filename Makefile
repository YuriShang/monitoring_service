CODE =  .

build:
	docker-compose up -d --build

run:
	docker-compose up app

stop:
	docker-compose stop app
	docker-compose stop db