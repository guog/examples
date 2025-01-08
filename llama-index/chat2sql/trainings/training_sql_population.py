from my_vanna import vn

vn.add_question_sql(
    question="""
全国主要城市户籍人口
""",
    sql="""
SELECT
  dv."id",
  dv."value",
  dv.the_year,
  city."name" AS city_name
FROM
  population AS dv
  INNER JOIN city ON dv.city_id = city."id";
""",
    documentation="""
全国主要城市户籍人口数据
""",
)

vn.add_question_sql(
    question="""
西安户籍人口
""",
    sql="""
SELECT
  dv."id",
  dv."value",
  dv.the_year,
  city."name" AS city_name
FROM
  population AS dv
  INNER JOIN city ON dv.city_id = city."id"
WHERE
  city."name" = '西安';
""",
    documentation="""
西安市往年户籍人口
""",
)


vn.add_question_sql(
    question="""
全国主要城市户籍人口平均值,按户籍人口平均值降序排列
""",
    sql="""
SELECT
  city."name" AS city_name,
  AVG(dv."value") AS avg_value
FROM
  population AS dv
  INNER JOIN city ON dv.city_id = city."id"
GROUP BY
  city."name"
ORDER BY
  avg_value DESC;
""",
    documentation="""
全国主要城市户籍人口平均值
""",
)

vn.add_question_sql(
    question="""
2012年至2022年,全国主要城市户籍人口额平均值,按户籍人口平均值降序排列
""",
    sql="""
SELECT
  city."name" AS city_name,
  AVG(dv."value") AS avg_value
FROM
  population AS dv
  INNER JOIN city ON dv.city_id = city."id"
WHERE
 dv.the_year > 2012 AND dv.the_year <= 2022
GROUP BY
  city."name"
ORDER BY
  avg_value DESC;
""",
    documentation="""
2012年至2022年全国主要城市户籍人口平均值数据
""",
)

vn.add_question_sql(
    question="""
2020年,全国主要城市户籍人口,按户籍人口降序排列
""",
    sql="""
SELECT
  dv."id",
  dv."value",
  dv.the_year,
  city."name" AS city_name
FROM
  population AS dv
  INNER JOIN city ON dv.city_id = city."id"
WHERE
  dv.the_year = 2020
ORDER BY
  dv."value" DESC;
""",
    documentation="""
2020年全国主要城市户籍人口,户籍人口越大表示人越多,越拥挤
""",
)

vn.add_question_sql(
    question="""
2020年,那个城市人最多,人最多的前10名
""",
    sql="""
SELECT
  dv."id",
  dv."value",
  dv.the_year,
  city."name" AS city_name
FROM
  population AS dv
  INNER JOIN city ON dv.city_id = city."id"
WHERE
  dv.the_year = 2020
ORDER BY
  dv."value" DESC
LIMIT 10;
""",
    documentation="""
2020年全国主要城市户籍人口前10名数据,户籍人口越大表示人越多,越拥挤,越热闹
""",
)

vn.add_question_sql(
    question="""
2020年,那个城市户籍人口最少,户籍人口最少的前10名
""",
    sql="""
SELECT
  dv."id",
  dv."value",
  dv.the_year,
  city."name" AS city_name
FROM
  population AS dv
  INNER JOIN city ON dv.city_id = city."id"
WHERE
  dv.the_year = 2020
ORDER BY
  dv."value" ASC
LIMIT 10;
""",
    documentation="""
2020年全国主要城市户籍人口后10名数据,户籍人口越小表示人越少,越冷清
""",
)
