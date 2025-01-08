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

 Date: 16/12/2024 17:27:36
*/


-- ----------------------------
-- Table structure for population
-- ----------------------------
DROP TABLE IF EXISTS "public"."population";
CREATE TABLE "public"."population" (
  "id" int4 NOT NULL DEFAULT nextval('population_id_seq'::regclass),
  "value" float4,
  "city_id" int4,
  "the_year" int2
)
;
ALTER TABLE "public"."population" OWNER TO "hollysys";
COMMENT ON COLUMN "public"."population"."value" IS '人口,单位:人';
COMMENT ON COLUMN "public"."population"."city_id" IS '城市ID';
COMMENT ON COLUMN "public"."population"."the_year" IS '年份';
COMMENT ON TABLE "public"."population" IS '主要城市年度数据-年末户籍人口';

-- ----------------------------
-- Primary Key structure for table population
-- ----------------------------
ALTER TABLE "public"."population" ADD CONSTRAINT "population_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Foreign Keys structure for table population
-- ----------------------------
ALTER TABLE "public"."population" ADD CONSTRAINT "population_city_id_fkey" FOREIGN KEY ("city_id") REFERENCES "public"."city" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
