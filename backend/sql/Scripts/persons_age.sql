

SELECT
	*
FROM
	information_schema.schemata ;

CREATE SCHEMA IF NOT EXISTS marts;

CREATE TABLE IF NOT EXISTS marts.viewer_age AS 
(
SELECT * FROM tittare.tabelldata_kon tk )
;


SELECT * from marts.viewer_age ;