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
迭代器对象有一个 next() 方法, 调用后返回下一个条目. 所有条目迭代完后, 迭代器引发一 个 StopIteration 异常告诉程序循环结束. for 语句在内部调用next()并捕获异常

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
