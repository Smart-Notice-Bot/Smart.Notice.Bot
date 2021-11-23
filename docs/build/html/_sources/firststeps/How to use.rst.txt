##########
How to use
##########

Prerequisites
#############
* Smart.Notice.Bot must be run with Python 3.7 or higher and the appropriate chromedriver.
* Django

Python
######

1. Please download Python version 3.7 or higher.
2. `Python download site <https://www.python.org/downloads/>`_ 


Django
######

Please install Django

1. `How to install Django(English) <https://docs.djangoproject.com/en/3.2/topics/install/#how-to-install-django>`_
2. `How to install Django(Korean) <https://docs.djangoproject.com/ko/3.2/topics/install/#how-to-install-django>`_

chromedriver
############
* (If chromedriver.exe is installed, move on to how to use ~)

1. Check the Chrome version of your computer and download chromedriver.exe.

2. How to check the Chrome version: https://help.zenplanner.com/hc/en-us/articles/204253654-How-to-Find-Your-Internet-Browser-Version-Number-Google-Chrome

3. Download chromedriver.exe: https://chromedriver.chromium.org/downloads

How to use GetUserData.py
#########################

How to use crawling.py
######################

1. Put crawling.py and chromedriver.exe in the same folder.

2. Run the program using PyCharm, Jumpyter Notebook, etc.

3. Enter the desired date (month and day).

4. The notice about the input date are divided by type and converted into variables.

How to use sendEmail.py
#######################

1. Put sendEmail.py and chromedriver.exe in the same folder.

2. Run the program using PyCharm, Jumpyter Notebook, etc.

3. Enter the ID and password of your email.

4. Select the notice data classified in crawling.py and send an e-mail according to the user's preference.


How to use notice folder
########################

This folder is intended to run web pages and collect subscribers' emails and interests.

#. Create a virtual environment.

   ``$ python -m venv [folder_name]``

   ``$ cd [folder_name]/Scripts`` (this is for window)

   ``$ source [folder_name]/bin`` (this is for mac)

   ``$ activate``

   Please check if the (folder_name) is displayed.

#. Installing the Djago

   ``$ pip install django``

#. Create a migration.

   ``$ python manage.py makemigrations``

   If there's warnings or errors,

     ``$ python -m pip install --upgrade pip``

     ``$ python -m pip install Pillow``
      
#. Create a database.

   ``$ python manage.py migrate``

#. Project execution.

   ``$ python manage.py runserver``

#. If you enter an address such as 'http://127.0.0.1:8000/' in your browser, you will see the web page.

   The address can be checked in the cmd/Terminal. 

#. You can modify and use the .py(extension) files as you want.

   If you are curious about the .py files in the 'notice/notice/', please refer to below.

   `Django tutorial01(English) <https://docs.djangoproject.com/en/3.2/intro/tutorial01/>`_

   `Django tutorial01(Korean) <https://docs.djangoproject.com/ko/3.2/intro/tutorial01/>`_