from my_vanna import vn

vn.add_question_sql(
    question="""
全国主要城市商品房销售面积
""",
    sql="""
SELECT
  dv."id",
  dv."value",
  dv.the_year,
  city."name" AS city_name
FROM
  house_sale AS dv
  INNER JOIN city ON dv.city_id = city."id";
""",
    documentation="""
全国主要城市商品房销售面积数据
""",
)

vn.add_question_sql(
    question="""
西安商品房销售面积
""",
    sql="""
SELECT
  dv."id",
  dv."value",
  dv.the_year,
  city."name" AS city_name
FROM
  house_sale AS dv
  INNER JOIN city ON dv.city_id = city."id"
WHERE
  city."name" = '西安';
""",
    documentation="""
西安市往年商品房销售面积
""",
)


vn.add_question_sql(
    question="""
全国主要城市商品房销售面积平均值,按面积平均值降序排列
""",
    sql="""
SELECT
  city."name" AS city_name,
  AVG(dv."value") AS avg_value
FROM
  house_sale AS dv
  INNER JOIN city ON dv.city_id = city."id"
GROUP BY
  city."name"
ORDER BY
  avg_value DESC;
""",
    documentation="""
全国主要城市商品房销售面积平均值
""",
)

vn.add_question_sql(
    question="""
2012年至2022年,全国主要城市商品房销售面积平均值,按面积平均值降序排列
""",
    sql="""
SELECT
  city."name" AS city_name,
  AVG(dv."value") AS avg_value
FROM
  house_sale AS dv
  INNER JOIN city ON dv.city_id = city."id"
WHERE
 dv.the_year > 2012 AND dv.the_year <= 2022
GROUP BY
  city."name"
ORDER BY
  avg_value DESC;
""",
    documentation="""
2012年至2022年全国主要城市商品房销售面积平均值数据
""",
)

vn.add_question_sql(
    question="""
2020年,全国主要城市商品房销售面积,按照面积降序排列
""",
    sql="""
SELECT
  dv."id",
  dv."value",
  dv.the_year,
  city."name" AS city_name
FROM
  house_sale AS dv
  INNER JOIN city ON dv.city_id = city."id"
WHERE
  dv.the_year = 2020
ORDER BY
  dv."value" DESC;
""",
    documentation="""
2020年全国主要城市商品房销售面积数据
""",
)

vn.add_question_sql(
    question="""
2020年,全国主要城市商品房销售面积,前10名
""",
    sql="""
SELECT
  dv."id",
  dv."value",
  dv.the_year,
  city."name" AS city_name
FROM
  house_sale AS dv
  INNER JOIN city ON dv.city_id = city."id"
WHERE
  dv.the_year = 2020
ORDER BY
  dv."value" DESC
LIMIT 10;
""",
    documentation="""
2020年全国主要城市商品房销售面积前10名数据
""",
)
