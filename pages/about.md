---
title: About
permalink: /about/
---

# About the Project
<div style='font-size: 18px; margin-left: 1rem;'>
😮 Didn’t you ever get information late because you couldn’t check the notice on time?<br>
😮 Don’t you want to get only the notice you want?
</div>
<br>
**Smart Notice Bot will solve it!**

Smart Notice Bot is an open source project that sends a main notice of university through email. <br>The inconvenience of checking notices on various sites every day will disappear and only the notices and information you want will be provided by e-mail.


## How to use
```
$ git clone https://github.com/Smart-Notice-Bot/Smart.Notice.Bot.git
```
* Install chromedriver.exe
    * Check the Chrome version of your computer and download chromedriver.exe.
        1. [check the Chrome version](https://help.zenplanner.com/hc/en-us/articles/204253654-How-to-Find-Your-Internet-Browser-Version-Number-Google-Chrome)
        2. [Download chromedriver.exe](https://chromedriver.chromium.org/downloads)
    * Move the chromedriver.exe file to Smart.Notice.Bot/notice 

After that, follow the process below.

```
$ cd notice
$ pip install pyperclip
$ pip install selenium
$ python manage.py makemigrations
$ python manage.py migrate

# create admin account
$ python manage.py inituser --username=admin --password=1234 --action=create_admin

$ python manage.py runserver
```

## How to Contribute
Contributions, issues are welcome. You can submit a PR to this repository and it will be depolyed once it’s accepted. You can write the commit message including PR Title as follows.
```
$ git commit -m "PR Title"
```

## License
APACHE LICENSE, VERSION 2.0

## Support

If you need help, please don't hesitate to [open an issue](https://www.github.com/{{ site.github_user }}/{{ site.github_repo }}).

