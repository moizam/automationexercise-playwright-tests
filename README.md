## Running the Project Locally

Follow these steps to set up and run the project on your local machine:

### 1. Download or Clone the Repository
- Download ZIP or clone the repository to your local machine:
git clone <repository-url>

### 2. Navigate to the Project Directory
cd automationexercise-playwright-tests

### 3. Install Python
Make sure Python is installed globally on your system.
Download it from https://www.python.org/downloads/

### 4. Create a Virtual Environment
py -m venv .venv

### 5. Activate the Virtual Environment
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

# Windows (CMD)
.\.venv\Scripts\activate.bat

# Linux/macOS
source .venv/bin/activate

### 6. Install Dependencies
pip install -r requirements.txt

### 7. Run the Tests Locally
To run the automation scripts, simply execute:
pytest

### 8. Run Tests via GitHub Actions
- Visit the workflow file to trigger or check GitHub Actions:
https://github.com/moizam/automationexercise-playwright-tests/actions/workflows/main.yml
- See the test results published here:
https://moizam.github.io/gh-pages/

Your environment is now ready to run the automation tests both locally and on GitHub Actions.
