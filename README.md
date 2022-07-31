# Conficon
A Favicon generator app, converts image design(.PNG, .JPEG) to smaller [favicon](https://en.wikipedia.org/wiki/Favicon) sizes which are available for download and available to use in the HTML code

# How to run the Project
- clone the project
- In the terminal run ```git clone https://github.com/zuri-training/Favicon_gen-Team-68.git```
- move into the directory
  - For windows, git-bash and linux users, run  ```cd Favicon_hgen-Team-68``
- create and activate your virtual environment and 
- run pip install -r requirements.txt
- For database
  - Do nothing to use sqlite as the default database
  - To use MySql
    - Install mysql, based on your os, when it's successfully installed, proceed to the next step
    - create a database named ```db_testing```, give it a password
    - create a ```.env``` file in your project root and define ```USE_PROD=1``` and ```DB_PWD=<your database password>``` in it.
    - run ```python manage.py makemigrations``` then ```python manage.py migrate```
    - run ```python manage.py runserver``` to run the project.
 
Images

![ico images](static/images/Vector1.png)

# Figma Workspace: 

[figma_designs_url](https://www.figma.com/file/Om0i0dm6XOQN27utcHw5QD/Favicon-general?node-id=0%3A1)
