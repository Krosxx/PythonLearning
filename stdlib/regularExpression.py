# 正则表达式
import re

s=re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(s)


# 将正则表达式编译成Pattern对象
pattern = re.compile(r'hello')
# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None

match = pattern.match('hello world!helo world!')

if match:
    # 使用Match获得分组信息
    print(match.group())
else:
    print("无法匹配")