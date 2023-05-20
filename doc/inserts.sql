-- Funcionarios
insert into funcionarios (nome, email, senha, nivel_acesso) values ('admin', 'admin@gmail.com', 'pbkdf2:sha256:260000$2HVggHOygKkKpdQf$2c74bb4e990084f14750789b5d8f48895233763dd1d38b0269b92cde8f81f844',0);

-- Agencias
insert into agencias (localizacao, nome) values ('Avenida Monsenhor Tabosa, 1234 Meireles, Fortaleza - CE', 'Agência Fortaleza');
INSERT INTO agencias (localizacao, nome) VALUES ('Avenida Beira Mar, 3000, Meireles, Fortaleza, CE, Brasil', 'Agência Beira Mar');
INSERT INTO agencias (localizacao, nome) VALUES ('Avenida Santos Dumont, 1500, Aldeota, Fortaleza, CE, Brasil', 'Agência Santos Dumont');
INSERT INTO agencias (localizacao, nome) VALUES ('Avenida Washington Soares, 1000, Edson Queiroz, Fortaleza, CE, Brasil', 'Agência Washington Soares');
INSERT INTO agencias (localizacao, nome) VALUES ('Rua das Flores, 123, Centro, São Paulo, SP, Brasil', 'Agência Central');
INSERT INTO agencias (localizacao, nome) VALUES ('Avenida Paulista, 1000, Bela Vista, São Paulo, SP, Brasil', 'Agência Paulista');
INSERT INTO agencias (localizacao, nome) VALUES ('Rua dos Pinheiros, 500, Pinheiros, São Paulo, SP, Brasil', 'Agência Pinheiros');
INSERT INTO agencias (localizacao, nome) VALUES ('Avenida Brigadeiro Faria Lima, 2000, Itaim Bibi, São Paulo, SP, Brasil', 'Agência Faria Lima');
INSERT INTO agencias (localizacao, nome) VALUES ('Rua Augusta, 150, Consolação, São Paulo, SP, Brasil', 'Agência Augusta');

-- Veículos
INSERT INTO veiculos (agencia, modelo, marca, placa, descricao, diaria, ocupantes, porta_malas, freio_abs)
VALUES (1, 'Civic', 'Honda', 'ABC1234', 'Honda Civic 2022, sedan, motor 2.0, completo', 200, 5, 430, true);

INSERT INTO veiculos (agencia, modelo, marca, placa, descricao, diaria, ocupantes, porta_malas, freio_abs)
VALUES (1, 'Civic', 'Honda', 'ABD4224', 'Honda Civic 2022, sedan, motor 2.0, completo', 200, 5, 430, true);

INSERT INTO veiculos (agencia, modelo, marca, placa, descricao, diaria, ocupantes, porta_malas, freio_abs)
VALUES (1, 'Corolla', 'Toyota', 'DEF5678', 'Toyota Corolla 2021, sedan, motor 2.0, completo', 210, 5, 470, true);

INSERT INTO veiculos (agencia, modelo, marca, placa, descricao, diaria, ocupantes, porta_malas, freio_abs)
VALUES (1, 'Gol', 'Volkswagen', 'GHI9012', 'Volkswagen Gol 2021, hatch, motor 1.0, básico', 100, 5, 285, false);

INSERT INTO veiculos (agencia, modelo, marca, placa, descricao, diaria, ocupantes, porta_malas, freio_abs)
VALUES (1, 'Fiesta', 'Ford', 'JKL3456', 'Ford Fiesta 2020, hatch, motor 1.6, completo', 150, 5, 300, true);

INSERT INTO veiculos (agencia, modelo, marca, placa, descricao, diaria, ocupantes, porta_malas, freio_abs)
VALUES (7, 'Fiesta', 'Ford', 'MLK1893', 'Ford Fiesta 2020, hatch, motor 1.6, completo', 150, 5, 300, true);


update veiculos set imagem='images/civic.png' where modelo = 'Civic';
update veiculos set imagem='images/gol.png' where modelo = 'Gol';
update veiculos set imagem='images/corolla.png' where modelo = 'Corolla';
update veiculos set imagem='images/fiesta.png' where modelo = 'Fiesta';


/* Simula operação de devolução do veículo */
update recibo set status_devolucao = true where usuario = 3 and veiculo = 2;
update veiculos set disponibilidade = true where id = 2;


select * from veiculos where modelo='Gol';

-- Usuarios
insert into usuarios (nome, email, data_nascimento, senha) values ('Alisson Augusto', 'alisson@gmail.com','2001-05-19', 'pbkdf2:sha256:260000$clflSUftq5drUoTZ$d7df5300383d7c8920a6172bee024066f9e672757e107c6c58c0ecbba69e5c3c');

select * from funcionarios;

select * from agencias;

select * from usuarios;

select * from veiculos;

select * from recibo;

