CREATE DATABASE  IF NOT EXISTS "lojinhaMA78" /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `lojinhaMA78`;
-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: henrique-717-henrique-1205.b.aivencloud.com    Database: lojinhaMA78
-- ------------------------------------------------------
-- Server version	8.0.45

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
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ 'a8a6ea6b-3e7c-11f1-bbbe-f21c1bd3e180:1-64';

--
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente` (
  `id_cliente` int NOT NULL AUTO_INCREMENT,
  `nome_cliente` varchar(100) NOT NULL,
  `sobrenome_cliente` varchar(100) DEFAULT NULL,
  `cpf_cliente` varchar(11) DEFAULT NULL,
  `telefone_cliente` varchar(20) DEFAULT NULL,
  `email_cliente` varchar(100) DEFAULT NULL,
  `cidade_cliente` varchar(50) NOT NULL,
  `cep_cliente` varchar(10) NOT NULL,
  PRIMARY KEY (`id_cliente`),
  UNIQUE KEY `cpf_cliente` (`cpf_cliente`),
  UNIQUE KEY `telefone_cliente` (`telefone_cliente`),
  UNIQUE KEY `email_cliente` (`email_cliente`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `estoque`
--

DROP TABLE IF EXISTS `estoque`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estoque` (
  `id_estoque` int NOT NULL AUTO_INCREMENT,
  `id_produto` int DEFAULT NULL,
  `quantidade_estoque` int NOT NULL,
  `qauntidade_minima_estoque` int NOT NULL,
  `local_estoque` varchar(50) NOT NULL,
  `data_hora_entrada` datetime NOT NULL,
  `data_hora_saida` datetime NOT NULL,
  `lote` varchar(100) NOT NULL,
  `validade` date NOT NULL,
  `status_estoque` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id_estoque`),
  KEY `id_produto` (`id_produto`),
  CONSTRAINT `estoque_ibfk_1` FOREIGN KEY (`id_produto`) REFERENCES `produto` (`id_produto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `fornecedor`
--

DROP TABLE IF EXISTS `fornecedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fornecedor` (
  `id_fornecedor` int NOT NULL AUTO_INCREMENT,
  `nome_fornecedor` varchar(100) NOT NULL,
  `cnpj_fornecedor` varchar(20) NOT NULL,
  `telefone_fornecedor` varchar(20) NOT NULL,
  `email_fornecedor` varchar(100) NOT NULL,
  `status_fornecedor` enum('ATIVO','INATIVO','BLOQUEADO') DEFAULT NULL,
  PRIMARY KEY (`id_fornecedor`),
  UNIQUE KEY `cnpj_fornecedor` (`cnpj_fornecedor`),
  UNIQUE KEY `email_fornecedor` (`email_fornecedor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `item_venda`
--

DROP TABLE IF EXISTS `item_venda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `item_venda` (
  `id_item_venda` int NOT NULL AUTO_INCREMENT,
  `id_produto` int DEFAULT NULL,
  `id_venda` int DEFAULT NULL,
  `quantidade_item` int NOT NULL,
  `precoUnitario` decimal(8,2) NOT NULL,
  `subtotal_item` decimal(8,2) NOT NULL,
  `imposto_item` decimal(8,2) DEFAULT NULL,
  `observacao_item` text,
  PRIMARY KEY (`id_item_venda`),
  UNIQUE KEY `id_venda` (`id_venda`,`id_produto`),
  CONSTRAINT `item_venda_ibfk_1` FOREIGN KEY (`id_item_venda`) REFERENCES `venda` (`id_venda`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pagamento`
--

DROP TABLE IF EXISTS `pagamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pagamento` (
  `id_pagamento` int NOT NULL AUTO_INCREMENT,
  `id_venda` int NOT NULL,
  `tipo_pagamento` varchar(40) NOT NULL,
  `valor_pagamento` decimal(5,2) NOT NULL,
  `data_pagamento` datetime NOT NULL,
  `parcelas_pagamento` int NOT NULL,
  `imposto_pagamento` decimal(5,2) NOT NULL,
  `bandeira_pagamento` varchar(25) DEFAULT 'Pagamento sem cartão',
  `observacao_pagamento` text,
  PRIMARY KEY (`id_pagamento`),
  KEY `id_venda` (`id_venda`),
  CONSTRAINT `pagamento_ibfk_1` FOREIGN KEY (`id_venda`) REFERENCES `venda` (`id_venda`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `produto`
--

DROP TABLE IF EXISTS `produto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `produto` (
  `id_produto` int NOT NULL AUTO_INCREMENT,
  `nome_produto` varchar(80) NOT NULL,
  `descricao_produto` text NOT NULL,
  `preco_produto` decimal(5,2) NOT NULL,
  `categoria_produto` varchar(30) NOT NULL,
  `marca_produto` varchar(30) NOT NULL,
  `codigo_barras` varchar(50) NOT NULL,
  `data_validade_produto` date NOT NULL DEFAULT '2026-01-09',
  `peso_produto` decimal(5,2) NOT NULL,
  `status_produto` enum('disponível','indisponível') NOT NULL,
  PRIMARY KEY (`id_produto`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `venda`
--

DROP TABLE IF EXISTS `venda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `venda` (
  `id_venda` int NOT NULL AUTO_INCREMENT,
  `data_hora_venda` datetime NOT NULL,
  `valor_total` decimal(10,2) DEFAULT NULL,
  `forma_pagamento` varchar(50) NOT NULL,
  `desconto_venda` decimal(10,2) DEFAULT NULL,
  `id_cliente_venda` int DEFAULT NULL,
  `status_venda` varchar(40) NOT NULL,
  `observacoes_venda` text,
  `caixa_venda` int NOT NULL,
  PRIMARY KEY (`id_venda`),
  KEY `id_cliente_venda` (`id_cliente_venda`),
  CONSTRAINT `venda_ibfk_1` FOREIGN KEY (`id_cliente_venda`) REFERENCES `cliente` (`id_cliente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-04-22 21:29:23
