# LUẬN VĂN TỐT NGHIỆP: HỆ THỐNG TỰ ĐỘNG CO GIÃN TÀI NGUYÊN THÔNG MINH CHO KIẾN TRÚC MICROSERVICES

**Sinh viên thực hiện:** [Điền tên của bạn]
**Chuyên ngành:** [Điền chuyên ngành của bạn] - [Điền tên trường]
**Giảng viên hướng dẫn:** [Điền tên Thầy/Cô]

---

## 📝 1. Giới thiệu đề tài

Đề tài tập trung nghiên cứu và triển khai hệ thống tự động co giãn (Autoscaling) thông minh cho các ứng dụng Microservices trên nền tảng Kubernetes. Khác với các cơ chế truyền thống, nghiên cứu này thực hiện co giãn dựa trên sự kết hợp giữa hai chiến lược:

*   **Chiến lược dự đoán (Proactive):** Sử dụng các mô hình học máy (Machine Learning) để phân tích dữ liệu lịch sử và dự báo trước lưu lượng truy cập web.
*   **Chiến lược phản ứng (Reactive):** Theo dõi và xử lý các biến động tải đột ngột trong thời gian thực.
*   **Môi trường thử nghiệm:** Triển khai trên hệ thống giả lập với ứng dụng benchmark Online Boutique và công cụ tạo tải Locust.
