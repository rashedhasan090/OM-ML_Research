USE OM_name_0





CREATE TABLE `class01_name` (
`c01_at1` c01_at1_type NOT NULL,
`c1_at1` c1_at1_type,
KEY `FK_class01_name_c1_at1_idx` (`c1_at1`),
PRIMARY KEY (`c01_at1`),
);








CREATE TABLE `class6_name` (
`c7_at1` c7_at1_type(64)
`c6_at1` c6_at1_type NOT NULL
PRIMARY KEY (`c6_at1`),
);








CREATE TABLE `class1_name` (
`c1_at1` c1_at1_type NOT NULL
PRIMARY KEY (`c1_at1`),
);








CREATE TABLE `assoc3` (
`c3_at1` c3_at1_type NOT NULL
`c2_at1` c2_at1_type NOT NULL
KEY `FK_assoc3_c3_at1_idx` (`c3_at1`)
KEY `FK_assoc3_c2_at1_idx` (`c2_at1`)
PRIMARY KEY (`c3_at1`,`c2_at1`)
);








CREATE TABLE `class13_name` (
`c13_at1` c13_at1_type(64)
`c12_at1` c12_at1_type NOT NULL
KEY `FK_class13_name_c12_at1_idx` (`c12_at1`)
PRIMARY KEY (`c12_at1`),
);








CREATE TABLE `class7_name` (
`c7_at3` c7_at3_type(64)
`c7_at2` c7_at2_type
`c7_at4` c7_at4_type(20,5)
`c7_at1` c7_at1_type NOT NULL
PRIMARY KEY (`c7_at1`),
);








CREATE TABLE `class11_name` (
`c11_at1` c11_at1_type(64)
`c7_at3` c7_at3_type(64)
`c7_at2` c7_at2_type
`c7_at4` c7_at4_type(20,5)
`c7_at1` c7_at1_type NOT NULL
PRIMARY KEY (`c7_at1`),
);








CREATE TABLE `class4_name` (
`c4_at1` c4_at1_type,
`c3_at1` c3_at1_type NOT NULL
KEY `FK_class4_name_c3_at1_idx` (`c3_at1`),
PRIMARY KEY (`c3_at1`),
);








CREATE TABLE `class2_name` (
`c2_at1` c2_at1_type NOT NULL
PRIMARY KEY (`c2_at1`),
);








CREATE TABLE `class8_name` (
`c8_at1` c8_at1_type NOT NULL
PRIMARY KEY (`c8_at1`),
);








CREATE TABLE `assoc7` (
`c7_at1` c7_at1_type NOT NULL
`c3_at1` c3_at1_type NOT NULL
KEY `FK_assoc7_c7_at1_idx` (`c7_at1`)
KEY `FK_assoc7_c3_at1_idx` (`c3_at1`)
PRIMARY KEY (`c7_at1`,`c3_at1`),
);








CREATE TABLE `class3_name` (
`c3_at2` c3_at2_type
`c3_at1` c3_at1_type NOT NULL
`c01_at1` c01_at1_type
KEY `FK_class3_name_c01_at1_idx` (`c01_at1`)
PRIMARY KEY (`c3_at1`),
);








CREATE TABLE `class10_name` (
`c10_at1` c10_at1_type(64)
`c7_at3` c7_at3_type(64)
`c7_at2` c7_at2_type
`c7_at4` c7_at4_type(20,5)
`c7_at1` c7_at1_type NOT NULL
PRIMARY KEY (`c7_at1`),
);








CREATE TABLE `class9_name` (
`c10_at2` c10_at2_type,
`c9_at1` c9_at1_type(20,5),
`c7_at1` c7_at1_type NOT NULL
KEY `FK_class9_name_c7_at1_idx` (`c7_at1`),
PRIMARY KEY (`c7_at1`),
);








CREATE TABLE `CustomerShippingCartAssociation` (

`c2_at1` c2_at1_type NOT NULL
`c1_at1` c1_at1_type NOT NULL
KEY `FK_CustomerShippingCartAssociation_shippingCartID_idx` (`shippingCartID`),

KEY `FK_CustomerShippingCartAssociation_customerID_idx` (`customerID`),

PRIMARY KEY (`shippingCartID`,`customerID`)

);








CREATE TABLE `assoc8` (
`c12_at1` c12_at1_type NOT NULL
`c7_at1` c7_at1_type NOT NULL
KEY `FK_assoc8_c12_at1_idx` (`c12_at1`)
KEY `FK_assoc8_c7_at1_idx` (`c7_at1`)
PRIMARY KEY (`c12_at1`,`c7_at1`),
);








CREATE TABLE `class14_name` (
`c14_at1` c14_at1_type(64)
`c12_at1` c12_at1_type NOT NULL
KEY `FK_class14_name_c12_at1_idx` (`c12_at1`)
PRIMARY KEY (`c12_at1`),
);








CREATE TABLE `class5_name` (
`c5_at1` c5_at1_type,
`c5_at2` c5_at2_type,
`c3_at1` c3_at1_type NOT NULL
KEY `FK_class5_name_c3_at1_idx` (`c3_at1`)
PRIMARY KEY (`c3_at1`),
);








CREATE TABLE `class12_name` (
`c12_at3` c12_at3_type(64)
`c12_at2` c12_at2_type(64)
`c12_at1` c12_at1_type NOT NULL
PRIMARY KEY (`c12_at1`),
);








