# Exit ticket

Đọc `docs/10-svm360-reading-vi.md` trước khi trả lời câu 1–2. Các câu về zone, `why`, rework, parking và sampling
đã nằm trong file tương ứng nên không hỏi lại ở đây.

1. Một vật ở vùng seam giữa hai camera thật xuất hiện với hai box khác nhau: đó là lỗi `DUPLICATE` hay cần một quy
   tắc riêng? Vì sao?

   **Trả lời:** Đây **không phải** lỗi `DUPLICATE` mà là một trường hợp hợp lệ cần một quy tắc cross-camera riêng. Lý do: `DUPLICATE` (theo docs/02 và findings.py ENUMS) chỉ áp dụng khi **cùng một camera** sinh ra hai box trùng lắp cho **cùng một đối tượng** trong cùng một frame. Khi đối tượng thực sự nằm ở vùng chồng (seam) giữa camera trái và camera trước, mỗi camera quan sát một góc chiếu khác nhau của cùng đối tượng đó — hai box là biểu diễn hình học hợp lệ trong không gian 2D của từng ảnh fisheye riêng biệt. Để quyết định merge hay giữ cả hai box, hệ thống cần: (a) timestamp đồng bộ giữa hai camera; (b) extrinsic calibration để map tọa độ 2D sang tọa độ thế giới thực 3D; (c) policy output rõ ràng (giữ hai box độc lập cho per-camera model, hay merge thành một representation trong BEV). Không có đủ ba điều kiện này thì không được xóa bất kỳ box nào.

2. Một vật đi qua nhiều frame trên cùng camera: khi nào giữ cùng track ID, khi nào thêm keyframe hoặc trạng thái
   Outside? Nêu bằng chứng sẽ cần trước khi nối track qua hai camera.

   **Trả lời:** Cùng một track ID được giữ khi đối tượng **liên tục quan sát được** trong phạm vi trường nhìn của camera, với hình học bounding box thay đổi **liên tục và có thể giải thích** (di chuyển, thay đổi khoảng cách). Cần thêm **keyframe** khi có thay đổi hình học đột ngột lớn (đối tượng xoay góc, bị che rồi xuất hiện lại, tốc độ thay đổi bất thường) để đánh dấu điểm bắt đầu chuỗi interpolation mới. Trạng thái **Outside** được đánh khi đối tượng rời khỏi trường nhìn của camera (ra ngoài vành kính hoặc biên khung hình) và chuỗi frame tiếp theo không còn quan sát được nữa — đây không phải bị che khuất tạm thời (occluded) mà là thoát hoàn toàn. Để nối track **qua hai camera**, cần bằng chứng: (a) timestamp đồng bộ giữa hai camera để xác nhận là cùng thời điểm; (b) extrinsic calibration để tính tọa độ thế giới thực và xác nhận đây là cùng vật thể vật lý; (c) vận tốc/trajectory hợp lý về mặt vật lý để track có thể đến từ camera A sang camera B trong khoảng thời gian đó; (d) policy về cross-camera track ID (có dùng global ID hay per-camera ID?). Không có đủ bằng chứng này, việc gán cùng track ID cho hai box ở hai camera là suy đoán không có căn cứ.

3. Nhìn lại cả buổi: một chỗ bạn tin nhãn mình đúng nhưng reference hoặc người soát nghĩ khác (dẫn frame/`object_ref`),
   bạn đã xử lý thế nào, và nếu làm lại slice này bạn sẽ đổi gì trong cách làm?

   **Trả lời:** Ca điển hình là `adasind_145860.jpg L7` (object_ref L7+R2, findings.csv). Khi gán nhãn ban đầu, tôi gán `Car` vì thân xe trông gọn nhẹ và kích thước không quá lớn so với các Car xung quanh. Teaching reference gán `Truck`. Khi mở compare.html và phóng to ảnh gốc, thấy rõ vách ngăn cabin-thùng hàng và phần thùng tải mở phía sau — đây là dấu hiệu theo R04 phải là Truck. Tôi xử lý bằng cách: (1) ghi vào findings.csv (WRONG_CLASS, E1_annotator_error); (2) sửa trong rework → annotations-v2.xml; (3) leo thang lên escalation_ticket vì rule R04 không đủ tiêu chí hình thái cụ thể; (4) đề xuất patch R04 lên v1.1.0 trong 20_guideline_patch.md. Nếu làm lại slice này, tôi sẽ: (a) luôn phóng to 100% ảnh gốc để kiểm tra phần phía sau phương tiện trước khi gán Car/Truck, không dựa vào kích thước tổng thể; (b) tham khảo trước docs/05-taxonomy-vi.md cho các loại xe địa phương Ấn Độ đặc thù; (c) khi không chắc, ghi ngay vào findings.csv với why=E5_unresolved thay vì đoán và có thể sai hệ thống.
