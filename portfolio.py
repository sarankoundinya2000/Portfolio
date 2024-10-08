import streamlit as st
import base64

# Setting the page layout
st.set_page_config(page_title="My Portfolio", layout="wide")

# CSS styles
st.markdown("""
    <style>
    /* Navigation menu styles */
    .nav-menu {
        position: fixed;
        top: 0;
        width: 100%;
        background-color: #f8f9fa;
        z-index: 9999;
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 10px 0;
    }
    .nav-menu a {
        margin: 0 15px;
        text-decoration: none;
        color: black;
        font-size: 16px;
        font-weight: bold;
    }
    .nav-menu a:hover {
        color: #4CAF50;
    }

    /* Adjust the main content to start below the fixed nav menu */
    .main-content {
        margin-top: 70px;
    }

    .text-reveal-container {
        display: flex;
        align-items: center;
        height: 100px;
    }
    
    .text-reveal {
        font-size: 28px;
        font-weight: bold;
        background: linear-gradient(90deg, #4CAF50, #36c);
        background-clip: text;
        -webkit-background-clip: text;
        color: transparent;
        white-space: nowrap;
        overflow: hidden;
        display: inline-block;
        animation: text-reveal-sequence 12s linear infinite;
    }
    
    @keyframes text-reveal-sequence {
        0% { content: " "; clip-path: inset(0 100% 0 0); }
        8% { clip-path: inset(0 0 0 0); }
        25% { clip-path: inset(0 0 0 0); }
        33% { clip-path: inset(0 100% 0 0); }
        42% { clip-path: inset(0 100% 0 0); }
        50% { clip-path: inset(0 0 0 0); }
        58% { clip-path: inset(0 0 0 0); }
        66% { clip-path: inset(0 100% 0 0); }
        75% { clip-path: inset(0 100% 0 0); }
        83% { clip-path: inset(0 0 0 0); }
        91% { clip-path: inset(0 0 0 0); }
        100% { clip-path: inset(0 100% 0 0); }
    }

    .text-reveal::before {
        content: "Machine Learning Engineer";
        animation: text-cycle 12s linear infinite;
    }

    @keyframes text-cycle {
        0%, 33% { content: "Machine Learning Engineer"; }
        33.34%, 66% { content: "Gen-AI Enthusiast"; }
        66.34%, 100% { content: "Software Developer"; }
    }

    /* Contact icons styles */
    .contact-icons {
        display: flex;
        justify-content: center;
        gap: 20px;
        padding: 20px 0;
    }

    .contact-icons img {
        width: 40px;
        height: 40px;
    }

    .contact-icons a {
        text-decoration: none;
        color: inherit;
    }

    </style>
""", unsafe_allow_html=True)

# Navigation menu at the top
st.markdown("""
<nav class="nav-menu">
    <a href="#home">Home</a>
    <a href="#about">About</a>
    <a href="#skills">Skills</a>
    <a href="#experience">Experience</a>
    <a href="#services">Services</a>
    <a href="#portfolio">Portfolio</a>
    <a href="#research">Research</a>
    <a href="#blog">Blog</a>
    <a href="#contact">Contact</a>
</nav>
""", unsafe_allow_html=True)

# Main content starts here
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Home Section
st.markdown('<a id="home"></a>', unsafe_allow_html=True)
col1, col2 = st.columns([2,1])  # Adjust the proportion as needed

with col1:
    st.title("Hi, I'm Saran Koundinya 👋")
    st.markdown('<div class="text-reveal-container"><div class="text-reveal"></div></div>', unsafe_allow_html=True)

    # Button to download resume (PDF)
    with open("SaranKoundinya_tummalagunta.pdf", "rb") as file:  # Replace with your actual resume file path
        btn = st.download_button(
            label="Download Resume",
            data=file,
            file_name="Saran_Resume.pdf",  # File name for download
            mime="application/pdf",
            key="resume_download"
        )

with col2:
    st.image("LinkedIN DP.jpeg", width=250)  # Replace with your image file

