web: python setup.py develop && gunicorn runapp:app -b "0.0.0.0:$PORT" -w 16 -t 3 --name kralingsekost
migrate: python setup.py develop && alembic -c production.ini upgrade head