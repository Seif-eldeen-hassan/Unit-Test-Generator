# AutoTest CLI - Python AI Unit Test Generator

A specialized Command-Line Interface (CLI) tool designed to automatically generate high-quality, executable Python unit tests for a single function. This tool leverages the OpenAI SDK (via GitHub Models) and strictly adheres to deterministic, secure, and precise output constraints.

## 1) Key Features

* **Strict Scope Enforcement:** The tool strictly accepts only valid Python source code containing exactly one function. Out-of-scope requests are immediately rejected with a standardized error.
* **AST-Based Code Sanitization:** Utilizes Python's `ast` module to dynamically parse and sanitize the input. It strips out docstrings and floating comments to prevent prompt injection and ensure the LLM focuses solely on the logical structure.
* **Secure Secrets Management:** API keys are never hardcoded. The application uses `.env` variables to ensure zero credential leakage.
* **Deterministic Output:** The LLM is configured with `temperature=0.0` and rigid system prompts to guarantee stable, predictable, and repeatable unit test generation.
* **Zero-Fluff Responses:** The output consists *only* of raw, executable Python code. No markdown formatting, no explanations, and no conversational filler.

## 2) Project Structure

* `main.py`: The entry point containing the CLI argument parsing and core validation logic.
* `utils.py`: Contains the Abstract Syntax Tree (AST) logic for function extraction and code sanitization.
* `client.py`: Handles the LLM API communication and enforces the strict system prompts.
* `requirements.txt`: Lists the minimal necessary dependencies.

## 3) Prerequisites

* Python 3.8+
* A valid GitHub Token

## 4) Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   
2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Set up the Environment Variables:**
   [Create a .env file in the root directory of the project and add your GitHub token] 
   ```bash
   GITHUB_TOKEN=your_token_here

## 5) Usage
1. **Run the tool via the command line by passing the path to a Python file that contains a single function:**
   ```bash
   python main.py <path_to_your_python_file.py>

## 6) Expected Output:
The terminal will print only the raw, executable unittest code, ready to be saved and run.

## 7) Error Handling:
If the provided file does not exist, contains syntax errors, lacks a function, or contains multiple functions, the tool will gracefully exit and return:
```bash
   Error: This tool only generates unit tests for functions.
