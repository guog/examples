from my_vanna import vn

vn.add_question_sql(
    question="""
全国主要城市道路交通等效声级
""",
    sql="""
SELECT
  dv."id",
  dv."value",
  dv.the_year,
  city."name" AS city_name
FROM
  noise AS dv
  INNER JOIN city ON dv.city_id = city."id";
""",
    documentation="""
全国主要城市道路交通等效声级数据
""",
)

vn.add_question_sql(
    question="""
西安道路交通等效声级
""",
    sql="""
SELECT
  dv."id",
  dv."value",
  dv.the_year,
  city."name" AS city_name
FROM
  noise AS dv
  INNER JOIN city ON dv.city_id = city."id"
WHERE
  city."name" = '西安';
""",
    documentation="""
西安市往年道路交通等效声级
""",
)


vn.add_question_sql(
    question="""
全国主要城市道路交通等效声级平均值,按道路交通等效声级平均值降序排列
""",
    sql="""
SELECT
  city."name" AS city_name,
  AVG(dv."value") AS avg_value
FROM
  noise AS dv
  INNER JOIN city ON dv.city_id = city."id"
GROUP BY
  city."name"
ORDER BY
  avg_value DESC;
""",
    documentation="""
全国主要城市道路交通等效声级平均值
""",
)

vn.add_question_sql(
    question="""
2012年至2022年,全国主要城市道路交通等效声级额平均值,按道路交通等效声级平均值降序排列
""",
    sql="""
SELECT
  city."name" AS city_name,
  AVG(dv."value") AS avg_value
FROM
  noise AS dv
  INNER JOIN city ON dv.city_id = city."id"
WHERE
 dv.the_year > 2012 AND dv.the_year <= 2022
GROUP BY
  city."name"
ORDER BY
  avg_value DESC;
""",
    documentation="""
2012年至2022年全国主要城市道路交通等效声级平均值数据
""",
)

vn.add_question_sql(
    question="""
2020年,全国主要城市道路交通等效声级,按道路交通等效声级降序排列
""",
    sql="""
SELECT
  dv."id",
  dv."value",
  dv.the_year,
  city."name" AS city_name
FROM
  noise AS dv
  INNER JOIN city ON dv.city_id = city."id"
WHERE
  dv.the_year = 2020
ORDER BY
  dv."value" DESC;
""",
    documentation="""
2020年全国主要城市道路交通等效声级
""",
)

vn.add_question_sql(
    question="""
2020年,全国主要城市道路交通等效声级,最吵的前10名
""",
    sql="""
SELECT
  dv."id",
  dv."value",
  dv.the_year,
  city."name" AS city_name
FROM
  noise AS dv
  INNER JOIN city ON dv.city_id = city."id"
WHERE
  dv.the_year = 2020
ORDER BY
  dv."value" DESC
LIMIT 10;
""",
    documentation="""
2020年全国主要城市道路交通等效声级前10名数据,道路交通等效声级越大越吵
""",
)

vn.add_question_sql(
    question="""
2020年,全国主要城市中最安静的前10名
""",
    sql="""
SELECT
  dv."id",
  dv."value",
  dv.the_year,
  city."name" AS city_name
FROM
  noise AS dv
  INNER JOIN city ON dv.city_id = city."id"
WHERE
  dv.the_year = 2020
ORDER BY
  dv."value" ASC
LIMIT 10;
""",
    documentation="""
2020年全国主要城市最安静的前10名,道路交通等效声级越小越安静
""",
)
