import streamlit as st
import streamlit_book as stb
from PIL import Image, ImageEnhance
import pandas as pd

# Add the title for the e-tutorial
st.markdown("""<style>
.button {
  border: none;
  color: white;
  padding: 16px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  transition-duration: 0.4s;
  cursor: pointer;
}

h1{
  text-align: center;
}

.button1 {
  background-color: white; 
  color: black; 
  border: 2px solid #990000;
  align-items: center;
  display: inline-block;
  display: block;     
  width: 200px;
}  

.margin-auto {    
  margin: 0 auto;
}

.button1:hover {
  background-color: #990000;
  color: white;
}


.center {
margin: 0;
position: absolute;
top: 150%;
left: 20%;
-ms-transform: translate(-50%, -50%);
transform: translate(-50%, -50%);
}

.center2 {
margin: 0;
position: absolute;
top: 150%;
left: 80%;
-ms-transform: translate(-50%, -50%);
transform: translate(-50%, -50%);
}

.button2 {
  background-color: white; 
  color: black; 
  border: 2px solid #990000;
  align-items: center;
  display: inline-block;
  display: block;     
  width: 200px;
}  

.button2:hover {
  background-color: #990000;
  color: white;
}

.center-image {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
  height: 50%;
}

</style>
</head>
<body>

<img class="center-image" 
src="https://static.vecteezy.com/system/resources/previews/005/042/825/non_2x/cyber-security-concept-free-vector.jpg">

<h1>How to prevent SPAM</h1>

<p style="text-align: justify;">You can block spam with a few simple tips and tricks. Here are a few ways to prevent
spam emails and avoid other spam messages</p>

<h4>1. Use the spam-reporting function</h4>

<p style="text-align: justify;">Most email providers have an option (button) to
report an email as spam. By reporting spam in your email, you can “train” your inbox
to get better at detecting spam. Any spam emails detected will be sent straight to
your spam folder. If your email client isn’t auto-detecting spam and phishing emails,
switch to one that does.</p>

<h4>2. Mark which emails are not spam.</h4>

<p style="text-align: justify;">Every so often, look at your spam folder,
because sometimes legitimate messages end up there. If you find anything in your spam folder that doesn’t belong, 
move it to your inbox. That also helps train your 
spam filter to learn which emails to block and which to let through.</p>

<h4>3. Sign up for some services with alternate email addresses</h4>

<p style="text-align: justify;">Lots of ecommerce
platforms and internet services require an email address. If it’s not absolutely
necessary, don’t use your primary email for throwaway or one-time signups.</p>

<h4>4. Don’t interact with spam</h4>

<p style="text-align: justify;">When you receive spam emails or text messages, don’t
click links, don’t download attachments, and never respond to the spammer. If you
do, they may think you’re a receptive target — meaning that they’ll send you more
spam. Or the links may be infected or redirect you to fraudulent websites.</p>

<h4>5. Don’t publish your contact information</h4>

<p style="text-align: justify;">Spammers can — and do — find
contacts online. Keep your online presence as private as possible. This also
extends to your phone number, physical address, and other personal information.
Check out our guide to hiding your IP address online.</p>

<h4>6. Check for data leaks involving your email</h4>

<p style="text-align: justify;">Pop over to our free Hack Check
tool and see if your passwords have leaked. If so, follow the instructions sent to
your email to change your passwords and start removing your personal information
from the web.</p>

<h4>7. If someone you know sent you spam, tell them</h4>

<p style="text-align: justify;">If you’ve received a spam
message from a trusted contact, tell them that their account has been hacked and
used for spamming. That way, they can take corrective measures and regain
control.</p>

<h4>8. Use updated software and strong security measures</h4>

<p style="text-align: justify;">Keep your devices,
software, and apps updated to protect yourself from spammers looking to exploit
vulnerabilities. Use strong passwords for all your accounts and two-factor
authentication when signing in to secure portals.</p>

<h4>9. Use strong security software</h4>

<p style="text-align: justify;">Keep your devices,
software, and apps updated to protect yourself from spammers looking to exploit
vulnerabilities. Use strong passwords for all your accounts and two-factor
authentication when signing in to secure portals.</p>


</body>""", unsafe_allow_html=True)

