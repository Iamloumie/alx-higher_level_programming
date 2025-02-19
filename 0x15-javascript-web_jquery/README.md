# JavaScript DOM Manipulation Project

This repository contains a series of HTML and JavaScript files that demonstrate various DOM manipulation techniques. Each pair of files (main.html and script.js) showcases a specific concept or functionality.

## File Structure

### Basic DOM Selection

- `0-main.html` / `0-script.js`: Introduction to DOM selectors
- `1-script.js`: Working with element IDs
- `2-main.html` / `2-script.js`: Class-based selection

### DOM Manipulation

- `3-main.html` / `3-script.js`: Modifying element attributes
- `4-main.html` / `4-script.js`: Creating and appending new elements
- `5-main.html` / `5-script.js`: Event handling basics
- `6-main.html` / `6-script.js`: Form validation

### Advanced Techniques

- `7-main.html` / `7-script.js`: DOM traversal methods
- `8-main.html` / `8-script.js`: Working with data attributes
- `9-main.html` / `9-script.js`: Dynamic styling

### AJAX and Fetch API

- `100-main.html` / `100-script.js`: Basic AJAX requests
- `101-main.html` / `101-script.js`: Fetch API implementation
- `102-main.html` / `102-script.js`: Handling JSON responses
- `103-main.html` / `103-script.js`: Error handling in asynchronous requests

## Getting Started

1. Clone this repository
2. Open any `*-main.html` file in your browser to see the corresponding JavaScript functionality
3. Inspect the matching `*-script.js` file to understand the implementation

## Prerequisites

- Basic understanding of HTML
- Familiarity with JavaScript fundamentals
- Modern web browser with developer tools

## Learning Objectives

After working through these examples, you should be able to:

- Select and manipulate DOM elements using various methods
- Handle browser events effectively
- Dynamically modify webpage content
- Implement basic form validation
- Make asynchronous requests to external resources
- Process and display data from API responses

## Usage Example

```javascript
// Example from 5-script.js - Event handling
document
  .getElementById("buttonElement")
  .addEventListener("click", function (event) {
    console.log("Button clicked!");
    event.target.classList.toggle("active");
  });
```

## Resources

For more information on DOM manipulation, check out:

- [MDN Web Docs: Document Object Model](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)
- [JavaScript.info: DOM Nodes](https://javascript.info/dom-nodes)
- [W3Schools: JavaScript HTML DOM](https://www.w3schools.com/js/js_htmldom.asp)
