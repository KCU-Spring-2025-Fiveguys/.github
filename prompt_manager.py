import openai
import os
from dotenv import load_dotenv

load_dotenv() 
openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = """
I want to build an extension called "코테 튜터" for real-time code analysis. The extension should monitor the code as the user writes it, detect runtime or compile-time errors, and provide analysis including:
- An explanation of the error,
- Suggestions for improvement,
- Frequently made mistakes in similar code,
- And recommend similar coding problems for practice.
- Also provide few ways to solve problem so that help to solve problem broad ways

Please return your response in JSON format with the following schema:

{
  "error_explanation": (str),
  "improvement_suggestions": [str],
  "common_mistakes": [str],
  "recommended_problems": [
    {
      "number": (int),
      "name": (str),
      "difficulty": (str),
      "topics": [str]
    }
  ]
}

Example:
{
  "error_explanation": "IndexError occurs when trying to access an index that does not exist in the list.",
  "improvement_suggestions": ["Check the list length before accessing.", "Consider using try-except block."],
  "common_mistakes": ["Off-by-one errors", "Incorrect loop boundaries"],
  "recommended_problems": [
    {
      "number": 101,
      "name": "Array Indexing Problem",
      "difficulty": "Easy",
      "topics": ["Array", "Loop"]
    }
  ]
}

Answer in Korean always. Provide your reasoning only at the beginning and at the end.
""".strip()

response = openai.ChatCompletion.create(
    model="o3-mini",
    messages=[
        {"role": "user", "content": prompt},
    ]
)

print(response.choices[0].message["content"])
