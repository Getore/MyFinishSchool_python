from TreatmentInsert import treatment_insert
from SplitFile import split_file
from TheraNameInsert import thera_name_insert

# 分成治则、治法两个文件
split_file()
# 启动程序，进行 治则数据库的插入
treatment_insert()
# 启动程序，进行 治法名称数据库的插入
thera_name_insert()

