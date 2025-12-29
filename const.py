import streamlit as st  

skill_col_size = 5

def menu():
    bar0, bar1, bar2, bar3, bar4= st.columns([0.1,1,1,1,1])
    bar1.page_link("Main_page.py", label="Introduction", icon="🏠")
    bar2.page_link("pages/Experience.py", label= "Experience", icon="📚")
    bar3.page_link("pages/Projects.py", label="Projects", icon="🎨")
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
        I am an AI-ML & Robotics enthusiast currently pursuing a B-Tech in Mathematics and Computing at the Indian Institute of Science (IISc).
        My experience includes building Agentic & RAG based applications, working with deep learning models especially in Audio ML & Computer Vision, designing CAD models for robotics applications, etc.
        **I am passionate about applying machine learning and robotics to solve real-world challenges**.
    """,
    'name': 'Sathvik Manthri', 
    'study': 'Indian Institute of Science (IISc)',
    'location': 'Bengaluru, India',
    'interest': 'Deep Learning, Computer Vision, NLP, AI, Data Science, Robotics',
    'skills': [
        'Python', 'C', 'C++', 'Langchain', 'LangGraph', 'Docker', 'FastAPI', 'TensorFlow', 'PyTorch', 'Fusion 360', 'Keras', 
        'Gazebo', 'ROS', 'HTML & CSS', 'MATLAB', 'PySpark',
        'Scipy', 'Pandas', 'Numpy', 'LaTeX'
    ]
}

# Experience
Experience = [
    [":yellow[LEAP Lab, IISc Bengaluru] | Research Intern", "Auditory Attention Decoding & Target Speech Extraction", 
     "Dec 2025 – Present", "Bengaluru, India",
     "",
     "Professor's webpage", "https://eecs.iisc.ac.in/people/sriram-ganapathy/"],

    [":violet[ThoughtSpot] | Engineering Intern", "AI-Driven Liveboard Agent & Testing Infrastructure", 
     "May 2025 – July 2025", "Bengaluru, India", 
     """
     - Developed AI-Driven Liveboard Agent using LangGraph to automate visualization grouping and layout based on narrative context (Who, Why, What).
     - Implemented Dynamic Tab Handling enabling selective beautification and auto-generation of tabs, improving dashboard usability and interpretability.
     - Built Screenshot-Based Regression Pipeline that used pixel-level comparison to catch UI regressions, successfully identifying issues in background rendering.
     - Added feature-rich Liveboards to the metadata, eliminating the need for manual setup during E2E testing and accelerating test case creation.
     """, 
     "Company website", "https://www.thoughtspot.com/"],

    [":green[AI Lab, IIT Indore] | Research Intern", "Audio classification using Multi Task Learning Frameworks", 
     "June 2024 – Present", "Indore, India", 
     """
     - Co-authoring a dataset paper on gun-sound classification for gun-type and broad direction prediction.
     - Explored Hierarchical Multi-Task Learning frameworks for audio classification .
     """, 
     "Professor's webpage", "https://chandreshiit.github.io/"],

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
     "Company website", "https://www.coboticca.com/"]
]

# Portfolio Projects
Portfolio = {
    1: [':blue[Interplanetary Rover Development]',
        """
        Led the design and development of a 100kg payload autonomous rover with a robotic arm for autonomous navigation and soil collection.
        Built and simulated the rover in Gazebo and Fusion 360 as part of IISc Robotics Club - Team Vicharaka.
        """],
    2: [':orange[Home Service Robot] - Elderly Assistance',
        """
        Designed a robot to assist elderly individuals with daily medication intake, 
        including a storage and dispensing system for pills and medication reminders.
        """],
    3: [':green[SaiMan] - Encrypted Messaging',
        """
        Developed an encrypted communication tool that encrypts text messages and images using pixelated canvases.
        Built with a focus on privacy and data security.
        """],
    4: [':red[Term Paper/Course Project] - State Space Models',
        """
        Wrote a report and gave a 15 min presentation on State Space Models & HiPPO framework
        """],
    5: [':violet[Bird Scouts] - AI-Powered Bird Classification',
        """
        Built a Streamlit web app that classifies over 50 bird species through separate image and audio pipelines. 
        Features EfficientNetV2-S and YOLO for feature extraction, community map for bird sightings, and RAG-powered AI chatbot.
        Achieved ROC_AUC score of 0.996.
        """],
    6: [':blue[Community Detection in Financial Networks]',
        """
        Implemented a Stochastic Block Model framework to analyze community structures within global trade 
        networks spanning 200+ countries and correlations in the Indian equity market.
        """],
    7: [':orange[Undecidability of Validity in First Order Logic]',
        """
        Course project exploring the theoretical foundations of computability theory, specifically focusing 
        on the undecidability of validity in First Order Logic with comprehensive analysis and formal proofs.
        """
    ],
    8: [':green[Krishi Mitra]',
        """
        Built a multilingual, AI-powered conversational agent that bridges information gaps for Indian farmers. \\
        It delivers real-time crop prices, aggregated government scheme guidance, localized weather insights, and image-based crop disease diagnostics through a single web chat interface. \\
        """
    ],
    9: [':blue[TachyView]',
        """
        It is a web-based visualization tool that combines topological spines, and volume rendering to enable intuitive, interactive exploration of scalar fields directly in a browser. \\
        """
    ]
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
