# Test Report
This test report contains the results of running TestTriangle on the original (buggy) triangle.py

----------------------------------------------------------------------
Running `python -m unittest TestTriangle` produced:
```
FFF
======================================================================
FAIL: testEquilateralTriangles (TestTriangle.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/niharshah/Documents/Admission/Assignment and Homework/SSW - 567/HW02a/Triangle567/TestTriangle.py", line 21, in testEquilateralTriangles
    self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
AssertionError: 'InvalidInput' != 'Equilateral'
- InvalidInput
+ Equilateral
 : 1,1,1 should be equilateral

======================================================================
FAIL: testRightTriangleA (TestTriangle.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/niharshah/Documents/Admission/Assignment and Homework/SSW - 567/HW02a/Triangle567/TestTriangle.py", line 15, in testRightTriangleA
    self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
AssertionError: 'InvalidInput' != 'Right'
- InvalidInput
+ Right
 : 3,4,5 is a Right triangle

======================================================================
FAIL: testRightTriangleB (TestTriangle.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/niharshah/Documents/Admission/Assignment and Homework/SSW - 567/HW02a/Triangle567/TestTriangle.py", line 18, in testRightTriangleB
    self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
AssertionError: 'InvalidInput' != 'Right'
- InvalidInput
+ Right
 : 5,3,4 is a Right triangle

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=3)
```

----------------------------------------------------------------------
| Test ID | Input | Expected Results | Actual Result | Pass or Fail |
|---|---|---|---|---|
| testEquilateralTriangles | (1,1,1) | Equilateral triangle | InvalidInput | Fail |
| testRightTriangleA | (3,4,5) | Right angle triangle | InvalidInput | Fail |
| testRightTriangleB | (5,3,4) |  Isosceles triangle | InvalidInput | Fail |


