import requests

def create_jira_ticket(summary, description):
    url = "https://your-domain.atlassian.net/rest/api/3/issue"
    auth = ('your-email', 'your-api-token')
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    payload = {
        "fields": {
            "project": {"key": "PROJ"},
            "summary": summary,
            "description": description,
            "issuetype": {"name": "Task"}
        }
    }
    response = requests.post(url, json=payload, auth=auth, headers=headers)
    return response.json()

if __name__ == "__main__":
    print(create_jira_ticket("Sample Issue", "This is a sample ticket created via API"))