# LUẬN VĂN TỐT NGHIỆP: DỰ ĐOÁN VÀ CHỦ ĐỘNG CO GIÃN TÀI NGUYÊN TRONG ỨNG DỤNG MICROSERVICES

**Sinh viên thực hiện:** Nguyễn Thị Kim Ngọc
**Chuyên ngành:** Mạng máy tính và Truyền thông dữ liệu - Đại học Cần Thơ
**Giảng viên hướng dẫn:** TS. Nguyễn Hữu Vân Long

---

## 📝 1. Giới thiệu đề tài

Đề tài tập trung nghiên cứu, thiết kế và hiện thực hóa một hệ thống co giãn chủ động (Predictive Autoscaling) dựa trên các mô hình Học máy (Machine Learning) cho kiến trúc Microservices. Khác với các cơ chế co giãn phản ứng (Reactive) thụ động truyền thống thường phản hồi chậm trễ và gây vi phạm cam kết chất lượng dịch vụ (SLO) khi tải tăng đột ngột, nghiên cứu này giải quyết bài toán thông qua sự kết hợp của hai giai đoạn:

*   **Dự báo khối lượng công việc (Workload Forecasting):** Áp dụng các mô hình học máy hồi quy  lên dữ liệu chuỗi thời gian để phân tích và dự báo trước lưu lượng truy cập web.
*   **Chủ động cấp phát tài nguyên (Proactive Provisioning):** Sử dụng mô hình học máy hồi quy để học chính sách ánh xạ số lượng bản sao (Replica/Pod) tối ưu dựa trên ngưỡng thời gian phản hồi (SLO) do người dùng định nghĩa.
*   **Môi trường đánh giá:** Cơ chế cấp phát chủ động được đưa vào kiểm chứng hoàn toàn trong môi trường mô phỏng. Hệ thống sử dụng kỹ thuật mô phỏng dựa trên truy vết (Trace-driven Simulation) để đánh giá hiệu năng qua các kịch bản tải đa dạng như tải tăng dần, tải tuần hoàn và mô phỏng dữ liệu thực tế từ sự kiện World Cup.

Cách tiếp cận chủ động này giúp hệ thống chuẩn bị sẵn sàng tài nguyên từ trước các cú sốc tải trọng, giảm thiểu đáng kể tỷ lệ vi phạm SLO và tối ưu hóa hiệu năng vận hành cho ứng dụng.
