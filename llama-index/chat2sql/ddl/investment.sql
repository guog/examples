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

 Date: 16/12/2024 17:27:14
*/


-- ----------------------------
-- Table structure for investment
-- ----------------------------
DROP TABLE IF EXISTS "public"."investment";
CREATE TABLE "public"."investment" (
  "id" int4 NOT NULL DEFAULT nextval('investment_id_seq'::regclass),
  "value" float4,
  "city_id" int4,
  "the_year" int2
)
;
ALTER TABLE "public"."investment" OWNER TO "hollysys";
COMMENT ON COLUMN "public"."investment"."value" IS '投资额,单位:元';
COMMENT ON COLUMN "public"."investment"."city_id" IS '城市ID';
COMMENT ON COLUMN "public"."investment"."the_year" IS '年份';
COMMENT ON TABLE "public"."investment" IS '主要城市年度数据-房地产开发投资额';

-- ----------------------------
-- Primary Key structure for table investment
-- ----------------------------
ALTER TABLE "public"."investment" ADD CONSTRAINT "investment_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Foreign Keys structure for table investment
-- ----------------------------
ALTER TABLE "public"."investment" ADD CONSTRAINT "investment_city_id_fkey" FOREIGN KEY ("city_id") REFERENCES "public"."city" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
