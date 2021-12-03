---
layout: page
title: Smart.Notice.Bot
permalink: /
---

# Smart Notice Bot
<div style="font-size: 1.3rem">
<b>Smart Notice Bot</b> sends information about students' interests by e-mail.
</div>
<br>
<button type="button" style="background-color:#08355a; border-radius: 1.5rem; padding: 0.75rem 1.25rem;
    font-size: 1.25rem; margin-right: 1.5rem;" class="btn btn-primary" onclick="location.href='https://github.com/Smart-Notice-Bot/Smart.Notice.Bot'">Download <i class="fas fa-arrow-circle-down"></i></button>
<button type="button" style="border-radius: 1.5rem; padding: 0.75rem 1.25rem; font-size: 1.25rem;" class="btn btn-primary" onclick="location.href='https://smart-notice-bot.readthedocs.io/en/main/'">Document <i class="fas fa-arrow-right"></i></button>

## Latest News
 <ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>
