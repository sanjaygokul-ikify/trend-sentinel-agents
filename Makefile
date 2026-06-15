build:
	pip install .
test:
	pytest tests/
lint:
	python -m flake8
format:
	python -m black .
analyze:
	python -m mypy .
	python -m radon complex .
clean:
	rm -rf __pycache__
	rm -rf **/__pycache__
install:
	pip install -r requirements.txt
docker:
	docker-compose up -d