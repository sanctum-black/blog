CREATE TABLE WRITERS (
  FirstName varchar(255),
  LastName varchar(255),
  Birth varchar(255),
  Death varchar(255)
);

INSERT INTO WRITERS (FirstName, LastName, Birth, Death)
VALUES ('Charles', 'Dickens', 1812, 1870),
	('Mark', 'Twain', 1835, 1910),
    ('Fyodor', 'Dostoevsky', 1821, 1881),
    ('Leo', 'Tolstoy', 1828, 1910),
    ('Joris-Karl', 'Huysmans', 1848, 1907),
    ('Dante', 'Alighieri', 1265, 1321);

SELECT *, Death-Birth
AS Lived
FROM WRITERS
ORDER BY Lived DESC