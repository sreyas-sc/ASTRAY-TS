/*
SQLyog Community v13.1.7 (64 bit)
MySQL - 8.0.22 : Database - text_summarization
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`text_summarization` /*!40100 DEFAULT CHARACTER SET latin1 */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `text_summarization`;

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `feedback` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`user_id`,`feedback`,`date`) values 
(1,1,'Dolor fugiat est o','2021-05-27 11:37:30'),
(2,1,'Dolor fugiat est o','2021-05-27 11:37:54'),
(3,1,'Dolor fugiat est o','2021-05-27 11:38:16'),
(4,1,'Dolor fugiat est o','2021-05-27 11:38:54');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int NOT NULL AUTO_INCREMENT,
  `Username` varchar(30) DEFAULT NULL,
  `Password` varchar(30) DEFAULT NULL,
  `user_type` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`Username`,`Password`,`user_type`) values 
(1,'admin','admin','admin'),
(2,'user','user','user');

/*Table structure for table `news_categories` */

DROP TABLE IF EXISTS `news_categories`;

CREATE TABLE `news_categories` (
  `category_id` int NOT NULL AUTO_INCREMENT,
  `category_name` varchar(100) DEFAULT NULL,
  `category_description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `news_categories` */

insert  into `news_categories`(`category_id`,`category_name`,`category_description`) values 
(2,'category 1','category description'),
(3,'category','description');

/*Table structure for table `news_content` */

DROP TABLE IF EXISTS `news_content`;

CREATE TABLE `news_content` (
  `news_id` int NOT NULL AUTO_INCREMENT,
  `category_id` int DEFAULT NULL,
  `Title` varchar(30) DEFAULT NULL,
  `Date` varchar(20) DEFAULT NULL,
  `Description` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`news_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `news_content` */

insert  into `news_content`(`news_id`,`category_id`,`Title`,`Date`,`Description`) values 
(2,2,'title1','2021-02-12','description_1');

/*Table structure for table `news_providers` */

DROP TABLE IF EXISTS `news_providers`;

CREATE TABLE `news_providers` (
  `provider_id` int NOT NULL AUTO_INCREMENT,
  `provider_name` varchar(100) DEFAULT NULL,
  `provider_contact` varchar(100) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`provider_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `news_providers` */

insert  into `news_providers`(`provider_id`,`provider_name`,`provider_contact`,`description`) values 
(3,'provider23','9876321562','desc');

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `login_id` int DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `Phone` varchar(20) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `Place` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `users` */

insert  into `users`(`user_id`,`login_id`,`first_name`,`last_name`,`Phone`,`Email`,`Place`) values 
(1,2,'user','name','1234567890','user@gmail.com','userhome'),
(2,3,'1','','','',''),
(3,4,'5','','','',''),
(4,5,'m','','','',''),
(5,6,'kk','','1111111111','','');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
