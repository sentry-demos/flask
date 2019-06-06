# sentry-demos/flask

## Summary:
To show how Sentry works in an example web app that uses Flask
- how to integrate the Sentry SDK into Flask (https://docs.sentry.io/platforms/python/flask/)
- trigger an error that gets sent as Event to Sentry.io Platform
- `app.py` has multiple endpoints for showing different ways that errors are handled
- Sentry Release cycle covered in `Makefile`

## Initial Setup & Run
1. `pip install -r ./requirements.txt`
2. Configure Sentry with your `DSN key` in app.py
3. Configure sentry-cli (is for creating Sentry releases) with your `SENTRY_AUTH_TOKEN` in Makefile or run `export SENTRY_AUTH_TOKEN=<your_auth_token>`. Do the same for `SENTRY_ORG` and `SENTRY_PROJECT`
4. Check your Github repo is integrated into your Sentry organization.
5. run make, which (Makefile) creates a Sentry release and runs Flask
```
make deploy
```

## GIF
based on 0.7.10
![Alt Text](flask-demo.gif)

## Changelog
**05/24/19**
The branch `tracing-integration` features a Sentry Tracing integration, using Sentry SDK 0.7.13
- It sets trace id by default, so you'll see the code for `scope.set_tag("transaction-id", transactionId)` is gone, no longer needed

## Optional
Create a virtualenv for your Sentry Flask project so you're accessing SDK ^0.7.13
```bash
virtualenv $HOME/my_virtualenvs/flask_tracing_sdk
source $HOME/my_virtualenvs/flask_tracing_sdk/bin/activate
pip install -r ./requirements.txt
```
