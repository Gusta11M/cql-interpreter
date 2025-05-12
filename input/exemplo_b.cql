IMPORT TABLE estacoes FROM "estacoes.csv";
IMPORT TABLE observacoes FROM "observacoes.csv";

SELECT * FROM observacoes;

SELECT DataHoraObservacao,Id FROM observacoes;

SELECT * FROM observacoes WHERE Temperatura > 22;

SELECT Id From observacoes WHERE Temperatura >= 16.4 AND Humidade < 50;

SELECT Id From observacoes WHERE Temperatura >= 16.4 AND Humidade < 50 LIMIT 1;