
run:
	./manage.py runserver


git-save:
	git add .
	git commit -am "update"

migrations:
	python manage.py makemigrations
	python manage.py migrate

update:
	git push heroku-release & git push heroku-holliday & git push prof & git push getmoefit

applymigrations:
	heroku run python manage.py migrate --app getdinerotoday & heroku run python manage.py migrate --app hollidayconsulting & heroku run python manage.py migrate --app sawcorp & heroku run python manage.py migrate --app professorhoneyscreditlenging & heroku run python manage.py migrate --app getmoefit

bashgdt:
	heroku run bash --app getdinerotoday

update_gdt:
	make migrations
	make git-save
	git push heroku-release master
	heroku run ./manage.py migrate --app getdinerotoday

pushdt:
	git push heroku-release master
	heroku run ./manage.py migrate --app getdinerotoday