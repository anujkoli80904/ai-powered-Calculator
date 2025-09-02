import os
import cv2
import PIL
import numpy as np
import google.generativeai as genai
import streamlit as st
from streamlit_drawable_canvas import st_canvas
from streamlit_extras.add_vertical_space import add_vertical_space
from dotenv import load_dotenv
from warnings import filterwarnings

# Suppress warnings for cleaner output
filterwarnings(action='ignore')

class Calculator:
    def streamlit_config(self):
        # Set Streamlit page config
        st.set_page_config(
            page_title="AI Math Solver",
            page_icon="🧮",
            layout="wide",
            initial_sidebar_state="expanded"
        )

        # Custom CSS for professional styling
        st.markdown("""
<style>
/* General App Background */
.stApp {
    background: #45555;
    font-family: 'Segoe UI', sans-serif;
}

/* Main Content Area */
.main {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
}

/* Sidebar */
.sidebar .sidebar-content {
    background: #2c3e50;
    color: white;
}
.sidebar .sidebar-content h1, 
.sidebar .sidebar-content h2, 
.sidebar .sidebar-content h3, 
.sidebar .sidebar-content p {
    color: white !important;
}

/* Header */
.header {
    text-align: center;
    margin-bottom: 30px;
}
.header h1 {
    color: #1a237e;
    font-weight: 700;
    font-size: 2.3rem;
}
.header p {
    color: #455a64;
    font-size: 1.05rem;
}

/* Canvas */
.canvas-container {
    background-color: e3f2fd;
    border-radius: 12px;
    padding: 5px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    margin-bottom: 25px; 
}
.canvas-container h3 {
    color: #455A64;
    margin: 0;
}

/* Card (Right Column) */
.card {
    background-color: e3f2fd;
    border-radius: 12px;
    padding: 5px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    margin-bottom: 25px;
}

.card h3 {
    color: #455A64;
    margin: 0;
}

/* Result Card */
.result-card {
    background-color: #e8f5e9;
    border-left: 5px solid #43a047;
    border-radius: 8px;
    padding: 18px;
    margin-top: 15px;
    font-size: 1.05rem;
    color: #455A64;
}



.instructions {
    background-color: #e3f2fd;
    border-radius: 8px;
    padding: 15px;
    margin-bottom: 20px;
    border-left: 4px solid #1565c0;
}
.instructions h4 {
    color: #1565c0;
    margin: 0;
}
.instructions ul {
    color: #455A64; 
    margin: 8px 0 0 18px;
    padding: 0;
}
.instructions li {
    margin-bottom: 6px;
}

/* Buttons */
.stButton button {
    background: #1e88e5;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 12px 20px;
    font-weight: 600;
    transition: all 0.3s ease;
}
.stButton button:hover {
    background: #1565c0;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

/* Pulse Animation for Analyze Button */
.pulse {
    animation: pulse 1.5s infinite;
}
    @keyframes pulse {
        0% { transform: scale(1); }
            50% { transform: scale(1.04); }
            100% { transform: scale(1); }
        }
        </style>
        """, unsafe_allow_html=True)

    def __init__(self):
        load_dotenv()
        if 'GOOGLE_API_KEY' not in os.environ:
            raise EnvironmentError("Please set the GOOGLE_API_KEY in your environment variables.")

    def analyze_image_with_genai(self, image):
        """Analyze the drawn image using the AI model."""
        # Convert the image to RGB format and prepare it for AI analysis
        imgCanvas = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        imgCanvas = PIL.Image.fromarray(imgCanvas)

        # Configure the AI model with API key
        genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
        model = genai.GenerativeModel(model_name='gemini-1.5-flash')

        # Define the prompt to send to the model
        prompt = ("You are a math tutor. Analyze the image and provide the following in a structured format:\n"
                  "1. The mathematical equation represented in the image.\n"
                  "2. The step-by-step solution to the equation.\n"
                  "3. The final answer clearly boxed.\n"
                  "4. A brief explanation of the mathematical concepts involved.\n"
                  "Make sure your response is clear, educational, and well-formatted.")

        # Request the model to generate content based on the prompt
        response = model.generate_content([prompt, imgCanvas])
        return response.text

    def main(self):
        """Main method to render UI and handle interactions."""
        # Sidebar for instructions and settings
        with st.sidebar:
            st.markdown("<h1 style='text-align: center;'>🧮 AI Math Solver</h1>", unsafe_allow_html=True)
            st.markdown("---")
            
            st.markdown("""
            <div class="instructions">
                <h4>How to Use:</h4>
                <ul>
                    <li>Draw a mathematical equation on the canvas</li>
                    <li>Choose your preferred pen color</li>
                    <li>Click the 'Analyze Equation' button</li>
                    <li>View the AI-powered solution with step-by-step explanation</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("---")
            
            # Pen settings
            st.markdown("### Pen Settings")
            stroke_color = st.color_picker("Pen Color:", "#000000")
            stroke_width = st.slider("Pen Width:", 1, 10, 3)
            
            st.markdown("---")
            
            # Additional information
            st.markdown("### About")
            st.markdown("This AI-powered tool can solve equations from handwritten input using Google's Gemini AI.")
            
        
        # Main content area
        st.markdown("<div class='header'><h1>AI Math Problem Solver</h1><p>Draw your mathematical equation below and get AI-powered solutions</p></div>", unsafe_allow_html=True)
        
        # Layout with two columns
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            <div class='canvas-container'>
            <h3>✍️ Drawing Canvas</h3>
            """, unsafe_allow_html=True)

            canvas_result = st_canvas(
                fill_color="rgba(255, 255, 255, 0.0)",
                stroke_width=stroke_width,
                stroke_color=stroke_color,
                background_color="#FFFFFF",
                height=450,
                width=700,
                drawing_mode="freedraw",
                key="canvas",
                display_toolbar=True
            )

            st.markdown("</div>", unsafe_allow_html=True)

        
        with col2:
            st.markdown("""
                <div class='card'>
                <h3>📊 Analysis</h3>
            """, unsafe_allow_html=True)

            # Analyze button with pulse animation
            st.markdown("<div class='pulse'>", unsafe_allow_html=True)
            analyze_btn = st.button("🧠 Analyze Equation", use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

            if analyze_btn:
                if canvas_result.image_data is not None:
                    with st.spinner("🔍 Analyzing your equation..."):
                        try:
                            result = self.analyze_image_with_genai(canvas_result.image_data)
                            st.session_state.last_result = result
                        except Exception as e:
                            st.error(f"❌ Error: {str(e)}")
                else:
                    st.warning("⚠️ Please draw an equation first.")

            if 'last_result' in st.session_state:
                st.markdown(f"<div class='result-card'>{st.session_state.last_result}</div>", unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)

# Initialize and run the calculator
try:
    calc = Calculator()
    calc.streamlit_config()
    calc.main()
except Exception as e:
    st.error(f"An error occurred: {str(e)}")

