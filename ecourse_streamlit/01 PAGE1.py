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
  width: 70%;
  height: 70%;
}

</style>
</head>
<body>

<img class="center-image" 
src="https://img.freepik.com/premium-vector/cyber-security-concept-people-work-screen-protecting-
data-confidentiality-illustration_138260-701.jpg">

<h1>How SPAM harm your business</h1>

<p style="text-align: justify;">Email spam has been around since the early days of email. By definition, spam is an
unwanted, useless message. It’s what we call junk mail.
Spam may contain different types of content and subject matter, such as
advertisements, promotions, miraculous proposals, pornography, and a myriad of other
things.
According to Gatefy’s team of email security experts, approximately 80% of the email
traffic that companies receive is junk mail.
If we stop to think that, according to data from the research firm Radicati Group, it’s
estimated that, by 2024, more than 360 billion emails will be sent and received per day,
we’re talking about billions of spam emails being sent and received daily.
The problem with spam is that it interferes a lot in the company’s environment. First,
there is an issue of productivity. Second, it’s about the security and protection of your
company’s information and data.</p>

<h3>Is spam dangerous?</h3>

<p style="text-align: justify;">Despite the fact that it’s an unwanted message, there is an imprecise idea that spam is
harmless.
However, if a lot of people continue to send spam, it’s because there’s a great interest
behind it and an opportunity to profit from it.
In the case of companies, the question is: why should I care so much about spam and
how does it affect my business?
Before we talk more about this topic, it’s important to keep in mind that any issue related
to email security should be taken seriously. The reason: email remains the most used
platform to hack companies and organizations.
Now, let’s go to the list of problems that spam can cause in the corporate environment.</p>

<h4>1. It affects productivity in your company</h4>

<p style="text-align: justify;">Spam is related to the loss of productivity in your company because it occupies your
team with an unnecessary task. It’s true that it might not take long to open a mailbox
and delete all spam.
Nonetheless, spam is a waste of time and a distraction for your employees, who could
be spending energy with more productive activities.</p>

<h4>2. It affects your business services and makes the company more vulnerable</h4>

<p style="text-align: justify;">It costs almost nothing for spammers to send millions of emails. The problem for your
business is a mass attack.
If your business isn’t ready to handle a large number of messages, many of your
services may be disrupted.
In addition to losing new business because the company’s communication has been
hampered, a mass attack often leaves your business vulnerable to other threats and
cyberattacks.</p>

<h4>3. It contains malware, such as ransomware and spyware</h4>

<p style="text-align: justify;">Today spam is one of the most widely used vectors for the spread of threats, including
malware.
Those seemingly harmless links and attachments can pose a real threat to your
business, hiding ransomware, spyware, and trojans, which allow the attacker to gain
access to the computer and then to the entire company’s network.
By the way, according to a Verizon report, about 94% of breaches involving malware
occur through the use of malicious emails.</p>

<h4>4. It contains phishing and spoofing threats</h4>

<p style="text-align: justify;">Spam is widely used for spoofing and phishing scams, which may also be related to
malware propagation.
Phishing and spoofing are used when a cybercriminal creates a fake website to steal
access credentials with the intention of hacking into your business network or gaining 
access to confidential information.
Imagine that the attacker may attempt to induce an employee to make a payment for an
invoice that doesn’t exist or to provide the system’s access credentials.</p>

<h4>5. It can cause legal problems</h4>

<p style="text-align: justify;">In an extreme case, depending on the type of spam, such as pornography spam, for
example, your company may face legal problems due to misuse of email for illegal
activity.
In addition, it may be that a cybercriminal hijacks and uses your company’s domain to
spread spam, which may have implications under some specific law.
These are extreme cases, but they deserve attention.</p>

</body>""", unsafe_allow_html=True)

