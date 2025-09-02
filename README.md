# 🧮 AI Powered Calculator  

## 📌 Overview  
The **AI Powered Calculator** is a **Streamlit-based web application** that allows users to **draw mathematical equations** on a canvas and get **step-by-step AI-powered solutions** using **Google Gemini AI**.  

This tool is designed for students, teachers, and math enthusiasts who want a quick way to solve handwritten equations with explanations.  

---

## 🚀 Features  
- ✍️ **Drawing Canvas** – Write equations with customizable pen color & width.  
- 🤖 **AI Solver** – Uses Google Gemini AI to analyze and solve handwritten equations.  
- 📊 **Step-by-Step Solutions** – Provides detailed explanations and final answers.  
- 🎨 **Modern UI** – Clean, responsive, and professional interface with custom styling.  
- ⚡ **Fast & Interactive** – Real-time results with a smooth user experience.  

---

## 🛠️ Tech Stack  
- **Frontend/UI**: [Streamlit](https://streamlit.io/)  
- **Canvas Drawing**: [streamlit-drawable-canvas](https://github.com/andfanilo/streamlit-drawable-canvas)  
- **AI Model**: [Google Gemini AI](https://ai.google/)  
- **Libraries**: OpenCV, PIL, NumPy, dotenv  

---

## 📂 Project Structure  
```
📦 AI_Powered_Calculator
 ┣ 📜 app.py              # Main Streamlit app
 ┣ 📜 requirements.txt    # Dependencies
 ┣ 📜 .env                # Environment variables (API Key)
 ┣ 📜 README.md           # Documentation
```

---

## 🔑 Setup & Installation  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/ai-powered-calculator.git
   cd ai-powered-calculator
   ```

2. **Create and activate virtual environment** (optional but recommended)  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up API Key**  
   Create a `.env` file in the root directory and add:  
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

5. **Run the application**  
   ```bash
   streamlit run app.py
   ```

---

## 🖼️ Usage  
1. Open the app in your browser (`http://localhost:8501`).  
2. Draw a mathematical equation on the canvas.  
3. Choose pen **color** and **width** in the sidebar.  
4. Click **"🧠 Analyze Equation"**.  
5. View AI-generated **step-by-step solution** in the analysis section.  

---

## 📌 Example  
- **Input (drawn on canvas):** `2x + 3 = 7`  
- **AI Output:**  
  - Equation recognized: `2x + 3 = 7`  
  - Step 1: Subtract 3 from both sides → `2x = 4`  
  - Step 2: Divide both sides by 2 → `x = 2`  
  - ✅ Final Answer: **x = 2**  

---

## 🤝 Contribution  
Feel free to fork this repo, open issues, and submit pull requests to improve this project.  

---

## 📜 License  
This project is licensed under the **MIT License** – you are free to use and modify it.  

---

## 👨‍💻 Author  
Developed by **Anuj Koli** ✨  
