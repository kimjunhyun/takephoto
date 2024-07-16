import cv2
import time
import configparser
import os

# config.ini 파일 읽기
config = configparser.ConfigParser()
config.read('config.ini')

# 설정값 불러오기
prefix = config['Settings']['prefix']
start_number = int(config['Settings']['start_number'])
max_images = int(config['Settings']['max_images'])

# 저장할 폴더 생성
output_folder = 'images'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 다양한 비디오 캡처 백엔드를 시도
backend_options = [cv2.CAP_ANY, cv2.CAP_DSHOW, cv2.CAP_MSMF, cv2.CAP_VFW]
cap = None

for backend in backend_options:
    cap = cv2.VideoCapture(4, backend)
    if cap.isOpened():
        break

if not cap or not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    exit()

# 이미지 촬영 및 저장
for i in range(start_number, start_number + max_images):
    ret, frame = cap.read()
    if not ret:
        print("프레임을 읽을 수 없습니다.")
        break
    
    filename = os.path.join(output_folder, f"{prefix}{i:03}.jpg")
    cv2.imwrite(filename, frame)
    print(f"{filename} 저장됨.")
    
    time.sleep(1)

# 카메라 해제
cap.release()
cv2.destroyAllWindows()