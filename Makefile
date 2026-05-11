PYTHON=/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

install:
	$(PYTHON) -m pip install --upgrade pip &&\
		$(PYTHON) -m pip install -r requirements.txt

test:
	$(PYTHON) -m pytest -vv --cov=main --cov=calCLI --cov=my_lib test_*.py

format:	
	black *.py my_lib/*.py

lint:
	pylint --disable=R,C --extension-pkg-whitelist='pydantic' main.py --ignore-patterns=test_.*?py *.py  my_lib/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 561744971673.dkr.ecr.us-east-1.amazonaws.com
	docker build -t logistics .
	docker tag logistics:latest 561744971673.dkr.ecr.us-east-1.amazonaws.com/logistics:latest
	docker push 561744971673.dkr.ecr.us-east-1.amazonaws.com/logistics:latest
		
		
all: install lint test format deploy