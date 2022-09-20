# Test Report
This test report contains the results of running TestTriangle on the new updated (fixed) triangle.py code.

----------------------------------------------------------------------
Running `python -m unittest TestTriangle` produced:
```
(base) niharshah@Nihars-MacBook-Pro Triangle567 % python -m unittest TestTriangle
.........
----------------------------------------------------------------------
Ran 9 tests in 0.002s

OK
```

----------------------------------------------------------------------
| Test ID | Input | Expected Results | Actual Result | Pass or Fail |
|---|---|---|---|---|
| test_invalid_sum_sides_a | (10,7,2) | Scalene | Scalene | Pass |
| test_invalid_sum_sides_b | (7, 10, 2) |  Scalene | Scalene  | Pass |
| test_valid_equilateral_triangle | (1,1,1) |  Equilateral | Equilateral  | Pass |
| test_valid_right_triangle_a | (3,4,5) |  Right | Right  | Pass |
| test_valid_right_triangle_b | (5,3,4) |  Right | Right  | Pass |
| test_valid_scalene_triangle_a | (4,6,9) |  Scalene | Scalene  | Pass |
| test_valid_scalene_triangle_b | (9,4,6) | Scalene | Scalene | Pass |
| test_valid_isosceles_triangle_a | (3,2,2) | Isosceles | Isosceles | Pass |
| test_valid_isosceles_triangle_b | (2,3,2) | Isosceles | Isosceles | Pass |