CREATE TABLE `assoc6` (
`c8_at1` c8_at1_type NOT NULL
`c7_at1` c7_at1_type NOT NULL
KEY `FK_assoc6_c8_at1_idx` (`c8_at1`)
KEY `FK_assoc6_c7_at1_idx` (`c7_at1`),
PRIMARY KEY (`c8_at1`,`c7_at1`)
);








CREATE TABLE `assoc5` (
`c7_at1` c7_at1_type NOT NULL
`c6_at1` c6_at1_type NOT NULL
KEY `FK_assoc5_c7_at1_idx` (`c7_at1`)
KEY `FK_assoc5_c6_at1_idx` (`c6_at1`)
PRIMARY KEY (`c7_at1`,`c6_at1`),
);



ALTER TABLE `class01_name`
ADD CONSTRAINT `FK_class01_name_c1_at1` FOREIGN KEY (`c1_at1`) REFERENCES `class1_name` (`c1_at1`) ON DELETE CASCADE ON UPDATE CASCADE;


ALTER TABLE `assoc3`
ADD CONSTRAINT `FK_assoc3_c3_at1` FOREIGN KEY (`c3_at1`) REFERENCES `class3_name` (`c3_at1`) ON DELETE CASCADE ON UPDATE CASCADE
ADD CONSTRAINT `FK_assoc3_c2_at1` FOREIGN KEY (`c2_at1`) REFERENCES `class2_name` (`c2_at1`) ON DELETE CASCADE ON UPDATE CASCADE,


ALTER TABLE `class13_name`
ADD CONSTRAINT `FK_class13_name_c12_at1` FOREIGN KEY (`c12_at1`) REFERENCES `class12_name` (`c12_at1`) ON DELETE CASCADE ON UPDATE CASCADE;


ALTER TABLE `class4_name`
ADD CONSTRAINT `FK_class4_name_c3_at1` FOREIGN KEY (`c3_at1`) REFERENCES `class3_name` (`c3_at1`) ON DELETE CASCADE ON UPDATE CASCADE,


ALTER TABLE `assoc7`
ADD CONSTRAINT `FK_assoc7_c7_at1` FOREIGN KEY (`c7_at1`) REFERENCES `class7_name` (`c7_at1`) ON DELETE CASCADE ON UPDATE CASCADE
ADD CONSTRAINT `FK_assoc7_c3_at1` FOREIGN KEY (`c3_at1`) REFERENCES `class3_name` (`c3_at1`) ON DELETE CASCADE ON UPDATE CASCADE,


ALTER TABLE `class3_name`
ADD CONSTRAINT `FK_class3_name_c01_at1` FOREIGN KEY (`c01_at1`) REFERENCES `class01_name` (`c01_at1`) ON DELETE CASCADE ON UPDATE CASCADE,


ALTER TABLE `class9_name`
ADD CONSTRAINT `FK_class10_name_c7_at1` FOREIGN KEY (`c7_at1`) REFERENCES `class7_name` (`c7_at1`) ON DELETE CASCADE ON UPDATE CASCADE,


ALTER TABLE `CustomerShippingCartAssociation`

  ADD CONSTRAINT `FK_CustomerShippingCartAssociation_shippingCartID` FOREIGN KEY (`shippingCartID`) REFERENCES `ShippingCart` (`shippingCartID`) ON DELETE CASCADE ON UPDATE CASCADE,

  ADD CONSTRAINT `FK_CustomerShippingCartAssociation_customerID` FOREIGN KEY (`customerID`) REFERENCES `Customer` (`customerID`) ON DELETE CASCADE ON UPDATE CASCADE;



ALTER TABLE `assoc8`
ADD CONSTRAINT FK_assoc5_c6_at1` FOREIGN KEY (`c6_at1`) REFERENCES `class6_name` (`c6_at1`) ON DELETE CASCADE ON UPDATE CASCADE,
ADD CONSTRAINT FK_assoc8_c7_at1` FOREIGN KEY (`c7_at1`) REFERENCES `class7_name` (`c7_at1`) ON DELETE CASCADE ON UPDATE CASCADE,


ALTER TABLE `class14_name`
ADD CONSTRAINT FK_class14_name_c12_at1` FOREIGN KEY (`c12_at1`) REFERENCES `class12_name` (`c12_at1`) ON DELETE CASCADE ON UPDATE CASCADE,


ALTER TABLE `class5_name`
ADD CONSTRAINT FK_class5_name_c3_at1` FOREIGN KEY (`c3_at1`) REFERENCES `class3_name` (`c3_at1`) ON DELETE CASCADE ON UPDATE CASCADE,


ALTER TABLE `assoc6`
ADD CONSTRAINT `FK_assoc6_c8_at1` FOREIGN KEY (`c8_at1`) REFERENCES `class8_name` (`c8_at1`) ON DELETE CASCADE ON UPDATE CASCADE
ADD CONSTRAINT `FK_assoc7_c7_at1` FOREIGN KEY (`c7_at1`) REFERENCES `class7_name` (`c7_at1`) ON DELETE CASCADE ON UPDATE CASCADE;


ALTER TABLE `assoc5`
ADD CONSTRAINT `FK_assoc5_c7_at1` FOREIGN KEY (`c7_at1`) REFERENCES `class7_name` (`c7_at1`) ON DELETE CASCADE ON UPDATE CASCADE
ADD CONSTRAINT FK_assoc5_c6_at1` FOREIGN KEY (`c6_at1`) REFERENCES `class6_name` (`c6_at1`) ON DELETE CASCADE ON UPDATE CASCADE,