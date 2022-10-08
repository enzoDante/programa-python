create database univap;
use univap;

create table disciplinas(
codigodisc int not null primary key,
nomedisc varchar(50)
);
create table professores(
registro int not null primary key,
nomeprof varchar(50),
telefoneprof varchar(30),
idadeprof int,
salarioprof float
);
create table disciplinasxprofessores(
codigodisciplinanocurso varchar(10) not null primary key,
coddisciplina int,
foreign key (coddisciplina)references disciplinas (codigodisc),
codprofessor int,
foreign key (codprofessor)references professores (registro),
curso int,
cargahoraria int,
anoletivo int
);










