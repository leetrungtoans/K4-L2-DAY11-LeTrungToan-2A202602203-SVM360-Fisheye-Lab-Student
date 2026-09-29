# So sánh L với R

Chỉ số L/R là thứ tự box cao ≥ H=40 trong từng frame, theo thứ tự XML; bắt đầu từ 1.
Box L trong ignore_region được báo IGNORE_SCOPE, không tính SPURIOUS.

## adasind_145860.jpg
- L2 mid SPURIOUS
- L3 center SPURIOUS
- L4 mid SPURIOUS
- L5 center SPURIOUS
- L6 mid SPURIOUS
- L7+R2 mid WRONG_CLASS
## adasind_167700.jpg
- L1 edge SPURIOUS
- L2 center SPURIOUS
- L3 center SPURIOUS
- L4 center SPURIOUS
- L5 mid SPURIOUS
- L6 center SPURIOUS
- R1 center MISSING
- R2 mid MISSING
- R3 mid MISSING
- R4 center MISSING
- R5 center MISSING
- R6 edge MISSING
- R7 center MISSING
- R8 center MISSING
- R9 mid MISSING
## adasind_199770.jpg
- L1+R2 edge BOX_GEOMETRY
- L2+R5 edge BOX_GEOMETRY
- L3 mid SPURIOUS
- L4+R8 center BOX_GEOMETRY
- L5 center SPURIOUS
- L6 center SPURIOUS
- L7 mid SPURIOUS
- R1 center MISSING
- R3 mid MISSING
- R4 mid MISSING
- R6 edge MISSING
- R7 mid MISSING
- R9 center MISSING

## Theo zone
| zone | n_ref | matched | missing | spurious |
|---|---|---|---|---|
| center | 9 | 1 | 8 | 9 |
| mid | 7 | 0 | 7 | 7 |
| edge | 4 | 0 | 4 | 3 |
