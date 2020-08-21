# hood-watch


##### By [George Karumbi](https://github.com/gkarumbi/) ,[Wenslaus Makumba](https://github.com/Wenslaus-Makumba/) and [Mishael](https://github.com/mishael254)


Github link: https://github.com/gkarumbi/hood-watch

Live site: [View Site](https://hood-watch.herokuapp.com/)
  
# Description  
This is a neighborhood application where a user have to signup first and be able to view different neighbourhoods. A user can join or leave a neighbourhood and once he/she joins, they can view information about that neighbourhood.


 
## User Story  
As a user I would like to:
* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.  
  

  
## Setup and Installation  
To get the project : 
  
##### Clone the repository:  
 ```bash 
 https://github.com/gkarumbi/hood-watch
```

##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual 
- source virtual/bin/activate  
```  


##### Navigate into the folder:
 ```bash 
cd hood-watch
```

##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrations:
 ```bash 
python manage.py makemigrations hood
 ``` 
 Then Migrate: 
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
 
 
 
## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 1.11](https://docs.djangoproject.com/en/1.1/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs at the moment.
  
## Contact Information   
If you have any question or contributions, please email any of us  at nyongesajoannanjala@gmail.com or maratah7@gmail.com or leave a comment here on Github.
  

### License
MIT Copyright (c) 2020 [George Karumbi](https://github.com/gkarumbi/) ,[Wenslaus Makumba](https://github.com/Wenslaus-Makumba/) and [Mishael](https://github.com/mishael254)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
