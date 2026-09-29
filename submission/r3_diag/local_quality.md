# Đối chiếu chất lượng cục bộ — rectangle

Teaching reference, không phải gold set đã phê duyệt; không có điểm đạt tự động.
Nguồn: export r1_craft đã khóa SHA256 `f3a4412b565c2ab826e9bba4afc2342d4b4dc7d6103debd7bcaf52e13aa35145`; slice `B3-dense`.
Ghép hình học greedy một-một theo IoU ≥ 0.50, rồi so class; H ≥ 40 px.
Box trái nằm chủ yếu trong ignore_region reference không tính. Polygon, polyline, track không được chấm.
Đây là phép tính offline của lab, không phải báo cáo hay kết quả tương đương CVAT Premium.

Frame được tính: adasind_145860.jpg, adasind_167700.jpg, adasind_199770.jpg. Frame thiếu trong export: không.
TP=1; FP=19; FN=19; số lần đối chiếu=38; mean IoU của TP=1.000.

| Chỉ số | Micro | Macro | Nhãn thấp nhất |
|---|---:|---:|---:|
| accuracy | 0.026 | 0.800 | 0.684 |
| precision | 0.050 | 0.100 | 0.000 |
| recall | 0.050 | 0.050 | 0.000 |
| jaccard | 0.026 | 0.040 | 0.000 |
| dice | 0.050 | 0.067 | 0.000 |

| Nhãn | TP | FP | FN | Accuracy | Precision | Recall | Jaccard | Dice |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Bike | 0 | 6 | 6 | 0.684 | 0.000 | 0.000 | 0.000 | 0.000 |
| Car | 0 | 6 | 2 | 0.789 | 0.000 | 0.000 | 0.000 | 0.000 |
| Pedestrian | 0 | 0 | 4 | 0.895 | 0.000 | 0.000 | 0.000 | 0.000 |
| ThreeWheeler | 0 | 6 | 4 | 0.737 | 0.000 | 0.000 | 0.000 | 0.000 |
| Truck | 1 | 1 | 3 | 0.895 | 0.500 | 0.250 | 0.200 | 0.333 |

| Frame | TP | FP | FN | Accuracy | Precision | Recall |
|---|---:|---:|---:|---:|---:|---:|
| adasind_145860.jpg | 1 | 6 | 1 | 0.143 | 0.143 | 0.500 |
| adasind_167700.jpg | 0 | 6 | 9 | 0.000 | 0.000 | 0.000 |
| adasind_199770.jpg | 0 | 7 | 9 | 0.000 | 0.000 | 0.000 |

Confusion matrix: hàng = teaching reference; cột = export đã khóa.
`<missing>` là thiếu box; `<extra>` là box thừa. Xem `local_quality_confusion.csv`.

| Reference \ Export | Bike | Car | Pedestrian | ThreeWheeler | Truck | <missing> |
|---|---:|---:|---:|---:|---:|---:|
| Bike | 0 | 0 | 0 | 0 | 0 | 6 |
| Car | 0 | 0 | 0 | 1 | 0 | 1 |
| Pedestrian | 0 | 0 | 0 | 0 | 0 | 4 |
| ThreeWheeler | 0 | 0 | 0 | 0 | 0 | 4 |
| Truck | 0 | 0 | 0 | 0 | 1 | 3 |
| <extra> | 6 | 6 | 0 | 5 | 1 | 0 |

Chi tiết xung đột trong `local_quality_conflicts.csv`; dữ liệu máy đọc trong `local_quality.json`.
Mismatching label đóng góp một FP cho class vẽ và một FN cho class reference; attribute khác được báo riêng.
Micro accuracy đếm mỗi cặp ghép sai class là một lần đối chiếu; Jaccard đếm cả FP và FN.
Macro/worst bỏ nhãn không xuất hiện ở cả hai phía; chỉ số không có mẫu là N/A.
