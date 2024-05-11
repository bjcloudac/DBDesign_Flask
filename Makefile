venv:
	python3.11 -m venv .venv

activate:
	. .venv/bin/activate   								#	or source .venv/bin/activate

install:
		pip install --upgrade pip &&\
	pip install -r requirements.txt

format:
	black app.py  										#	format code with black

lint:
	pylint *.py											#	static code analysis tool

docker:
	docker build -t dbdesign_flask_api .
	docker run -dp 5050:5000 -w /app -v .:/app dbdesign_flask_api

#	-w essentially tells docker the working directory where the command runs
#	-v Creates a volume for the container to populate the changes in the directory to docker working directory /app



all:  venv activate install format lint docker
