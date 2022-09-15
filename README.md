# SimmiFoundation

version 1.0 (work till august 31st 2022)

apps made :-
->faq - contains models for FAQ page
->fundraisers - contains models of all the fundraisers and campaigns and even NGO details
->home_app - contains the dynamic field models of home page
->payments -  transaction backend ( Razzor pay)
->User_Auth - User account model

api directory contains DJANGO REST API STRUCTURE 

All API end points can be seen at http://127.0.0.1:8000/api/

SET UP INSTRUCTIONS

1 install git 

2 clone the repository using 
```
git clone https://github.com/CoderRounak/SimmiFoundation.git
```
command on git bash at a particular directory you want to clone the project

3 use cd command to go inside the SimmiFoundation folder that has just got cloned in previous step

4 use "git checkout staging" command to get the files of staging branch

5 delete the migration folders from each of the django apps in the project otherwise they might cause errors while future migrations u might want to do.

6 create a virtual enviornment and install are pre requirement packages listed in requirements.txt using the following command on terminal
```
pip install -r requirements.txt
```

7 makemigrations then migrate for each of the django apps seperations, 
example - 
```
py manage.py makemigrations fundraisers
```
then 
```
python manage.py migrate fundraisers
```
do this for all the apps then 
```
python manage.py migrate
```
at last

8 create super user using 
```
python manage.py createsuperuser
```

9 START IMPROVING AND DEVELOPING !!


