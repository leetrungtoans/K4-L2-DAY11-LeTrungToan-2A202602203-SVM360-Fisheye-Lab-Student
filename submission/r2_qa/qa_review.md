# QA review · B2-center

Mã khóa: 9897-004F

| frame | object_ref | rule_id | nhận xét |
|---|---|---|---|
| adasind_062370.jpg | L8 | R04 | Đối tượng tại (316, 740, 418, 817) đang được gán nhãn Car; tuy nhiên quan sát hình thái có thùng hàng phía sau dạng xe tải nhỏ/pickup. Theo R04, xe bán tải nhỏ/xe chở hàng cần phân loại là Truck. |
| adasind_086220.jpg | L1 | R05 | Đối tượng ThreeWheeler lớn ở góc phải (653, 865, 1080, 1293) bị cắt mép khung hình và vành quang học; cần đảm bảo attribute truncated=true theo đúng định nghĩa hình học R05. |
| adasind_117120.jpg | L8 | R01 | Phương tiện ở làn đường phía xa có chiều cao đo đạc khoảng 37–40 px; cần rà soát lại theo ngưỡng H=40 px của quy tắc R01 để quyết định giữ hay loại nhất quán. |
| adasind_062370.jpg | L3 | R02 | Xe máy ở biên phải bị biến dạng cong lớn do hiệu ứng mắt cá; box bao bọc đúng phần điểm ảnh nhìn thấy thực tế trên ảnh gốc, tuân thủ đúng R02 không nắn thẳng phối cảnh. |

Ghi finding r2_qa: cell=L_only, rule_id có giá trị, why để trống.
