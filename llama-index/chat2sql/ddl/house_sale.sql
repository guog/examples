/*
 Navicat Premium Dump SQL

 Source Server         : localhost-postgres
 Source Server Type    : PostgreSQL
 Source Server Version : 160003 (160003)
 Source Host           : localhost:5432
 Source Catalog        : hollysys
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 160003 (160003)
 File Encoding         : 65001

 Date: 16/12/2024 17:27:04
*/


-- ----------------------------
-- Table structure for house_sale
-- ----------------------------
DROP TABLE IF EXISTS "public"."house_sale";
CREATE TABLE "public"."house_sale" (
  "id" int4 NOT NULL DEFAULT nextval('house_sale_id_seq'::regclass),
  "value" float4,
  "city_id" int4,
  "the_year" int2
)
;
ALTER TABLE "public"."house_sale" OWNER TO "hollysys";
COMMENT ON COLUMN "public"."house_sale"."value" IS '商品房销售面积,单位平方米';
COMMENT ON COLUMN "public"."house_sale"."city_id" IS '城市ID';
COMMENT ON COLUMN "public"."house_sale"."the_year" IS '年份';
COMMENT ON TABLE "public"."house_sale" IS '主要城市年度数据-商品房销售面积';

-- ----------------------------
-- Primary Key structure for table house_sale
-- ----------------------------
ALTER TABLE "public"."house_sale" ADD CONSTRAINT "house_sale_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Foreign Keys structure for table house_sale
-- ----------------------------
ALTER TABLE "public"."house_sale" ADD CONSTRAINT "house_sale_city_id_fkey" FOREIGN KEY ("city_id") REFERENCES "public"."city" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
