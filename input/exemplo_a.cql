IMPORT TABLE teste FROM "estacoesmetereologicas.csv";
EXPORT TABLE teste AS "estacoesmetereologicasExport.csv";

PRINT TABLE teste;
RENAME TABLE teste teste1;

PRINT TABLE teste1;
DISCARD TABLE teste1;

PRINT TABLE est1;
