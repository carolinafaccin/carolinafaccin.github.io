---
title: "Enchentes de 2024 em Pequenas Cidades do RS"
date: 2024-09-23T11:00:00+00:00
categories:
  - "Clima e Ambiente"
draft: false
aliases: ["/projects/floods-in-small-cities/"]
summary: "Um diagnóstico geoespacial rápido, feito por uma força-tarefa voluntária de pesquisadores, sobre quais edificações as enchentes de maio de 2024 atingiram nas pequenas cidades dos vales do Rio Pardo e do Taquari, entregue a gestores regionais."
period: "2024"
location: "Vale do Rio Pardo e Vale do Taquari, RS"
partners: "Força-tarefa voluntária de pesquisadores; relatório entregue a gestores públicos via COREDE Vale do Rio Pardo"
role: "Coautora do relatório técnico e do artigo; responsável pela análise geoespacial que identificou as áreas urbanas e edificações atingidas pela inundação."
data: ["Mancha de inundação IPH/UFRGS (6 maio 2024)", "Google Open Buildings", "Setores censitários IBGE (2010)", "Rodovias DAER-RS"]
tools: ["QGIS", "Python", "Análise de sobreposição espacial", "Análise documental de instrumentos de planejamento"]
---

{{< lead >}}
Nas semanas seguintes às enchentes de 2024, como pesquisadores poderiam oferecer aos pequenos municípios um retrato rápido e confiável do que foi atingido?
{{< /lead >}}

{{< facts >}}

## O desafio

Em maio de 2024, o Rio Grande do Sul enfrentou o pior desastre climático de sua história. Pequenas cidades dos vales do Rio Pardo e do Taquari, muitas com equipes técnicas reduzidas, precisavam tomar decisões emergenciais sem uma visão geral de quais bairros e edificações tinham sido alcançados pela água.

## Abordagem

Uma força-tarefa voluntária de pesquisadores se reuniu para produzir um relatório técnico em poucas semanas. Eu conduzi a análise geoespacial, cruzando a mancha de inundação observada com as edificações, e a equipe revisou os instrumentos de planejamento existentes nos municípios.

{{< flow title="Diagnóstico rápido do impacto das enchentes" >}}
{{< step label="Mancha de inundação" >}}
Área inundada observada em 6 de maio de 2024 (IPH/UFRGS)
{{< /step >}}
{{< step label="Exposição" >}}
Edificações (Google Open Buildings) e setores censitários de 2010 (urbanos ou rurais)
{{< /step >}}
{{< step label="Sobreposição" >}}
Edificações dentro da mancha, mapeadas cidade a cidade
{{< /step >}}
{{< step label="Relatório" accent="true" >}}
Diagnóstico e recomendações para gestores públicos
{{< /step >}}
{{< /flow >}}

## Resultados

- **43.600 edificações** foram atingidas nos dois vales: 26.633 no Vale do Taquari e 16.967 no Vale do Rio Pardo, 8,7% de todas as edificações e 11,6% das que estão em setores urbanos.
- **As cidades pequenas foram as mais atingidas**: a inundação alcançou cerca de metade das edificações urbanas de Marques de Souza (54%) e Muçum (51%), e mais de 40% em Roca Sales, Cruzeiro do Sul e Estrela.
- Mapas em escala urbana para os dois vales (incluindo Santa Cruz do Sul, Rio Pardo, Candelária, Lajeado, Estrela, Encantado, Muçum e Roca Sales), mostrando onde se concentram as edificações inundadas.
- A análise evidenciou a fragilidade da infraestrutura (estradas bloqueadas, pontes danificadas) e instrumentos de planejamento que não consideravam o risco de inundação.

## Impacto

O relatório técnico foi entregue diretamente a gestores públicos por meio do COREDE Vale do Rio Pardo, apoiando decisões emergenciais e o debate sobre adaptação climática. O trabalho foi depois publicado como artigo revisado por pares, que destaca a necessidade de apoio institucional dos governos estadual e federal às pequenas cidades e de coordenação de políticas entre escalas.

