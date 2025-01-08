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

 Date: 16/12/2024 17:27:46
*/


-- ----------------------------
-- Table structure for purchase_land
-- ----------------------------
DROP TABLE IF EXISTS "public"."purchase_land";
CREATE TABLE "public"."purchase_land" (
  "id" int4 NOT NULL DEFAULT nextval('purchase_land_id_seq'::regclass),
  "value" float4,
  "city_id" int4,
  "the_year" int2
)
;
ALTER TABLE "public"."purchase_land" OWNER TO "hollysys";
COMMENT ON COLUMN "public"."purchase_land"."value" IS '土地面积,单位:平方米';
COMMENT ON COLUMN "public"."purchase_land"."city_id" IS '城市ID';
COMMENT ON COLUMN "public"."purchase_land"."the_year" IS '年份';
COMMENT ON TABLE "public"."purchase_land" IS '主要城市年度数据-房地产开发企业购置土地面积';

-- ----------------------------
-- Primary Key structure for table purchase_land
-- ----------------------------
ALTER TABLE "public"."purchase_land" ADD CONSTRAINT "purchase_land_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Foreign Keys structure for table purchase_land
-- ----------------------------
ALTER TABLE "public"."purchase_land" ADD CONSTRAINT "purchase_land_city_id_fkey" FOREIGN KEY ("city_id") REFERENCES "public"."city" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
