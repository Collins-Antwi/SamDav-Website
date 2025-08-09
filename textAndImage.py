import streamlit as st

st.set_page_config(layout="wide")

# --- Custom CSS Styling ---
st.markdown(
    """
    <style>
        .fade-in {
            animation: fadeIn 1s ease-in-out;
        }

        @keyframes fadeIn {
            from {opacity: 0; transform: translateY(20px);}
            to {opacity: 1; transform: translateY(0);}
        }

        .service-box {
            background-color: #ffffff;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
            transition: transform 0.3s ease-in-out;
        }

        .service-box:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 20px rgba(0, 0, 0, 0.2);
        }

        .service-box h3 {
            text-align: center;
            color: #0000CD;
            font-size: 26px;
            font-weight: bold;
            margin-bottom: 20px;
        }

        .service-box ul {
            font-size: 20px;
            color: #808000;
            line-height: 2.2;
            padding-left: 20px;
        }

        .rounded-img {
            border-radius: 20px;
            box-shadow: 0 6px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s ease-in-out;
        }

        .rounded-img:hover {
            transform: scale(1.05);
        }

        .gallery-title {
            background-color: #808000;
            padding: 10px;
            border-radius: 20px;
            text-align: center;
            margin-top: 50px;
            margin-bottom: 30px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }

        .gallery-title h3 {
            color: white;
            font-size: 30px;
            margin: 0;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Title Banner ---
st.markdown(
    """
    <div class="gallery-title">
        <h3>📸 Sample Installation Gallery</h3>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Layout Section: Text & Logo ---
col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div class="service-box fade-in">
            <h3>✅ Our Services</h3>
            <ul>
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
    st.markdown(
        """
        <img class="rounded-img" src="https://i.postimg.cc/ryHkMJvT/logo.jpg" alt="SamDav Logo" width="100%">
        """,
        unsafe_allow_html=True
    )

# --- 3-Column Image Gallery ---
st.markdown(
    """
    <div class="gallery-title">
        <h3>🖼️ Recent Projects</h3>
    </div>
    """,
    unsafe_allow_html=True
)

g1, g2, g3 = st.columns(3)

with g1:
    st.markdown(
        """
        <img class="rounded-img" src="https://i.postimg.cc/1RzFcJhW/sample1.jpg" alt="AC Install 1" width="100%">
        """,
        unsafe_allow_html=True
    )

with g2:
    st.markdown(
        """
        <img class="rounded-img" src="https://i.postimg.cc/KjGz5M6f/sample2.jpg" alt="AC Install 2" width="100%">
        """,
        unsafe_allow_html=True
    )

with g3:
    st.markdown(
        """
        <img class="rounded-img" src="https://i.postimg.cc/sDCDH1Fx/sample3.jpg" alt="AC Install 3" width="100%">
        """,
        unsafe_allow_html=True
    )
