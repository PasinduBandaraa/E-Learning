import streamlit as st

import pyfiglet
import sys
import socket
from datetime import datetime

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#
# s.settimeout(5)
#
#
# host = st.text_input("please enter the IP you want to scan: ")
#
#
# port = st.text_input("please enter the port you want to scan: ")
#
# # host2 = int(host)
#
#
# def portScanner(port):
#     if s.connect_ex((host,port)):
#
#         st.header("The port is closed")
#     else:
#
#         st.header("The port is open")
#
#
# portScanner(port)

x = st.text_input("please enter the IP you want to scan: ")

y = st.text_input("please enter the IP you want to scan: ")

sum = int(x+y)

st.header("The sum is: ", sum)
