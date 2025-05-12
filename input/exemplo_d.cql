IMPORT TABLE observacoes FROM "observacoes.csv";
IMPORT TABLE estacoes FROM "estacoes.csv";

PROCEDURE atualizar_observacoes DO
    CREATE TABLE mais_quentes SELECT * FROM observacoes WHERE Temperatura > 22 ;
    CREATE TABLE completo FROM estacoes JOIN observacoes USING(Id);
<<<<<<< HEAD
    IMPORT TABLE alunos FROM "alunos.csv";
    CREATE TABLE alunoMais20 FROM alunos WHERE Idade >= 20;
=======
    IMPORT TABLE alunos FROM "data/alunos.csv";
    CREATE TABLE alunoMais20 SELECT * FROM alunos WHERE Idade >= 20;
>>>>>>> 924ef183f85415ce88e1f2485b2c82b09416bd09
END

CALL atualizar_observacoes;

SELECT * FROM mais_quentes;
SELECT * FROM completo;
SELECT * FROM alunoMais20;