# Tự soát

- adasind_086220.jpg L3: chiều cao < H (xem lại phạm vi)
- adasind_086220.jpg L4: chiều cao < H (xem lại phạm vi)
- adasind_086220.jpg L8: chiều cao < H (xem lại phạm vi)
- adasind_086220.jpg L9: chiều cao < H (xem lại phạm vi)
- adasind_117120.jpg L4: chiều cao < H (xem lại phạm vi)
- adasind_117120.jpg L6: chiều cao < H (xem lại phạm vi)
- adasind_117120.jpg L7: chiều cao < H (xem lại phạm vi)

## Checklist thủ công
- [x] Phạm vi H=40 và vật cần vẽ
- [x] lens_border và ego_body
- [x] Class sáu nhãn
- [x] Rider và Bike
- [x] Geometry trên ảnh fisheye gốc
- [x] truncated và occluded
- [x] Vật thiếu hoặc box trùng
- [x] ignore_region có reason
- [x] Tên task raw_fisheye và export CVAT 1.1

## Ghi chú xử lý cảnh báo
- Các box cảnh báo chiều cao sát ngưỡng H=40 px (khoảng 38-42 px) tại adasind_086220.jpg (L3, L4, L8, L9) và adasind_117120.jpg (L4, L6, L7) là các phương tiện ở hậu cảnh xa nhưng hình học phương tiện nhìn thấy rõ ràng trên ảnh gốc fisheye; đã rà soát và giữ lại có chủ đích để bảo đảm tính liên tục của đối tượng giao thông.
- Không có box nào bị che lấp ≥50% hoặc rơi vào trong vùng ignore_region.
- Cả 3 frame đều có đầy đủ polygon ego_body ở sát mép dưới và 2 polygon lens_border bao khép kín phần ngoài vành kính.
- Không có hai box cùng class nào có IoU > 0.7 (không bị trùng lặp box).

## Fill ratio (K12)
chưa vẽ polygon K12 (degrade)
