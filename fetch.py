import time  # Importing the time module to introduce a delay
import yaml  # Importing the YAML module to load configuration data from a file
import requests  # Importing the requests library to make HTTP requests
import signal  # Importing the signal module to handle program termination

def load_configuration(file_path):
    # Function to load configuration data from a YAML file
    with open(file_path, "r") as file:
        return yaml.safe_load(file)

def health_check(endpoint):
    # Function to check the health of an endpoint by making an HTTP request
    try:
        response = requests.request(
            method=endpoint.get("method", "GET"),
            url=endpoint["url"],
            headers=endpoint.get("headers", {}),
            data=endpoint.get("body"),
            timeout=5
        )
        # Checking if the response status code is within the 2xx range (successful) and the response time is less than 500 ms
        if response.status_code >= 200 and response.status_code < 300 and response.elapsed.total_seconds() * 1000 < 500:
            return True
        return False
    except requests.RequestException:
        return False

def calculate_availability(availability_counts):
    # Function to calculate the availability percentage for each domain based on the counts
    total = sum(availability_counts.values())
    if total == 0:
        return {domain: 0 for domain in availability_counts.keys()}
    # Calculating the availability percentage for each domain
    availability_percentages = {
        domain: 100 * (count / total) for domain, count in availability_counts.items()
    }
    return availability_percentages

def log_availability(availability_percentages):
    # Function to log the availability percentages for each domain
    for domain, percentage in availability_percentages.items():
        print(f"{domain} has {round(percentage)}% availability percentage")

def signal_handler(signal, frame):
    # Function to handle the termination signal (Ctrl+C) and exit the program gracefully
    print("\nProgram exited by user.")
    exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)  # Setting up the signal handler for Ctrl+C termination

    file_path = "/Users/kishorekarthick/Desktop/sample.yaml"  # Path to the YAML configuration file (Change it accordingly)
    config = load_configuration(file_path)  # Loading configuration data from the YAML file
    
    domain_availability = {endpoint["url"]: 0 for endpoint in config}  # Initializing domain availability counts
    
    while True:
        for endpoint in config:
            domain = endpoint["url"]
            # Checking the health of each endpoint and updating the availability count
            if health_check(endpoint):
                domain_availability[domain] += 1
        
        # Calculating availability percentages and logging them
        availability_percentages = calculate_availability(domain_availability)
        log_availability(availability_percentages)
        
        time.sleep(15)  # Introducing a 15-second delay before the next iteration


