# Test Report
This test report contains the results of running TestTriangle on the original (buggy) triangle.py

----------------------------------------------------------------------
Running `python -m unittest TestTriangle` produced:
```
======================================================================
FAIL: test_isosceles_triangle (TestTriangle.TestTriangle)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/niharshah/Documents/Admission/Assignment and Homework/SSW - 567/HW02a/Triangle567/TestTriangle.py", line 25, in test_isosceles_triangle
    self.assertEqual(classifyTriangle(4, 4, 5), "Isosceles triangle ")
AssertionError: 'Isosceles triangle' != 'Isosceles triangle '
- Isosceles triangle
+ Isosceles triangle 
?                   +


----------------------------------------------------------------------
Ran 4 tests in 0.001s

FAILED (failures=1)
```

----------------------------------------------------------------------
| Test ID | Input | Expected Results | Actual Result | Pass or Fail |
|---|---|---|---|---|
| test_equilateral_triangle | (2, 2, 2) | Equilateral triangle | Equilateral triangle | Pass |
| test_right_angle | (3, 4, 5) | Right angle triangle | Right angle triangle  | Pass |
| test_isosceles_triangle | (4, 4, 5) |  Isosceles triangle | Assertion Error  | Fail |
| test_scalene_triangle | (10, 12, 15) |  Scalene triangle | Scalene triangle  | Pass |

