# Identify VN Cash (Nhận Diện Tiền VNĐ)

Dự án này sử dụng mô hình YOLOv8 kết hợp với OpenCV để nhận diện các mệnh giá tiền Việt Nam Đồng (VNĐ) theo thời gian thực (real-time) thông qua webcam.

## Tính Năng
- Phát hiện và phân loại các loại tiền VNĐ theo thời gian thực.
- Hiển thị bounding box và độ tự tin (confidence score) trực tiếp trên màn hình camera.
- Hỗ trợ đánh giá và huấn luyện lại trên môi trường Kaggle.

## Cấu Trúc Thư Mục
- `app.py`: Script chính để chạy ứng dụng nhận diện real-time bằng webcam.
- `best.pt`: File trọng số (weights) của mô hình YOLOv8 đã được huấn luyện tốt nhất.
- `train_yolov8_kaggle.ipynb`: File Jupyter Notebook chứa script hướng dẫn huấn luyện lại mô hình trên nền tảng Kaggle.
- `Nhan-Dien-Tien-VND1.v1i.yolov8/`: Thư mục chứa cấu hình dataset (`data.yaml`) từ Roboflow (nếu có).

## Yêu Cầu Hệ Thống (Prerequisites)
Bạn cần cài đặt Python (khuyên dùng Python 3.8 trở lên) và các thư viện sau:
- `ultralytics` (YOLOv8)
- `opencv-python` (cv2)

Cài đặt nhanh thông qua pip:
```bash
pip install ultralytics opencv-python
```

## Hướng Dẫn Sử Dụng
1. Đảm bảo file mô hình `best.pt` nằm cùng thư mục với file `app.py`.
2. Mở terminal tại thư mục gốc của dự án và chạy lệnh sau:
   ```bash
   python app.py
   ```
3. Đưa các tờ tiền VNĐ ra trước camera để mô hình nhận diện.
4. Nhấn phím **`q`** trên bàn phím để tắt ứng dụng và đóng camera.

## Huấn Luyện Lại (Tuỳ chọn)
Nếu bạn muốn tự train lại mô hình trên dữ liệu mới:
1. Import file `train_yolov8_kaggle.ipynb` lên nền tảng Kaggle.
2. Tải dataset của bạn lên phần "Input" của Kaggle.
3. Chạy các ô code trong Notebook để train và xuất file `best.pt` mới.
