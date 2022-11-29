CREATE DATABASE  IF NOT EXISTS `todolist` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `todolist`;
-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: todolist
-- ------------------------------------------------------
-- Server version	8.0.30

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
-- Table structure for table `lists`
--

DROP TABLE IF EXISTS `lists`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lists` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `star` tinyint DEFAULT '0',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lists`
--

LOCK TABLES `lists` WRITE;
/*!40000 ALTER TABLE `lists` DISABLE KEYS */;
INSERT INTO `lists` VALUES (1,'My Day',1,'2022-08-22 20:49:11','2022-08-26 12:42:35'),(2,'Important',0,'2022-08-22 20:49:11','2022-09-22 23:41:26'),(3,'Plan',0,'2022-08-22 20:49:11','2022-08-26 12:59:27'),(4,'Mercy\'s Day',0,'2022-08-23 12:04:59','2022-08-23 17:59:26'),(5,'Grocery',0,'2022-08-23 12:05:12','2022-08-23 17:59:26'),(6,'Reading',0,'2022-08-23 12:07:37','2022-08-23 17:59:26'),(14,'Test',0,'2022-08-23 23:17:01','2022-08-24 19:33:09'),(23,'Ana\'s list',0,'2022-08-25 15:55:46','2022-08-25 15:55:46'),(24,'Ana\'s test',0,'2022-08-25 15:55:52','2022-08-25 15:55:52');
/*!40000 ALTER TABLE `lists` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shares`
--

DROP TABLE IF EXISTS `shares`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shares` (
  `id` int NOT NULL AUTO_INCREMENT,
  `from_id` int NOT NULL,
  `to_id` int NOT NULL,
  `list_id` int NOT NULL,
  `accept` tinyint DEFAULT '10',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`,`from_id`,`to_id`,`list_id`),
  KEY `fk_shares_users1_idx` (`from_id`),
  KEY `fk_shares_users2_idx` (`to_id`),
  KEY `fk_shares_lists1_idx` (`list_id`),
  CONSTRAINT `fk_shares_lists1` FOREIGN KEY (`list_id`) REFERENCES `lists` (`id`),
  CONSTRAINT `fk_shares_users1` FOREIGN KEY (`from_id`) REFERENCES `users` (`id`),
  CONSTRAINT `fk_shares_users2` FOREIGN KEY (`to_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shares`
--

LOCK TABLES `shares` WRITE;
/*!40000 ALTER TABLE `shares` DISABLE KEYS */;
INSERT INTO `shares` VALUES (1,1,2,1,10,'2022-08-25 10:32:36','2022-08-25 10:32:36'),(2,1,3,1,10,'2022-08-25 10:32:36','2022-08-25 10:32:36'),(3,1,4,1,1,'2022-08-25 13:51:14','2022-08-26 00:47:32'),(4,2,1,4,1,'2022-08-25 15:50:59','2022-08-26 00:45:18'),(5,4,1,23,0,'2022-08-25 15:55:59','2022-08-26 00:45:21'),(6,4,1,24,1,'2022-08-25 15:56:04','2022-08-26 12:44:32'),(7,1,4,3,10,'2022-08-26 11:26:09','2022-08-26 11:26:09'),(8,1,4,1,10,'2022-08-26 12:43:29','2022-08-26 12:43:29');
/*!40000 ALTER TABLE `shares` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tasks`
--

DROP TABLE IF EXISTS `tasks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tasks` (
  `id` int NOT NULL AUTO_INCREMENT,
  `content` text,
  `due_date` date DEFAULT NULL,
  `complete` tinyint DEFAULT '0',
  `star` tinyint DEFAULT '0',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `list_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_tasks_lists1_idx` (`list_id`),
  CONSTRAINT `fk_tasks_lists1` FOREIGN KEY (`list_id`) REFERENCES `lists` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tasks`
--

LOCK TABLES `tasks` WRITE;
/*!40000 ALTER TABLE `tasks` DISABLE KEYS */;
INSERT INTO `tasks` VALUES (1,'complete button',NULL,1,1,'2022-08-23 15:01:19','2022-08-25 18:42:59',1),(2,'star button',NULL,1,0,'2022-08-23 15:01:19','2022-10-18 20:54:19',1),(3,'list one page',NULL,1,1,'2022-08-23 15:01:19','2022-08-26 01:36:34',1),(5,'Thursday and Monday',NULL,0,1,'2022-08-23 19:36:47','2022-08-26 01:24:19',3),(6,'z letter','2022-08-25',0,1,'2022-08-24 10:57:53','2022-08-24 11:26:07',1),(7,'a letter','2022-08-31',0,0,'2022-08-24 10:58:00','2022-08-24 11:26:12',1),(8,'I should have a test',NULL,0,1,'2022-08-24 15:11:55','2022-08-26 01:03:03',14),(10,'delete function',NULL,0,1,'2022-08-24 17:37:47','2022-08-25 14:28:25',1),(11,'collapse',NULL,0,1,'2022-08-24 17:38:13','2022-08-26 01:24:44',1),(12,'edit list & task',NULL,0,0,'2022-08-24 17:38:34','2022-08-25 14:28:37',1),(13,'plan to cook tomorrow',NULL,0,1,'2022-08-24 18:37:50','2022-08-26 01:24:37',3),(14,'test2',NULL,0,0,'2022-08-24 18:37:57','2022-08-26 01:02:46',14),(18,'test3 - something','2022-08-24',0,1,'2022-08-24 19:13:39','2022-08-26 01:51:33',14),(19,'P-test',NULL,0,0,'2022-08-24 19:24:23','2022-08-24 19:24:23',3),(20,'t-test',NULL,0,0,'2022-08-24 19:24:26','2022-08-24 19:24:26',3),(21,'the whole height','2022-08-26',0,1,'2022-08-26 01:09:34','2022-10-25 15:30:48',2),(22,'the personal page','2022-08-27',0,1,'2022-08-26 01:09:47','2022-10-25 15:30:58',2);
/*!40000 ALTER TABLE `tasks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_list`
--

DROP TABLE IF EXISTS `user_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_list` (
  `user_id` int NOT NULL,
  `list_id` int NOT NULL,
  PRIMARY KEY (`user_id`,`list_id`),
  KEY `fk_users_has_lists_lists1_idx` (`list_id`),
  KEY `fk_users_has_lists_users_idx` (`user_id`),
  CONSTRAINT `fk_users_has_lists_lists1` FOREIGN KEY (`list_id`) REFERENCES `lists` (`id`),
  CONSTRAINT `fk_users_has_lists_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_list`
--

LOCK TABLES `user_list` WRITE;
/*!40000 ALTER TABLE `user_list` DISABLE KEYS */;
INSERT INTO `user_list` VALUES (1,1),(4,1),(1,2),(1,3),(1,4),(2,4),(2,5),(2,6),(1,14),(4,23),(1,24),(4,24);
/*!40000 ALTER TABLE `user_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `pw` char(60) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Jingwen','jwhu@uw.edu','$2b$12$EJaBRHXYdjm/4Kwm.j9nKeiC4xNx.KkJjMNYWotPeSMzPUowdzwsm','2022-08-22 16:28:40','2022-08-26 10:55:48'),(2,'Mercy','mercy@uw.edu','$2b$12$D/BBAutZDSkYVyJ4M5nbVOvMEPBtZhwO9P1fJTs3EHFYOT1FUjt1W','2022-08-22 16:31:18','2022-08-22 16:31:18'),(3,'Tracer','tracer@uw.edu','$2b$12$yts.wNdi4CssyGt5jrsKNu0BnzhquAXzHfkkWkiWJ1YI2jN7IepCK','2022-08-23 14:50:44','2022-08-23 14:50:44'),(4,'Ana','ana@uw.edu','$2b$12$iRx8xDVaCNgPrwfHtUVM9u/1djFuo9f.ebIJ2.Iu2Vd39ugOvLd7O','2022-08-23 21:04:47','2022-08-23 21:04:47'),(5,'Mei','mei@uw.edu','$2b$12$1FNkAHR1LNd2ye6XIaWXwOVfyPgAlAMOZ1tkeaGkB7e0LAk5cxWii','2022-08-24 20:08:59','2022-08-24 20:08:59');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-25 15:59:15
