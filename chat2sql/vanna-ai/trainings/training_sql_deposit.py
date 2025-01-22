from my_vanna import vn

vn.add_question_sql(
    question="""
全国主要城市住户存款
""",
    sql="""
SELECT
	dv."id",
	dv."value",
	dv.the_year,
	city."name" AS city_name
FROM
	deposit AS dv
	INNER JOIN city ON dv.city_id = city."id";
""",
    documentation="""
全国主要城市住户存款余额数据
""",
)

vn.add_question_sql(
    question="""
西安市住户存款
""",
    sql="""
SELECT
	dv."id",
	dv."value",
	dv.the_year,
	city."name" AS city_name
FROM
	deposit AS dv
	INNER JOIN city ON dv.city_id = city."id"
WHERE
  city."name" = '西安';
""",
    documentation="""
西安市住户存款余额数据
""",
)


vn.add_question_sql(
    question="""
那个城市居民最有钱
""",
    sql="""
SELECT
	city."name" AS city_name,
	AVG(dv."value") AS avg_value
FROM
	deposit AS dv
	INNER JOIN city ON dv.city_id = city."id"
GROUP BY
	city."name"
ORDER BY
	avg_value DESC;
""",
    documentation="""
全国主要城市住户平均存款余额数据,存款余额越多,表示越有钱
""",
)

vn.add_question_sql(
    question="""
2012年至2022年,全国主要城市住户平均存款余额,按余额降序排列
""",
    sql="""
SELECT
	city."name" AS city_name,
	AVG(dv."value") AS avg_value
FROM
	deposit AS dv
	INNER JOIN city ON dv.city_id = city."id"
WHERE
 dv.the_year > 2012 AND dv.the_year <= 2022
GROUP BY
	city."name"
ORDER BY
	avg_value DESC;
""",
    documentation="""
2012年至2022年全国主要城市住户平均存款余额数据,存款余额越多,表示越有钱
""",
)

vn.add_question_sql(
    question="""
2020年,全国主要城市住户存款,按照余额降序排列
""",
    sql="""
SELECT
	dv."id",
	dv."value",
	dv.the_year,
	city."name" AS city_name
FROM
	deposit AS dv
	INNER JOIN city ON dv.city_id = city."id"
WHERE
	dv.the_year = 2020
ORDER BY
	dv."value" DESC;
""",
    documentation="""
2020年全国主要城市住户存款余额数据,存款余额越多,表示越有钱
""",
)

vn.add_question_sql(
    question="""
2020年,全国主要城市住户存款,前10名
""",
    sql="""
SELECT
	dv."id",
	dv."value",
	dv.the_year,
	city."name" AS city_name
FROM
	deposit AS dv
	INNER JOIN city ON dv.city_id = city."id"
WHERE
	dv.the_year = 2020
ORDER BY
	dv."value" DESC
LIMIT 10;
""",
    documentation="""
2020年全国主要城市住户存款余额前10名数据,存款余额越多,表示越有钱,越富裕;反之,越贫穷
""",
)
