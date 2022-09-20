# Test Report
This test report contains the results of running TestTriangle on the new updated (fixed) triangle.py code.

----------------------------------------------------------------------
Running `python -m unittest TestTriangle` produced:
```
Ran 28 tests in 0.001s

OK
```

----------------------------------------------------------------------
| Test ID | Input | Expected Results | Actual Result | Pass or Fail |
|---|---|---|---|---|
| testInvalidFloatInputA | (10.0,7,4) | InvalidInput | InvalidInput | Pass |
| testInvalidFloatInputB | (10,'7',4) |  InvalidInput | InvalidInput  | Pass |
| testInvalidFloatInputC | (10,7,'4') |  InvalidInput | InvalidInput  | Pass |
| testInvalidOverMaxInputA | (201,200,200) |  InvalidInput | InvalidInput  | Pass |
| testInvalidOverMaxInputB | (200,201,200) |  InvalidInput | InvalidInput  | Pass |
| testInvalidOverMaxInputC | (200,200,201) |  InvalidInput | InvalidInput  | Pass |
| testInvalidStringInputA | ('10',7,4) | InvalidInput | InvalidInput | Pass |
| testInvalidStringInputB | (10,'7',4) | InvalidInput | InvalidInput | Pass |
| testInvalidStringInputC | (10,7,'4') | InvalidInput | InvalidInput | Pass |
| testInvalidSumSidesA | (10,7,2) |  NotATriangle | NotATriangle  | Pass |
| testInvalidSumSidesB | (7,10,2) |  NotATriangle | NotATriangle  | Pass |
| testInvalidSumSidesC | (7,2,10) |  NotATriangle | NotATriangle  | Pass |
| testInvalidUnderMinInputA | (0,1,1) |  InvalidInput | InvalidInput  | Pass |
| testInvalidUnderMinInputB | (1,0,1) |  InvalidInput | InvalidInput  | Pass |
| testInvalidUnderMinInputC | (1,1,0) |  InvalidInput | InvalidInput  | Pass |
| testValidEquilateralTriangles | (1,1,1) | Equilateral | Equilateral | Pass |
| testValidIsoscelesTriangleA | (3,2,2) | Isosceles | Isosceles | Pass |
| testValidIsoscelesTriangleB | (2,3,2) | Isosceles | Isosceles | Pass |
| testValidIsoscelesTriangleC | (2,2,3) | Isosceles | Isosceles | Pass |
| testValidRightTriangleA | (3,4,5) | Right | Right | Pass |
| testValidRightTriangleB | (5,3,4) | Right | Right | Pass |
| testValidRightTriangleC | (4,5,3) | Right | Right | Pass |
| testValidScaleneTriangleA | (4,6,9) | Scalene | Scalene | Pass |
| testValidScaleneTriangleB | (9,4,6) | Scalene | Scalene | Pass |
| testValidScaleneTriangleC | (6,9,4) | Scalene | Scalene | Pass |
| testValidSumSidesA | (10,7,4) | Scalene | Scalene | Pass |
| testValidSumSidesB | (7,10,4) | Scalene | Scalene | Pass |
| testValidSumSidesC | (7,4,10) | Scalene | Scalene | Pass |