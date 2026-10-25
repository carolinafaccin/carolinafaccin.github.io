---
title: "Dados"
description: "Bases de dados geoespaciais abertas de Carolina Faccin sobre população, suscetibilidade a desastres, condomínios fechados e fragmentação urbana no Brasil."
showTableOfContents: false
---

Bases de dados que construí ou das quais sou coautora, publicadas com DOI e licença aberta para que possam ser citadas e reutilizadas. Cada uma vem com a documentação das fontes e dos métodos, e a maioria com o código que a produziu.

## Brasil

### BrazilPop: grades de população e de endereços

Grades raster (GeoTIFF) de todo o Brasil com estimativas de população e contagens de endereços dos censos de 2010 e 2022, a partir do Cadastro Nacional de Endereços para Fins Estatísticos (CNEFE/IBGE). A população é distribuída pelos endereços por desagregação dasimétrica dos totais dos setores censitários. As camadas formam três grupos: população, tipo de endereço e subtipo de domicílio.

{{< dataset authors="Possantti, I.; **Faccin, C. R.** (2026)" coverage="Brasil" years="2010, 2022" format="GeoTIFF; grades de 30 m, 100 m e 1 km" license="CC BY 4.0" doi="10.5281/zenodo.22918300" code="https://github.com/iporepos/build-brazilpop" >}}

### Cartas de suscetibilidade do SGB: base nacional harmonizada

As cartas municipais de suscetibilidade a movimentos gravitacionais de massa e inundação publicadas pelo Serviço Geológico do Brasil (SGB/CPRM), reunidas numa base única e harmonizada: 839 municípios de 27 UFs e 2,57 milhões de polígonos, com o código IBGE do município em todo polígono, classes normalizadas e geometria original. Cartas de suscetibilidade indicam a propensão do terreno a cada processo; não são mapas de risco.

{{< dataset authors="**Faccin, C. R.** (2026)" coverage="Brasil (839 municípios, 27 UFs)" years="Cartas publicadas até outubro de 2026" format="GeoParquet, um arquivo por grupo de processos e UF; SIRGAS 2000" license="CC BY 4.0" access="Dados com acesso restrito no Zenodo por enquanto. O código (coleta do catálogo, download, harmonização e conferência) é aberto." doi="10.5281/zenodo.23417168" code="https://github.com/carolinafaccin/cartas-suscetibilidade-sgb" >}}

## Rio Grande do Sul

### Condomínios fechados de Porto Alegre

A delimitação e os atributos dos 1.024 condomínios residenciais fechados mapeados em Porto Alegre em 2022, identificados em imagens de satélite, delimitados com a camada de cercas e muros da Prefeitura e confirmados no Street View, com dicionário de dados e as camadas de bairros e de áreas de preservação permanente usadas na análise.

{{< dataset authors="**Faccin, C. R.** (2025)" coverage="Porto Alegre, RS" years="2022" format="GeoPackage, CSV" license="CC BY 4.0" doi="10.5281/zenodo.17023731" code="https://github.com/carolinafaccin/housing-poa" project="/projects/housing-poa" paper="[Faccin, Almeida & Campos (2024)](https://doi.org/10.11606/issn.2317-2762.posfauusp.2024.226515)" >}}

### Fragmentação urbana em Santa Cruz do Sul

A base de dados da minha tese de doutorado: camadas do IBGE, da Prefeitura, do MapBiomas, do OpenStreetMap e do Google Open Buildings para a cidade de Santa Cruz do Sul, usadas na construção do índice de fragmentação socioespacial, junto com o texto da tese e seus anexos.

{{< dataset authors="**Faccin, C. R.** (2025)" coverage="Santa Cruz do Sul, RS" years="1970–2022" format="GeoPackage, PDF" license="CC BY 4.0" doi="10.5281/zenodo.16423545" code="https://github.com/carolinafaccin/urb-frag" project="/projects/urb-frag" paper="[Tese](https://lume.ufrgs.br/handle/10183/294929)" >}}
