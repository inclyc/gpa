# GPA

A library used to calculate your GPA. Now the GPA algorithm varies slightly from school to school, and calculating your GPA score one by one when applying to schools is a complicated and time-consuming process. This library is used to implement some common GPA calculation methods, which is convenient for you to calculate your GPA.

一个用来计算你GPA的库。现在各个学校的GPA算法略有不同，在申请学校时逐个计算你的GPA分数是很复杂且耗费时间的过程。这个库用来实现一些常见的GPA计算方法，方便你计算你的GPA。

# How to use

```python
import gpalib
a = ['A', 'B', 'A', 'A']
r = gpalib.convert_to_4(a, 'rank')
print(r)
```

```
[4, 3, 4, 4]
```


```python
import gpalib
a = [99, 87, 89, 83, 96]
r = gpalib.convert_to_4(a, 'hundred', 'Beida_4')
print(r)
```
```
[4, 3.7, 3.7, 3.3, 4]
```