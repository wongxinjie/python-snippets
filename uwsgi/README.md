uwsgi --http :9090 --w wsgi:app --master --processes 4 --threads 2 --stats 127.0.0.1:9191 --virtualenv VENV
