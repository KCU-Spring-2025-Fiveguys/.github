# server.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
from api_client import get_analysis_response

# FastAPI 인스턴스 생성
app = FastAPI(title="코테 튜터 API")

# 요청 모델: 클라이언트가 보내는 JSON 구조를 정의합니다.
class AnalysisRequest(BaseModel):
    question: str

@app.post("/analyze")
def analyze(request: AnalysisRequest):
    # 클라이언트가 보낸 질문(예: 에러 메시지 또는 Input/Output 정보)을 읽어옴
    question = request.question.strip()
    
    # 기존 api_client 모듈을 사용해 OpenAI API에 질문 전달 및 결과 받아오기
    response_text = get_analysis_response(question)
    
    # 받아온 결과를 JSON으로 파싱
    try:
        response_data = json.loads(response_text)
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="응답을 JSON으로 파싱하는데 실패했습니다.")
    
    return response_data

# 로컬 테스트를 위한 실행 코드
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
