# glob模块提供了一个函数用于从目录通配符搜索中生成文件列表
import glob,sys
files=glob.glob('*')
print(files)

# sys.exit(1)
sys.stderr.write('Warning, log file not found starting a new one\n')