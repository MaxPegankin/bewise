App initialization sequence:

1.  (optional) create env with python 3: <BR>
                       `python -m venv .wenv`<BR>
                enter the environment: <BR>
                      `source .wenv/Scripts/activate` (for windows)<BR>
                       `source .wenv/bin/activate` (for linux)<BR>
2.  initialize rest_app package:<BR> 
                      `pip install -e .`
3.  create .env file near the docker-compose.yaml with the following vars as in the example below:<BR>
                
                #POSTGRES
                POSTGRES_VERSION=latest
                POSTGRES_USER=docker
                POSTGRES_PASSWORD=docker
                POSTGRES_DB=quizdb
                #flask envs
                FLASK_APP=rest_app
                FLASK_DEBUG=1
                FLASK_FORMS_SECRET_KEY=my_secret
                
4.  run docker compose: `docker-compose up -d`
5.  run flask: `flask run`
6.  open flask adress in a browser (<a href=http://127.0.0.1:5000>http://127.0.0.1:5000</a>)
7.  enter number of questions to add to DB (number from 1 to 100)
8.  receive the result with questions added to DB 
9.  (optional) open adminer to exemine the db http://127.0.0.1:8080/ (use credentials from your .env file)

Request example:
![image](https://user-images.githubusercontent.com/54612661/183261805-1fc1ae3a-8405-4e88-81a1-d5a990dca375.png)

