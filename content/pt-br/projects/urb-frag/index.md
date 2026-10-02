---
title: "Fragmentação Urbana em uma Cidade Média"
date: 2025-06-16T14:00:00+00:00
categories:
  - "Habitação e Desigualdade"
  - "Forma Urbana e Uso do Solo"
draft: false
aliases: ["/projects/sociospatial-fragmentation/"]
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
- O índice divide os 144 setores censitários urbanos em **70 de baixa, 54 de média e 20 de alta fragmentação**: o centro é o mais integrado; os condomínios fechados do norte e os loteamentos populares do sul e do oeste, os mais fragmentados.
- A cidade se urbanizou de forma rápida e extensiva: de 12,5 km² em 1985 para 35 km² em 2022 (MapBiomas), com 22 condomínios fechados e 37 loteamentos populares aprovados pela Prefeitura, a maioria entre 1993 e 2013.
- A segregação persistiu por cinco décadas, **reforçada por políticas públicas e pela dinâmica imobiliária**, reproduzindo em uma cidade média exclusões típicas das metrópoles.

## Por que importa

O índice e o banco de dados oferecem um diagnóstico que pode ser atualizado e reutilizado para orientar zoneamento, política habitacional e investimentos em infraestrutura, e o método pode ser aplicado a outras cidades médias.

- [Tese](https://lume.ufrgs.br/handle/10183/294929)
- [Base de dados aberta no Zenodo](https://doi.org/10.5281/zenodo.16423545)
- [Faccin (2025)](https://editorarealize.com.br/artigo/visualizar/122487): artigo apresentado no XXI ENANPUR.

Depois, reconstruí o índice e as figuras em um pipeline aberto e reproduzível em Python a partir da base da tese, conferido com os números da tese: [código e figuras no GitHub](https://github.com/carolinafaccin/urb-frag).

## Figuras

Produzidas pelo pipeline aberto acima (legendas internas em inglês).

{{< fig src="/img/projects/urb-frag/map_index.webp" alt="Mapa dos setores censitários de Santa Cruz do Sul coloridos pelo índice de fragmentação: baixo no centro, alto no norte em torno dos condomínios fechados e no oeste e no sul em torno dos loteamentos populares, com rodovias, zona industrial e Cinturão Verde" caption="Índice de fragmentação socioespacial, com condomínios fechados, loteamentos populares e barreiras urbanas." >}}

{{< fig src="/img/projects/urb-frag/index_profile.webp" alt="Histograma do índice de fragmentação nos 144 setores censitários com limiares em 50 e 55, e barras das pontuações médias ambiental, social, habitacional e de infraestrutura por classe" caption="Como o índice é construído: distribuição e dimensões por classe." >}}

{{< fig src="/img/projects/urb-frag/map_indicators.webp" alt="Seis pequenos mapas de setores censitários: domicílios de alta renda e condomínios fechados ao norte; baixa renda, ZEIS e loteamentos populares ao sul e a oeste; áreas de deslizamento em torno do Cinturão Verde" caption="Seis das 23 variáveis do índice." >}}

{{< fig src="/img/projects/urb-frag/map_expansion.webp" alt="Mapa da área urbanizada de Santa Cruz do Sul por período: um núcleo compacto urbanizado até 1985 e crescimento para o norte, leste e sul até 2022" caption="Área urbanizada por período, 1985–2022." >}}

{{< fig src="/img/projects/urb-frag/growth_and_developments.webp" alt="Gráfico de barras da área urbanizada, de 12,5 km² em 1985 para 35 km² em 2022, e linhas em degrau da área acumulada de condomínios fechados e loteamentos populares, que crescem sobretudo entre 1993 e 2013" caption="Crescimento urbano e os dois produtos habitacionais que o impulsionaram." >}}

{{< fig src="/img/projects/urb-frag/map_location.webp" alt="Dois mapas de localização: Santa Cruz do Sul destacada no Rio Grande do Sul, e a área urbanizada no sul do município" caption="Localização de Santa Cruz do Sul." >}}
