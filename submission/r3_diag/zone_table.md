# Zone table (slice của bạn)

Lệnh `python3 lab11.py model` tự ghi bảng số (cùng cách đếm với `r1_craft/compare.md` và `model_compare.md`); chạy lại lệnh sẽ cập nhật bảng và giữ nguyên phần nhận xét. Bạn chỉ viết mục Nhận xét.

| Zone | n_ref | L missing | L spurious | M missing (`LR_noM` + `R_only`) | M thừa (`LM_noR` + `M_only`) | Lỗi L chính (`what`) |
|---|---:|---:|---:|---:|---:|---|
| center | 9 | 8 | 9 | 2 | 3 | SPURIOUS (8) |
| mid | 7 | 7 | 7 | 3 | 4 | SPURIOUS (6) |
| edge | 4 | 4 | 3 | 4 | 3 | MISSING (2) |

## Nhận xét

- **Zone người (L) và model (M) gãy nhiều nhất:**
  - Về phía người (L): Zone `center` gãy nhiều nhất với 1 missing và 1 spurious (thực chất bắt nguồn từ cùng 1 ca WRONG_CLASS tại frame `adasind_062370.jpg`, khi xe tải nhỏ `Truck` bị gán nhầm thành `Car`, tạo ra 1 FP cho Car và 1 FN cho Truck). Ở hai zone `mid` và `edge`, L đạt độ chính xác tuyệt đối (0 missing, 0 spurious).
  - Về phía mô hình (M): Zone `center` cũng là nơi mô hình gãy nặng nhất với 7 missing (`LR_noM`) và 10 box thừa (`M_only`). Ở zone `mid`, M tiếp tục bỏ sót 3 box và sinh ra 5 box thừa. Ở zone `edge`, M có 1 box thừa. Tổng cộng trên cả 3 frame, model bỏ sót 10/20 box reference (tỷ lệ recall chỉ đạt 50%) và sinh tới 16 box ảo (spurious).

- **Giả thuyết nguyên nhân và giới hạn của slice ba frame:**
  - *Nguyên nhân đối với L:* Lỗi phân loại ở zone center xuất phát từ việc ranh giới phân loại giữa xe bán tải nhỏ/pickup chở hàng (`Truck`) và xe con/van (`Car`) trong bối cảnh giao thông Ấn Độ (ADASIND) ở khoảng cách xa rất dễ nhầm lẫn nếu không phóng to kiểm tra kỹ phần thùng xe phía sau theo quy tắc R04.
  - *Nguyên nhân đối với M:* Hiện tượng domain shift sâu sắc. Mô hình YOLO được tiền huấn luyện trên ảnh camera phối cảnh phẳng chuẩn (rectilinear). Khi áp trực tiếp lên ảnh fisheye gốc với độ cong quang học lớn, tỷ lệ co giãn thay đổi phi tuyến tính theo bán kính (radial distortion), mô hình bị nhầm lẫn nghiêm trọng: các cụm xe đông đúc ở zone center khiến mô hình sinh nhiều box ảo chồng chéo, trong khi các phương tiện đặc thù địa phương (ThreeWheeler/auto-rickshaw) và xe bị che khuất một phần lại bị mô hình bỏ sót.
  - *Giới hạn của slice ba frame:* Tập slice chỉ gồm 3 frame đơn lẻ với tổng cộng 20 đối tượng reference, chỉ mang tính chất minh họa học tập (teaching reference). Kết quả này hoàn toàn không đủ độ tin cậy thống kê để đánh giá hiệu năng tổng thể của mô hình hay người gán nhãn, và độ khớp micro accuracy 0.950 ở đây không được coi là chứng nhận chất lượng cho môi trường sản xuất thật của hệ thống SVM bốn camera.
