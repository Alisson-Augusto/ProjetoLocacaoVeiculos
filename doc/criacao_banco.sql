create database locacao;

create table if not exists funcionarios (
	id SERIAL primary key,
	nome VARCHAR(128) not null,
	email VARCHAR(128) not null unique,
	senha VARCHAR(120) not null,
	nivel_acesso INT not null,
	agencia INT,
	
	constraint FK_AGENCIA foreign key(agencia) references agencias(id)
);

create table if not exists agencias (
	id SERIAL primary key,
	localizacao VARCHAR(500) not null,
	nome VARCHAR(144) not null
);

create table if not exists usuarios (
	id SERIAL primary key,
	nome VARCHAR(128) not null,
	email VARCHAR(128) not null unique,
	senha VARCHAR(120) not null,
	data_nascimento DATE not null
);

create table if not exists veiculos (
	id SERIAL primary key,
	agencia SERIAL,
	disponibilidade Boolean default true,
	modelo VARCHAR(50) not null,
	marca VARCHAR(50) not null,
	placa VARCHAR(8) not null unique,
	imagem VARCHAR(50),
	descricao VARCHAR(128),
	diaria INT not null,
	ocupantes INT,
	porta_malas INT,
	freio_abs BOOL,
	
	constraint FK_AGENCIA foreign key(agencia) references agencias(id)
);


create table if not exists recibo  (
	id SERIAL primary key,
	usuario SERIAL,
	veiculo SERIAL,
	data_retirada DATE not null,
	data_devolucao DATE not null,
	status_devolucao BOOLEAN default False,
	
	constraint FK_USUARIO foreign key(usuario) references usuarios(id),
	constraint FK_VEICULO foreign key(veiculo) references veiculos(id)
);
