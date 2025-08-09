import streamlit as st
import smtplib
import textwrap
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



st.markdown("""
    <style>
        body {
            background-color: #FFE4B5;
        }

        .main-title {
            font-size: 80px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 0px;
            color: #000000;
        }

        .subtitle {
            text-align: center;
            font-size: 30px;
            font-weight: bold;
            color: #0000CD;
            margin-bottom: 20px;
        }

        /* Hover effect for images */
        img {
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            border-radius: 10px;
        }
        img:hover {
            transform: scale(1.05);
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
        }

        .service-box {
            background: #DAA520;
            padding: 30px;
            border-radius: 10px;
            font-size: 36px;
            font-weight: bold;
            box-shadow: 0 5px 15px rgba(0,0,0,1.1);
            margin-top: 0px;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .service-box:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4);
        }

        /* Hover effect for Our Services list container */
        .services-container {
            background-color: #ffffff;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .services-container:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
        }

        .contact-box {
            background: #DAA520;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 5px 15px rgba(0,0,0,1.1);
            margin-top: 10px;
        }

        .logo-img {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 200px;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)
