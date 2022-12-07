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
  width: 80%;
  height: 80%;
}

</style>
</head>
<body>

<img class="center-image" 
src="https://itsocial.fr/wp-content/uploads/2020/04/iStock-1069207102.jpg">

<h1>What is a SPAM</h1>

<h3>1. Why is it called spam?</h3>

<p style="text-align: justify;">The origin of the term “spam” for invasive bulk messaging refers to a Monty Python skit.
In it, a group of diners (clad in Viking costumes) loudly and repeatedly proclaim that
everyone must eat Spam — whether they want it or not. It’s similar to how an email
spammer floods your inbox with unwanted messages.
When spelled with a capital “S,” Spam refers to the canned pork product that the abovementioned
Vikings love. Spelled with a lower-case “s” and spam means the unsolicited,
disruptive emails and other messages that flood your inbox and other feeds.
Types</p>

<h4>2. Why am I getting spammed?</h4>

<p style="text-align: justify;">You receive spam messages because many companies sell their customers’ email
address and other contact info to advertisers and other third parties. And spammers
send bulk emails because it’s cheap. If only a handful of recipients respond to their
spam campaign, the spammer will likely see a positive return.
Because most spammers use spoofing to conceal their identity from recipients and
internet service providers, it’s difficult to hold them accountable. The low risk and cost of
spamming make it an attractive option for less-scrupulous advertisers and marketers.
The problem of selling data to spammers was getting so bad that in 2018, the EU
passed the General Data Protection Regulation (GDPR), a series of rules aimed at
limiting what companies are allowed to do with their customers’ personal data.
By 2021, many companies had shifted away from third-party data processing, opting
instead to keep customer data in house — reducing spam and increasing consumer
privacy.</p>

</body>""", unsafe_allow_html=True)

st.markdown("""---""", unsafe_allow_html=True)

st.subheader("Quiz Session")

st.markdown("""<p><b>What is your name?</b></p>""", unsafe_allow_html=True)
# Add a true or false question
stb.true_or_false("2. The reason why we need to put 'r' before the file path is because the file path contains "
"backslashes which are treated as escape characters. An alternative way is to use forwardslashes.", answer=True)
