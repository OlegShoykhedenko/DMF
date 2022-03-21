# DMF
To run app: 
- clone it from github
- you need to have postgresql (pip install psycopg2)
- you need to have django rest framework (install djangorestframework)
- create a virtual enviornment and activate it
- run: python3 manage.py runserver (or for mac: python manage.py runserver)
- go to localhost:8000/admin and login (username: oleg, password: Testing12345) (you can also create your superuser if you want)
- then go to tokens and copy key for user oleg (or the user you have created) (also you can reach to the page with the key with this link http://localhost:8000/admin/authtoken/tokenproxy/)
To test rest api endpoint: 
- open postman
- in headers add new key "Authorization" with value "Token 'the key you took from admin pages from previous steps'"
- use the following address to test all api's: http://localhost:8000/api/task/getTasks/11/
- GET: http://localhost:8000/api/task/getTasks/11/ (any id is allowed not only 11)
- POST: http://localhost:8000/api/task/getTasks/11/ (any id is allowed not only 11)
- PATCH: http://localhost:8000/api/task/getTasks/11/ (you should provide an id of a task you want to update)
- DELETE: http://localhost:8000/api/task/getTasks/11/ (you should provide an id of a task you want to delete)
Sample task object to add to POST and/or PATCH: 
{
    "title": "Test",
    "description": "Test task",
    "due_date": "2022-05-27",
    "task_state": "TODO"
}
For filtering and sorting (for both requests use GET method): 
- http://localhost:8000/api/task/getFilteredTask?search=6 (to search/filter tasks. to add more filter option use &: search=6&search=oleg)
- http://localhost:8000/api/task/getFilteredTask?ordering=due_date (to sort/order tasks. to reverse the order of sorting change to orderting=-due_date)

For testing run: python3 manage.py test (or for mac: python manage.py test). It will execute all the tests for endpoints that are presentated in the project.

----Deployemnt----
I run into several issues with deployment project to nginx. Due to unavailability to work of Mac or native Linux I work on Windows machine with WSL 2.0, 
an upgraded version of WSL designed to run a full Linux kernel in a Hyper-V enviornment. That WSL turned to be problematic to deploy the project to Linux server due to 
issues with connecting configurations with Windows. 
I have configured necessary scripts for Dockerfiles and docker-compose. Some adjustments are still needed in order ot use docker-compose to deploy the project to nginx.
I have tried various methods to resolve deployment issues with my WSL, but my attempts have not positively resulted. With more suitable machine this task would be 
easier to solve.
