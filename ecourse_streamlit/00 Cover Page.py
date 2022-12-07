import streamlit as st
import streamlit_book as stb
from PIL import Image, ImageEnhance

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
top: 130%;
left: 20%;
-ms-transform: translate(-50%, -50%);
transform: translate(-50%, -50%);
}

.center2 {
margin: 0;
position: absolute;
top: 130%;
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
  width: 70%;
  height: 70%;
}

</style>

<body>

<img class="center-image" src="https://cdn.dribbble.com/users/12459411/screenshots/20080343/media/b812e3e33e0c1b80
649a23679bb5b329.jpg">

<h1>BITWALLS SPAM MAIL DETECTOR</h1>

<p>The term spam refers to any form of unwanted, unsolicited digital communication that is sent in large quantities. 
Most spam is sent via email, but it can also be distributed by phone calls, text messages, or social media. In last few
years there have been so many attacks and problems related to spams. One of the main reasons to this is the lack of 
tools to scan spam emails and the lack of knowledge related to spams and information technology.
Reconit is a tool</p>

<button class="button button1 center"><a href="https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_button_test">
Spam Detector</a></button>
<button class="button button1 center"><a href="https://pasindubandaraa.github.io/Quiz-app/">
Quiz</a></button>
<button class="button button2 center2"><a href="https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_button_test">
Awareness</a></button>

</body>""", unsafe_allow_html=True)
