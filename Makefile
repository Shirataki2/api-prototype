API_DIR = api
BOT_DIR	= bot
WEB_DIR	= web

# Load .env file
ifneq (,$(wildcard ./.env))
	include .env
	export
endif

api-setup: 
	cd $(API_DIR); pipenv install

bot-setup:
	cd $(BOT_DIR); pipenv install

web-setup:
	cd $(WEB_DIR); yarn install --production=false

setup:
	@make api-setup
	@make bot-setup
	@make web-setup

api-dev:
	cd $(API_DIR); pipenv run uvicorn src:app --reload --log-level debug --port $(API_PORT) --host 0.0.0.0

bot-dev:
	cd $(BOT_DIR); pipenv run python -m src

web-dev:
	cd $(WEB_DIR); yarn dev

api-run:
	cd $(API_DIR); pipenv run uvicorn src:app --port $(API_PORT)

bot-run:
	cd $(BOT_DIR); pipenv run python -m src

web-build:
	cd $(WEB_DIR); yarn build

web-run:
	cd $(WEB_DIR); yarn start
