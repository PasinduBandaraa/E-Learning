import streamlit as st
import streamlit_book as stb

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
src="https://static.vecteezy.com/system/resources/previews/000/517/735/original/cyber-security-vector.png">
<h1>How to recognize spam</h1>

<p style="text-align: justify;">
You can often recognize spam by its apparent urgency, commercial aims, and the
unrealistic or exaggerated promises included in the message. Regardless of how it
reaches you — via email, text message, social media, or a phone call — most spam fits
into one of a handful of genres.</p>

<h1>Spamming vs Phishing</h1>

<p style="text-align: justify;">The difference between spamming and phishing lies in the intent of the spammer (or
phisher).Spammers are a nuisance, but they usually aren’t out to hurt you. Phishing
attacks, on the other hand, are carried out by cybercriminals who want to access your
personal information or infect your device with malware.</p>
<br><br>
<p style="text-align: justify;">Spammers have something to sell, and they’ve decided that spamming is an effective
technique for promoting their product or service — of course, some products and
services may be low quality or fraudulent. And while phishing attacks that cast a wide
net are a type of spam, they usually have more nefarious goals — such as
fraud, identity theft, and even corporate espionage.
What is a SPAM 4
The email shown below is an example of the infamous advance-fee “Nigerian prince”
phishing scam. A browser with anti-phishing technology, such as Avast Secure Browser,
can protect you against this type of scam</p>


</body>

""", unsafe_allow_html=True)
