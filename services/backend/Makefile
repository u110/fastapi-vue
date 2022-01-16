setup: env pip

env:
	python3 -m venv env
	env/bin/pip install --upgrade pip

pip:
	env/bin/pip install -r requirements.txt

aerich-%:
	docker compose exec backend aerich $(*F)

migrate: aerich-migrate

upgrade: aerich-upgrade