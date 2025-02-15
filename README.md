# Enigma Machine Simulator: A Web-Based Cryptographic Cipher Implementation  

## 🎥 Video Demo  
[Watch the Demo](https://youtu.be/Uxmv4FdbMSY?si=dYKhkR0CIh6MklcY)  

## 📖 Overview  
The **Enigma Machine Simulator** is a Python-based recreation of the famous **Enigma encryption device** used during World War II. This project explores the inner workings of the machine by accurately implementing its encryption mechanism and providing an interactive **web-based interface** for users to experience its functionality.  

![overview](output.gif)

### 🔹 Key Technologies  
- **Python** – Implements the core Enigma Machine logic  
- **Flask** – Enables a web interface for real-time encryption  
- **HTML & CSS** – Designs the user-friendly front-end  
- **SQL** – Stores rotor and reflector configurations for efficient retrieval  

---

## 🚀 Features  

### 🔑 Enigma Machine Simulation  
✅ Supports multiple Enigma variants, including:  
   - **Commercial**  
   - **German Railway**  
   - **Swiss K**  
   - **M3 & M4 models**  
✅ Accurately replicates rotor and reflector mechanisms  
✅ Implements **Caesar Cipher adjustments** between rotors  

### 🌐 Interactive Web Interface  
✅ Built using **Flask, HTML, and CSS**  
✅ Allows selection of reflectors, rotors, and initial positions  
✅ Provides instant encryption results  

### 📊 Database Integration  
✅ Stores rotor and reflector configurations in a **SQL database**  
✅ Ensures efficient loading of machine settings  

### 🎨 Modern UI & Styling  
✅ **Matrix Rain animation** for an immersive experience  
✅ **Rounded corners & modern design elements** for enhanced usability  

### 🔍 Input Validation & Error Handling  
✅ Prevents invalid rotor/reflector selections  
✅ Redirects errors to a **custom apology page**  

---

## 📂 Project Structure  

### 🔹 Core Code  
📌 **`app.py`** – Runs the Flask web application & integrates encryption logic  
📌 **`enigma.py`** – Implements the Enigma encryption process  

### 🔹 Web Interface  
📌 **`templates/`** – HTML templates for the front-end UI  
📌 **`static/`** – CSS styles & JavaScript animations  

### 🔹 Database  
📌 **`log.sql`** – SQL script for creating the database  
📌 **`rotorstable.db`** – Stores rotor & reflector configurations  

---

## 🛠️ Implementation Journey  

### 1️⃣ Initial Concept & Development  
- Started with a **simplified three-rotor model** using a basic **Caesar Cipher**  
- Expanded to **historically accurate wiring configurations**  
- Debugged encryption results using online **Enigma simulators**  

### 2️⃣ Web Application Integration  
- Developed a **Flask-based UI** for user interaction  
- Enabled **real-time encryption** through web input  

### 3️⃣ Database Optimization  
- Migrated rotor & reflector settings to a **SQL database**  
- Improved efficiency by mapping **rotor names to wiring configurations**  

### 4️⃣ UI & User Experience Enhancements  
- Implemented **Matrix Rain animation** for a cyberpunk feel  
- Resolved styling conflicts using **CS50’s Duck debugging technique**  

### 5️⃣ Error Handling & Input Validation  
- Built **custom error messages** for invalid user inputs  
- Redirected errors to a **dedicated apology page**  

---

## ▶️ Usage  

1. Clone the repository:  
   ```sh
   git clone https://github.com/atishramkhe/enigma-machine-simulator.git
   cd enigma-machine-simulator
   ```
2. Create and activate a virtual environment (recommended):  
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```
3. Install dependencies:  
   ```sh
   pip install -r requirements.txt
   ```
4. Set up the database:  
   ```sh
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```
5. Run the application:  
   ```sh
   flask run
   ```
6. Open your browser and visit:  
   ```
   http://127.0.0.1:5000
   ```

---

## 🔮 Future Improvements  
🔹 **Add a Plugboard** – Enhance encryption accuracy by swapping letters dynamically  
🔹 **Improve UI with JavaScript** – Enable real-time visual feedback for better usability  

---

## 🤝 Contributing  
Contributions are welcome! Feel free to:  
- **Report issues** 🐞  
- **Suggest improvements** 🚀  
- **Submit pull requests** 📌  

Let's make this project even better together!  

---

## 📜 License  
This project is licensed under the **MIT License**.  

---

## 📧 Contact  
**Created by:** Atish K. Ramkhelawon  

🔗 **GitHub**: [atishramkhe](https://github.com/atishramkhe)  
🔗 **LinkedIn**: [Atish K. Ramkhelawon](https://www.linkedin.com/in/atishramkhelawon)  

---

Thank you for exploring the **Enigma Machine Simulator**! 🛠️🔐

