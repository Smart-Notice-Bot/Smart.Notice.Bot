
<h1 align="center" style='font-family: palatino Linotype'> Smart Notice Bot</h1>
<p align="center">
    <a href ="https://github.com/Smart-Notice-Bot/Smart.Notice.Bot/blob/main/LICENSE">
        <img src="https://img.shields.io/badge/license-Apache--2.0-blue?style=plastic&link=https://github.com/Smart-Notice-Bot/Smart.Notice.Bot/blob/main/LICENSE">
    </a>
</p>
<h4 align="center">
    <p>
        <b>English</b> |
        <a href="https://github.com/Smart-Notice-Bot/Smart.Notice.Bot/blob/main/README.md">한국어</a>
    <p>
</h4>

<p align='center' style='font-size:150%'>Smart Notice Bot is an open source project that sends a main notice of university through email</p>

<br>



## :star: Features
1. (Complete)After signing up for membership on the website, select your department, e-mail, and interests.
2. (Complete)Whenever articles such as what users need (employment, start-up, graduate school, internship, etc.) are updated, they are sent by e-mail.
3. (Complete)Frequent questions (FAQs) are provided on the website.
4. (Complete)It provides a bulletin board service that allows you to answer questions if someone posts them.

<br>

## :desktop_computer: Prerequisites
Python 3.7 & Jupyter notebook

<br>

## :white_check_mark: Installation
```
$ git clone https://github.com/Smart-Notice-Bot/Smart.Notice.Bot.git
$ cd notice
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py inituser --username=admin --password=1234 --action=create_admin
$ python manage.py runserver
```

**< How to use main.py >**

Step 1.

(If chromedriver.exe is installed, move on to step 2)

Check the Chrome version of your computer and download chromedriver.exe.

How to check the Chrome version: https://help.zenplanner.com/hc/en-us/articles/204253654-How-to-Find-Your-Internet-Browser-Version-Number-Google-Chrome

Download chromedriver.exe: https://chromedriver.chromium.org/downloads

Step 2.

Put mian.py and chromedriver.exe in the same folder.

Run the program using PyCharm, Jumpyter Notebook, etc.

Enter the desired date (month and day).

The title and content of the notice on the relevant date are put in variables and printed.

<br>

## :loudspeaker: Contributing
Contributions, issues are welcome. You can submit a PR to this repository and it will be depolyed once it's accepted. <br>
You can write the commit message including PR Title as follows.<br>
```
$ git commit -m "PR Title"
```

<br>

## :page_with_curl: License
APACHE LICENSE, VERSION 2.0



