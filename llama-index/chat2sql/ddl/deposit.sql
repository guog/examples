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

 Date: 16/12/2024 17:26:53
*/


-- ----------------------------
-- Table structure for deposit
-- ----------------------------
DROP TABLE IF EXISTS "public"."deposit";
CREATE TABLE "public"."deposit" (
  "id" int4 NOT NULL DEFAULT nextval('deposit_id_seq'::regclass),
  "value" float4,
  "city_id" int4,
  "the_year" int2
)
;
ALTER TABLE "public"."deposit" OWNER TO "hollysys";
COMMENT ON COLUMN "public"."deposit"."value" IS '住户存款余额,单位元';
COMMENT ON COLUMN "public"."deposit"."city_id" IS '城市ID';
COMMENT ON COLUMN "public"."deposit"."the_year" IS '年份';
COMMENT ON TABLE "public"."deposit" IS '主要城市年度数据-住户存款余额';

-- ----------------------------
-- Primary Key structure for table deposit
-- ----------------------------
ALTER TABLE "public"."deposit" ADD CONSTRAINT "deposit_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Foreign Keys structure for table deposit
-- ----------------------------
ALTER TABLE "public"."deposit" ADD CONSTRAINT "deposit_city_id_fkey" FOREIGN KEY ("city_id") REFERENCES "public"."city" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
