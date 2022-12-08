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
  width: 60%;
  height: 60%;
}

</style>
</head>
<body>

<img class="center-image" 
src="https://img.freepik.com/premium-vector/global-data-security-personal-data-security-cyber-data-
security-online-concept-illustration_1150-65534.jpg?w=740">

<h1>Types of SPAM</h1>

<p style="text-align: justify;">Spam can range from annoying emails to different types of internet spam, like social
media comments full of excessive links or even sensationalist headlines in media
outlets and on other websites that you can’t seem to not see.
Here are the main types of spam you can find online:</p>

<h4>1. Spam emails</h4>

<p style="text-align: justify;">Spam emails are the most common type of spam you’re likely to encounter online. They
clog up your inbox and distract you from the emails you actually want to read.
Thankfully, most email clients allow you to report, filter, and block most spam emails.</p>

<h4>2. SEO spam</h4>

<p style="text-align: justify;">Also known as “spamdexing,” SEO spam refers to the manipulation of search engine
optimization (SEO) methods to improve the rankings of a spammer’s website in search </p>

<h4>3. Content spam</h4>

<p style="text-align: justify;">Some spammers cram their pages full of popular keywords to try and rank the pages of
their website higher when people make searches with those keywords. Others will use
existing content without permission to make their own pages seem more substantial and
unique.</p>

<h4>5. Social media spam</h4>

<p style="text-align: justify;">With the rise of social media, spammers have been quick to take advantage of all the
attention on those platforms, spreading their spam via bots and other sketchy accounts.
Most social media spam contains links to commercial pages, which aim to increase
traffic or revenue for a spammer’s website.</p>

<h4>6. Social media spam</h4>

<p style="text-align: justify;">With the rise of social media, spammers have been quick to take advantage of all the
attention on those platforms, spreading their spam via bots and other sketchy accounts.
Most social media spam contains links to commercial pages, which aim to increase
traffic or revenue for a spammer’s website.</p>

<h4>7. Spam text messages and spam calls</h4>

<p style="text-align: justify;">Some spammers send text messages (SMS), push notifications, or even call your cell
phone to get your attention. Spam messages can also take the form of instant
messages via popular messaging apps like WhatsApp, Skype, and Snapchat. It's best
to block spam texts and calls from suspected spammers, not answer weird texts, and
never click links on any spam messages.</p>

<h4>8. Tech support scams</h4>

<p style="text-align: justify;">Tech support scams usually begin with a phone call from someone pretending to be an
IT professional from a legitimate company. The scammer will try to convince you there’s something wrong with your 
computer and that if you give them remote access they can
fix it. Tech support scams can also start with malicious advertisements on infected sites.</p>

<h4>9. Current events scams</h4>

<p style="text-align: justify;">The deluge of sensationalist news published daily gives spammers the opportunity to
exploit headlines to capitalize on tragedies or political events. You might receive a spam
message or spam email asking you to contribute to a fundraising campaign that isn’t
legitimate.</p>

<h4>10. Malware spam (malspam)</h4>

<p style="text-align: justify;">Malware spam is exactly what it sounds like: spam that includes malware. It’s usually
delivered to your computer or mobile device via a spam text message or spam email.
This type of spam can deliver almost any type of malware,
from ransomware to trojans to spyware.</p>


</body>""", unsafe_allow_html=True)

