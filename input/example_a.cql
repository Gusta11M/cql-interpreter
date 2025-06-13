IMPORT TABLE test FROM "weather_stations.csv";
EXPORT TABLE test AS "weather_stations_Export.csv";

PRINT TABLE test;
RENAME TABLE test test1;

PRINT TABLE test1;
DISCARD TABLE test1;

PRINT TABLE est1;