st.write("""
## Welcome to My Portfolio!
I'm glad you're here. Explore my journey in Machine Learning, AI, and Software Development. Take a look at my projects, my skills, and learn        more about my academic and professional background. I hope you find my work interesting and inspiring!
""")

st.markdown("""
<div style="text-align:center; font-size: 2em; color:#F9F3F3;">
🚀 Explore, Learn, Innovate!
</div>
""", unsafe_allow_html=True)

#st.write("Let's embark on this journey together and make great things happen! 😎")

# Adding more elements like stickers using text-based icons

# About Section
st.markdown('<a id="about"></a>', unsafe_allow_html=True)
st.header("About")
st.write("""
I'm Saran Koundinya, a Machine Learning Engineer and Software Developer with a Master’s in Engineering Science (Artificial Intelligence) from the University at Buffalo. With nearly two years of industry experience, I’ve implemented AI solutions that reduced equipment downtime by 40% and improved performance by 70% at AssetSense Technologies. My expertise spans machine learning, reinforcement learning, and cloud technologies like AWS, and I am passionate about leveraging AI to solve complex, real-world problems.

In the field of Generative AI, I developed ReadRobo, an advanced OCR and document classification system, and Smart Conversations on Wheels, a voice chatbot for automating customer interactions in car showrooms. I am currently collaborating with a research professor on a project aimed at making websites more accessible to visually impaired users. I’m always open to collaborating on innovative projects—Let's collaborate and build innovative solutions!
""")



# Tech-Stack Section with Expanders
st.markdown('<a id="Skills & Tools "></a>', unsafe_allow_html=True)
st.header("Skills & Tools")

