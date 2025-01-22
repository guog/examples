from my_vanna import vn

df_information_schema = vn.run_sql("SELECT * FROM INFORMATION_SCHEMA.COLUMNS")

df_information_schema_tables = vn.run_sql(
    sql="""
SELECT
    table_schema,
    table_name,
    obj_description(('"' || table_schema || '"."' || table_name || '"')::regclass, 'pg_class') AS table_comment
FROM
    information_schema.tables
WHERE
    table_schema = 'public'
ORDER BY
    table_schema, table_name;
"""
)

df_information_schema_columns = vn.run_sql(
    sql="""
SELECT
    c.table_schema,
    c.table_name,
    c.column_name,
    c.data_type,
    pgd.description AS column_comment
FROM
    information_schema.columns c
LEFT JOIN
    pg_catalog.pg_statio_all_tables as st on c.table_schema = st.schemaname and c.table_name = st.relname
LEFT JOIN
    pg_catalog.pg_description pgd on pgd.objoid = st.relid and pgd.objsubid = c.ordinal_position
WHERE
    c.table_schema = 'public'
ORDER BY
    c.table_schema, c.table_name, c.ordinal_position;
"""
)

plan_schema = vn.get_training_plan_generic(df_information_schema)
# plan_tables = vn.get_training_plan_generic(df_information_schema_tables)
# plan_columns = vn.get_training_plan_generic(df_information_schema_columns)

vn.train(
    documentation="""
这是一份来自中国国家统计局的数据，包含了中国各个主要城市历年数据。
"""
)
vn.train(plan=plan_schema)
# vn.train(plan=plan_tables)
# vn.train(plan=plan_columns)
