# pickle 模块
# python的pickle模块实现了基本的数据序列和反序列化。
#
# 通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
#
# 通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。
#
# 基本接口：pickle.dump(obj, file, [,protocol])
import pickle,pprint

data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}
file=open('data.pk','wb')
x=pickle.dump(data1,file)
file.close()


pkl_file = open('data.pk', 'rb')
data1 = pickle.load(pkl_file)
pprint.pprint(data1)

pkl_file.close()