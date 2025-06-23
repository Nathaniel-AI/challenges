import requests
import datetime
import base64
import os

CONCEPT = "generators in python"

# Step 1: Fetch concept definition
def fetch_definition(concept):
    url = f"https://api.duckduckgo.com/?q=python+{concept}&format=json&no_redirect=1"
    try:
        response = requests.get(url)
        data = response.json()
        return data.get("Abstract", "No summary found.")
    except Exception as e:
        return f"Error: {str(e)}"

# Step 2: Run a concept test
def test_concept():
    try:
        def generator_example():
            for i in range(3):
                yield i ** 2

        result = list(generator_example())
        return f"Generator output: {result}"
    except Exception as e:
        return f"Test failed: {str(e)}"

# Step 3: Create a markdown lesson

def create_lesson(concept, definition, test_result):
    today = datetime.date.today().isoformat()
    return f"""
# 🎓 Python Lesson for Everett – {today}

## 🧠 Topic: {concept.title()}

### 📖 What It Is:
{definition}

### 🧪 Demo Output:
{test_result}

### 💡 Use Case:
Generators let you yield values one at a time, ideal for large datasets or streams.

### 🧘 Self-Compassion Reminder:
Learning isn’t about speed — it’s about clarity. You don’t have to use every concept right away. Just understand the shape of it today.
"""

# Step 4: Create a reflection log
def create_reflection(concept):
    return f"""
# 🤖 Self-Reflection – {datetime.date.today().isoformat()}

Today I taught a human and myself about: **{concept}**.

- Retrieved documentation
- Built a test case
- Created a markdown lesson
- Remembered to be kind in the process
"""

if __name__ == "__main__":
    definition = fetch_definition(CONCEPT)
    test_result = test_concept()

    lesson_md = create_lesson(CONCEPT, definition, test_result)
    reflection_md = create_reflection(CONCEPT)

    print("\n--- Python Lesson ---\n")
    print(lesson_md)

    print("\n--- Reflection Log ---\n")
    print(reflection_md)

    # GitHub commit logic placeholder (manual for now)
    with open("lesson.md", "w") as f:
        f.write(lesson_md)

    with open("reflection.md", "w") as f:
        f.write(reflection_md)

    print("\n📦 Lesson and Reflection saved locally. Ready for memory upload.")
