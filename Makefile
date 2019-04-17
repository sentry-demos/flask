# Must have `sentry-cli` installed globally
# Following variable must be passed in:

#SENTRY_AUTH_TOKEN=<your_auth_token>
SENTRY_ORG=testorg-az
SENTRY_PROJECT=will-frontend-react
VERSION=`sentry-cli releases propose-version`

#echo $(VERSION)

deploy: setup_release run_flask

setup_release: create_release associate_commits

create_release:
	sentry-cli releases -o $(SENTRY_ORG) new -p $(SENTRY_PROJECT) $(VERSION)

# makes Sentry look at commits sitting on Sentry, and associates them to this Release that's getting pushed up
# "unassociated commits"
# set a release range, , because might cover more than what's on the release branch.
associate_commits:
	sentry-cli releases -o $(SENTRY_ORG) -p $(SENTRY_PROJECT) set-commits --auto $(VERSION)

run_flask:
	flask run -p 3001
