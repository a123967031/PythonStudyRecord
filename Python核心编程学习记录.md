- method for printing dict char
```Python
dict2 = {'name': 'venus', 'port': 6969}
print 'host %(name)s is running on port %(port)d' %dict2
```
**Python核心编程 P167**

- dict中的sorted()方法使用
```Python
dict2 = {'name': 'venus', 'port': 6969}
for eachKey in sorted(dict2):
  print 'dict2 key', eachKey, 'has value', dict2[eachKey]
```
**Python核心编程 P173**

- dict.update() and dict.fromkeys() method
`dicta.update({}.fromkeys(srcstr[len(dststr):]))`

- list.append()分辨错误实例和正确实例
```Python
mylist = mylist.append(mychr) #error
mylist.append(mychr) #correct
```

- ['m', 'n', 'o', None, None, None, 'g', 'h', 'i']中NoneType使用join方法
```Python
mylist = ['m', 'n', 'o', None, None, None, 'g', 'h', 'i']
''.join(mylist)
TypeError: sequence item 3: expected string, NoneType found
```

- 过滤None字符
`mylist = [ch for ch in mylist if ch]`

-模块显示名字、类型、值用法
```Python
#!/usr/bin/env python
#-*- coding:utf-8 -*-

module = raw_input('输入模块名：')
m1 = __import__(module)
m2 = dir(m1)
print m2
for i in m2:
    print 'name: ',i
    print 'type: ', type(getattr(m1, i))
    print 'value: ', getattr(m1, i)
    print
```
**练习9-8**
