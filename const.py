import streamlit as st  

skill_col_size = 5

def menu():
    bar0, bar1, bar2, bar3, bar4= st.columns([0.1,1,1,1,1])
    bar1.page_link("Main_page.py", label="Introduction", icon="🏠")
    bar2.page_link("pages/Experience.py", label= "Experience", icon="📚")
    bar3.page_link("pages/Projects.py", label="Projects", icon="🎨")
    bar4.page_link("pages/Contact.py", label="Contacts", icon="🌏")
    st.write("")

#publication_url --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
linkedin_logo = '''                                                                                                                                          
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
  <i class="fa-brands fa-linkedin" style="font-size: 28px;"></i>                                                                           
'''

github_logo = '''
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
  <i class="fa-brands fa-github" style="font-size: 28px;"></i>                                                                           
'''

# personal info (for main page) --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
info = {
    'brief': """    
        I am an AI & Robotics enthusiast currently pursuing a B-Tech in Mathematics and Computing at the Indian Institute of Science (IISc).
        My experience spans designing autonomous rovers, working with audio datasets for machine learning models, and developing a home service robot to assist elderly individuals.
        **I am passionate about applying machine learning and robotics to solve real-world challenges**.
    """,
    'name': 'Sathvik Manthri', 
    'study': 'Indian Institute of Science (IISc)',
    'location': 'Bangalore, India',
    'interest': 'AI, Robotics, Machine Learning, Autonomous Systems',
    'skills': [
        'Python', 'C', 'C++', 'TensorFlow', 'PyTorch', 'Fusion 360', 'Keras', 
        'Gazebo', 'ROS', 'HTML & CSS', 'MATLAB', 'PySpark',
        'Scipy', 'Pandas', 'Numpy', 'LaTeX', 'Streamlit'
    ]
}

# Experience
Experience = [
    [":green[IIT Indore] | Research Intern", "Audio classification using Hierarchical Multi Task Learning", 
     "June 2024 – Present", "Indore, India", 
     """
     - Working with hierarchical multi-task learning models for audio classification
     - Applying advanced deep learning techniques to predict patterns from audio signals.
     """, 
     "Institution website", "https://chandreshiit.github.io/"],

    [":orange[IIT Indore] | Research Intern", "Deep Learning for Genetic Studies", 
     "May 2024 – Aug 2024", "Indore, India", 
     """
     - Developed deep learning and attention models to predict gaps in genome sequences.
     - Contributed to custom model architecture for handling large-scale genomic data.
     """, 
     "Institution website", "https://cse.iiti.ac.in/"],

    [":blue[Coboticca Automation Pvt. Ltd.] | Design Intern", "Home Service Robot Design",
     "May 2024 – June 2024", "Mumbai, India", 
     """
     - Designed a prototype for a robot aimed at assisting the elderly with timely medication intake.
     - Focused on creating an intuitive storage and dispensing system for the medication.
     """, 
     "Company website", "https://www.coboticca.com/"],

    [":red[IISc Robotics Club - Team Vicharaka] | Mechanical Team Lead", "Interplanetary Rover Development", 
     "August 2023 – March 2024", "Bangalore, India", 
     """
     - Led the mechanical design of a rover with a 100kg payload for autonomous navigation and soil collection.
     - Built and simulated the rover in Gazebo and Fusion 360.
     """, 
     "Team website", "https://vicharaka.iisc.ac.in/"
     # add a screenshot of the rover

     ],

    [":violet[SaiMan] | Co-Developer", "Encrypted Communication Tool",
     "June 2023", "Bangalore, India", 
     """
     - Developed an encrypted communication tool that encrypts text messages and images using pixelated canvases.
     """, 
     "Project Link", "https://sathvik040105.github.io/crypto-SaiMan/"]
]

# Portfolio Projects
Portfolio = {
    1: [':blue[Interplanetary Rover Development]',
        """
        Led the design and development of a 100kg payload autonomous rover with a robotic arm, 
        focusing on soil sample collection and life detection.
        """],
    2: [':orange[Home Service Robot] - Elderly Assistance',
        """
        Designed a robot to assist elderly individuals with daily medication intake, 
        including a storage and dispensing system for pills and medication reminders.
        """],
    3: [':green[SaiMan] - Encrypted Messaging',
        """
        Developed a text and image encryption tool using pixelated canvases to secure messages. 
        Built with a focus on privacy and data security.
        """],
    4: [':red[Term Paper/Course Project] - State Space Models',
        """
        Wrote a report and gave a 15 min presentation on State Space Models & HiPPO framework
        """]
}

# Contact Information
phone = "7396011700"
email = "sathvikm@iisc.ac.in"
linkedin_link = "https://www.linkedin.com/in/sathvik-manthri-365984259/"
github_link = "https://github.com/Sathvik040105"

# iframes --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
figma_iframe = '<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FlMYyNOptCmZb5JlYXmKkif%2FCourseEvaluation%3Ftype%3Ddesign%26node-id%3D160%253A1249%26mode%3Ddesign%26t%3DEj6BVdYEZCLgxthB-1" allowfullscreen></iframe>'

figma_link = "https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FlMYyNOptCmZb5JlYXmKkif%2FCourseEvaluation%3Ftype%3Ddesign%26node-id%3D160%253A1249%26mode%3Ddesign%26t%3DEj6BVdYEZCLgxthB-1"

StoryMap_iframe = "https://storymaps.arcgis.com/stories/dfb9689618e343cf9f6ef36d9a8329a7?header"

Evaluation_html = '''
                <div class="github-card" data-github="Rsirp0c/deis-course-evaluation" data-width="400" data-height="" data-theme="default"></div>
                <script src="https://cdn.jsdelivr.net/github-cards/latest/widget.js"></script>                
                '''
