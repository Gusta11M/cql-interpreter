IMPORT TABLE stations FROM "stations.csv";
IMPORT TABLE observations FROM "observations.csv";

SELECT * FROM observations;

SELECT ObservationDateTime,Id FROM observations;

SELECT * FROM observations WHERE Temperature > 22;

SELECT Id From observations WHERE Temperature >= 16.4 AND Humidity < 50;

SELECT Id From observations WHERE Temperature >= 16.4 AND Humidity < 50 LIMIT 1;