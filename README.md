# Interview Scheduler

This Repository mainly contain two APIs designed to register the candidate/interviewer time slots and return the available free slots as list

## Installation

After you cloned the repository, you want to create a virtual environment, so you have a clean python installation. You can do this by running the command.

```bash
python -m venv env
```
After this, it is necessary to activate the virtual environment, you can get more information about this here

You can install all the required dependencies by running

```bash
pip install -r requirements.txt
```
You can start the web server via 

```bash
python manage.py runserver
```

## Structure 

1)API root

```python
http://127.0.0.1:8000/
```
2)API for candidates/interviewers to register their available time slots.
```python
http://127.0.0.1:8000/users
```
3)API to return available time slots as a list which will take candidate
id and interviewer id as input. Here candidate id is userId and interviewer id is interId.

```python
http://127.0.0.1:8000/availableslots?userId=<>interId=<>
```
## Testing

APIs has been tested using Postman and was working fine.



