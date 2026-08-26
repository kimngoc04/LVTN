# LUẬN VĂN TỐT NGHIỆP: DỰ ĐOÁN VÀ CHỦ ĐỘNG CO GIÃN TÀI NGUYÊN TRONG ỨNG DỤNG MICROSERVICES

**Sinh viên thực hiện:** Nguyễn Thị Kim Ngọc<br>
**Chuyên ngành:** Mạng máy tính và Truyền thông dữ liệu - Đại học Cần Thơ<br>
**Giảng viên hướng dẫn:** TS. Nguyễn Hữu Vân Long<br>

---

## 📝 1. Giới thiệu đề tài

Đề tài tập trung nghiên cứu, thiết kế và hiện thực hóa một hệ thống co giãn chủ động (Predictive Autoscaling) dựa trên các mô hình Học máy (Machine Learning) cho kiến trúc Microservices. Khác với các cơ chế co giãn phản ứng (Reactive) thụ động truyền thống thường phản hồi chậm trễ và gây vi phạm cam kết chất lượng dịch vụ (SLO) khi tải tăng đột ngột, nghiên cứu này giải quyết bài toán thông qua sự kết hợp của hai giai đoạn:

*   **Dự báo khối lượng công việc (Workload Forecasting):** Áp dụng các mô hình học máy hồi quy  lên dữ liệu chuỗi thời gian để phân tích và dự báo trước lưu lượng truy cập web.
*   **Chủ động cấp phát tài nguyên (Proactive Provisioning):** Sử dụng mô hình học máy hồi quy để học chính sách ánh xạ số lượng bản sao (Replica/Pod) tối ưu dựa trên ngưỡng thời gian phản hồi (SLO) do người dùng định nghĩa.
*   **Môi trường đánh giá:** Cơ chế cấp phát chủ động được đưa vào kiểm chứng hoàn toàn trong môi trường mô phỏng. Hệ thống sử dụng kỹ thuật mô phỏng dựa trên truy vết (Trace-driven Simulation) để đánh giá hiệu năng qua các kịch bản tải đa dạng như tải tăng dần, tải tuần hoàn và mô phỏng dữ liệu thực tế từ sự kiện World Cup.

Cách tiếp cận chủ động này giúp hệ thống chuẩn bị sẵn sàng tài nguyên từ trước các cú sốc tải trọng, giảm thiểu đáng kể tỷ lệ vi phạm SLO và tối ưu hóa hiệu năng vận hành cho ứng dụng.

## ⚙️ 2. Kiến trúc và Quy trình thực hiện

Hệ thống được thiết kế theo một quy trình khép kín, tự động hóa từ khâu thu thập dữ liệu đến ra quyết định cấp phát tài nguyên, bao gồm các bước cốt lõi sau

*   **Bước 1 - Mô hình hóa thời gian phản hồi:** Tiến hành kiểm thử chịu tải (Stress Test) bằng công cụ Locust trên dịch vụ Frontend của ứng dụng Online Boutique. Dữ liệu giám sát được thu thập qua Istio, Prometheus và Grafana để xây dựng hàm số mũ xấp xỉ thời gian phản hồi của hệ thống.
*   **Bước 2 - Mô phỏng dựa trên truy vết (Trace-driven Simulation):** Sử dụng mô hình toán học vừa thiết lập để chạy mô phỏng cơ chế co giãn, nhằm tự động tạo ra tập dấu vết hiệu năng (performance traces) quy mô lớn làm dữ liệu huấn luyện mà không cần thử nghiệm tốn kém trên hạ tầng vật lý.
*   **Bước 3 - Dự báo khối lượng công việc:** Sử dụng kỹ thuật đặc trưng trễ (Lag Features) kết hợp với các mô hình học máy hồi quy để phân tích dữ liệu quá khứ và dự báo chính xác lưu lượng truy cập tương lai.
*   **Bước 4 - Cấp phát tài nguyên chủ động:** Đưa lưu lượng dự báo vào mô hình học máy hồi quy để tính toán trước số lượng bản sao (Replica/VM) cần thiết, đảm bảo thời gian phản hồi luôn nằm dưới ngưỡng SLO an toàn.
*   **Bước 5 - Đánh giá hiệu năng:** So sánh trực tiếp hiệu quả của cơ chế chủ động (Predictive) so với cơ chế phản ứng (Reactive) thông qua các kịch bản mô phỏng tải tăng dần tuyến tính, tải tuần hoàn và tải thực tế World Cup.

## 🔄 4. Chi tiết quy trình thực hiện

**Khởi tạo cụm K8s với Kind**
kind delete cluster --name online-boutique 
