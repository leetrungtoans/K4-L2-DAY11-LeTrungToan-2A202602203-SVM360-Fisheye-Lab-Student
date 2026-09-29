# Escalation ticket

## Ticket 1

- **Frame:** adasind_145860.jpg (slice B3-dense) — object L7 tại tọa độ (218, 820, 310, 920)
- **Ảnh chụp:** submission/screenshots/145860_wrong_class.png
- **Mô tả vấn đề:** Phương tiện tại L7 được annotator gán nhãn `Car` nhưng teaching reference gán `Truck`. Quan sát ảnh gốc cho thấy phương tiện có thùng hàng mở phía sau (cargo bed) — dấu hiệu điển hình của xe tải nhỏ địa phương Ấn Độ (Tata Ace / mini truck). Rule R04 hiện tại nói "xe bán tải nhỏ → Truck" nhưng không có tiêu chí hình thái cụ thể để phân biệt với `Car` trên ảnh fisheye zone center nơi chiều dài xe bị co giãn.
- **Expected impact:** Nếu không làm rõ rule này, lỗi WRONG_CLASS sẽ tái diễn hệ thống trong tất cả slice có phương tiện tải nhỏ Ấn Độ (chiếm ~15-20% lưu lượng giao thông trong tập ADASIND). Tỷ lệ precision của class `Truck` sẽ thấp bất thường; class `Car` sẽ bị inflate FP tương ứng.
- **Owner:** guideline (cần Lab Coach / AI team xác nhận tiêu chí phân loại và cập nhật docs/02-rules-vi.md)
- **Recommendation:** Bổ sung vào R04 tiêu chí hình thái: "nếu nhìn thấy vách ngăn cabin-thùng hàng hoặc thùng tải mở phía sau = Truck; nếu chỉ thấy cốp xe thông thường = Car". Cập nhật rules_version lên v1.1.0 và thông báo cho tất cả annotator đang làm slice B-series.
