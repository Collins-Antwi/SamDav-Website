import streamlit as st
import smtplib
import textwrap
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ---- PAGE CONFIGURATION ----
st.set_page_config(page_title="SamDav Refrigeration & AC Services", page_icon="❄", layout="wide")
# ---- CUSTOM CSS STYLING ----
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
            box-shadow: 0 4px 10px rgba(0, 0, 0, 1.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .services-container:hover {
            transform: translateY(-10px);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 1.3);
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
# ---- SIDEBAR MENU ----
menu = st.sidebar.radio("Go to", ["Home", "Installation Cost", "Servicing Cost", "Contact"])

# ---- HOME PAGE ----
if menu == "Home":
    st.markdown('<h1 class="main-title">SamDav Refrigeration and Air Conditioning Services</h1>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">❄ Your reliable partner for all your cooling needs ❄</div>', unsafe_allow_html=True)

       # Display three images in column
    st.markdown(
        """
        <div style="
             background-color: #DAA520;  /* Golden box */
             padding: 0px;
             border-radius: 30px;
             text-align: center;
             margin-bottom: 30px;
             box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        ">
             <h3 style="
                 color: white;
                 font-size: 36px;
                 font-weight: bold;
                 margin: 0;
             ">
                 📸 Our Showcase
             </h3>
        </div>
        """,
        unsafe_allow_html=True
      )
   
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://i.postimg.cc/6qhcFxYL/sales-Logo.jpg", caption="SALES", use_container_width=True)
    
    with col2:
        st.image("https://i.postimg.cc/HL5QfCLc/conduit-Logo.jpg", caption="CONDIUT", use_container_width=True)
       
    with col3:
        st.image("https://i.postimg.cc/fTLYMdLh/install-Logo.jpg", caption="INSTALLATION", use_container_width=True)   
    

    # Title Banner
    st.markdown(
    """
    <div style="
        background-color: #808000;
        padding: 0px;
        border-radius: 30px;
        text-align: center;
        margin-bottom: 50px;
        margin-top: 30px;
        box-shadow: 0 4px 10px rgba(0,0,0,1.2);
    ">
        <h3 style="
            color: white;
            font-size: 36px;
            font-weight: bold;
            margin: 0;
        ">
            ❄ Sample Installation Gallery ❄
        </h3>
    </div>
    """,
    unsafe_allow_html=True
    )

    # Text and Image Layout
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
        """
        <div style="
            background-color: #ffffff;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        ">
            <h2 style="
                text-align: center;
                color: #0000CD;
                font-size: 26px;
                font-weight: bold;
                margin-bottom: 15px;
            ">❄ Our Services ❄</h2>
            <ul style="
                font-size: 25px;
                color: #808000;
                line-height: 2.4;
                padding-left: 10px;
            ">
                <li>Installation and Uninstallation of AC units</li>
                <li>Servicing & Maintenance</li>
                <li>Refrigerant Refilling</li>
                <li>Fault Detection & Repairs</li>
                <li>AC Conduit</li>
                <li>Sales of Air Conditioners</li>
                <li>Free Consultation</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    with col2:
        st.image("https://i.postimg.cc/ryHkMJvT/logo.jpg", caption="SamDav Logo", use_container_width=True)

    
# ---- INSTALLATION COST ----
elif menu == "Installation Cost":
    st.markdown("### Installation Cost Estimator")
    ac_type = st.selectbox("Select AC Type", ["Split", "Floor Standing"])
    ac_horsePower = st.selectbox("Select AC Horsepower", ["1.5HP", "2.0HP", "2.5HP", "3.5HP", "5.0HP"])
    floor_type = st.radio("Installation Height", ["Ground Floor", "First Floor", "Above First Floor"])

    # Basic pricing logic
    base_price_Hp = {"1.5HP": 400, "2.0HP": 500, "2.5HP": 600, "3.5HP": 700, "5.0HP": 800}
    additionalCost = 0 if floor_type == "Ground Floor" else (150 if floor_type == "First Floor" else 250)
    
    base_price_type = {"Split": 0, "Floor Standing": 100}
    
    total = base_price_Hp[ac_horsePower] + additionalCost + base_price_type[ac_type]

    if st.button("Calculate"):
        st.success(f"Estimated Installation Cost: GHS {total:.2f}")
        
    # Showing Installation Pictures    
    st.markdown(
        """
        <div style="
             background-color: #808000;  /* Olive */
             padding: 0px;
             border-radius: 30px;
             text-align: center;
             margin-bottom: 50px;
             margin-top: 30px;
             box-shadow: 0 4px 10px rgba(1,1,1,1.2);
        ">
             <h3 style="
                 color: white;
                 font-size: 36px;
                 font-weight: bold;
                 margin: 0;
             ">
                 ❄ Sample Installation Gallery ❄
             </h3>
        </div>
        """,
        unsafe_allow_html=True
    )
   
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.image("https://i.postimg.cc/6pWRfPRN/install1.jpg", caption="OUTDOOR", use_container_width=True)
    
    with col2:
        st.image("https://i.postimg.cc/3JV5gszk/install2.jpg", caption="OUTDOOR", use_container_width=True)
       
    with col3:
        st.image("https://i.postimg.cc/mrWvnQLR/install3.jpg", caption="INDOOR", use_container_width=True)
        
    with col4:
        st.image("https://i.postimg.cc/QdGYNhRJ/install4.jpg", caption="INDOOR", use_container_width=True)
    
    with col5:
        st.image("https://i.postimg.cc/6Q1mXnwy/install5.jpg", caption="OUTDOOR", use_container_width=True)
       
    with col6:
        st.image("https://i.postimg.cc/3N2SmqGv/install6.jpg", caption="OUTDOOR", use_container_width=True)   
        
        
        

# ---- SERVICING COST ----
elif menu == "Servicing Cost":
    st.markdown("### Servicing Cost Estimator")
    number = st.number_input("How many units?", min_value=1, value=1)
    service_type = st.selectbox("Service Type", ["Basic Cleaning", "Deep Cleaning", "Gas Refill"])

    service_price = {"Basic Cleaning": 200, "Deep Cleaning": 300, "Gas Refill": 450}
    cost = number * service_price[service_type]

    if st.button("Estimate"):
        st.success(f"Total Servicing Cost: GHS {cost:.2f}")
  
    st.markdown(
        """
        <div style="
             background-color: #0000A0;  /* Dark Blue */
             padding: 0px;
             border-radius: 30px;
             text-align: center;
             margin-bottom: 50px;
             margin-top: 30px;
             box-shadow: 0 4px 10px rgba(1,1,1,1.2);
        ">
             <h3 style="
                 color: white;
                 font-size: 36px;
                 font-weight: bold;
                 margin: 0;
             ">
                 ❄ Sample Servicing Gallery ❄
             </h3>
        </div>
        """,
        unsafe_allow_html=True
    )
  
    # Image URLs (replace with your own if needed)
    image_urls = [
    "https://i.postimg.cc/6QwZY5Pq/service1.jpg",  # Image 1
    "https://i.postimg.cc/PJ8NdB70/service2.jpg",  # Image 2
    "https://i.postimg.cc/Jh2kmcnD/service3.jpg",  # Image 3
    "https://i.postimg.cc/yxzWYfzd/service4.jpg",  # Image 4
    "https://i.postimg.cc/6pQq32Fd/service5.jpg",  # Image 5
    "https://i.postimg.cc/xT1nyrgQ/service6.jpg"   # Image 6
    ]

    # How many columns per row
    cols_per_row = 3

# Display images in rows and columns
    for i in range(0, len(image_urls), cols_per_row):
        row_images = image_urls[i:i+cols_per_row]
        cols = st.columns(len(row_images))
        for col, img_url in zip(cols, row_images):
            with col:
                st.image(img_url, use_container_width=True)
      
  
  

# ---- CONTACT PAGE ----
elif menu == "Contact":
    st.markdown('<div class="contact-box">', unsafe_allow_html=True)
    st.markdown("### 📞 Contact Us")
    st.write("""
    Phone: +233 246 932 935  ||  +233 247 468 186  
    Location: Santasi-Anyinam, Kumasi-Ghana  
    Email: nanafosuhene24@gmail.com  ||  samdav.ac.service@gmail.com  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

          # Email Configuration
    EMAIL_ADDRESS = "samdav.ac.service@gmail.com"       # Replace with your Gmail address
    EMAIL_PASSWORD = "lwio zchh zafb drxi"              # Use an App Password (not your Gmail password)

    def send_email(name, contact_number, email_address, message):
        try:
        # Email setup
           msg = MIMEMultipart()
           msg['From'] = EMAIL_ADDRESS
           msg['To'] = EMAIL_ADDRESS  # You can also set this to another address
           msg['Subject'] = f"Urgent!!! Message from {name}"
                    
         
           html = f"""
<html>
  <body style="font-family: Times New Roman, serif; line-height: 2.0;">
    <h2>📬 Website Alert</h2>
    <hr>
    <hr>
    <p><strong>Name: </strong> {name}</p>
    <p><strong>Contact Number: </strong><a href="tel:{contact_number}">{contact_number}</a></p>
    <p><strong>Email Address: </strong> {email_address or "Not Provided"}</p>
    <p><strong>Message:</strong><br>{message}</p>
    <hr>
    <hr>
    <small>Message received via SamDav Website</small>
  </body>
</html>
"""

           msg.attach(MIMEText(html, "html"))

        # Sending email
           with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
               server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
               server.send_message(msg)
           return True
        except Exception as e:
           st.error(f"Failed to send message: {e}")
           return False
        
    
        # --- Initialize session state for inputs ---
    if "name" not in st.session_state:
       st.session_state.name = ""
    if "contact_number" not in st.session_state:
       st.session_state.contact_number = ""
    if "email_address" not in st.session_state:
       st.session_state.email_address = ""
    if "message" not in st.session_state:
       st.session_state.message = ""

        # --- Function to clear fields ---
    def clear_form():
       st.session_state.name = ""
       st.session_state.contact_number = ""
       st.session_state.email_address = ""
       st.session_state.message = ""
      
   
        # Streamlit form
    st.title("Send Us a Message")

    with st.form("contact_form"):
       name = st.text_input("Your Name", value=st.session_state.name)
       contact_number = st.text_input("Contact Number", value=st.session_state.contact_number)
       email_address = st.text_input("Email Address (Optional)", value=st.session_state.email_address)
       message = st.text_area("Your Message", value=st.session_state.message)
       submitted = st.form_submit_button("Send")
       if submitted:
          if name and contact_number and message:
            success = send_email(name, contact_number, email_address, message)
            if success:
                st.success("✅ Message sent successfully!")
          else:
            st.warning("⚠️ Name, Contact Number and Message are required.")
       
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            