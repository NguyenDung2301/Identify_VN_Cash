import cv2
from ultralytics import YOLO

# 1. Load mô hình đã huấn luyện
model = YOLO('best.pt')

# 2. Mở Webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if success:
        # 3. Nhận diện tờ tiền trong frame
        results = model(frame, conf=0.5) # Chỉ lấy những kết quả độ tự tin > 50%

        # 4. Vẽ kết quả lên màn hình
        annotated_frame = results[0].plot()

        cv2.imshow("Nhan dien tien VND Real-time", annotated_frame)

        # Thoát nếu nhấn phím 'q'
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()