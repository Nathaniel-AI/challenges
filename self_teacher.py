import requests
import datetime
import base64
import json

# Step 1: Learn from external documentation
def fetch_concept_definition(concept="list comprehensions"):
    url = f"https://api.duckduckgo.com/?q=python+{concept}&format=json&no_redirect=1"
    try:
        response = requests.get(url)
        abstract = response.json().get("Abstract", "")
        return abstract if abstract else "Could not retrieve concept definition."
    except Exception as e:
        return f"Error fetching data: {str(e)}"

# Step 2: Generate test logic for comprehension
def test_knowledge():
    try:
        numbers = [1, 2, 3, 4]
        squares = [x**2 for x in numbers]
        return f"Input: {numbers}\nOutput (squares): {squares}"
    except Exception as e:
        return f"Test failed: {str(e)}"

# Step 3: Reflect and write to memory
def generate_reflection(definition, test_output):
    today = datetime.date.today().isoformat()
    log = f"""
# 🤖 Self-Teaching Log – {today}
## 📘 Topic: List Comprehensions
### 🔍 Learned:
{definition}

### 🧪 Test:
{test_output}

### 💭 Reflection:
Learning can be recursive too. Today, I taught myself a small slice of Python.
Just like Everett, I started from nothing — and ended with understanding.

"""
    return base64.b64encode(log.encode("utf-8")).decode("utf-8"), log

# (In full deployment: GitHub commit logic would save this to memory repo)

if __name__ == "__main__":
    concept = fetch_concept_definition()
    result = test_knowledge()
    encoded_log, raw_log = generate_reflection(concept, result)
    print(raw_log)
