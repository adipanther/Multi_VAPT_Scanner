# 🔍 Multi VAPT Scanner

A **Vulnerability Assessment and Penetration Testing (VAPT)** tool built with **Python + Flask**.  
This scanner provides multiple modules to analyze and detect common web vulnerabilities.

---

## ✨ Features
- ✅ **URL Analysis** – Check for issues in target URLs
- ✅ **Header Security Check** – Analyze HTTP response headers
- ✅ **Subdomain Enumeration** – Find subdomains of a target
- ✅ **SQL Injection Test** – Detect possible SQLi vulnerabilities
- ✅ **XSS Test** – Identify Cross-Site Scripting issues
- ✅ **Open Redirect Check** – Detect URL redirection issues
- ✅ **Restricted Access Check** – Test for unauthorized access
- ✅ **Credential Tester** – Basic credential brute force check

---

## 🛠️ Tech Stack
- **Backend:** Python (Flask)
- **Frontend:** HTML, CSS, JavaScript (via templates/static)
- **Libraries:** `Flask`, `requests`

---

## ⚙️ Installation & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/adipanther/Multi_VAPT_Scanner.git
cd Multi_VAPT_Scanner

**## 2. Setup Virtual Environment (Recommended)**
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

**3. Install Dependencies**

pip install -r requirements.txt


**4. Run the Application**

python app.py


The app will start at:
👉 http://127.0.0.1:5000/


📂 Project Structure

Multi_VAPT_Scanner/
│── app.py                # Main Flask app
│── requirements.txt       # Dependencies
│── services/              # Vulnerability scanner modules
│   ├── url_analysis.py
│   ├── headers.py
│   ├── subdomain.py
│   ├── sql_injection.py
│   ├── xss.py
│   ├── redirect.py
│   ├── restricted_access.py
│   └── credential_tester.py
│── templates/             # HTML templates (index.html)
│── static/                # CSS, JS, Images





















