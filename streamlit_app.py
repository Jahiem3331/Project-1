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
                        ['🏠 Home', '🤠 About', '💼 Projects', '🛠 Skills' ,'📝 Resume', '📩 Contact' ])

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
    st.subheader('Welcome to my  Future Plan !👌')
    st.write('''
                I’m a student athlete at Medgar Evers College (CUNY), 
                majoring in business with a concentration in marketing.
            
                🎯 **Current Focus:** Marking,Trading,Communication am in to right now.
           
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
                - Relevant Coursework: Business Law, Internet & Emerging Technologies,Financial Accounting, Computer 101,
                - Activities: Track and Field ,team captain for MEC Track and filed team 
            ''')

  with st.expander('2021 - 2023: W.H Maxwell High School'):
    st.write('''
                - Graduated with honors
                -  Award for Apparel Design (Score: 5)
                -  PSAL Athetic improvement
            ''')

  st.subheader('Interests & Hobbies 🏃🏿‍♂️‍➡️')
  interests = ['Track and firld', 'Fashion ', 'Photography', ' Trading', ' GYM',  ' Skating', 'Travel',  ' Content', 'Games']

  # Display the interests in columns
  cols = st.columns(3)
  for i, interest in enumerate(interests):
    with cols[i % 3]:
      st.info(f'🔷 {interest}')
      
elif page == '💼 Projects':
    st.title ('MY Projects')
    st.write('Here are some project I have worked on:')

    # Project 1
    with st.container():
       col1, col2 = st.columns([1, 2])
      
       with col1:
             st.image('https://th.bing.com/th/id/OIP.zZP1cJUmeimIlZtdQ_0p9AHaEd?w=270&h=180&c=7&r=0&o=7&cb=ucfimgc2&dpr=1.5&pid=1.7&rm=3')
          
       with col2:
            st.subheader('🏢 office of communication')
            st.write(' Help with marketing events,Media platforms,Photograph, Media day')	
            st.caption('**Technologies:** Adobe,GoPro,CapCut,')
            

    # Project 2
    with st.container():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image('https://www.archmorebusinessweb.com/wp-content/uploads/content-archmore.jpg') 
        with col2:
          st.subheader('📱 Content Producer ')
          st.write(' Marketing content produce on the college websites')
          st.caption('**Technologies:** Adobe,GoPro,CapCut, Instagram accoun, Tiktok,Facebook')
  
elif page == '🛠 Skills': 
  st.title('Technical Skills')
  
  # Skills with progress bars
  st.subheader('Programming Languages')
  
  skills_data = {
    'Teamwork ' : 95,
    'Microsoft Office Suite ' : 70,
    'Content/Design' : 90,
    'Marketing' : 80,
    'Technical Writing' : 50
  }

  for skill, level in skills_data.items():
    col1, col2 = st.columns([1,3])
    with col1:
      st.write(skill)
    with col2:
      st.progress(level/100)

  st.subheader('Tools & Technologies')

#   col1, col2, col3 = st.columns(3)
#   with col1:
#     st.success('Excel')
#     st.info('Word')
#     st.warning('Access')

#   with col2:
#     st.success('PowerPoint')
#     st.info('Google Docs')
#     st.warning('ChatGPT/AI Tools')
    
#   with col3:
#     st.success('Presentations')
#     st.info('Writing')
#     st.warning('Social Media')

elif page == '📝 Resume':
  st.title('Resume')

  # Read PDF from my GitHub repository
  with open('Resume.pdf', 'rb') as pdf_file:
    PDFbyte = pdf_file.read()
  
  st.download_button(
    label ='🔻 Download Full Resume (PDF)',
    data = PDFbyte,
    file_name = 'Resume.pdf',
    mime ='application/pdf'
  )

elif page == '📩 Contact':
    st.title("Let's Connect!")

#   col1, = st.columns(1)

#   with col1:
#     st.subheader('Send me a message.')

#     st.write('''
#         📧 **Email:** richkid333212@gmail.com

#         🏢 **LinkedIn:** [linkedin.com/in/yourname](www.linkedin.com/in/jahiem-johnson-355670363)

#         👩‍💻 **Github:** [https://github.com/avinashjairam](https://github.com/Jahiem3331/Project-1/edit/main/streamlit_app.py)

#         📷 **Instagram:** [@yourhandle](https://www.instagram.com/_5starjah?igsh=MXRxNXVzMmxhZ3NoNQ%3D%3D&utm_source=qr)

#     ''')

#     # Fun interative element
#     st.subheader('Current Status')

#     status = st.selectbox(
#         "I'm currently:",
#         [
#             ' Running Track',
#             '📕 Making Content',
#             '☕ Studying',
#             '🎮 Gaming',
#             '😴 Chilling'
#         ]
#     )


#     st.info(f'Status: {status}')

#     # Footer
#     st.write('---')
#     st.markdown(
#         f'<center>Made with 💗 using Streamlit | © {datetime.now().year} Jahiem Johnson </center>',
#         unsafe_allow_html = True
#     )
    

















