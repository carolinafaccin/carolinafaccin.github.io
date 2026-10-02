---
title: "Fragmentação Socioespacial e Repercussões na Paisagem"
date: 2025-06-16T14:00:00+00:00
categories:
  - "Habitação e Desigualdade"
  - "Forma Urbana e Uso do Solo"
draft: false
summary: "Minha pesquisa de doutorado: um índice composto, construído a partir de indicadores ambientais, sociais, habitacionais e de infraestrutura, que mede 50 anos de fragmentação socioespacial em uma cidade média brasileira."
period: "2021–2025"
location: "Santa Cruz do Sul, RS"
partners: "PROPUR/UFRGS (Doutorado em Planejamento Urbano e Regional)"
role: "Pesquisa de doutorado independente: desenho da pesquisa, coleta de dados e banco de dados, indicadores e índice, análise espacial, entrevistas e redação."
data: ["Censos IBGE", "Bases da prefeitura", "MapBiomas", "Google Open Buildings", "OpenStreetMap", "FEPAM/RS", "DAER", "Documentos de políticas públicas", "Entrevistas semiestruturadas"]
tools: ["Python", "QGIS", "PostgreSQL/PostGIS", "Índice composto", "Métodos mistos"]
---

{{< lead >}}
Como medir a fragmentação socioespacial ao longo de cinco décadas e relacioná-la às políticas públicas e às dinâmicas de mercado que a produziram?
{{< /lead >}}

{{< facts >}}

## O desafio

A segregação costuma ser estudada nas grandes metrópoles. As cidades médias, que crescem rapidamente no Brasil, muitas vezes reproduzem os mesmos padrões com menos atenção. Santa Cruz do Sul, polo da indústria do tabaco com cerca de 130 mil habitantes, permitia acompanhar como uma cidade se dividiu, do boom agroindustrial até hoje.

## Abordagem

A pesquisa combinou uma leitura histórica da cidade com um modelo espacial quantitativo. Identifiquei três fases do desenvolvimento urbano, construí um banco de indicadores e os sintetizei em um único índice de fragmentação.

{{< flow title="Medindo a fragmentação" >}}
{{< step label="Periodização" >}}
Documentos e entrevistas definem três fases: 1970–1993, 1993–2013, 2013–2022
{{< /step >}}
{{< step label="Indicadores" >}}
Quatro grupos: ambientais, sociais, habitacionais e de infraestrutura
{{< /step >}}
{{< step label="Síntese" >}}
Síntese espacial quantitativa em um índice de fragmentação (alto, médio, baixo)
{{< /step >}}
{{< step label="Interpretação" accent="true" >}}
Barreiras, condomínios e habitação de interesse social lidos junto com políticas e mercado
{{< /step >}}
{{< /flow >}}

## Resultados

- Três fases da fragmentação: **ascensão agroindustrial e migração** (1970–1993), **diversificação econômica e segregação** (1993–2013) e **consolidação da fragmentação** (2013–2022).
- **Barreiras** físicas e simbólicas (rodovias, zonas industriais, elementos naturais) que acentuam desigualdades e limitam a integração urbana.
- Uma forte **divisão norte–sul**: o norte concentra condomínios fechados e infraestrutura de qualidade para a população de alta renda; o sul concentra loteamentos populares com serviços públicos precários.
- A segregação persistiu por cinco décadas, **reforçada por políticas públicas e pela dinâmica imobiliária**, reproduzindo em uma cidade média exclusões típicas das metrópoles.

## Por que importa

O índice e o banco de dados oferecem um diagnóstico que pode ser atualizado e reutilizado para orientar zoneamento, política habitacional e investimentos em infraestrutura, e o método pode ser aplicado a outras cidades médias.

- [Tese](https://lume.ufrgs.br/handle/10183/294929)
- [Base de dados aberta no Zenodo](https://doi.org/10.5281/zenodo.16423545)
- [Faccin (2025)](https://editorarealize.com.br/artigo/visualizar/122487): artigo apresentado no XXI ENANPUR.

## Mapas

{{< fig src="/img/projects/sociospatial-fragmentation/sociospatial_03.webp" alt="Mapa da área urbana de Santa Cruz do Sul colorido pelo índice de fragmentação de baixo a alto, com triângulos marcando loteamentos populares ao sul, círculos marcando condomínios fechados ao norte, rodovias, zona industrial e barreiras naturais" caption="Índice de fragmentação socioespacial, com loteamentos populares, condomínios fechados e barreiras urbanas." >}}

{{< figs cols="2" >}}
{{< fig src="/img/projects/sociospatial-fragmentation/sociospatial_02.webp" alt="Dois mapas do distrito sede de Santa Cruz do Sul com a área urbanizada em 1993, 2013 e 2022, com crescimento nas bordas" caption="Expansão urbana, 1993–2013 e 2013–2022." >}}
{{< fig src="/img/projects/sociospatial-fragmentation/sociospatial_01.webp" alt="Mapas de localização situando o Rio Grande do Sul na América do Sul, Santa Cruz do Sul no estado e a área urbana no município" caption="Localização de Santa Cruz do Sul." >}}
{{< /figs >}}
