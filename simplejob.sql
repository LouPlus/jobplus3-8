-- MySQL dump 10.13  Distrib 5.5.50, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: simplejob
-- ------------------------------------------------------
-- Server version	5.5.50-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `simplejob`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `simplejob` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `simplejob`;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('0d03e26cf9e5');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company`
--

DROP TABLE IF EXISTS `company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company` (
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `email` varchar(64) NOT NULL,
  `password` varchar(128) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `website` varchar(64) DEFAULT NULL,
  `address` varchar(64) DEFAULT NULL,
  `logo` varchar(256) DEFAULT NULL,
  `finance_stage` varchar(128) DEFAULT NULL,
  `field` varchar(128) DEFAULT NULL,
  `tags` varchar(128) DEFAULT NULL,
  `description` varchar(1024) DEFAULT NULL,
  `company_info` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_company_email` (`email`),
  UNIQUE KEY `ix_company_name` (`name`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `company_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company`
--

LOCK TABLES `company` WRITE;
/*!40000 ALTER TABLE `company` DISABLE KEYS */;
INSERT INTO `company` VALUES ('2018-02-03 13:17:13','2018-02-04 02:00:36',1,'SenseTime初创团队','st@st.com','pbkdf2:sha256:50000$J0Riu4bV$317b097a544e6e872a7674abd1a59d1fe97d1415358e0c7061f15484b279c49d',1,'http://sensetime.com/','北京海淀区中关村东路1号院清华科技园创业大厦7层','https://www.lgstatic.com/thumbnail_300x300/i/image2/M00/1B/63/CgotOVoCv-eAPNQcAARRTfkzqqo936.png','B轮','移动互联网',NULL,'专注于计算机视觉和深度学习','<p>SenseTime商汤集团是一家科技创新公司，致力于引领人工智能核心&ldquo;深度学 习&rdquo;技术突破，构建人工智能、大数据分析行业解决方案。我们成功聚集了当下华人中最出色、最有影响力的的深度学习、计算机视觉科学家，以及来自于谷歌、百 度、微软、联想等一批产业界的领军人物。</p>\r\n\r\n<p><img alt=\"\" src=\"https://www.lgstatic.com/i/image/M00/03/0D/CgqKkVanQISAd-4JAAIVLzmEmlU930.jpg\" style=\"height:302px; width:403px\" /></p>\r\n\r\n<p>在人工智能产业兴起的大背景下，商汤集团凭借在技术、人才、专利上超过十年的积累，迅速成为了人工智能行业领军企业。在应用性技术上，基于深度学习 的人脸识别、文字识别、人体识别、车辆识别、物体识别、图像处理等技术在业界遥遥领先；在业务上，商汤集团深耕金融、移动互联网、安防监控三大行业，与银 联、京东、拉卡拉、华为、小米、新浪微博、科大讯飞、东方网力、英伟达等各行业巨头深度合作，推动行业产品智能化升级。</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>商汤集团已经在北京、深圳、香港成立工作地点，立足中国，汇集世界各地顶尖人才，合力打造一家独一无二的中国的原创技术公司，让中国智造慧及全球。加入我们，参与这个激动人心的改变世界的历程！</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>核心技术：人脸技术；视频监控；图像识别；图像及视频编辑；深度学习。</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>SenseTime团队对外提供全球最精准的人脸识别技术，2014年，我们已经在人脸识别和物体识别上分别超过了&nbsp;Facebook和 Google（相关可见媒体报道）。也是在2014年，SenseTime已吸引来自顶级风投的千万美元注资。目前，SenseTime已经开始对外提供 全球最精准的人脸识别技术以及集成了人脸识别、危险品识别、行为检测、车辆检测等的安防监控系统。</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>SenseTime的使命是向中国注入世界领先的计算机视觉原创技术，引领计算机视觉、深度学习技术创新，赋予计算机看懂世界的能力，以此改变世界。</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>加入我们，一起做中国的原创技术。</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>-搜索&ldquo;SenseTime&rdquo;关注公众微信号，获取来自&nbsp;SenseTime&nbsp;的更多资讯</p>\r\n'),('2018-02-03 13:35:18','2018-02-03 13:35:18',2,'德邦物流','db@db.com','pbkdf2:sha256:50000$EQ2wSHJL$28dd0dfc1f14b2669550cf30c24413bff2c30d298cc5a3ba53cf529b5759be7f',2,'http://www.deppon.com/','上海青浦区徐泾镇明珠路1018号','https://www.lgstatic.com/thumbnail_300x300/image1/M00/00/34/Cgo8PFTUXJGAH6cpAABbzm-gnx4711.jpg','不需要融资','企业服务',NULL,'物畅其流，人尽其才。','<p>&nbsp; &nbsp; &nbsp; IBM、麦肯锡、埃森哲在华长期合作伙伴。</p>\r\n\r\n<p>&nbsp; &nbsp; &nbsp; 德邦目前在职 IT 技术人员1500 余名，独占德邦园区 2栋办公楼。 业务内容主要提供管理平台、系统应用及移动的需求研发运维等配套服务。 提供管理平台、系统应用及移动的需求研发运维等配套服务。 作为德邦旗下最重要的子公司，全年投入资金3亿左右用以开展创新型项目、咨询公司合作及软硬件更新 ，且投资持续增长。旨在提供最优化的物流 IT 决方案，成为 IT 反推业务发展的创新型互联网企。&nbsp;</p>\r\n\r\n<p>&nbsp; &nbsp; &nbsp; 公司投资过亿与世界知名咨询公麦肯锡、 IBM等咨询公司合作，梳理运作流程，结合 IT 规划设计，为公司发展新蓝图。&nbsp;</p>\r\n\r\n<p>&nbsp; &nbsp; &nbsp; 在这里，你可以接触行业技术领先的咨询顾问 ；</p>\r\n\r\n<p>&nbsp; &nbsp; &nbsp; 在这里，你可以学习到圈内最专业的技术 ；&nbsp;</p>\r\n\r\n<p>&nbsp; &nbsp; &nbsp; 在这里，你可以触及到极具规模的开发项目 ；&nbsp;</p>\r\n\r\n<p>&nbsp; &nbsp; &nbsp; 德邦所承接大型项目无一不体现着国内物流行业信息化建设的高端水平。</p>\r\n'),('2018-02-03 13:44:34','2018-02-03 13:44:34',3,'小站教育','xz@xz.com','pbkdf2:sha256:50000$lsR9q7fM$456259c1e26656ee71e7aab2073302276a11c525a8a836c27458ea0eb0e4f697',3,'http://www.zhan.com/','上海静安区延平路121号三和大厦3楼','https://www.lgstatic.com/thumbnail_300x300/i/image/M00/01/81/CgqKkVZuVzOAapNrAAAVX5ft27M478.jpg','C轮','教育',NULL,'全国最大在线留学培训机构','<p>社会荣誉:</p>\r\n\r\n<p>中国网：2014最具学员满意度在线教育品牌</p>\r\n\r\n<p>网&nbsp; 易：2014最具影响力外语培训品牌</p>\r\n\r\n<p>腾&nbsp; 讯：2014最具影响力外语机构</p>\r\n\r\n<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2015年度知名教育品牌</p>\r\n\r\n<p>新&nbsp; 浪：2014最具口碑影响力在线教育机构</p>\r\n\r\n<p>2015最具口碑影响力在线教育机构</p>\r\n\r\n<p>2016中国家长及学员最喜爱的在线教育产品</p>\r\n\r\n<p>福布斯：2015中国最快成长科技公司</p>\r\n\r\n<p>百&nbsp; 度：2016年度权威外语教育机构</p>\r\n\r\n<p>36&nbsp; 氪：TMT行业未上市企业估值TOP200</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>公司介绍</p>\r\n\r\n<p>小站教育作为一家只专注留学领域的互联网教育品牌，始终走在真人在线授课模式及教育理念前沿，引领着国内留学在线语培的革新方向，已深耕中国本土多 年，更基于对中国式留学的深入理解与积极探索，至今已发展成为拥有500多万注册用户、15万付费学员的知名真人在线留学语培机构，目前已开设 TOEFL、IELTS、SAT、ACT、GRE 和 GMAT等1对1及1对多，多元化在线课程。未来更会以&ldquo;一站式留学生态圈&rdquo; 为服务理念，在教学模式上不断推陈出新，优化最短提分路径，为中国留学生打造一条轻松愉快的赢+留学之路。</p>\r\n'),('2018-02-03 13:55:23','2018-02-03 13:55:23',4,'妙计旅行','mj@mj.com','pbkdf2:sha256:50000$ehTjKjkO$53d84f28cf9f4f7cdd7d3af0095e57238a2a7938dab9638d305db5a0d9210d37',4,'http://www.mioji.com/','北京东城区国学胡同11号','https://www.lgstatic.com/thumbnail_300x300/i/image/M00/07/17/Cgp3O1bNjT-AFsa6AAA83c0vejw711.jpg','B轮','移动互联网',NULL,'技术实力派，境外自由行智能搜索引擎。','<p>标配Mac、人体工程学座椅、23寸IPS显示器，入职员工人人都有；</p>\r\n\r\n<p>十四薪、五险一金、补充医保、丰厚期权，该有的都有了；</p>\r\n\r\n<p>坐拥雍和宫国子监，二环内近2000平私家妙府四合院，别人家可真没有；</p>\r\n\r\n<p>星级大厨in house，自助早餐午餐，下午茶零食饮料，竟然还有Lavazza咖啡无限供应；</p>\r\n\r\n<p>顶级配置的互联网研发团队，真正扁平管理，顶级美元基金的品牌背书，足够靠谱绝无仅有。</p>\r\n\r\n<p><img alt=\"\" src=\"https://www.lgstatic.com/i/image/M00/03/43/CgqKkVaxyEqAagz5AAJJrN6Ca6U549.png\" style=\"height:302px; width:403px\" /></p>\r\n'),('2018-02-04 01:17:47','2018-02-04 09:46:29',5,'实验楼','syl@syl.com','pbkdf2:sha256:50000$Ujwxe4bX$e3b7aafae98cef8ec5bd2df352b9df191e2e4ef8287918c9058a72dcd35d7b88',5,'http://www.shiyanlou.com/','成都成都市武侯区天府软件园e区','https://www.lgstatic.com/thumbnail_300x300/i/image/M00/3E/22/CgqKkVdzobeAB7eoAAIUnE7Fe1M567.png','A轮','教育','绩效奖金,专项奖金,带薪年假,弹性工作,技能培训,扁平管理','国内领先的IT技术实训平台，提供编程、运维、测试、云计算、大数据等全面的IT技术在线实践课程。','<p>成都琛石科技有限公司成立于2013年，前身是SimpleCloud虚拟化技术团队，一直致力于为IT相关专业学生提供在线实验平台，同时为企业、高校提供简单易用的虚拟化及云计算产品。<br />\r\n核心产品是国内首家以实验为核心的IT在线教育平台&ldquo;实验楼&rdquo;，基于虚拟化技术的SimpleCloud&trade;轻量级云平台软件以及面向计算机教育培训领域的SimpleLab&trade;虚拟实训室解决方案。</p>\r\n\r\n<p><img alt=\"\" src=\"https://www.lgstatic.com/i/image/M00/4B/94/CgqKkVef-OCAW37OAAFd3BfBCVQ201.jpg\" style=\"height:302px; width:402px\" /></p>\r\n'),('2018-02-04 01:32:58','2018-02-04 01:32:58',6,'推想科技','tx@tx.com','pbkdf2:sha256:50000$EPsXxvwF$11d1553b3bf2a669df1ce596bb4498aa820dff97c0f211bc3eb32603119867fc',6,'http://www.infervision.com/',' 北京朝阳区北京市朝阳区远洋国际','https://www.lgstatic.com/thumbnail_300x300/i/image/M00/32/49/CgpEMlk2a02ANq7hAAF_5Ga34-0970.jpg','B轮','企业服务',NULL,' 推想科技，想医所想','<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 北京推想科技有限公司，致力于采用人工智能深度学习的方法分析医学影像数据，期待为影像科医生提供精确、高效的辅助工具，从而让医生从繁重的重复性工作中得以解放。</p>\r\n\r\n<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;推想科技推出的智能影像辅助筛查产品目前已与北京协和医院、上海长征医院、武汉同济医院等40余家中国顶级三甲医院及顶级医学设备制造 商GE达成合作，在AI医疗影像辅助诊断领域已申请7项国内外专利与科研成果。获得红杉资本、启明创投、广发证券、英诺天使基金等中国最顶尖的投资机构的 近两亿元人民币投资，其中B轮融资1.2亿元的成绩更是创造了人工智能领域单笔最大的投资额。</p>\r\n\r\n<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;公司以研发为生命力，全公司80%人员为研发人员，其中90%来自芝加哥大学、加利福尼亚大学洛杉矶分校、杜克大学、剑桥大学和帝国理 工大学等全球顶级名校，并在当代深度学习领域中具有深度研究经验。公司还在不断扩大研发团队，紧密与临床相结合，确保产品始终保持领先，满足医生不断提升 的诊断辅助需求。</p>\r\n\r\n<p><img alt=\"\" src=\"https://www.lgstatic.com/i/image2/M00/00/7A/CgoB5lm7ngKAeeiZAApH5kLGn74813.jpg\" style=\"height:302px; width:403px\" /></p>\r\n'),('2018-02-04 01:44:49','2018-02-04 02:02:47',7,'Udesk','udesk@udesk.com','pbkdf2:sha256:50000$6yFj7ncE$fb65cadf55397e0f84eec7900b425064f57df53ebbe75c7c5abe48ff97e81e0e',7,'http://www.udesk.cn/','北京市西直门南大街2号成铭大厦C座16层（西直门地铁站C口）','https://www.lgstatic.com/thumbnail_300x300/i/image/M00/5A/F5/CgpFT1mNZfWAXLGYAAAM0qJze1U983.png','B轮','企业服务',NULL,'中国最具创新力的客户服务平台','<p>Udesk（www.udesk.cn），致力于为中国企业提供最优秀的新一代企业级智能客服系统，由顶级风投DCM、君联资本投资。</p>\r\n\r\n<p><img alt=\"\" src=\"https://www.lgstatic.com/i/image/M00/01/39/Cgp3O1Zk8heAN01hAAC3H7Y2nNI482.png\" style=\"height:302px; width:403px\" /></p>\r\n'),('2018-02-04 01:55:09','2018-02-04 01:55:09',8,'58到家','58dj@58dj.com','pbkdf2:sha256:50000$pGKtFAyV$a7edc6ec9bfbeebdcb7c1109c80dbb6ecdd9051f4d1eeee2e4eafd8418f9fb6a',8,'http://58daojia.com/','北京 - 朝阳区 - 北苑 - 北苑路大羊坊10号桑普大厦5层','https://www.lgstatic.com/thumbnail_300x300/i/image/M00/1E/7B/CgpFT1kQS-CASJMHAABBN5ZSEu071.jpeg','A轮','O2O',NULL,'互联网O2O领域领先企业 ','<p>&bull;58到家是由纽交所上市集团58.com Inc. (NYSE:WUBA) 旗下独立运营的生活服务O2O品牌，与信息分类品牌58同城并行；<br />\r\n&bull;58到家是以居家场景为核心，以上门服务为切入点，正逐步发展为全国唯一一家提供一站式、标准化专业到家服务的平台；<br />\r\n&bull;58到家是后分类时代唯一一家实现全国性布局的生活服务O2O开放平台。</p>\r\n\r\n<p><img alt=\"\" src=\"https://www.lgstatic.com/i/image/M00/87/C5/Cgp3O1hrcdGAZT7gAAEd_UuWxds369.jpg\" style=\"height:302px; width:403px\" /></p>\r\n');
/*!40000 ALTER TABLE `company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `delivery`
--

DROP TABLE IF EXISTS `delivery`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `delivery` (
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `company_id` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `company_response` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `job_id` (`job_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `delivery_ibfk_1` FOREIGN KEY (`job_id`) REFERENCES `job` (`id`) ON DELETE SET NULL,
  CONSTRAINT `delivery_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `delivery`
--

LOCK TABLES `delivery` WRITE;
/*!40000 ALTER TABLE `delivery` DISABLE KEYS */;
INSERT INTO `delivery` VALUES ('2018-02-04 14:08:36','2018-02-04 14:08:36',1,6,10,5,1,NULL),('2018-02-05 00:44:22','2018-02-05 00:45:28',2,10,10,7,2,NULL);
/*!40000 ALTER TABLE `delivery` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job`
--

DROP TABLE IF EXISTS `job`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `job` (
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `salary_low` int(11) NOT NULL,
  `salary_high` int(11) NOT NULL,
  `description` text,
  `treatment` text,
  `exp` varchar(64) NOT NULL,
  `degree` varchar(64) NOT NULL,
  `stacks` varchar(128) DEFAULT NULL,
  `location` varchar(24) DEFAULT NULL,
  `is_fulltime` tinyint(1) DEFAULT NULL,
  `tags` varchar(128) DEFAULT NULL,
  `company_id` int(11) DEFAULT NULL,
  `is_enable` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `company_id` (`company_id`),
  KEY `ix_job_name` (`name`),
  CONSTRAINT `job_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `user` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job`
--

LOCK TABLES `job` WRITE;
/*!40000 ALTER TABLE `job` DISABLE KEYS */;
INSERT INTO `job` VALUES ('2018-02-03 13:20:59','2018-02-03 13:20:59',1,'计算机图形学算法研究员',15,25,'<p>任职资格：</p>\r\n\r\n<p>1. 本科或以上学历，计算机、电子信息或软件等相关专业；<br />\r\n2. 有较强的编程和算法实现能力，算法基础扎实，掌握常见设计模式，具有良好代码风格和质量意识，能独立完成算法模块设计、开发和测试；<br />\r\n3. 优秀的分析问题和解决问题的能力，对解决具有挑战性的问题充满激情；<br />\r\n4. 良好的沟通能力和团队合作能力；<br />\r\n5. 满足以下一个或多个条件，包括但不限于：<br />\r\n1) 熟悉GPU并行计算，熟悉CUDA或OpenCL编程；<br />\r\n2) 精通计算机图形学，熟悉游戏的图形渲染技术及算法；<br />\r\n3) 精通OpenGL/OpenGL ES开发，熟练Shader及移动端3D开发；<br />\r\n4) 掌握3D建模软件（例如3DMAX, MAYA, Blender等）的使用，了解常用的3D模型格式；<br />\r\n5) 掌握自研绘制引擎或者常用游戏引擎框架（例如Unity3D, UrealEngine等）等开发；<br />\r\n6. 有较丰富的相关经验者优先，比如有一年以上在知名公司进行计算机图形学方面实习的经验，或来自国内外计算机图形学/计算机视觉等领域内知名实验室。</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>工作职责：</p>\r\n\r\n<p>1. 负责计算机图形学算法的开发与性能提升，负责下述研究课题中的一项或多项，包括但不限于：3D渲染、3D引擎、材质恢复、光照估计、3D重建等相关算法等；<br />\r\n2. 推动计算机图形学算法在众多实际应用领域的性能优化和落地；<br />\r\n3. 提出和实现最前沿的算法，保持算法在工业界和学术界的领先。</p>\r\n\r\n<h3>&nbsp;</h3>\r\n','发展空间大,弹性工作,技术大牛,扁平管理','3-5年','本科及以上','opengl,C++','北京',1,'游戏,算法,图像处理,计算机视觉',1,1),('2018-02-03 13:38:39','2018-02-03 13:38:39',2,'MySQL（DBA）',14,25,'<p>具体职责：数据库运维</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>负责mysql相关系统的架构设计、容灾备份，健康状态监 控、性能优化及故障处理，确保数据库服务的正常稳定运行和应急响应。</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>任职要求</p>\r\n\r\n<p>1.熟悉数据库的各项技术：包括高可用架构、监控、数据库性能调优、备份恢复、故障诊断等；</p>\r\n\r\n<p>2.熟悉mysql的SQL开发,熟悉SQL Tuning；精通mysql数据库分库分表策略、数据迁移方案；</p>\r\n\r\n<p>3.具备大型数据库高并发量设计经验，熟悉分布式架构设计；</p>\r\n\r\n<p>4.熟悉linux操作系统，能熟练编写shell脚本，熟悉操作系统、存储、网 络以及硬件的优化和诊断能力；</p>\r\n\r\n<h3>&nbsp;</h3>\r\n','1500+IT团队，IBM战略合作','3-5年','大专','MySQL','上海',1,'数据库,DBA',2,1),('2018-02-03 13:49:34','2018-02-03 13:49:34',3,'Java',15,25,'<p>岗位职责：</p>\r\n\r\n<p>1、负责公司项目的研发、升级及维护；</p>\r\n\r\n<p>2、参与项目需求分析、技术调研，负责设计完成需求规格、软件架构、测试策略，撰写相关的技术文档；</p>\r\n\r\n<p>3、搭建研发环境，完成系统中相关软件模块的编码、调试、单元测试、功能验证，保证项目进度和产品质量；</p>\r\n\r\n<p>4、协助完成项目的系统集成测试、版本交付等工作，对项目实施和维护提供支持。</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>岗位要求：</p>\r\n\r\n<p>1、3年以上Java开发工作经验，本科及以上学历，计算机相关专业（985、211学校优先考虑）；</p>\r\n\r\n<p>2、精通SSH等JAVA开源框架，有EJB开发经验；</p>\r\n\r\n<p>3、熟悉Jboss，Tomcat等服务的部署、配置和优化 ；</p>\r\n\r\n<p>4、熟悉MYSQL数据库，具有数据库设计和编程经验；</p>\r\n\r\n<p>5、熟悉使用svn，git等版本管理工具；</p>\r\n\r\n<p>6、熟悉SOAP&amp;REST Web Service及其设计规范；</p>\r\n\r\n<p>7、熟悉大型项目的版本管理及分支管理；</p>\r\n\r\n<p>8、了解持续集成及持续部署的概念及常用框架；</p>\r\n\r\n<p>9、了解NoSQL类数据库及其应用；</p>\r\n\r\n<p>10、有参与开源项目的经验或能提供自己的Github者优先；</p>\r\n\r\n<p>11、有大规模Web项目的开发经验者优先；</p>\r\n\r\n<p>12、有PHP,ANDROID,IOS一项或多项经验者优先。</p>\r\n\r\n<p>13、有大型互联网公司经验、教育行业工作经验的优先考虑</p>\r\n\r\n<h3>&nbsp;</h3>\r\n','团队协作佳,平台发展好,福利待遇好,上升空间大','3-5年','本科及以上','Java','上海',1,'专家,资深,高级,中级,教育',3,1),('2018-02-03 13:59:24','2018-02-04 01:12:24',4,'Web前端',10,20,'<p>【工作职责】</p>\r\n\r\n<ul>\r\n	<li>\r\n	<p>负责妙计旅行PC端和移动端的Web产品开发，并确保产品的兼容性。</p>\r\n	</li>\r\n</ul>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>【职位要求】</p>\r\n\r\n<ul>\r\n	<li>\r\n	<p>计算机、通信、电子等相关专业本科以上学历；</p>\r\n	</li>\r\n	<li>\r\n	<p>熟悉reactjs，jquery，有react native开发经验优先；</p>\r\n	</li>\r\n	<li>\r\n	<p>精通HTML5，CSS3，熟悉移动WebAPP开发、跨平台、UIWebView、Webkit；</p>\r\n	</li>\r\n	<li>\r\n	<p>熟悉nodejs，npm，了解php；</p>\r\n	</li>\r\n	<li>\r\n	<p>较好的团队协作能力，较强的学习能力。</p>\r\n	</li>\r\n</ul>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>【妙计福利】</p>\r\n\r\n<ul>\r\n	<li>\r\n	<p>标配Mac、人体工程学座椅、23寸IPS显示器，入职员工人人都有；</p>\r\n	</li>\r\n	<li>\r\n	<p>十四薪、五险一金、补充医保、丰厚期权，该有的都有了；</p>\r\n	</li>\r\n	<li>\r\n	<p>坐拥雍和宫国子监，二环内近2000平私家妙府四合院，别人家可真没有；</p>\r\n	</li>\r\n	<li>\r\n	<p>星级大厨in house，自助早餐午餐，下午茶零食饮料，竟然还有Lavazza咖啡无限供应；</p>\r\n	</li>\r\n	<li>\r\n	<p>顶级配置的互联网研发团队，真正扁平管理，顶级美元基金的品牌背书，足够靠谱绝无仅有。</p>\r\n	</li>\r\n</ul>\r\n\r\n<h3>&nbsp;</h3>\r\n','十四薪,六险一金,良好平台,包三餐','3年及以下','本科及以上','web','北京',1,'中级,初级,前端,web前端,移动端',4,1),('2018-02-03 14:02:51','2018-02-03 14:02:51',5,'Python高级开发工程师',15,25,'<p>【工作职责】 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p>\r\n\r\n<ul>\r\n	<li>\r\n	<p>参与妙计大数据平台、旅行知识图谱的构建； &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p>\r\n	</li>\r\n	<li>\r\n	<p>参与数据抓取、数据清洗、数据融合、数据统计分析等工作。 &nbsp; &nbsp; &nbsp;</p>\r\n	</li>\r\n</ul>\r\n\r\n<p>&nbsp; &nbsp; &nbsp; &nbsp;</p>\r\n\r\n<p>【职位要求】 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</p>\r\n\r\n<ul>\r\n	<li>\r\n	<p>精通Python，2年或以上Python项目经验；熟悉网络编程、多线程编程、大规模文本数据处理等，有良好代码风格；</p>\r\n	</li>\r\n	<li>\r\n	<p>有Team leader经验或拥有成为Team leader的潜力；</p>\r\n	</li>\r\n	<li>\r\n	<p>熟悉常见的数据结构和算法，有数据抓取/融合/挖掘经验优先； &nbsp;</p>\r\n	</li>\r\n	<li>\r\n	<p>&nbsp;熟悉数据库知识，熟练掌握SQL，熟悉redis/mongodb/rabbitmq等；</p>\r\n	</li>\r\n	<li>\r\n	<p>熟练使用Linux/Mysql/Gitlab/Vim等，1年或以上Linux平台下的项目经验，有shell编程基础优先； &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p>\r\n	</li>\r\n	<li>\r\n	<p>&nbsp;强烈的责任感，善于分析和解决问题，有较好的沟通和团队合作的能力。&nbsp;</p>\r\n	</li>\r\n</ul>\r\n\r\n<p>【妙计福利】</p>\r\n\r\n<ul>\r\n	<li>\r\n	<p>标配Mac、人体工程学座椅、23寸IPS显示器，入职员工人人都有；</p>\r\n	</li>\r\n	<li>\r\n	<p>十四薪、五险一金、补充医保、丰厚期权，该有的都有了；</p>\r\n	</li>\r\n	<li>\r\n	<p>坐拥雍和宫国子监，二环内近2000平私家妙府四合院，别人家可真没有；</p>\r\n	</li>\r\n	<li>\r\n	<p>星级大厨in house，自助早餐午餐，下午茶零食饮料，竟然还有Lavazza咖啡无限供应；</p>\r\n	</li>\r\n	<li>\r\n	<p>顶级配置的互联网研发团队，真正扁平管理，顶级美元基金的品牌背书，足够靠谱绝无仅有。</p>\r\n	</li>\r\n</ul>\r\n\r\n<h3>&nbsp;</h3>\r\n','福利待遇好,气氛活跃,免费三餐','3年及以下','本科及以上','Python,Java','北京',1,'爬虫,算法,大数据',4,1),('2018-02-04 01:21:29','2018-02-04 01:21:29',6,'大数据技术专家',15,20,'<p>这是一份有趣的工作，你的实验及课程可以帮助很多互联网行业的企业及在职人员，让几十万用户在实践中收获最新的技术。</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>工作职责：</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>1. 探索最前沿的 Spark/Hadoop 等大数据相关技术并设计实验教程；</p>\r\n\r\n<p>2. 负责实验楼大数据相关实验课程的维护和开发；</p>\r\n\r\n<p>3. 负责设计大数据技术学习路径，进阶的教学项目；</p>\r\n\r\n<p>4. 为企业客户的技术员工提供创新的内部实训解决方案；</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>工作要求：</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>1. 大学本科及以上学历，计算机或相关专业，至少3年以上大数据平台研发经验；</p>\r\n\r\n<p>2. 熟悉 Spark 或 Hadoop 等主流平台，具备丰富的项目经验；</p>\r\n\r\n<p>3. 较好的学习能力和沟通能力；</p>\r\n\r\n<p>4. 写过出版过技术书籍、技术教程或技术博客优先；</p>\r\n\r\n<p>5. 较好的 Presentation 能力，有内部培训经验优先，在 Github 有开源项目维护者优先；</p>\r\n\r\n<h3>&nbsp;</h3>\r\n','在线教育,最新技术,工程师团队,技术氛围好','3-5年','本科及以上','算法','成都',1,'专家,数据分析,搜索,数据挖掘,推荐',5,1),('2018-02-04 01:23:09','2018-02-04 01:23:09',7,'PHP 技术专家',15,20,'<p>这是一份有趣的工作，你的实验及课程可以帮助很多互联网行业的企业及在职人员，让几十万用户在实践中收获最新的技术。</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>工作职责：</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>1. 探索最前沿的 PHP 相关技术并设计实验教程；</p>\r\n\r\n<p>2. 负责实验楼 PHP 相关实验课程的维护和开发；</p>\r\n\r\n<p>3. 负责设计 PHP 技术学习路径，进阶的教学项目；</p>\r\n\r\n<p>4. 为企业客户的技术员工提供创新的内部实训解决方案；</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>工作要求：</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>1. 大学本科及以上学历，计算机或相关专业，至少3年以上 PHP 研发经验；</p>\r\n\r\n<p>2. 熟悉 PHP Laravel 或 Lumen 等主流框架，具备丰富的项目经验；</p>\r\n\r\n<p>3. 熟悉 MySQL，MongoDB，Redis，并具备相关开发经验，可以独自完成基本的 Web 前端页面；</p>\r\n\r\n<p>4. 较好的学习能力和沟通能力；</p>\r\n\r\n<p>5. 写过出版过技术书籍、技术教程或技术博客优先；</p>\r\n\r\n<p>6. 较好的 Presentation 能力，有内部培训经验优先，在 Github 有开源项目维护者优先；</p>\r\n','在线教育,最新技术,工程师团队,技术氛围好','3-5年','本科及以上','PHP','成都',1,'专家',5,1),('2018-02-04 01:25:49','2018-02-04 01:25:49',8,'市场运营',5,7,'<p>岗位职责：</p>\r\n\r\n<p>&nbsp;&nbsp; 1.在线学习平台活动策划及运营；</p>\r\n\r\n<p>&nbsp;&nbsp; 2.收集用户反馈，处理用户需求；</p>\r\n\r\n<p>&nbsp;&nbsp; 3.完善用户拉新、促活、留存机制；</p>\r\n\r\n<p>&nbsp;&nbsp; 4.技术社区内容编辑运营。</p>\r\n\r\n<p>岗位要求：</p>\r\n\r\n<p>&nbsp;&nbsp; 1.文字功底扎实，1年以上互联网相关工作经验；</p>\r\n\r\n<p>&nbsp;&nbsp; 2.互联网重度使用者，热爱在线教育行业；</p>\r\n\r\n<p>&nbsp;&nbsp; 3.计算机相关专业，熟悉编程语言，自学能力强。</p>\r\n\r\n<p>加分：</p>\r\n\r\n<p>&nbsp;&nbsp; 1.对IT技术有兴趣，经常刷Github、知乎、V2EX等；</p>\r\n\r\n<p>&nbsp;&nbsp; 2.有线上活动策划成功经验或经常参加线下技术交流活动。</p>\r\n','旅游团建,商业保险,成长快速,学习资源多','3年及以下','本科及以上','新媒体','成都',1,'网站,内容,用户,用户增长,社区',5,1),('2018-02-04 01:35:47','2018-02-04 01:35:47',9,'python工程师',6,12,'<p>-我们是谁- &nbsp;</p>\r\n\r\n<p>推想科技是一家人工智能+医疗行业的高科技公司，运用深度学习技术为医疗影像辅助筛查提供快捷、准确的解决方案，目前我们的产品已经渗透到了全国众多顶级医院的影像临床工作中，并获得一致好评，我们希望可以运用人工智能技术，将优质的医学诊断带给千家万户。&nbsp;</p>\r\n\r\n<p>&nbsp;-你未来的小伙伴- &nbsp;</p>\r\n\r\n<p>公司保持开放的工作环境，全公司80%的人员为研发人员，其中90%来自芝加哥大学、杜克大学、剑桥大学和帝国理工大学等全球顶级名校，并在当代深度学习领域具有深度研究经验。&nbsp;</p>\r\n\r\n<p>-你需要做的事- &nbsp;</p>\r\n\r\n<p>①带着我们的服务器到各合作医院进行上线和维护； ②和我们可爱的医生群体保持沟通，及时解决他们使用过程中的问题，随时反馈总结。&nbsp;</p>\r\n\r\n<p>-我们期待的你-</p>\r\n\r\n<p>&nbsp;①计算机相关专业毕业，学历大专以上；&nbsp;</p>\r\n\r\n<p>②有编程基础（会python），了解linux和SQL数据库；&nbsp;</p>\r\n\r\n<p>③喜欢出差、喜欢与人交流&nbsp;</p>\r\n\r\n<p>&nbsp;-我们给到你的-</p>\r\n\r\n<p>&nbsp;广阔的成长空间&nbsp;</p>\r\n\r\n<p>&nbsp;完善的培训制度&nbsp;</p>\r\n\r\n<p>&nbsp;技术大牛分享会&nbsp;</p>\r\n\r\n<p>&nbsp;12+2的薪资报酬&nbsp;</p>\r\n\r\n<p>&nbsp;入职即有的五险一金&nbsp;</p>\r\n\r\n<p>&nbsp;加班打车报销&nbsp;</p>\r\n\r\n<p>&nbsp;饭费补贴&nbsp;</p>\r\n\r\n<p>&nbsp;无限零食&nbsp;</p>\r\n\r\n<p>&nbsp;节日福利&nbsp;</p>\r\n\r\n<p>&nbsp;不定时团建&nbsp;</p>\r\n\r\n<p>&nbsp;其他福利启动中。。。</p>\r\n','人工智能,快速成长,弹性工作,14薪','3年及以下','大专','运维','北京',1,'数据库,实施,医疗健康',6,1),('2018-02-04 01:47:43','2018-02-04 01:47:43',10,'Go',25,35,'<p>职位描述：</p>\r\n\r\n<p>+ VoIP通讯平台设计开发；</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>职位要求：</p>\r\n\r\n<p>+ 2年以上Go/C++实际项目经验，5年以上开发经验；</p>\r\n\r\n<p>+ 有大型系统设计经验；</p>\r\n\r\n<p>+ 熟练使用git；</p>\r\n\r\n<p>+ 熟悉Nginx配置；</p>\r\n\r\n<p>+ 自信，工作习惯良好：自驱动，擅于合作，代码清晰整洁；</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>职位亮点：</p>\r\n\r\n<p>Udesk是国内领先的企业级智能客服平台，拥有数千家企业用户，为企业提供了一套集智能问答、即时通讯、VoIP、工单、知识库、数据分析为一体的完整的客服系统解决方案。</p>\r\n\r\n<p>Udesk知名客户有海底捞、星巴克、凯撒旅游、中青旅耀悦、金山WPS、每日优鲜、58转转、宝洁等。覆盖了餐饮、本地生活、旅游、O2O、企业服务等行业。</p>\r\n\r\n<p>Udesk去年6月完成B轮1亿人民币融资，投资方为君联资本、DCM。公司收入增长迅速，有大量的付费用户并开始盈利。</p>\r\n\r\n<p>Udesk前端用Ember.js，后台用Java、Ruby、Go。日接口调用量超过200,000,000次。</p>\r\n\r\n<h3>&nbsp;</h3>\r\n','高成长企业,团队强悍,待遇丰厚','5-10年','本科及以上','Java,Go','北京',1,'平台设计',7,1),('2018-02-04 01:58:58','2018-02-04 01:58:58',11,'人力资源经理',10,20,'<p>岗位职责：</p>\r\n\r\n<p>1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;根据公司的发展战略，深入了解业务与人员发展状况，评估并明确组织发展与人才发展对HR的需求，协助公司各业务部门负责人做好人员招聘、人员培训、人员管理、内部激励、员工关系、团队文化等人力资源工作，全方位提供专业性建议方案并推动实施；</p>\r\n\r\n<p>2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;根据业务需求，负责公司各空缺岗位的招聘，长期、持续推动人才招聘和储备工作，并完善招聘流程；</p>\r\n\r\n<p>3.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;负责公司HR政策、制度、体系、重点项目和各项人才管理活动在业务部门的落地与推动执行，并针对执行结果进行有效反馈和改进；</p>\r\n\r\n<p>4.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;建立、维护人事档案，办理和更新劳动合同，包括员工劳动合同续签、转签、改签相关手续的办理；</p>\r\n\r\n<p>5.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;负责员工入职、转正、调岗、晋升、离职等人事手续办理；</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>任职要求：</p>\r\n\r\n<p>1、全日制本科及以上学历，2年以上相关工作经验；有招聘&amp;BP工作经验优先。</p>\r\n\r\n<p>2、熟悉并深入理解人力资源工作，在人才招聘、员工关系管理模块有扎实的专业功底及丰富实践经验，熟悉劳动法相关法律、法规；</p>\r\n\r\n<p>3、有极强的成就导向和责任心，学习能力强，有良好的合作精神、执行力强，工作有计划性，逻辑性和条理性好,抗压能力强；</p>\r\n\r\n<p>4、能独立解决复杂的人事管理实际问题，具有较强的协调能力、人际理解力，善于整合资源驱动目标达成。&nbsp;&nbsp;</p>\r\n\r\n<h3>&nbsp;</h3>\r\n','发展空间大','3-5年','本科及以上','HRBP','北京',1,'招聘,企业培训,薪酬福利,绩效考核',8,1);
/*!40000 ALTER TABLE `job` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobhunter_job`
--

DROP TABLE IF EXISTS `jobhunter_job`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jobhunter_job` (
  `user_id` int(11) NOT NULL,
  `job_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  KEY `job_id` (`job_id`),
  CONSTRAINT `jobhunter_job_ibfk_1` FOREIGN KEY (`job_id`) REFERENCES `job` (`id`) ON DELETE CASCADE,
  CONSTRAINT `jobhunter_job_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobhunter_job`
--

LOCK TABLES `jobhunter_job` WRITE;
/*!40000 ALTER TABLE `jobhunter_job` DISABLE KEYS */;
/*!40000 ALTER TABLE `jobhunter_job` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) DEFAULT NULL,
  `password` varchar(128) NOT NULL,
  `phone` varchar(18) DEFAULT NULL,
  `is_enable` tinyint(1) DEFAULT NULL,
  `email` varchar(64) NOT NULL,
  `role` smallint(6) DEFAULT NULL,
  `company_id` int(11) DEFAULT NULL,
  `resume_url` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_user_email` (`email`),
  UNIQUE KEY `ix_user_phone` (`phone`),
  UNIQUE KEY `ix_user_username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('2018-02-03 13:13:21','2018-02-03 13:13:21',1,'SenseTime初创团队','pbkdf2:sha256:50000$goLctciC$5a4c2a660ae975ed4a83949c536bf8cddafe42f5d096f5ebffde525f075dcc02',NULL,1,'st@st.com',20,NULL,NULL),('2018-02-03 13:31:32','2018-02-03 13:31:32',2,'德邦物流','pbkdf2:sha256:50000$U9mfqW68$0134b66a571f51d0954e61b6416abbd329c7af686807b873d9d3597a05b835e3',NULL,1,'db@db.com',20,NULL,NULL),('2018-02-03 13:41:28','2018-02-03 13:41:28',3,'小站教育','pbkdf2:sha256:50000$Z0VyW0NH$5d23b17e8cedbecfafdfd739544db7ab1ee2e54da5467099528502e0f62f22f0',NULL,1,'xz@xz.com',20,NULL,NULL),('2018-02-03 13:52:14','2018-02-03 13:52:14',4,'妙计旅行','pbkdf2:sha256:50000$SZNTg5Ls$e9126a25b39506038ae1ef283d942defaacbd59972ea175c4e125671c0b1be31',NULL,1,'mj@mj.com',20,NULL,NULL),('2018-02-04 01:14:04','2018-02-04 01:14:04',5,'实验楼','pbkdf2:sha256:50000$bRHkx0hL$d5197f46514ad29cb428d0032e594e547e39fcb685c1af7b6b8d063b47b89244',NULL,1,'syl@syl.com',20,NULL,NULL),('2018-02-04 01:29:02','2018-02-04 01:29:02',6,'推想科技','pbkdf2:sha256:50000$nZB6QI3d$6f87b162f1f6edf714a9b21b94dd0f8a8b4520c220fa69966f4f602c79929b47',NULL,1,'tx@tx.com',20,NULL,NULL),('2018-02-04 01:41:25','2018-02-04 01:41:25',7,'Udesk企业级智能客服平台','pbkdf2:sha256:50000$aRTsG8uu$30a2fef7f6ec78216080dce4efb3e887100a34625b7283d5666bcd107181299c',NULL,1,'udesk@udesk.com',20,NULL,NULL),('2018-02-04 01:51:54','2018-02-04 01:51:54',8,'58到家','pbkdf2:sha256:50000$b6rSYRGj$3c7fdf87d28b6376584811ce6af745fb7a136b2f689e09ebd4fedd9bb0a090aa',NULL,1,'58dj@58dj.com',20,NULL,NULL),('2018-02-04 13:53:30','2018-02-04 13:53:30',9,'admin','pbkdf2:sha256:50000$YZ4rsOLL$2387e635d2ea90fb9a44ccf1ca49c68d0658ed776b0e3a8cc2cd887999e16987','18666551234',1,'admin@admin.com',30,NULL,NULL),('2018-02-04 13:54:26','2018-02-05 00:44:09',10,'job','pbkdf2:sha256:50000$urtb0PsC$858d1b79a35ab2a75d838969bfa14f6d2663a38819da17fbff4449af92f87a69','18666211234',1,'job@job.com',10,NULL,'http://127.0.0.1:5000/_uploads/pdfs/mozilla.pdf');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-02-05  9:57:05
