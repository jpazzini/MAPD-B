-- MySQL dump 10.13  Distrib 8.0.28, for Linux (x86_64)
--
-- Host: localhost    Database: my_db
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `productID` int NOT NULL AUTO_INCREMENT,
  `productName` varchar(30) NOT NULL DEFAULT '',
  `unitPrice` float NOT NULL DEFAULT '100000',
  `unitsInStock` int unsigned NOT NULL DEFAULT '0',
  `isDiscontinued` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`productID`),
  UNIQUE KEY `productID` (`productID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'Founders Porter',4.9,12,0),(2,'Punk IPA',5.2,45,0),(3,'HB Dunkel',4.5,250,0),(5,'Damm Complot',3.7,120,0);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supplier_to_product`
--

DROP TABLE IF EXISTS `supplier_to_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `supplier_to_product` (
  `prodID` int NOT NULL,
  `supID` int NOT NULL,
  PRIMARY KEY (`prodID`,`supID`),
  KEY `FK_sup` (`supID`),
  CONSTRAINT `FK_prod` FOREIGN KEY (`prodID`) REFERENCES `products` (`productID`),
  CONSTRAINT `FK_sup` FOREIGN KEY (`supID`) REFERENCES `suppliers` (`supplierID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supplier_to_product`
--

LOCK TABLES `supplier_to_product` WRITE;
/*!40000 ALTER TABLE `supplier_to_product` DISABLE KEYS */;
INSERT INTO `supplier_to_product` VALUES (2,1),(3,1);
/*!40000 ALTER TABLE `supplier_to_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suppliers`
--

DROP TABLE IF EXISTS `suppliers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suppliers` (
  `supplierID` int NOT NULL AUTO_INCREMENT,
  `supplierName` varchar(30) NOT NULL DEFAULT '',
  `countryCode` char(3) NOT NULL DEFAULT 'ITA',
  `email` varchar(30) NOT NULL,
  PRIMARY KEY (`supplierID`),
  UNIQUE KEY `supplierID` (`supplierID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suppliers`
--

LOCK TABLES `suppliers` WRITE;
/*!40000 ALTER TABLE `suppliers` DISABLE KEYS */;
INSERT INTO `suppliers` VALUES (1,'A hop in the park','USA','anewemail@ahop.com'),(2,'Allez Hops! Cave à bièr','FRA','itsme@allezhops.com'),(3,'Wild Hops','ITA','myemail@wildhops.it'),(4,'Beer Paradise','ITA','beer@beerparadise.it');
/*!40000 ALTER TABLE `suppliers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-29 20:32:29
