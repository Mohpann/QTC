import requests

# Make a GET request to the API endpoint
response = requests.get('https://api.example.com/financial-data')

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract the JSON data from the response
    data = response.json()

    # Process the data as needed
    # ...

    # Print the data
    print(data)
else:
    # Print an error message if the request was not successful
    print('Error:', response.status_code)