IMPORT TABLE observacoes FROM "data/observacoes.csv";
CREATE TABLE mais_quentes SELECT * FROM observacoes WHERE Temperatura > 22;
SELECT * FROM mais_quentes;

IMPORT TABLE estacoes FROM "data/estacoes.csv";
CREATE TABLE completo FROM estacoes JOIN observacoes USING(Id);
SELECT * FROM completo;

IMPORT TABLE alunos FROM "data/alunos.csv";
SELECT * FROM alunos;