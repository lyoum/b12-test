import requests
import json
import hmac
import hashlib
import os
from datetime import datetime, timezone

# Load secret key from environment variable
secret_key = os.getenv("SIGNING_SECRET")
if not secret_key:
    raise RuntimeError("SIGNING_SECRET not set")

# Prepare payload data
repo = os.environ["GITHUB_REPOSITORY"]
run_id = os.environ["GITHUB_RUN_ID"]
print(f"Repository: {repo}, Run ID: {run_id}")
payload = {
    "timestamp": datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z"),
    "name": "Low You Ming",
    "email": "lyming97@gmail.com",
    "resume_link": "https://my.linkedin.com/in/you-ming-low-3b7370158",
    "repository_link": repo,
    "action_run_link": run_id
}

# Canonicalize JSON: sorted keys, compact separators, UTF-8 encoding
json_body = json.dumps(payload, separators=(",", ":"), sort_keys=True).encode("utf-8")

# Compute HMAC-SHA256 signature
signing_secret = secret_key.encode("utf-8")
signature = hmac.new(signing_secret, json_body, hashlib.sha256).hexdigest()
header_signature = f"sha256={signature}"

# Prepare headers
headers = {
    "Content-Type": "application/json",
    "X-Signature-256": header_signature
}

# API endpoint
url = "https://b12.io/apply/submission"

# Send POST request
response = requests.post(url, data=json_body, headers=headers)

# Print response details
print(f"Status Code: {response.status_code}")
print(f"Response Headers: {dict(response.headers)}")
print(f"Response Body: {response.text}")

# Check if request was successful
if response.status_code == 200:
    print("\n✓ Submission successful!")
else:
    print(f"\n✗ Submission failed with status code {response.status_code}")
