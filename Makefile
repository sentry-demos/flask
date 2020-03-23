# Must have `sentry-cli` installed globally
# Following variable must be passed in:

#SENTRY_AUTH_TOKEN=<your_auth_token>

SENTRY_ORG=testorg-az
SENTRY_PROJECT=flask
VERSION=`sentry-cli releases propose-version`

REPOSITORY=us.gcr.io/sales-engineering-sf
COMMIT_SHA=$(shell git rev-parse HEAD)
GCP_DEPLOY=gcloud run deploy $(shell whoami)
GCP_SERVICE_NAME=flask-errors
GCP_WORKSPACE_NAME=workspace_flask_errors


deploy: create_release associate_commits run_flask

create_release:
	sentry-cli releases -o $(SENTRY_ORG) new -p $(SENTRY_PROJECT) $(VERSION)

# makes Sentry look at commits sitting on Sentry, and associates them to this Release that's getting pushed up
associate_commits:
	sentry-cli releases -o $(SENTRY_ORG) -p $(SENTRY_PROJECT) set-commits --auto $(VERSION)

run_flask:
	VERSION=$(VERSION) FLASK_APP=app.py flask run -p 3001

# GCP
deploy_to_gcp: build deploy-flask

build:
	gcloud builds submit --substitutions=COMMIT_SHA=$(COMMIT_SHA) --config=cloudbuild.yaml

deploy-flask:
	$(GCP_DEPLOY)-$(GCP_SERVICE_NAME) --image $(REPOSITORY)/$(GCP_WORKSPACE_NAME):$(COMMIT_SHA) --platform managed
# ---

.PHONY: deploy create_release associate_commits run_flask deploy_to_gcp build flask
