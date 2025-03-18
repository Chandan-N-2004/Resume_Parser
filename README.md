# Resume_Parser
# 📄 Resume Parser

## 📌 Overview
This project is a **Python-based Resume Parser** that extracts key information such as **name, phone number, email, skills, and education** from a plain text resume using **regular expressions (regex)**.

## 🚀 Features
✅ **Extracts Name, Phone Number, Email, Skills, and Education**  
✅ **Uses Regular Expressions (Regex) for Pattern Matching**  
✅ **Stores Extracted Data in JSON Format**  
✅ **Handles Various Resume Formats (TXT, Optional PDF Support)**  
✅ **Easy to Extend and Modify**  

## 🛠 Technologies Used
- **Python** – Core logic
- **Regular Expressions (re module)** – Extracting structured data from text
- **Pandas (Optional)** – For structured data storage
- **JSON** – For output formatting

## 📂 Project Structure
```
📁 resume-parser
│── 📄 README.md
│── 📄 resume_parser.py
│── 📂 data/
│   ├── sample_resume.txt
│── 📂 output/
│   ├── parsed_resume.json
```

## 🔍 How It Works
1️⃣ **Load a Resume** – Reads a plain text resume file.  
2️⃣ **Apply Regex Patterns** – Extracts Name, Email, Phone, Skills, and Education.  
3️⃣ **Store Data** – Saves extracted details in JSON format.  

## 🛠 Installation & Usage
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/resume-parser.git
cd resume-parser
```
### 2️⃣ Install Dependencies
```sh
pip install pandas
```
### 3️⃣ Run the Parser
```sh
python resume_parser.py
```
### 4️⃣ View Extracted Data
Parsed data will be saved in `output/parsed_resume.json`.

## 📑 Example Output (JSON Format)
```json
{
    "Name": "John Doe",
    "Phone": "+1 234-567-8900",
    "Email": "johndoe@example.com",
    "Skills": ["Python", "Data Analysis", "SQL"],
    "Education": "Bachelor of Science in Computer Science, XYZ University"
}
```

## 🔥 Why This Project Matters?
📌 **Automates Resume Screening** – Useful for HR and recruiters.  
📌 **Enhances NLP & Text Processing Skills** – Regex-based parsing.  
📌 **Real-World Application** – Can be extended with ML for intelligent parsing.  

## 💻 Contributing
Contributions are welcome! Fork the repo and submit pull requests.

## 📜 License
This project is **open-source** under the **MIT License**.


