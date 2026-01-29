# b12 Submission Script

This project contains a Python script (`abc.py`) to submit a job application payload to the B12 API with a signed HMAC-SHA256 header.

## Requirements

- Python 3.7+
- `requests` library

## Setup (Recommended: Use a Virtual Environment)

1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
2. Activate the virtual environment:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Edit `abc.py` to fill in your personal details (name, email, resume link, repository link, action run link).

Run the script:

```bash
python abc.py
```

The script will:
- Generate a canonicalized JSON payload
- Sign the payload with HMAC-SHA256
- POST to `https://b12.io/apply/submission` with the required headers
- Print the response status and body

## Security

The signing secret is public for this exercise, but treat it as a secret in real implementations.
