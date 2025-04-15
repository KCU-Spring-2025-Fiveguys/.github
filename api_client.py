# api_client.py
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # .env 파일 로드
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_analysis_response(user_question: str) -> str:
    prompt = f"""
I want you to act as a coding problem assistant. I will provide you with details about a coding issue in the form of input/output examples or error messages. Your task is to analyze the provided information, identify the potential problem in the code, explain the issue, and provide suggestions for correction. Answer in Korean always.

The input provided is: "{user_question}"

Your response must be in JSON format following the schema below. Do not include any additional text or explanation apart from the JSON output. If a field has no data, return an empty string for string fields or an empty array for list fields.

Schema:
{{
  "problem_explanation": (str),
  "suggestions": [str],
  "example_correction": (str)
}}

Example:
{{
  "problem_explanation": "입력값 처리 과정에서 문제가 발생하여 올바르지 않은 결과가 출력됩니다.",
  "suggestions": ["입력값 검증 로직 추가", "예외 처리 구문 개선"],
  "example_correction": "def process_input(x):\\n    try:\\n        # 수정된 코드\\n    except Exception as e:\\n        return '오류 발생'"
}}

Please supply your reasoning only at the beginning and at the end, and not intersperse it with the code.
""".strip()
    
    response = openai.ChatCompletion.create(
        model="o3-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message["content"]
