from my_vanna import vn

vn.add_question_sql(
    question="""
主要城市有多少个?
""",
    sql="""
SELECT
  COUNT(0)
FROM
  city;
""",
    documentation="""
这个问题是关于主要城市的数量。
""",
)

vn.add_question_sql(
    question="""
主要城市有哪些?
""",
    sql="""
SELECT
  id,name
FROM
  city
ORDER BY
  name ASC;
""",
    documentation="""
这个问题是关于主要城市信息,能获取主要城市列表,并按照城市名称升序排列。
""",
)
