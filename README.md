
# Conficon
A Favicon generator app, converts image design(.PNG, .JPEG) to smaller [favicon](https://en.wikipedia.org/wiki/Favicon) sizes which are available for download and available to use in the HTML code

# Projects Description
The application allows users to upload images and they convert the images into the different sizes of favicon. Users can choose the sizes they want and then download.
The HTML [embed](https://en.wikipedia.org/wiki/Embedded) code is also available to use during coding process.


![My Image](media/footer.png)



# Website Preview Image



![HeaderImage](media/header.png)

# Technologies Used to Achieve this project 🛠️🧲

This project was created with ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white) and the following technologies were used: <br/>
* ♎ __Design__<br/>
        ![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white)

* ⚛️ __Frontend__<br/>
      ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
      ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
      ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

* ⚙️ __Backend__<br/>
        ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
        ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)


* 🛢️ __Database__<br/>
        ![PostgreSQL](https://img.shields.io/badge/postgres-%23316192.svg?&style=for-the-badge&logo=postgresql&logoColor=white)


* 🎡 __Project Management and Version Control__<br/>
        ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

Python, Django Framework, HTML, CSS Javascript and MySQL are used to build the project. The design structure of the project is a [Monolithic](https://en.wikipedia.org/wiki/Monolithic_application) application. HTML, CSS and Javascript are use in the frontend, Python Django framework is used for the backend and MySQL as the database

# How to Install and Run the Project
-  run git clone https://github.com/zuri-training/Favicon_gen-Team-68.git 
- create a virtual environment
- run ```pip install -r requirements.txt```
  - # Database
    - To use the default sqlite database
      - run ```python manage.py makemigrations```
      - run ```python manage.py migrate```
      - run ```python manage.py runserver localhost:8000```
    - To use postgreSQL as default database
      - Install [postgreSQL](https://www.postgresql.org/download/)
      - create a ```.env``` file in your project root directory
      - In the ```.env``` define variable name ```USE_PROD=1``` and ```DB_PWD=<your database password>```
      - run ```python manage.py makemigrations```
      - run ```python manage.py migrate```
      - run ```python manage.py runserver localhost:8000```


- [Figma WorkSpace](https://www.figma.com/file/Om0i0dm6XOQN27utcHw5QD/Favicon-general?node-id=0%3A1)