[Leia o artigo (PT/EN)](https://www.rbgdr.net/revista/index.php/rbgdr/article/view/8020): Detoni, Faccin, Silveira, Rorato & Machado (2025), *Eventos climáticos extremos e seus impactos socioespaciais em cidades pequenas do Rio Grande do Sul*.

Depois, reconstruí a análise em um pipeline aberto e reproduzível em Python, que reproduz as contagens publicadas no artigo: [código e figuras no GitHub](https://github.com/carolinafaccin/floods-rs-2024).

## Figuras

Produzidas pelo pipeline aberto acima (legendas internas em inglês).

{{< fig src="/img/projects/floods-rs-2024/map_region.webp" alt="Mapa dos vales do Rio Pardo e do Taquari com a mancha de inundação de 6 de maio de 2024 ao longo dos rios, edificações inundadas em laranja e retângulos marcando os sete mapas de cidades" caption="A inundação nos dois vales, com a área dos mapas de cidades." >}}

{{< fig src="/img/projects/floods-rs-2024/flooded_by_municipality.webp" alt="Dois gráficos de barras com as edificações inundadas por município, divididas em setores urbanos e rurais: Estrela lidera o Vale do Taquari com 6.495 e Venâncio Aires o Vale do Rio Pardo com 7.502" caption="Edificações inundadas por município, urbanas e rurais." >}}

{{< fig src="/img/projects/floods-rs-2024/share_flooded.webp" alt="Gráfico de pontos com a proporção de edificações inundadas em setores urbanos e rurais por município, com Marques de Souza, Muçum, Roca Sales, Cruzeiro do Sul e Estrela acima de 40% no urbano" caption="Proporção de edificações inundadas, setores urbanos e rurais." >}}

{{< fig src="/img/projects/floods-rs-2024/map_lajeado_estrela.webp" alt="Mapa de Lajeado, Estrela, Arroio do Meio e Cruzeiro do Sul com ampla mancha de inundação ao longo do Rio Taquari e edificações inundadas em laranja nos centros ribeirinhos" caption="Lajeado, Estrela, Arroio do Meio e Cruzeiro do Sul." >}}

{{< fig src="/img/projects/floods-rs-2024/map_encantado_mucum.webp" alt="Mapa de Encantado, Roca Sales e Muçum com a mancha de inundação acompanhando o Rio Taquari e edificações inundadas concentradas nos centros ribeirinhos das três cidades" caption="Encantado, Roca Sales e Muçum." >}}

{{< fig src="/img/projects/floods-rs-2024/map_santa_cruz.webp" alt="Mapa de Santa Cruz do Sul e Vera Cruz com a mancha de inundação ao longo do Rio Pardinho a oeste da cidade e edificações inundadas na borda oeste" caption="Santa Cruz do Sul e Vera Cruz." >}}

{{< fig src="/img/projects/floods-rs-2024/map_rio_pardo.webp" alt="Mapa de Rio Pardo cercado pela mancha de inundação dos rios Jacuí e Pardo, com edificações inundadas no sudoeste da cidade" caption="Rio Pardo." >}}

{{< fig src="/img/projects/floods-rs-2024/map_candelaria.webp" alt="Mapa de Candelária com a mancha de inundação ao longo do Rio Pardo, a leste da cidade, e edificações inundadas junto ao rio" caption="Candelária." >}}

{{< fig src="/img/projects/floods-rs-2024/map_marques_de_souza.webp" alt="Mapa de Marques de Souza e Travesseiro com a mancha de inundação ao longo do Rio Forqueta e edificações inundadas nas duas cidades" caption="Marques de Souza e Travesseiro." >}}

{{< fig src="/img/projects/floods-rs-2024/map_sinimbu.webp" alt="Mapa de Sinimbu com uma estreita mancha de inundação ao longo do Rio Pardinho e edificações inundadas ao longo da rua principal, no centro" caption="Sinimbu." >}}
