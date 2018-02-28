# 知识点

## 8.1 elif语句
- 可代替switch-case
```
if user.cmd == 'create':
  action = "create item"
elif user.cmd == 'delete':
  action == 'update'
else:
  action = 'invlalid choice... try again!'
```

- 更优解法,使用字典。使用字典对象搜索操作比for/while循环快很多
```
msgs = {'create': 'create item', 'delete': 'delete item', 'update': 'update item'}
default = 'invlalid choice... try again!'
action = msgs.get(user.cmd, default)
```

## 8.2 条件表达式
- 表达式：`X if C else Y`
  1. `smaller = (x < y and [x] or [y])[0]`
  2. `smaller = x if x < y else y`

## 8.3 while语句和for语句
- `while True:`无限循环
+ for循环会访问一个**可迭代对象**中的所有元素，并在所有条目都处理过后结束循环
  - 序列项迭代
  - 序列索引迭代(直接序列迭代比通过索引迭代快)
  - 项和索引迭代

### 8.3.2 迭代器
迭代器对象有一个 next() 方法, 调用后返回下一个条目. 所有条目迭代完后, 迭代器引发一个
StopIteration 异常告诉程序循环结束. for 语句在内部调用next()并捕获异常

### 8.3.3 range()和xrnage()
- `range(start=0, end, step =1)`完整语法
+ `xrange()`
  - 适合在列表范围大时使用
  - 不会再内存中创建列表的完整拷贝。只在for循环中被调用，for循环以外没有意义。
  - 性能远高出`range()`,因为它不生成完整列表
  - 生成的可迭代对象既不是列表也不是一个迭代器
- 判断是否为可迭代对象
```
>>> from collections import Iterable
>>> isinstance(Object, Iterable)
```

### 8.3.4 与序列相关的内建函数
- `sorted()`和`zip()`：返回一个序列（列表）
- `reversed()`和`enumerate()`: 返回迭代器

## 8.4 else语句
- Python中else可以放在条件语句范围外，在while和for循环中使用。
- 在循环使用时,else子句只在循环完成后执行，break语句会同时跳出else代码块

## 8.5 迭代器和iter()函数
通过next()方法，而不是索引来计数。条目全部取出后，会引发一个StopIterartion异常，告诉
外部调用者
  - 为类序列对象提供了一个可扩展迭代器的接口
  - 对列表迭代带来性能提升
  - 在字典中迭代中性能提升
  - 创建真正的迭代接口，而不是原来的随机对象访问
  - 与所有已经存在的用户定义的类以及扩展的模拟序列和映射的对象向后兼容
  - 迭代非序列集合时，可以创建更简洁的代码

```
fetch = iter(seq)
while True:
  try:
    i = fetch.next()
  except StopIteration:
    break
  do_something_to(i)
```
- 文件对象生成的迭代器会自动调用`readline()`方法。循环就可访问文本文件的所有行。
- 对一个对象调用iter()就可以得到他的迭代器

## 8.6 列表解析
列表解析的语法：
```
[expr for iter_var in iterable]
```
这个语句的语法核心是for循环，它迭代iterable对象的所有条目。前面的expr应用于序列的每个
成员，最后的结果值是该表达式产生的列表。
列表解析可以取代`map()`和`lambda`函数
- 计算txt文件的中非空白字符的数目
```
>>> f = open('hhga.txt', 'r')
>>> len([word for line in f for word in line.split()])
```
- 快速计算文件大小
```
import os
>>> os.stat('hhga.txt').st_size
499L
>>> f.seek(0)
>>> sum([len(word) for line in f for word in line.line.split()])
408
```

## 8.7生成器表达式
- 列表解析的不足就是必须要生成所有的数据，用以创建整个列表。对有大量数据的迭代器有负面效应。
生成器表达式可以解决这个问题。
- 生成器表达式与列表解析非常相似，而且它们的基本语法基本相同；不过它并不真正创建数字列表，
而是返回一个生成器，这个生成器在每次计算一个条目后，把这个条目“产生”(yield)出来。生成器
表达式使用了“延迟计算”(lazy evaluation),所以它在内存上更有效。

- 利用简单的生成器和生成器表达式创建交叉配对。
```
rows = [1, 2, 3, 17]
def cols():
  yield 56
  yield 2
  yield 1
x_product_pairs = ((i, j) for i in rows for j in cols())
```
- 一行Python程序读取文件最长的行:
`return max(len(x.strip()) for x in open('/etx/motd'))`
