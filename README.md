# devops-bootcamp-1

Chapter 1: runing app locally
Postgres container:
docker run --name flask_postgres -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=password -e POSTGRES_DB=postgres -p 5432:5432 -d postgres
redis container:
docker run --name flask_redis -p 6379:6379 -d redis

# setup a virtual environment
 python3 -m venv venv
 source venv/bin/activate
 pip install -r app/requirements.txt   # install app dependencies

 # run app locally  without celery
 python app/app.py

### Run flask with gunicorn and celery in background

# Start Gunicorn to serve the Flask application
gunicorn -w 4 -b 0.0.0.0:8080 app:app &
# Start Celery worker with logging to a file
celery -A app.celery worker --loglevel=info --logfile=celery.log &
# Wait for all background processes to finish
wait
# or run with bash script, run.sh

## Access the application on port 8080
http://0.0.0.0:8080 