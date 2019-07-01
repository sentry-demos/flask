# Must have `sentry-cli` installed globally
# Following variable must be passed in:

#SENTRY_AUTH_TOKEN=<your_auth_token>

SENTRY_ORG=testorg-az
SENTRY_PROJECT=flask
VERSION=`sentry-cli releases propose-version`

deploy: create_release associate_commits run_flask

create_release:
	sentry-cli releases -o $(SENTRY_ORG) new -p $(SENTRY_PROJECT) $(VERSION)

# makes Sentry look at commits sitting on Sentry, and associates them to this Release that's getting pushed up
associate_commits:
	sentry-cli releases -o $(SENTRY_ORG) -p $(SENTRY_PROJECT) set-commits --auto $(VERSION)

run_flask:
	VERSION=$(VERSION) FLASK_APP=app.py FLASK_ENV=development flask run -p 3001
