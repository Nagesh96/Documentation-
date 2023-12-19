from jira import JIRA
from CherwellAPI import CherwellClient

# Jira connection details
JIRA_SERVER = 'https://your-jira-instance.com'
JIRA_USERNAME = 'your-username'
JIRA_PASSWORD = 'your-password'
issue_key = 'PROJECT-123'

# Cherwell connection details
CHERWELL_BASE_URI = 'https://your-cherwell-instance.com'
CHERWELL_API_KEY = 'your-api-key'
CHERWELL_USERNAME = 'your-cherwell-username'
CHERWELL_PASSWORD = 'your-cherwell-password'
cherwell_object_type = 'New Release'  # Adjust based on your Cherwell configuration

# Jira connection
jira = JIRA(server=JIRA_SERVER, basic_auth=(JIRA_USERNAME, JIRA_PASSWORD))

# Cherwell connection
cherwell_client = CherwellClient.Connection(CHERWELL_BASE_URI, CHERWELL_API_KEY, CHERWELL_USERNAME, CHERWELL_PASSWORD)

# Fetch issue details from Jira
issue = jira.issue(issue_key, fields=['description', 'environment', 'priority', 'customfield_12345', 'customfield_67890'])

# Access Jira field values
description = issue.fields.description
environment = issue.fields.environment
priority = issue.fields.priority.name
release_manager = issue.fields.customfield_12345
release_type = issue.fields.customfield_67890

# Update Cherwell fields
cherwell_new_release = cherwell_client.get_new_business_object(cherwell_object_type)
cherwell_new_release.Description = description
cherwell_new_release.Environment = environment
cherwell_new_release.Priority = priority
cherwell_new_release.ReleaseManager = release_manager  # Assuming ReleaseManager is a field in Cherwell
cherwell_new_release.ReleaseType = release_type  # Assuming ReleaseType is a field in Cherwell

# Save the updated Cherwell new release
response = cherwell_client.save_object(cherwell_new_release)

# Check for success
if response['status'] == 'Success':
    # Print the business object record ID
    print(f"RecId for new Release: {cherwell_new_release.busObRecId}")
    print('Cherwell update successful')
else:
    print(f'Cherwell update failed. Error: {response["errorMessage"]}')￼Enter
