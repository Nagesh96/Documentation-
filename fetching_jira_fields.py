from jira import JIRA

# Replace these values with your Jira server information
JIRA_SERVER = 'https://your-jira-instance.com'
JIRA_USERNAME = 'your-username'
JIRA_PASSWORD = 'your-password'

# Initialize Jira connection
jira = JIRA(server=JIRA_SERVER, basic_auth=(JIRA_USERNAME, JIRA_PASSWORD))

# Replace 'PROJECT-123' with the key of your specific issue
issue_key = 'PROJECT-123'

# Fetch issue details
issue = jira.issue(issue_key, fields=['description', 'environment', 'priority', 'customfield_12345', 'customfield_67890'])

# Access and print the field values
description = issue.fields.description
environment = issue.fields.environment
priority = issue.fields.priority.name
release_manager = issue.fields.customfield_12345  # Replace with your Release Manager field ID
release_type = issue.fields.customfield_67890  # Replace with your Release Type field ID

# Print the fetched values
print(f'Description: {description}')
print(f'Environment: {environment}')
print(f'Priority: {priority}')
print(f'Release Manager: {release_manager}')
print(f'Release Type: {release_type}')
