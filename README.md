# LUẬN VĂN TỐT NGHIỆP: DỰ ĐOÁN VÀ CHỦ ĐỘNG CO GIÃN TÀI NGUYÊN TRONG ỨNG DỤNG MICROSERVICES

**Sinh viên thực hiện:** Nguyễn Thị Kim Ngọc[cite: 1]
**Chuyên ngành:** Mạng máy tính và Truyền thông dữ liệu - Đại học Cần Thơ[cite: 1]
**Giảng viên hướng dẫn:** TS. Nguyễn Hữu Vân Long[cite: 1]

---

## 📝 1. Giới thiệu đề tài

Đề tài tập trung nghiên cứu, thiết kế và hiện thực hóa một hệ thống co giãn chủ động (Predictive Autoscaling) dựa trên các mô hình Học máy (Machine Learning) cho kiến trúc Microservices[cite: 1]. Khác với các cơ chế co giãn phản ứng (Reactive) thụ động truyền thống thường phản hồi chậm trễ và gây vi phạm cam kết chất lượng dịch vụ (SLO) khi tải tăng đột ngột, nghiên cứu này giải quyết bài toán thông qua sự kết hợp của hai giai đoạn[cite: 1]:

*   **Dự báo khối lượng công việc (Workload Forecasting):** Áp dụng các thuật toán Hồi quy (như Linear Regression, Elastic Net) lên dữ liệu chuỗi thời gian để phân tích và dự báo trước lưu lượng truy cập web[cite: 1].
*   **Chủ động cấp phát tài nguyên (Proactive Provisioning):** Sử dụng thuật toán Cây quyết định hồi quy (Decision Tree Regressor) để học chính sách ánh xạ số lượng bản sao (Replica/Pod) tối ưu dựa trên ngưỡng thời gian phản hồi (SLO) do người dùng định nghĩa[cite: 1].
*   **Môi trường đánh giá:** Triển khai thử nghiệm thực tế trên hệ thống Kubernetes với ứng dụng benchmark Online Boutique[cite: 1]. Hệ thống sử dụng mô phỏng dựa trên vết (Trace-driven Simulation) để đánh giá hiệu năng qua các kịch bản tải đa dạng như tải tăng dần, tải tuần hoàn và dữ liệu thực tế từ sự kiện World Cup[cite: 1].

Cách tiếp cận chủ động này giúp hệ thống chuẩn bị sẵn sàng tài nguyên từ trước các cú sốc tải trọng, giảm thiểu đáng kể tỷ lệ vi phạm SLO và tối ưu hóa hiệu năng vận hành cho ứng dụng[cite: 1].
