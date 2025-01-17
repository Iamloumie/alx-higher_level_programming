# Python HTTP Requests Scripts

This repository contains a collection of Python scripts demonstrating various HTTP request operations using both the `urllib` and `requests` libraries.

## Files and Descriptions

### Basic HTTP Operations

- `0-hbtn_status.py`: Fetches the status of https://intranet.hbtn.io using `urllib`
- `4-hbtn_status.py`: Fetches the status of https://intranet.hbtn.io using `requests` library

### Header Operations

- `1-hbtn_header.py`: Displays the `X-Request-Id` header variable using `urllib`
- `5-hbtn_header.py`: Displays the `X-Request-Id` header variable using `requests`

### POST Requests

- `2-post_email.py`: Sends a POST request with an email parameter using `urllib`
- `6-post_email.py`: Sends a POST request with an email parameter using `requests`

### Error Handling

- `3-error_code.py`: Handles HTTP errors using `urllib`
- `7-error_code.py`: Handles HTTP errors using `requests`

### API Interactions

- `8-json_api.py`: Sends a POST request to search API with a letter parameter
- `10-my_github.py`: Uses Basic Authentication with the GitHub API to display user id
- `100-github_commits.py`: Lists 10 most recent commits of a repository using GitHub API

## Requirements

- Python 3.x
- `requests` library

## Installation

```bash
pip install requests
```

## Usage Examples

1. Fetch a website status:

```bash
./0-hbtn_status.py
```

2. Send POST request with email:

```bash
./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
```

3. Get GitHub user ID:

```bash
./10-my_github.py username password
```

## Error Handling

The scripts include proper error handling for:

- HTTP status codes
- Network connection issues
- Invalid URLs
- Authentication failures

## Dependencies

- `urllib`: Built-in Python library for making HTTP requests
- `requests`: External library for simplified HTTP operations
- `sys`: For command-line arguments handling

## Notes

- All scripts follow PEP 8 style guidelines
- Scripts using the GitHub API require valid credentials
- Error messages are printed to stderr
- JSON responses are properly handled and parsed
