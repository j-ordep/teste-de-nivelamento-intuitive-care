CREATE TABLE operadoras (
    cnpj VARCHAR(20) PRIMARY KEY,
    nome_fantasia VARCHAR(255),
    tipo_plano VARCHAR(100),
    status_operadora VARCHAR(50),
    data_cadastro DATE
);

CREATE TABLE demonstrativos_financeiros (
    id SERIAL PRIMARY KEY,
    cnpj_operadora VARCHAR(20) REFERENCES operadoras(cnpj),
    data_referencia DATE,
    categoria VARCHAR(255),
    despesa NUMERIC(15,2)
);

COPY operadoras(cnpj, nome_operadora, status_operadora, data_cadastro)
FROM 'c:/teste-de-nivelamento/teste3-data-base-sql/dados-das-operadoras/Relatorio_cadop.csv' -- caso necessário, ajuste o caminho do arquivo CSV
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';

COPY demonstrativos_financeiros(cnpj_operadora, data_referencia, categoria, despesa)
FROM 'c:/teste-de-nivelamento/teste3-data-base-sql/repositorio/1T2023.csv' -- caso necessário, ajuste o caminho do arquivo CSV
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';

SELECT o.nome_operadora, SUM(df.despesa) AS total_despesa
FROM demonstrativos_financeiros df
JOIN operadoras o ON df.cnpj_operadora = o.cnpj
WHERE df.categoria = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
  AND df.data_referencia >= (CURRENT_DATE - INTERVAL '3 months')
GROUP BY o.nome_operadora
ORDER BY total_despesa DESC
LIMIT 10;

SELECT o.nome_operadora, SUM(df.despesa) AS total_despesa
FROM demonstrativos_financeiros df
JOIN operadoras o ON df.cnpj_operadora = o.cnpj
WHERE df.categoria = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
  AND df.data_referencia >= (CURRENT_DATE - INTERVAL '1 year')
GROUP BY o.nome_operadora
ORDER BY total_despesa DESC
LIMIT 10;
