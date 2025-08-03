# AI-Powered Customer Support Automation Bot 🚀

## Overview
This project automates L1 customer support workflows using AI. It combines an OpenAI GPT-powered chatbot, automated Jira ticket creation, and an RCA helper for analyzing log files.

## Features
- AI Chatbot for FAQs (OpenAI API)
- Jira Ticket Creation for complex queries
- Log File Analyzer for RCA summaries
- Workflow automation via Zapier (or Python scripts)

## Tech Stack
- OpenAI API
- Python (Flask/Streamlit)
- Jira REST API
- Zapier / Google Sheets API

## Folder Structure
- /chatbot: Handles AI chatbot responses
- /jira_integration: Automates ticket creation in Jira
- /rca_tool: Analyzes logs and suggests RCA
- /automation_workflow: Zapier workflow guides

## How to Run
pip install -r requirements.txt
python app.py

## Future Enhancements
- VoiceBot Layer (Google Dialogflow)
- Dashboard for visualizing RCA reports