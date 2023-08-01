# fetch_code
**Program to check the health of a set of HTTP endpoints.**
This Python program allows you to monitor the health of a set of HTTP endpoints listed in a YAML configuration file. The program checks the availability of the endpoints every 15 seconds and calculates the availability percentage for each domain. The results are logged to the console after each 15-second test cycle.

**Requirements**
- Python 3.x
- Requests library (to make HTTP requests)
- PyYAML library (to parse YAML configuration)
- Install the required libraries using pip:

- pip install requests pyyaml

Create a YAML configuration file with a list of HTTP endpoints to monitor. Each endpoint should include the following fields:

**url:** The URL of the HTTP endpoint (required).
method: The HTTP method to use for the request (optional, default is GET).
headers: A dictionary containing custom headers for the request (optional).
body: The JSON-encoded request body (optional).
For example, the YAML file might look like this:


- url: https://example.com/
- url: https://api.example.com/data
  method: POST
  headers:
    Authorization: Bearer your_token_here
Set the file_path variable in the script to point to the location of your YAML configuration file.

- Run the script using Python:

python health_checker.py

**Functionality**
The program loads the YAML configuration file and sets up a signal handler to handle program termination (Ctrl+C).
It periodically checks the health of each HTTP endpoint by making HTTP requests.
An endpoint is considered "UP" if the response code is in the range 200-299 (successful) and the response time is less than 500 ms.
The program calculates the availability percentage for each domain based on the counts of successful responses.
After each 15-second test cycle, the availability percentages are logged to the console.
Notes
The program runs indefinitely until you manually exit it (Ctrl+C).
The availability percentages are rounded to the nearest whole percentage.

***FYI: I have the sample yaml file in the repo.***