st.markdown("""
<style>
    .stExpander {
        font-size: 19px !important;
    }
    .stExpander .st-emotion-cache-1795nqf {
        font-size: 24px !important;
    }
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

def create_expander(title, content):
    return st.markdown(f"""
    <div class="stExpander">
        <details>
            <summary>{title}</summary>
            <p>{content}</p>
        </details>
    </div>
    """, unsafe_allow_html=True)

with col1:
    create_expander("📊 Machine Learning (2+ Years XP)", """
    • Classification and Regression Models<br>
    • Exploratory Data Analysis (EDA)<br>
    • Feature Engineering<br>
    • MLOps<br>
    • Data Preprocessing
    """)
    
    create_expander("🧠 Deep Learning (2+ Years XP)", """
    • Artificial Neural Networks (ANNs)<br>
    • Recurrent Neural Networks (RNNs)<br>
    • Convolutional Neural Networks (CNNs)
    """)
    
    create_expander("💻 Programming Languages (2+ Years XP)", """
    • Python (Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn, Plotly, TensorFlow)<br>
    • SQL<br>
    • Java<br>
    • C
    """)

with col2:
    create_expander("🤖 Reinforcement Learning (2+ Years XP)", """
    • Markov Decision Process-based models<br>
    • Q-learning<br>
    • Policy Gradient methods<br>
    • Actor Critic Methods<br>
    • Function Approximations
    """)
    
    create_expander("🌟 Generative AI", """
    • Language Model (LLM) Development & Fine tuning<br>
    • Retrieval-Augmented Generation (RAG)<br>
    • Chatbot Development<br>
    • Prompt Engineering
    """)
    
    create_expander("🛠️ Tools & Soft skills (4+ Years XP)", """
    • <strong>Tools</strong>: Slack, Notion, Tableau, VS Code, GitHub, AWS<br>
    • <strong>Soft Skills</strong>: Communication, Leadership, Teamwork
    """)


# Experience Section
st.markdown('<div class="experience-section">', unsafe_allow_html=True)
st.markdown('<div class="experience-header"><h2>Experience</h2><p>My professional & academic journey </p></div>', unsafe_allow_html=True)
# Set up the selection radio buttons side by side
col1, col2 = st.columns(2)
with col1:
    option = st.radio("Select Experience Type", ('Professional', 'Academic'), label_visibility="hidden", key='experience_selection')
with col2:
    pass  # Keep the second column empty to maintain side-by-side layout

# CSS styles for layout and appearance
st.markdown("""
<style>
.experience-section {
    padding: 20px;
    border-radius: 10px;
    text-align: center;
}
.experience-header {
    text-align: left;
    margin-bottom: 30px;
}
.experience-header h2 {
    font-size: 2.5em;
    margin-bottom: 10px;
}
.experience-header p {
    font-size: 1.2em;
    color: #a6a6a6;
}
.experience-columns {
    display: flex;
    justify-content: center;
}
.experience-column {
    width: 60%;
}
.experience-title {
    font-size: 1.5em;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
}
.experience-title i {
    margin-right: 10px;
    font-size: 1.2em;
}
.timeline {
    position: relative;
    padding-left: 30px;
}
.timeline:before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 2px;
    background: #bd93f9;
}
.timeline-item {
    position: relative;
    margin-bottom: 30px;
}
.timeline-item:before {
    content: '';
    position: absolute;
    left: -34px;
    top: 0;
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: #bd93f9;
}
.timeline-content h3 {
    font-size: 1.2em;
    margin-bottom: 5px;
}
.timeline-content h4 {
    font-size: 1.3em;
    color: #ffffff;
    margin-bottom: 5px;
}
.timeline-content p {
    font-size: 1.0em;
    color: #8044CE;
}
.emoji {
    font-size: 1.5em;
    margin-right: 10px;
}
</style>
""", unsafe_allow_html=True)

# Main experience section


# Display the selected option (Professional or Academic) with centered content
if option == 'Professional':
    st.markdown("""
    <div class="experience-columns">
        <div class="experience-column">
            <div class="experience-title"><span class="emoji">💼</span> Professional Experience</div>
            <div class="timeline">
                <div class="timeline-item">
                    <div class="timeline-content">
                        <h3>Project Researcher in Generative AI for Web Accessibility - </h3>
                        <h4>University at Buffalo</h4>
                        <p>Aug 2024 - Current</p>
                    </div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-content">
                        <h3> Machine Learning Engineer , R&D</h3>
                        <h4> AssetSense Technologies Pvt. Ltd</h4>
                        <p>Feb 2022 - June 2023</p>
                    </div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-content">
                        <h3>Software Engineer Trainee(Machine Learning)</h3>
                        <h4>AssetSense Technologies Pvt. Ltd</h4>
                        <p>Aug 2021 - Jan 2022</p>
                    </div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-content">
                        <h3>Data Analyst Intern</h3>
                        <h4>ANZ</h4>
                        <p>June 2020 - July 2020</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif option == 'Academic':
    st.markdown("""
    <div class="experience-columns">
        <div class="experience-column">
            <div class="experience-title"><span class="emoji">🎓</span> Academic Experience</div>
            <div class="timeline">
                <div class="timeline-item">
                    <div class="timeline-content">
                        <h3>Masters Degree - Artificial Intelligence</h3>
                        <h4>University at Buffalo , SUNY </h4>
                        <p>Aug 2023 - Current</p>
                    </div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-content">
                        <h3>B.Tech - Information Technology</h3>
                        <h4>J.B.I.E.T</h4>
                        <p>2017 - 2021</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


#st.header("Experience")
#st.write("""
#- **Software Developer - Machine Learning**, AssetSense Technologies Pvt. Ltd (Feb 2022 - June 2023)
#- **Data Analyst Intern**, ANZ (June 2020 - July 2020)
#""")


# Portfolio Section
import streamlit as st
from PIL import Image

# Technical Contributions Section
st.markdown('<a id="Technical Contributions"></a>', unsafe_allow_html=True)
st.header("Technical Contributions")

# Sample project data: titles, descriptions, images, and full page links
projects = [
    {
        "id": "readrobo",
        "title": "ReadRobo - Intelligent Document OCR and Classification System",
        "description": "Engineered a scalable OCR application capable of processing and classifying 100+ documents, leveraging AI models and innovative RAG approaches for intelligent document embedding and retrieval.",
        "image": "readrobo_image.png",  # Path to your image file
        "full_content": """ 
        Title : ReadRobo - Intelligent Document OCR and Classification System
        Description:
        ReadRobo is designed to simplify document processing and classification by leveraging advanced OCR capabilities for handwritten and printed text. This system handles over 100+ document types (e.g., birth certificates, death certificates) and extracts structured data using AI models, making the retrieval of legacy records seamless and accurate.
        
        Use Case:
        Ideal for organizations managing large volumes of legacy records, ReadRobo ensures efficient classification and retrieval of critical documents. It can be applied in archives, legal settings, healthcare, or government agencies where accurate data extraction is essential for operational success.
        
        Technologies Used:
        
        Backend: Python, Groq API, Google API
        Document Embedding and Retrieval: ChromaDB, LLaMA3
        OCR: AI models for handwritten and printed text recognition
        Functionalities:
        
        Scalable OCR: Processes 100+ document types
        Intelligent Document Classification: Uses AI for embedding and retrieval
        Multiformat Handling: Handles handwritten and printed texts for both structured and unstructured data
        
        """
    },
    {
        "id": "deep_racer",
        "title": "AWS Deep Racer",
        "description": "Developed autonomous racing models using reinforcement learning, achieving a 30% improvement in lap times and outperforming 80% of AI-controlled opponents.",
        "image": "deep_racer_image.png",  # Path to your image file
        "full_content": """
         Title: AWS Deep Racer.
         
         Description:
        This project focuses on autonomous racing models trained using reinforcement learning (RL) in simulated environments. By leveraging AWS services and Python, the project enhances decision-making for autonomous vehicles, achieving a significant 30% improvement in lap times and outperforming 80% of AI-controlled opponents.

        Use Case:
        AWS Deep Racer can be used to demonstrate the potential of RL in real-world applications such as self-driving cars, autonomous navigation systems, and AI decision-making in dynamic environments. The project also serves as a competitive platform for AI enthusiasts to test their autonomous systems.
        
        Technologies Used:
        
        Backend: AWS Services, Python
        Reinforcement Learning: Custom RL models for racing optimization
        Functionalities:
        
        Autonomous Vehicle Control: RL-based decision-making
        Lap Time Optimization: 30% improvement using RL techniques
        Competitive AI Racing: Outperforms AI-controlled opponents
      """
    },
    {
        "id": "smart_conversations",
        "title": "Smart Conversations on Wheels",
        "description": "Developed a next-gen voice chatbot for car showrooms, integrating Google Calendar API and speech recognition to automate appointments and customer interactions.",
        "image": "chatbot_image.png",  # Path to your image file
        "full_content": """ 
        Title:Smart Conversations on Wheels
        Description:
        This next-gen voice chatbot was built for car showrooms, using voice recognition, text-to-speech, and appointment management features. By integrating Google Calendar API and Groq API, the chatbot handles real-time customer interactions, answering queries, scheduling appointments, and enhancing showroom efficiency.
        
        Use Case:
        Smart Conversations on Wheels automates customer interaction in car showrooms. It can be applied in industries like retail, healthcare, or hospitality, where automating customer service with natural language understanding is key to improving customer satisfaction.
        
        Technologies Used:
        
        Frontend: TensorFlow, Google Colab
        Backend: Groq API for natural language processing, Google Calendar API
        Functionalities:
        
        Voice Chatbot: Handles customer queries and schedules appointments
        Appointment Management: Uses Google Calendar for real-time scheduling
        Car Inventory Management: Integrates inventory systems for query handling
"""
    },
    
    {
        "id": "portfolio",
        "title": "Optimized Portfolio Management Using Reinforcement Learning",
        "description": "Implemented a reinforcement learning-based algorithm for optimizing portfolio management, growing initial investments by 89% in 20 days.",
        "image": "portfolio_image.png",  # Path to your image file
        "full_content": """ 
        Title: Optimized Portfolio Management Using Reinforcement Learning
        Description:
        This project applied reinforcement learning to optimize financial portfolio management. Using Q-learning, the model dynamically adjusts buy, hold, and sell strategies, increasing an initial $100,000 investment to $189,000 in just 20 days. The system maximizes returns while mitigating risk, showcasing the potential for RL in financial decision-making.
        
        Use Case:
        Financial institutions and individual investors can use this model to automate portfolio management decisions, improving long-term returns while minimizing risk. It can be applied in algorithmic trading, wealth management, and financial forecasting systems.
        
        Technologies Used:
        
        Backend: Python, Q-learning
        Frontend: Google Colab for training and simulations
        Functionalities:
        
        Portfolio Optimization: Dynamic buy, hold, and sell decisions
        Reinforcement Learning: Uses Q-learning for strategic decision-making
        High Returns: Achieves significant portfolio growth over a short period
        """
    }
]

# Get query parameters to check if a project is selected
query_params = st.experimental_get_query_params()
selected_project = query_params.get('project', [''])[0]  # Get 'project' param if exists

if not selected_project:
    # Display projects in a grid of 2 columns
    for i in range(0, len(projects), 2):
        cols = st.columns(2,gap="large")  # Create two columns
        for j, col in enumerate(cols):
            if i + j < len(projects):  # Ensure we don't go out of bounds
                project = projects[i + j]
                image = Image.open(project["image"])
                with col:
                    st.image(image, width=350)  # Set custom width for smaller images
                    if st.button(f"View {project['title']}", key=project['id']):
                        st.experimental_set_query_params(project=project['id'])  # Update query params to navigate to full page
                    #st.markdown(f'**{project["title"]}**')
                    #st.markdown(f'<p>{project["description"]}</p>', unsafe_allow_html=True)
    
else:
    # Display the selected project's full details
    project = next((proj for proj in projects if proj["id"] == selected_project), None)
    
    if project:
        st.header(project['title'])
        image = Image.open(project["image"])
        st.image(image, use_column_width=True)  # Full-size image for the project details page
        st.write(project['full_content'])
        
        # Add a back button to go back to the main project list
        if st.button("Back to Projects"):
            st.experimental_set_query_params()  # Clear the query params to go back


# Research Section
st.markdown('<a id="research"></a>', unsafe_allow_html=True)
st.header("Research")
st.write("""
I am actively involved in research on generative models, reinforcement learning, and time series forecasting. 
Some of my published work includes:

- "AutogitPy Library: Automating Git Commands with Python"
""")

# Blog Section
st.markdown('<a id="blog"></a>', unsafe_allow_html=True)
st.header("Blog")
st.write("""
I write about AI trends, tutorials, and insights. Stay updated with my latest articles!
""")

st.markdown("""
## Some Fun Facts 🎉
- 💻 I love working on innovative machine learning projects.
- 🤖 Generative AI is my passion!
- 🌱 Continuously learning and growing.
- 🎵 Music and dance keep me creative!

Let's connect and create something amazing together! 🌟
""")

# Contact Section
st.markdown('<a id="contact"></a>', unsafe_allow_html=True)
st.header("Contact")
st.write("Get in touch with me ")

st.markdown("""
<div class="contact-icons" style="display: flex; align-items: center; gap: 15px;">
    <a href="https://www.linkedin.com/in/saran-koundinya/" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/8/81/LinkedIn_icon.svg" alt="LinkedIn" width="40" height="40">
    </a>
    <a href="https://github.com/sarankoundinya2000" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" alt="GitHub" width="40" height="40">
    </a>
    <a href="mailto:koundinyasaran@gmail.com" style="text-decoration: none;">
        <span style="font-size: 40px; display: inline-block; vertical-align: middle;">📧</span>  <!-- Email emoji -->
    </a>
</div>
""", unsafe_allow_html=True)


st.write("""
Feel free to connect with me on LinkedIn, check out my projects on GitHub, or send me an email for inquiries.
""")

# Close main-content div
st.markdown('</div>', unsafe_allow_html=True)


# Enable dark mode if user selects it in Streamlit settings
st.write("Toggle light/dark mode using the settings in the top-right corner!")