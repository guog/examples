from my_vanna import vn
from utils import read_file_to_string

vn.add_ddl(
    ddl=read_file_to_string("ddl/city.sql"),
    documentation="""
这个表是中国的主要城市。包含两列,id列表示城市主键,name列表示城市名称。""",
)

vn.add_ddl(
    ddl=read_file_to_string("ddl/deposit.sql"),
    documentation="""
这个表是中国的主要城市以往每年的住户存款余额(单位:元)数据。
包含四列,id列表示主键,value列表示住户存款余额(单位:元),the_year列表示年份,city_id列表示城市外键,与city表关联,city表的name字段表示城市名称。""",
)

vn.add_ddl(
    ddl=read_file_to_string("ddl/house_sale.sql"),
    documentation="""
这个表是中国的主要城市以往每年的商品房销售面积(单位:平方米)数据。
包含四列,id列表示主键,value列表示商品房销售面积(单位:平方米),the_year列表示年份,city_id列表示城市外键,与city表关联,city表的name字段表示城市名称。""",
)

vn.add_ddl(
    ddl=read_file_to_string("ddl/investment.sql"),
    documentation="""
这个表是中国的主要城市以往每年的房地产开发投资额(单位:元)数据。
包含四列,id列表示主键,value列表示房地产开发投资额(单位:元),the_year列表示年份,city_id列表示城市外键,与city表关联,city表的name字段表示城市名称。""",
)

vn.add_ddl(
    ddl=read_file_to_string("ddl/noise.sql"),
    documentation="""
这个表是中国的主要城市以往每年的道路交通等效声级(单位:dB(A))数据。
包含四列,id列表示主键; value列表示道路交通等效声级(单位:dB(A)),value值越小越好,表示越安静;the_year列表示年份,city_id列表示城市外键,与city表关联,city表的name字段表示城市名称。""",
)

vn.add_ddl(
    ddl=read_file_to_string("ddl/population.sql"),
    documentation="""
这个表是中国的主要城市以往每年的年末户籍人口(单位:人)数据。
包含四列,id列表示主键,value列表示年末户籍人口(单位:人),the_year列表示年份,city_id列表示城市外键,与city表关联,city表的name字段表示城市名称。""",
)

vn.add_ddl(
    ddl=read_file_to_string("ddl/purchase_land.sql"),
    documentation="""
这个表是中国的主要城市以往每年的房地产开发企业购置土地面积(单位:平方米)数据。
包含四列,id列表示主键,value列表示房地产开发企业购置土地面积(单位:平方米),the_year列表示年份,city_id列表示城市外键,与city表关联,city表的name字段表示城市名称。""",
)
