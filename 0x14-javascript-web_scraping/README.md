# JavaScript API Project

This repository contains a collection of JavaScript scripts for working with APIs, focusing on Star Wars data and general HTTP requests.

## File Descriptions

### Basic Operations

- `0-readme.js`: Script to read and display the content of a file
- `1-writeme.js`: Script to write content to a file
- `2-statuscode.js`: Script to display the status code of an HTTP request

### Star Wars API Scripts

- `3-starwars_title.js`: Retrieves and displays Star Wars movie titles
- `4-starwars_count.js`: Counts specific elements in Star Wars API data
- `5-request_store.js`: Stores responses from Star Wars API requests
- `6-completed_tasks.js`: Manages and tracks completed tasks
- `100-starwars_characters.js`: Fetches and displays Star Wars character information
- `101-starwars_characters.js`: Enhanced version of character information retrieval

### Additional Files

- `cisfun`: Configuration or binary file for the project
- `my_file.txt`: Text file used for read/write operations

## Requirements

- Node.js (v12 or higher recommended)
- Internet connection for API requests
- Required npm packages (specified in package.json)

## Setup

1. Clone this repository
2. Install dependencies:

```bash
npm install
```

## Usage

Run any script using Node.js:

```bash
node <script-name>.js
```

Example:

```bash
node 3-starwars_title.js
```

## API Reference

This project primarily works with:

- Star Wars API (SWAPI)
- Local file system operations
- HTTP requests

## Error Handling

- All scripts include basic error handling for API requests
- File operations include appropriate try-catch blocks
- Network errors are properly managed

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details
