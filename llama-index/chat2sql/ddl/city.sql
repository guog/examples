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

 Date: 16/12/2024 17:26:37
*/


-- ----------------------------
-- Table structure for city
-- ----------------------------
DROP TABLE IF EXISTS "public"."city";
CREATE TABLE "public"."city" (
  "id" int4 NOT NULL DEFAULT nextval('city_id_seq'::regclass),
  "name" varchar(255) COLLATE "pg_catalog"."default"
)
;
ALTER TABLE "public"."city" OWNER TO "hollysys";
COMMENT ON COLUMN "public"."city"."name" IS '城市名称';
COMMENT ON TABLE "public"."city" IS '城市列表';

-- ----------------------------
-- Primary Key structure for table city
-- ----------------------------
ALTER TABLE "public"."city" ADD CONSTRAINT "city_pkey" PRIMARY KEY ("id");
