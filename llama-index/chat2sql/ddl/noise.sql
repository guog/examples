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

 Date: 16/12/2024 17:27:27
*/


-- ----------------------------
-- Table structure for noise
-- ----------------------------
DROP TABLE IF EXISTS "public"."noise";
CREATE TABLE "public"."noise" (
  "id" int4 NOT NULL DEFAULT nextval('noise_id_seq'::regclass),
  "value" float4,
  "city_id" int4,
  "the_year" int2
)
;
ALTER TABLE "public"."noise" OWNER TO "hollysys";
COMMENT ON COLUMN "public"."noise"."value" IS '噪声值,单位dB(A)';
COMMENT ON COLUMN "public"."noise"."city_id" IS '城市ID';
COMMENT ON COLUMN "public"."noise"."the_year" IS '年份';
COMMENT ON TABLE "public"."noise" IS '主要城市年度数据-道路交通等效声级';

-- ----------------------------
-- Primary Key structure for table noise
-- ----------------------------
ALTER TABLE "public"."noise" ADD CONSTRAINT "noise_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Foreign Keys structure for table noise
-- ----------------------------
ALTER TABLE "public"."noise" ADD CONSTRAINT "noise_city_id_fkey" FOREIGN KEY ("city_id") REFERENCES "public"."city" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
