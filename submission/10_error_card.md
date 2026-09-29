# Error analysis card

## Zone × block

| zone | block | what | count |
|---|---|---|---:|
| center | B2 | ATTRIBUTE | 1 |
| center | B2 | MISSING | 7 |
| center | B2 | SPURIOUS | 4 |
| center | B2 | WRONG_CLASS | 2 |
| edge | B2 | SPURIOUS | 1 |
| mid | B2 | ATTRIBUTE | 1 |
| mid | B2 | MISSING | 2 |
| mid | B2 | SPURIOUS | 2 |
| unknown | B2 | MISSING | 1 |

## Top defects
- MISSING: 10 (ví dụ frame adasind_117120.jpg)
- SPURIOUS: 7 (ví dụ frame adasind_062370.jpg)
- WRONG_CLASS: 2 (ví dụ frame adasind_062370.jpg)

## Phân tích của bạn

Hai bảng trên do `python3 lab11.py card` tính từ `findings.csv`; chạy lại lệnh sẽ cập nhật bảng và giữ nguyên mục này. Viết cho lỗi nổi bật nhất, dẫn frame/`object_ref`.

- Nguyên nhân khả dĩ (`why`) và vì sao bạn nghĩ vậy: Lỗi nổi bật nhất là MISSING (10 ca, tập trung zone center/mid) với why=E4_model_domain — mô hình YOLO26M huấn luyện trên ảnh camera rectilinear bị domain shift nặng khi áp dụng trực tiếp lên ảnh fisheye gốc. Zone center có độ méo thấp nhất nhưng phương tiện đặc thù Ấn Độ (ThreeWheeler/auto-rickshaw) mô hình chưa đủ data huấn luyện. WRONG_CLASS (2 ca tại adasind_062370.jpg object_ref L8+R8) có why=E1_annotator_error gốc từ why=E2_guideline_gap: rule R04 không có tiêu chí hình thái cụ thể để phân biệt xe tải nhỏ và xe con lớn trên fisheye zone center.
- Cách sửa và ai nhận việc (`owner`): (1) WRONG_CLASS owner=annotator — đã sửa trong rework/annotations-v2.xml (L8: Car→Truck); cần broadcast R04-EXT patch cho annotator B-series; (2) MISSING do model owner=ai_team — cần fine-tune với ảnh fisheye ADASIND và bổ sung ThreeWheeler/Bike vào training data; (3) SPURIOUS do model owner=ai_team — điều chỉnh NMS/confidence threshold cho fisheye; (4) Rule gap owner=guideline — Lab Coach cập nhật docs/02-rules-vi.md lên v1.1.0 với tiêu chí hình thái R04-EXT.
- Bằng chứng (ảnh trong `screenshots/`, dòng findings, rule): screenshots/062370_wrong_class.png (adasind_062370 L8 WRONG_CLASS); screenshots/086220_model_missing.png (adasind_086220 L1 LR_noM MISSING); findings.csv dòng 1 (WRONG_CLASS L8+R8 E1_annotator_error R04); zone_table.md (10 MISSING 7 SPURIOUS từ model toàn slice); 30_escalation_ticket.md (escalated guideline gap R04); 20_guideline_patch.md (đề xuất R04-EXT v1.1.0).
