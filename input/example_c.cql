IMPORT TABLE observations FROM "../data/observations.csv";
CREATE TABLE most_hot SELECT * FROM observations WHERE Temperature > 22;
SELECT * FROM most_hot;

IMPORT TABLE stations FROM "../data/stations.csv";
CREATE TABLE complet FROM stations JOIN observations USING(Id);
SELECT * FROM complet;