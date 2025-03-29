''' main.py

python3 main.py --model [model명] --input [파일명]

'''
import argparse
import os

INPUT = "models"
OUTPUT = "save"

def main():
    
    parser = argparse.ArgumentParser()
    
    # 몀령줄 옵션 추가
    parser.add_argument(
        "--model", 
        type=str, 
        required=True, 
        help="모델명"
    )
    
    parser.add_argument(
        "--input", 
        type=str, 
        required=True, 
        help="파일명)"
    )
    
    # 인자 파싱
    args = parser.parse_args()
    
    # 모델 로드 경로 및 저장 경로 생성
    model_load_path = os.path.join(INPUT, args.model, args.input)
    model_save_path = os.path.join(OUTPUT, args.model)
    
    # 경로 출력
    print(f"Model Load Path: {model_load_path}")
    print(f"Model Save Path: {model_save_path}")
    

if __name__ == "__main__":
    
    # main 함수 실행
    main()