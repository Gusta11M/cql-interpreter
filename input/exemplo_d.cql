IMPORT TABLE observacoes FROM "observacoes.csv";
IMPORT TABLE estacoes FROM "estacoes.csv";

PROCEDURE atualizar_observacoes DO
    CREATE TABLE mais_quentes SELECT * FROM observacoes WHERE Temperatura > 22 ;
    CREATE TABLE completo FROM estacoes JOIN observacoes USING(Id);
    IMPORT TABLE alunos FROM "alunos.csv";
    CREATE TABLE alunoMais20 SELECT * FROM alunos WHERE Idade >= 20;
END

CALL atualizar_observacoes;

SELECT * FROM mais_quentes;
SELECT * FROM completo;
SELECT * FROM alunoMais20;