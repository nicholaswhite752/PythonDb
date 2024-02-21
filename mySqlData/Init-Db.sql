CREATE DATABASE testPythonDb;

USE testPythonDb;

-- As a note, can't name a column key or value without other complications
CREATE TABLE `TestData` (
  `id` varchar(45) NOT NULL,
  `keyCol` varchar(45) DEFAULT NULL,
  `valueCol` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

GRANT ALL PRIVILEGES ON testPythonDb.* TO 'testUser'@'%';

INSERT INTO TestData (id, keyCol, valueCol) VALUES ('some-uuid', 'some-key', 'some-value');