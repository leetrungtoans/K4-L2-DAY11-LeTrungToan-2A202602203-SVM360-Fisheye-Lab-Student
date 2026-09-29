# Kế hoạch review từ lỗi quan sát được

Từ `findings.csv` và `zone_table.md`, chọn **hai lát cắt của bài ADASIND một camera** cần review trước. Bảng này
giải thích dữ liệu thật bạn vừa làm; nó không thay cho kế hoạch bốn camera giả lập ở `45_sampling_plan.csv`.

| Lát cắt / frame | Số ca và loại lỗi | Vì sao review trước | Bằng chứng cần giữ |
|---|---|---|---|
| adasind_145860.jpg (B3-dense) | 1 WRONG_CLASS (L7: Car→Truck), 4 LR_noM (M bỏ sót ThreeWheeler), 5 M_only (box thừa zone center/edge) | Frame này có lỗi phân loại WRONG_CLASS duy nhất trong cả slice, kéo FP/FN đồng thời; đồng thời có số ca model gãy cao nhất (9 ca) tập trung ở zone center — cần review để xác định ranh giới R04 có đủ rõ cho phương tiện địa phương Ấn Độ không | compare.html L7 overlay, screenshots/145860_wrong_class.png |
| adasind_167700.jpg (B3-dense) | 3 LR_noM (M bỏ sót: ThreeWheeler lớn zone mid, Bike zone center), 6 M_only (box thừa) | Frame có ThreeWheeler lớn bị cắt mép phải (cần truncated=true theo R05) và nhiều box thừa từ mô hình; là ca điển hình để minh họa vì sao model yolo26m domain-shift trên fisheye gốc sinh box ảo nhiều hơn zone mid | qa_overlay.html, model_compare.html, decision_log dòng 2 |

Giới hạn của kết luận từ ba frame ADASIND: Ba frame đơn lẻ từ một camera (front-facing, góc nhìn một chiều) trong tập ADASIND không đủ để rút ra kết luận tổng quát về hiệu năng mô hình hay người gán nhãn. Số lượng đối tượng tổng cộng chỉ là 20-28 box reference, không đủ độ tin cậy thống kê (cần ít nhất vài trăm đối tượng mỗi class). Các loài phương tiện đặc thù (ThreeWheeler/auto-rickshaw) có phân bố không đều theo thời gian ngày. Điều kiện ánh sáng, mật độ giao thông, và cảnh nền trong ba frame chỉ đại diện cho một khoảnh khắc rất hẹp. Bất kỳ kết luận nào từ ba frame này chỉ mang tính chất minh họa học tập (teaching/illustrative) chứ không phải đánh giá hệ thống.

## Chuyển sang kế hoạch bốn camera giả lập

Cách soát độ phủ của 200 frame ở `45_sampling_plan.csv`: Mỗi camera được phân bổ riêng (front/rear/left/right × normal/hard) để đảm bảo đại diện cho tất cả góc nhìn và điều kiện khó; không lấy nhiều frame liên tiếp trong cùng một cảnh (cùng vị trí GPS, cùng thời điểm) vì chúng không mang thông tin độc lập — giãn cách tối thiểu 1-2 giây giữa các frame được chọn. Tuy nhiên, kế hoạch 200 frame chỉ giúp **tìm ca cần soi** (phát hiện pattern lỗi, phân bố đối tượng) chứ chưa đo được tỷ lệ lỗi thực vì: (1) sample không phải random stratified từ toàn bộ 50.000 frame; (2) selection bias do chủ đích chọn "hard" frame; (3) không có ground truth được xác nhận độc lập cho 200 frame này — chỉ có teaching reference của lab, không phải gold set đã được nhiều reviewer đồng thuận.
