SELECT
	*
FROM
	information_schema.schemata ;

CREATE SCHEMA IF NOT EXISTS marts;

CREATE TABLE IF NOT EXISTS marts.prenumeration AS 
(
SELECT * FROM prenumerationsstatus.tabelldata )
;

SELECT * FROM marts.prenumeration;
