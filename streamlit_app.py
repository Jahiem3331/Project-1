import streamlit as st
import pandas as pd 
from datetime import datetime

# Page Config
st.set_page_config(
  page_title ='Jahiem Johnson | Portfolio',
  page_icon='🎯',
  layout = 'wide'
)

# Custom CSS (optional - for styling)
st.markdown('''
                <style>
                    .main-header {font-size: 42px; font-weight: bold; text-align:center;}
                    .sub-header {font-size: 24px; text-align:center; color: #666;}
                </style>
            ''', unsafe_allow_html = True)

# Sidebar
st.sidebar.title('📍 Navigation')
page = st.sidebar.radio('Go to',
                        ['🏠 Home', '🤠 About', ' 💼 Projects', '🛠 Skills' ,'📝 Resume', '📩 Contact' ])

# Home Page
if page == '🏠 Home':
  st.markdown('<p class="main-header">Jahiem Johnson</p>', unsafe_allow_html=True)
  st.markdown('<p class="sub-header">Aspiring In Business | Medgar Evers College</p>', unsafe_allow_html=True)

  # Three Columns for stats
  col1, col2, col3 = st.columns(3)

  with col1:
      st.metric('GPA', '3.1', '📚')
  with col2:
      st.metric('Projects', '5', '💻')
  with col3:
      st.metric('Skills', '9+', '🚀')

  st.write('---')

  # Introduction with columns
  col1, col2 = st.columns([2,1])
  with col1:
    st.subheader('Welcome to my digital space!👋')
    st.write('''
                I’m a student athlete at Medgar Evers College (CUNY), majoring in business with a concentration in marketing.
            
                🎯 **Current Focus:** Marking,Trading,Communication am in to right now                            Building interactive web applications with Streamlit
            
                📚 **Currently Learning:**  Marketing Principles, Advanced, Career Planning, •	Business Law.
            
                🌱 **Fun Fact:** I can skate really well ! 
            ''')
  with col2:
    # Placeholder for image
    st.image('https://i.etsystatic.com/43918556/r/il/5dd1d0/5345459497/il_fullxfull.5345459497_jras.jpg', use_column_width=True)

# About Page
elif page == '🤠 About':
  st.title('About Me')

  # Timeline of my Professional Journey
  st.subheader('My Journey 🗺️')

  with st.expander('2025 - Present: Medgar Evers College'):
    st.write('''
                - Major: Business
                - Relevant Coursework:   •	Business Law, Internet & Emerging Technologies,Financial Accounting, Computer 101,
                - Activities: Track and Field team captain for MEC Track and filed team 
            ''')

  with st.expander('2021 - 2023: W.H Maxwell High School'):
    st.write('''
                - Graduated with honors
                -  Award for Apparel Design (Score: 5)
                -  PSAL Athetic improvement
            ''')

  st.subheader('Interests & Hobbies 🏃🏿‍♂️‍➡️')
  interests = ['Track and firld', 'Fashion ', 'Photography', ' Trading', ' GYM', 'Travel', 'Games']

  # Display the interests in columns
  cols = st.columns(3)
  for i, interest in enumerate(interests):
    with cols[i % 3]:
      st.info(f'🔷 {interest}')
elif page == '💼 Projects':
    st.title ('MY Projects')
    st.Write('Here are some project I have worked on:')

import streamlit as st

# Project 1
with st.container():
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image('https://th.bing.com/th/id/OIP.zZP1cJUmeimIlZtdQ_0p9AHaEd?w=270&h=180&c=7&r=0&o=7&cb=ucfimgc2&dpr=1.5&pid=1.7&rm=3')
    with col2:
        st.subheader('🛒 E-Commerce Price Tracker')
        st.write('Python web scraper that monitors Amazon prices and sends alerts')
        st.caption('**Technologies:** Python, BeautifulSoup, Streamlit')
        

# Project 2
with st.container():
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image('https://i.pinimg.com/736x/95/75/91/957591296622900be1b004289d040dae.jpg')
    with col2:
        st.subheader('📊 Student Grade Calculator')
        st.write('Interactive web app for calculating and visualizing grades')
        st.caption('**Technologies:** Python, Pandas, Plotly')




















