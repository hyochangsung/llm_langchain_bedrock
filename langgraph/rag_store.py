'''
- RAG 기반 검색 기능 제공
- 필요시 백터 디비 초기화(초기 데이터 구축)
    - 인메모리 구성하되, 1회성 설정 (향후 백터 디비는 외부에 구성 필요)
- 검색어 => 벡터디비 검색(유사도) => 결과값 반환
'''
from langchain_community.vectorstores import FAISS
from langchain_aws import BedrockEmbeddings
import boto3
from dotenv import load_dotenv
import os

# 환경변수 로드 => 장기키 os 환경변수에 세팅
load_dotenv()

# 임베딩 모델 구성 => 토크나이저 획득