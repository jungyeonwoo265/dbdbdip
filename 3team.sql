-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: 3team
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `elementary`
--

DROP TABLE IF EXISTS `elementary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `elementary` (
  `행정구역별` text,
  `2016` int DEFAULT NULL,
  `2017` int DEFAULT NULL,
  `2018` int DEFAULT NULL,
  `2019` int DEFAULT NULL,
  `2020` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elementary`
--

LOCK TABLES `elementary` WRITE;
/*!40000 ALTER TABLE `elementary` DISABLE KEYS */;
INSERT INTO `elementary` VALUES ('행정구역별',2016,2017,2018,2019,2020),('전국',2672843,2674227,2711385,2747219,2693716),('서울특별시',436121,428333,424800,422293,409536),('부산광역시',151207,150863,152775,155589,153527),('대구광역시',125541,124708,125160,126122,122587),('인천광역시',155590,156470,158871,160853,156928),('광주광역시',89095,88189,88622,88990,86419),('대전광역시',85939,84240,83453,82743,79807),('울산광역시',65629,66016,67290,68512,67397),('세종특별자치시',17910,20764,24865,27892,29487),('경기도',727380,733941,752499,769744,761731),('강원도',76772,75722,75412,75617,73478),('충청북도',84052,84240,85344,86709,85135),('충청남도',115309,116963,120152,122424,120115),('전라북도',97895,97383,97606,97731,94661),('전라남도',92981,93233,94134,94952,92405),('경상북도',127825,127642,129290,131374,129079),('경상남도',185325,186619,191016,194606,190849),('제주특별자치도',38272,38901,40096,41068,40575);
/*!40000 ALTER TABLE `elementary` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `new_marry`
--

DROP TABLE IF EXISTS `new_marry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `new_marry` (
  `행정구역별` text,
  `2016` int DEFAULT NULL,
  `2017` int DEFAULT NULL,
  `2018` int DEFAULT NULL,
  `2019` int DEFAULT NULL,
  `2020` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `new_marry`
--

LOCK TABLES `new_marry` WRITE;
/*!40000 ALTER TABLE `new_marry` DISABLE KEYS */;
INSERT INTO `new_marry` VALUES ('행정구역별',2016,2017,2018,2019,2020),('전국',1436948,1379766,1322406,1260117,1183750),('서울특별시',278294,263148,246867,232454,219101),('부산광역시',88339,83545,77755,72403,67632),('대구광역시',61356,59102,56985,54078,49774),('인천광역시',87898,83619,80023,75794,69296),('광주광역시',39309,37534,35659,33878,31648),('대전광역시',42449,40061,37736,35066,32559),('울산광역시',37507,35376,32861,30431,27835),('세종특별자치시',9898,11031,12432,12966,12225),('경기도',383763,372622,366403,356169,341434),('강원도',37445,36456,35685,34928,33486),('충청북도',42984,41480,40021,38744,36691),('충청남도',59967,58589,56829,54280,50406),('전라북도',43026,40699,38328,36082,33503),('전라남도',44128,42584,40173,38275,35888),('경상북도',68288,65118,61237,57670,53145),('경상남도',93833,90261,85031,79222,72264),('제주특별자치도',18469,18546,18387,17682,16868);
/*!40000 ALTER TABLE `new_marry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `solo`
--

DROP TABLE IF EXISTS `solo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `solo` (
  `행정구역별` text,
  `2016` double DEFAULT NULL,
  `2017` double DEFAULT NULL,
  `2018` double DEFAULT NULL,
  `2019` double DEFAULT NULL,
  `2020` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `solo`
--

LOCK TABLES `solo` WRITE;
/*!40000 ALTER TABLE `solo` DISABLE KEYS */;
INSERT INTO `solo` VALUES ('행정구역별',2016,2017,2018,2019,2020),('전국',27.9,28.6,29.3,30.2,31.7),('서울특별시',30.1,31,32,33.4,34.9),('부산광역시',27.7,28.7,29.7,30.7,32.4),('대구광역시',26.4,27.4,28.2,29.4,30.9),('인천광역시',23.9,24.7,25.2,26.6,28.3),('광주광역시',29,29.8,30.2,31.1,32.4),('대전광역시',30.4,31.5,32.5,33.7,36.3),('울산광역시',24.6,25.1,25.6,26.5,27.7),('세종특별자치시',30.6,30.2,30,30.1,31.3),('경기도',23.8,24.4,25.2,26.3,27.6),('강원도',32.1,32.2,32.8,32.9,35),('충청북도',30.3,31,31.8,32.9,34.8),('충청남도',30.4,31.1,31.8,32.5,34.2),('전라북도',30.7,31.2,31.7,32.3,33.8),('전라남도',31.2,31.6,31.9,32.1,33.7),('경상북도',31.3,31.9,32.3,32.7,34.4),('경상남도',28.1,28.6,29.1,29.6,30.9),('제주특별자치도',27.4,28.6,29.4,29.7,31.1);
/*!40000 ALTER TABLE `solo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-03 11:49:33
