import streamlit as st
import pandas as pd 
from datetime import datetime

# Page Config
st.set_page_config(
  page_title ='Avinash Jairam | Portfolio',
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
  st.markdown('<p class="main-header">Avinash Jairam</p>', unsafe_allow_html=True)
  st.markdown('<p class="sub-header">Aspiring Tech Professional | Medgar Evers College</p>', unsafe_allow_html=True)

  # Three Columns for stats
  col1, col2, col3 = st.columns(3)

  with col1:
      st.metric('GPA', '3.8', '📚')
  with col2:
      st.metric('Projects', '5', '💻')
  with col3:
      st.metric('Skills', '10+', '🚀')

  st.write('---')

  # Introduction with columns
  col1, col2 = st.columns([2,1])
  with col1:
    st.subheader('Welcome to my digital space!👋')
    st.write('''
                I am a Computer Information Systems student passionate about web development and emerging technologies. Currently learning
                HTML, CSS, JavaScript, and Python to build innovative solutions.
            
                🎯 **Current Focus:** Building interactive web applications with Streamlit
            
                📚 **Currently Learning:** Internet and Emergin Technologies (CIS 211)
            
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
                - Relevant Coursework: Internet & Emerging Technologies, Programming, Database Systems, AI
                - Activities: Track and Field team captain for MEC Track and filed team 
            ''')

  with st.expander('2021 - 2023: W.H Maxwell High School'):
    st.write('''
                - Graduated with honors
                -  Award for Apparel Design (Score: 5)
                -  PSAL Athetic improvement
            ''')

  st.subheader('Interests & Hobbies 🏀')
  interests = ['Web Development', 'AI/Machine Learning', 'Photography', 'Basketball', 'Travel', 'Baseball']

  # Display the interests in columns
  cols = st.columns(3)
  for i, interest in enumerate(interests):
    with cols[i % 3]:
      st.info(f'🔷 {interest}')
elif page == '💼 Projects':
    st.title ('MY Projects')
    st.Write('Here are some project I have worked on:')

# Project 1 
with st.container():
  coll, col2 = st.colums([1,2])





