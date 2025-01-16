# HTTP Request Scripts

This repository contains a collection of shell scripts and a Python script designed to interact with HTTP servers. Each script demonstrates different functionalities related to HTTP requests and responses.

## Files Overview

### Bash Scripts

#### 0-body_size.sh

Retrieves the size of the body of the response from a specified URL.

#### 1-body.sh

Fetches and displays the body of the response from a URL, only if the status code is 200.

#### 2-delete.sh

Sends a `DELETE` request to a specified URL and displays the response.

#### 3-methods.sh

Displays all HTTP methods that a server accepts by sending an `OPTIONS` request to a specified URL.

#### 4-header.sh

Sends a `GET` request to a specified URL with a custom header.

#### 5-post_params.sh

Sends a `POST` request to a specified URL with custom parameters.

#### 100-status_code.sh

Sends a request to a specified URL and displays only the status code of the response.

#### 101-post_json.sh

Sends a JSON payload via a `POST` request to a specified URL and displays the response.

#### 102-catch_me.sh

Crafts a request that meets certain server requirements to "catch" a specific response.

### Python Script

#### 6-peak.py

Finds a peak element in an unsorted list of integers. The script is optimized for performance.

### Text File

#### 6-peak.txt

Contains a detailed explanation of the algorithm used in `6-peak.py` to find a peak element.

## Usage

### Prerequisites

Ensure you have the following installed:

- Bash
- Python 3
- curl (for HTTP requests in Bash scripts)

### Running the Scripts

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Make the Bash scripts executable:

   ```bash
   chmod +x *.sh
   ```

3. Execute the desired script. For example:
   ```bash
   ./0-body_size.sh <URL>
   ./6-peak.py
   ```

## Notes

- Replace `<URL>` with the target URL when running the scripts.
- Ensure proper permissions and dependencies are met before execution.
