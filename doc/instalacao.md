# Criação de Banco de Dados para testes
docker run --name locacao-carros-banco-teste -p 5430:5432 -e POSTGRES_PASSWORD=senha_segura123 -e POSTGRES_DB=test_locacao -d postgres
