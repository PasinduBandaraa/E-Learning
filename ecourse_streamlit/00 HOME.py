import streamlit as st
import streamlit_book as stb
from PIL import Image, ImageEnhance

# Add the title for the e-tutorial
st.markdown("""<style>


h1{
  text-align: center;
}

/* This is button for spam email detector */

.button{
   background-color:#EF432F; 
   border-radius: 8px;
   border:none;
   padding: 14px 25px;
   font-size:15px;
   text-align: center;
}

.button1 a,.button3 a{
  text-decoration: none;
  color: white;
  padding: 14px 25px;
  display: inline-block;
}

.button2 a{
    text-decoration:none;
    color:white;
    font-size:15px;
    padding: 14px 25px;
    display: inline-block;

}

.margin-auto {    
  margin: 0 auto;
}

.button1:hover, .button2:hover, .button3:hover{
  background-color: #B42117;
}


.center {
margin: 0;
position: absolute;
top: 120%;
left: 20%;
-ms-transform: translate(-50%, -50%);
transform: translate(-50%, -50%);
}
/* This is button for quiz  */

.button2 {
  align-items: center;
  
  display: block;     
  width: 200px;
}  

.center2 {
margin: 0;
position: absolute;
top: 120%;
left: 50%;
-ms-transform: translate(-50%, -50%);
transform: translate(-50%, -50%);
}

.button3 {
  align-items: center;
  display: inline-block;
  display: block;     
  width: 200px;
}  

.center3 {
margin: 0;
position: absolute;
top: 120%;
left: 80%;
-ms-transform: translate(-50%, -50%);
transform: translate(-50%, -50%);
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
<img class="center-image" src="https://lh3.googleusercontent.com/j4Bj_8ZRriBPtzv7xtke0-qJ_JSS-mmvOKlivFqtg1Lf1M55vetn14P6IPkZSfbHvQ6MyS2J4391ppw9MPyyr1ariBCUHK9DdVXRbZnuoa_gF1_VmTRVHjPgt4YXMr57k9hSfHIwnWKRVlM1hVmRqvlyIbTr3Y1R15CDIkyqehweAodUWUc1GbUT_CbsownP_LL5zm2z-Ipeew1IQQhNRysQrIxHuXCjS_wLWKf5fggGIJAdZDcB-wRNc9cEpHeVI7VI7JQ7HZ6oom-Ce7oJ1ZZ2BvQxTeJ-jy74w3OL92p6jDnAhdk1LHVdWdupc80pIufw2M3FOeaneyRIYj2Tj7DEfWqoSYcx0f9nzyLzB3ZzoKktZzDzofWcBu2TGYyLnPKcL6zb89x2qEgX0MuS6df4R-OI37hjbQFC_UsciqjZZNaYjz3OaYfb1IR9XCpXzkP-AsFWqzudLbPGYD-5mdpHQo3ZfIyJlPgqwAS16jOPLHfagKN7dItmqXn4yA9xqAkLV1LAaiFjvZgSKyJ1owJAAqHXUxahL8FT1-0B7mQ_0Ms7UztjxJEpYzM3uaI_mUt7MkuhibHka59dSPeSLpiAJS2l6aEhhrIHxLIaqtpktSFUhyvTR1StX7NW58YmssZ_pGfa6DoOyDWJL2_C0Oq5bLUgR1YGVMd2JSClHQMXHNgw40xKLY2Frx8dJ5sLQLemthFRNl1wiX5WT7PmFrI9Rbo65OdwGmTMyAOhjuygzpZgo1qomZ2QWtpZwuxnic_yeNpkiEHlFtPS_3--M3WujQsh4Fm6N6D02d4v0x8nBo2SjfZs00pag7pzp_Nu2t69Hf7_OKpwIrQqRcBhcRoSTQdfn72-OoDq9BxAEWLaSZ9K65p4qx62XQ2nxV6hWw0SMYSRXi6RfHQz_bxv79pLCAXnUh3noKxXa0nNpFZfpHy2glbwfLqQ2_IjusvPsWS3svyWvSbcJLqJlPfR57_IsBp295kcsvr-qdIeT0belfILPXEFrQiC=w1921-h539-no?authuser=0">


<h1>BITWALLS SPAM MAIL DETECTOR</h1>

<p>The term spam refers to any form of unwanted, unsolicited digital communication that is sent in large quantities. 
Most spam is sent via email, but it can also be distributed by phone calls, text messages, or social media. In last few
years there have been so many attacks and problems related to spams. One of the main reasons to this is the lack of 
tools to scan spam emails and the lack of knowledge related to spams and information technology.</p>


<button class="button button1 center"><a href="https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_button_test">
Spam Detector</a></button>

<button class="button button3 center3"><a href="https://pasindubandaraa.github.io/Quiz-app/">
Quiz</a></button>

</body>""", unsafe_allow_html=True)
