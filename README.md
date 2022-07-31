
# Conficon
A Favicon generator app, converts image design(.PNG, .JPEG) to smaller [favicon](https://en.wikipedia.org/wiki/Favicon) sizes which are available for download and available to use in the HTML code

# Projects Description
The application allows users to upload images and they convert the images into the different sizes of favicon. Users can choose the sizes they want and then download.


![My Image](media/files/icons/footer.png)



The HTML [embed](https://en.wikipedia.org/wiki/Embedded) code is also available to use during coding process.
Python, Django Framework, HTML, CSS Javascript and MySQL are used to build the project. The design structure of the project is a [Monolithic](https://en.wikipedia.org/wiki/Monolithic_application) application. HTML, CSS and Javascript are use in the frontend, Python Django framework is used for the backend and MySQL as the database

# How to Install and Run the Project
-  run git clone https://github.com/zuri-training/Favicon_gen-Team-68.git 
- create a virtual environment
- run ```pip install -r requirements.txt```
  - # Database
    - To use the default sqlite database
      - run ```python manage.py makemigrations```
      - run ```python manage.py migrate```
      - run ```python manage.py runserver```
    - To use MySQL as default database
      - Install [MySQL](https://www.mysql.com/downloads/)
      - create a ```.env``` file in your project root directory
      - In the ```.env``` define variable name ```USE_PROD=1``` and ```DB_PWD=<your database password>```
      - run ```python manage.py makemigrations```
      - run ```python manage.py migrate```
      - run ```python manage.py runserver```


Link to the figma Workspace:  https://www.figma.com/file/Om0i0dm6XOQN27utcHw5QD/Favicon-general?node-id=0%3A1

<a href = "https://github.com/Conradgabe">
  <img src = "https://avatars.githubusercontent.com/u/98839344??s=460&v=4"/>
</a>

Made with [contributors-img](https://contrib.rocks).
