# main.py
import json
from api_client import get_analysis_response

def main():
    print("코테 튜터 Q&A에 오신 것을 환영합니다!")
    print("문제 상황(코드의 Input/Output 또는 에러 메시지 등)을 입력해 주세요.")
    user_question = input("질문: ").strip()

    # API 호출하여 분석 결과 받기
    response_text = get_analysis_response(user_question)
    
    try:
        response_data = json.loads(response_text)
        print("\n--- 분석 결과 (JSON) ---")
        print(json.dumps(response_data, indent=4, ensure_ascii=False))
    except json.JSONDecodeError:
        print("JSON 파싱에 실패하였습니다. 원문:")
        print(response_text)

if __name__ == "__main__":
    main()
