# 🌐 Google Crawler & SMTP Email Automation

<p align="center">
<img src="https://img.shields.io/badge/Python-3.x-blue.svg">
<img src="https://img.shields.io/badge/Web%20Scraping-BeautifulSoup-green.svg">
<img src="https://img.shields.io/badge/SMTP-Email%20Automation-orange.svg">
<img src="https://img.shields.io/badge/Status-Completed-success.svg">
</p>

---

# 📖 Overview

This project was completed as part of the **Python Developer Internship at Hackveda Solutions**.

The objective of this task was to understand how Python can automate common operational activities performed in organizations. The project focuses on two important automation concepts:

* Google Search Crawling
* Email Automation using Google's SMTP Server

By implementing these features, the project demonstrates how Python can reduce manual effort, automate repetitive workflows, and interact with internet-based services.

---

# 🎯 Project Objective

The primary goals of this task were:

* Learn Python scripting for operational automation.
* Understand how search engines can be accessed programmatically.
* Learn the basics of web scraping.
* Understand email communication through SMTP.
* Automate repetitive business tasks.
* Improve Python programming skills through practical implementation.

---

# 🛠 Project Description

This project consists of two independent modules.

## 1️⃣ Google Crawler

The Google crawler is designed to retrieve search results automatically based on a keyword entered by the user.

Instead of manually opening a browser and searching for information, the crawler automates the process by sending requests, retrieving web page content, and extracting useful information.

Typical workflow:

* User enters a search keyword.
* Python sends a request.
* The HTML content is downloaded.
* Required information is extracted.
* Results are displayed to the user.

---

## 2️⃣ SMTP Email Automation

SMTP (Simple Mail Transfer Protocol) is the standard protocol used to send emails.

This module automates email sending using Python.

The application:

* Connects to Gmail's SMTP server.
* Authenticates the sender.
* Creates an email message.
* Sends the email automatically.

This eliminates the need to manually compose and send repetitive emails.

---

# ✨ Features

## Google Crawler

* Keyword-based search
* Automated web requests
* HTML parsing
* Extract useful information
* Fast execution
* Easy to customize

## Email Automation

* Gmail SMTP integration
* Secure authentication
* Send emails automatically
* Custom email subject
* Custom email body
* Error handling

---

# 🧰 Technologies Used

## Programming Language

* Python 3

## Libraries

* requests
* BeautifulSoup4
* smtplib
* email
* ssl

## Tools

* Visual Studio Code
* Git
* GitHub

---

# 📂 Project Structure

```text
Task - 1/

│── crawler.py
│── email_sender.py
│── requirements.txt
│── README.md
```

Depending on your implementation, additional configuration or helper files may also be included.

---

# ⚙ Prerequisites

Before running the project, make sure the following software is installed:

* Python 3.9 or later
* pip
* Internet connection

Install the required Python packages:

```bash
pip install requests beautifulsoup4
```

or

```bash
pip install -r requirements.txt
```

---

# ▶ How to Run

## Step 1

Clone the repository.

```bash
git clone https://github.com/mohammedzubairuddinzameer/Hackveda-Internship-projects-tasks.git
```

---

## Step 2

Navigate to the project folder.

```bash
cd "Task - 1 Google Crawler & SMTP Email Automation"
```

---

## Step 3

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Step 4

Run the Google crawler.

```bash
python crawler.py
```

---

## Step 5

Run the Email Automation module.

```bash
python email_sender.py
```

---

# 🔄 Project Workflow

```text
User Input
      │
      ▼
Python Script
      │
      ▼
Google Search Request
      │
      ▼
Retrieve HTML
      │
      ▼
Extract Information
      │
      ▼
Display Results
```

Email Automation Workflow

```text
User Input
      │
      ▼
Create Email
      │
      ▼
SMTP Authentication
      │
      ▼
Connect Gmail Server
      │
      ▼
Send Email
      │
      ▼
Success Message
```

---

# 📊 Expected Output

### Google Crawler

* Search results based on user keywords.
* Extracted webpage information.
* Organized output in the terminal.

### SMTP Email Sender

* Email successfully delivered to the recipient.
* Success or failure message displayed in the console.

---

# 🌍 Real-World Applications

The concepts implemented in this project are widely used across industries.

### Google Crawling

* SEO Analysis
* Market Research
* Competitor Analysis
* News Aggregation
* Product Monitoring
* Data Collection

### Email Automation

* Marketing Campaigns
* Customer Notifications
* OTP Services
* Password Reset Emails
* Report Distribution
* Appointment Reminders

---

# 📚 Concepts Learned

During this task, I learned:

* Python scripting
* HTTP requests
* Web scraping basics
* HTML parsing
* Working with external libraries
* SMTP protocol
* Email authentication
* Exception handling
* Python automation
* Modular programming

---

# 💡 Challenges Faced

Some common challenges during implementation included:

* Understanding HTML page structure.
* Handling website restrictions.
* Configuring Gmail SMTP authentication.
* Managing secure credentials.
* Handling runtime exceptions.

These challenges improved my debugging and problem-solving skills.

---

# 🚀 Future Improvements

Potential enhancements include:

* Support multiple search engines.
* Export search results to CSV or Excel.
* Email attachments support.
* HTML formatted emails.
* GUI using Tkinter or Streamlit.
* Scheduled email automation.
* Logging system.
* Database integration.
* Multi-threaded crawling.
* Proxy support.

---

# 🎓 Learning Outcomes

By completing this task, I gained practical experience in:

* Python programming
* Automation scripting
* Internet protocols
* Web scraping
* Email services
* Software debugging
* Python libraries
* Project documentation

This project strengthened my understanding of automation and demonstrated how Python can simplify repetitive operational tasks.

---

# 🙏 Acknowledgements

This project was completed as part of the **Python Developer Internship at Hackveda Solutions**.

The internship provided valuable exposure to Python automation, practical software development, and real-world programming tasks.

---

# 👨‍💻 Author

**Mohammed Zubair Uddin**

Python Developer | Data Science Student

GitHub:
https://github.com/mohammedzubairuddinzameer

LinkedIn:
https://www.linkedin.com/in/mohammed-zubair-uddin-zameer

---

# 📄 License

This project is intended for educational purposes and was completed during the Hackveda Python Developer Internship.

It may be used for learning and reference purposes.
