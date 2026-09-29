# Quan sát vạch ô đỗ

- Hai vạch `parking_line` đã vẽ (mô tả vị trí trong ảnh):
  1. Vạch thứ nhất: Đoạn vạch sơn trắng tiền cảnh ở khu vực giữa/dưới khung hình (từ x=400.0, y=653.0 đến x=539.0, y=719.0), có vai trò phân định ranh giới giữa hai ô đỗ xe liền kề ở hàng trước.
  2. Vạch thứ hai: Đoạn vạch sơn trắng tiền cảnh ở góc phải dưới (từ x=693.0, y=623.0 đến x=952.0, y=681.0), đóng vai trò ranh giới phân chia ô đỗ xe ở phía bên phải.
- Một vạch/dấu sơn hoặc biên **không** vẽ, và vì sao:
  - Các vệt sơn dẫn luồng xe chạy (driving aisle) ở khoảng giữa bãi và dải ranh giới nhựa đường sát bờ rào hàng cây ở hậu cảnh: Không vẽ nhãn `parking_line` vì chúng chỉ có chức năng điều hướng giao thông nội bộ bãi đỗ hoặc ngăn cách khu đất, không có chức năng tạo ranh giới cho một ô đỗ riêng lẻ (parking stall boundary). Đồng thời tuân thủ quy tắc không vẽ các vạch mờ/nhiễu ở quá xa khi không xác định rõ hình học.
- Polygon `free_space` dừng ở đâu; có phần bị che nào không:
  - Polygon `free_space` bao trùm vùng mặt đường nhựa trống của lối xe chạy ở khu vực tiền cảnh (tọa độ y từ 520 đến 650, x từ 50 đến 920). Ranh giới polygon dừng ngay mép ngoài của các ô đỗ, tuyệt đối không xâm lấn vào ô có vạch đỗ, cách ly hoàn toàn với chiếc xe màu đỏ ở hậu cảnh xa phía bên trái và dừng trước bờ rào/hàng cây. Không có vật cản nào che khuất trong vùng này; polygon bám sát bề mặt asphalt thực tế nhìn thấy được trên ảnh tĩnh.
- Ca chưa chắc cần hỏi người soát (nếu không có, ghi “không có”):
  - không có
