---
title: contactus
permalink: /contactus/
---

<head>
   <style>         
      input[type=text], select, textarea {
         width: 100%; /* Full width */
         padding: 12px; /* Some padding */ 
         border: 1px solid #ccc; /* Gray border */
         border-radius: 4px; /* Rounded borders */
         box-sizing: border-box; /* Make sure that padding and width stays in place */
         margin-top: 6px; /* Add a top margin */
         margin-bottom: 16px; /* Bottom margin */
         resize: vertical /* Allow the user to vertically resize the textarea (not horizontally) */
         }
      input[type=submit] {
         background-color: #04AA6D;
         color: white;
         padding: 12px 20px;
         border: none;
         border-radius: 4px;
         cursor: pointer;
         }
      input[type=submit]:hover {
      background-color: #45a049;
      }
      .container {
         border-radius: 5px;
         background-color: #f2f2f2;
         padding: 20px;
      }
   </style>
   <h1>Contact Us</h1>
</head>
<body>
   <div class="container">
      <form action="action_page.php">
         <label for="name">name</label>
         <input type="text" id="name" name="firstname" placeholder="Your name..">
         <label for="email">email address</label>
         <input type="text" id="email" name="lastname" placeholder="Your email address..">
         <label for="subject">message</label>
         <textarea id="subject" name="subject" placeholder="Write something.." style="height:200px"></textarea>
         <input type="submit" value="SEND">
  </form>
</div>
</body>