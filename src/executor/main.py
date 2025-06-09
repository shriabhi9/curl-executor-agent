#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crew import Executor
import os
import agentops
import json
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information
AGENTOPS_API_KEY = os.getenv("AGENTOPS_API_KEY") 

agentops.init(
    api_key=AGENTOPS_API_KEY,
    default_tags=['openai agents sdk']
)
def run():
    """
    Run the crew.
    """
    inputs = {
        'JSON': """curl -X POST https://libbi-backend-g8w0.onrender.com/api/dev-user \
-H "Content-Type: application/json" \
-d '{
  "name": "Abhishek",
  "email": "abhi910@gmail.com",
  "companyName": "tc dev",
  "physicalAddress": "58, sector 17 delhi",
  "phoneNumber": "9889788765",
  "aiExperience": "4 years",
  "paymentInfo": {
    "accountType": "paypal",
    "email": "abhishek.paypal@gmail.com"
  },
  "password": "Password@123",
  "agreement": true
}'
""",
    }
    
    try:
        result = Executor().crew().kickoff(inputs=inputs)
        print(json.dumps(result, indent=2, default=str))
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


run()