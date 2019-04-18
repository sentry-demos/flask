# sentry-demos/flask

## Summary:
To show how Sentry works in an example web app that uses Flask
- how to integrate the Sentry SDK into Flask
- trigger an error that gets sent as Event to Sentry.io Platform
- `app.py` has multiple endpoints for showing different ways that errors are handled
- Sentry Release cycle covered in `Makefile`

## Initial Setup & Run
1. setup flask
```
pip install flask sentry_sdk flask-cors
```
1. Configure Sentry with your `DSN key` in app.py
2. Configure sentry-cli (is for creating Sentry releases) with your `SENTRY_AUTH_TOKEN` in Makefile or run `export SENTRY_AUTH_TOKEN=<your_auth_token>`. Do the same for `SENTRY_ORG` and `SENTRY_PROJECT`
3. Check your Github repo is integrated into your Sentry organization.
4. run make, which (Makefile) creates a Sentry release and runs Flask
```
make deploy
```

## GIF
![Alt Text](sentry-demos-flask.gif)