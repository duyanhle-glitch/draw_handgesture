# 🖐️ Air Drawing with Hand Gesture (Computer Vision)

## 📌 Mô tả dự án

Dự án này cho phép bạn **vẽ trên màn hình máy tính bằng cử chỉ tay** thông qua **Webcam** và **Computer Vision**.

👉 Sử dụng **MediaPipe** để nhận diện và theo dõi vị trí ngón trỏ.

👉 Người dùng có thể **bật/tắt chế độ vẽ**, **lưu tranh**, **xem trực tiếp nét vẽ xuất hiện trên video webcam**.

---

## 🎯 Chức năng chính

- ✅ Phát hiện bàn tay bằng **MediaPipe**
- ✅ Theo dõi vị trí ngón trỏ (Landmark số 8)
- ✅ Vẽ nét trên màn hình khi di chuyển tay
- ✅ Bật/tắt chế độ vẽ bằng phím `d`
- ✅ Lưu tranh vẽ ra file `.png` bằng phím `s`
- ✅ Thoát chương trình bằng phím `q`

---

## 🗂️ Cấu trúc thư mục

hand_drawing_cv/
├── main.py # File chạy chính
├── utils.py # Các hàm hỗ trợ vẽ và lưu tranh
├── requirements.txt # Thư viện cần cài
├── README.md # Mô tả dự án
└── output/ # Thư mục chứa các bức tranh đã lưu

## 🚀 Cách cài đặt và chạy

### Bước 1: Tạo folder và các file theo cấu trúc trên

### Bước 2: Cài đặt thư viện cần thiết

```bash
pip install -r requirements.txt
Bước 3: Chạy chương trình

python main.py
🎮 Hướng dẫn sử dụng
Phím	Chức năng
d	Bật/tắt chế độ vẽ
s	Lưu bức tranh hiện tại vào thư mục output/
q	Thoát chương trình