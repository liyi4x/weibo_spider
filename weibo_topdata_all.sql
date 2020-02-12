/*
 Navicat Premium Data Transfer

 Source Server         : test
 Source Server Type    : MySQL
 Source Server Version : 50729
 Source Host           : 127.0.0.1:3306
 Source Schema         : weibo

 Target Server Type    : MySQL
 Target Server Version : 50729
 File Encoding         : 65001

 Date: 12/02/2020 15:23:43
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for weibo_topdata_all
-- ----------------------------
DROP TABLE IF EXISTS `weibo_topdata_all`;
CREATE TABLE `weibo_topdata_all`  (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `time` timestamp(0) NULL DEFAULT NULL,
  `pos` tinyint(2) NULL DEFAULT NULL,
  `desc` varchar(30) CHARACTER SET gb2312 COLLATE gb2312_chinese_ci NULL DEFAULT NULL,
  `desc_extr` int(10) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
