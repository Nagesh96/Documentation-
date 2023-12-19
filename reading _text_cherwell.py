# Path to your text file
text_file_path = 'path/to/your/text/file.txt'

# Read fields and values from the text file
with open(text_file_path, 'r') as file:
    lines = file.readlines()

# Create a dictionary to store field-value pairs
field_values = {}
for line in lines:
    field, value = map(str.strip, line.split('='))
    field_values[field] = value

# Cherwell connection
cherwell_client = CherwellClient.Connection(CHERWELL_BASE_URI, CHERWELL_API_KEY, CHERWELL_USERNAME, CHERWELL_PASSWORD)

# Create a new Cherwell release and set fields from the text file
cherwell_new_release = cherwell_client.create_new_business_object(cherwell_object_type, field_values)

# Save the created Cherwell new release
response = cherwell_client.save_object(cherwell_new_release)

# Check for success
if response['status'] == 'Success':
    # Print the business object record ID
    print(f"RecId for new Release: {cherwell_new_release.busObRecId}")
    print('Cherwell creation successful')
else:
    print(f'Cherwell creation failed. Error: {response["errorMessage"]}')
