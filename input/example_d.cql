IMPORT TABLE observations FROM "observations.csv";
IMPORT TABLE stations FROM "stations.csv";

PROCEDURE update_observations DO
    CREATE TABLE most_hot SELECT * FROM observations WHERE Temperature > 22 ;
    CREATE TABLE complet FROM stations JOIN observations USING(Id);
END

CALL update_observations;

SELECT * FROM most_hot;
SELECT * FROM complet;