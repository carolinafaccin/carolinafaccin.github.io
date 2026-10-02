---
title: "Padrões de Transformação Urbana em Cidades Costeiras"
date: 2025-08-14T10:00:00+00:00
featured: true
categories:
  - "Clima e Ambiente"
  - "Forma Urbana e Uso do Solo"
draft: false
summary: "Quatro décadas de dados de cobertura do solo por satélite mostram como o crescimento impulsionado pelo turismo no Litoral Norte gaúcho ampliou a área urbanizada em 60% e avançou sobre dunas, banhados e restingas."
period: "2025–2026"
location: "Osório, Tramandaí e Imbé, Litoral Norte do RS"
partners: "Coautoria com Juliana Lombard de Souza e Guilherme Kruger Dalcin"
role: "Autora principal: desenho da pesquisa, processamento de dados em Python, análise espacial e mapas."
data: ["MapBiomas uso e cobertura da terra (1985–2023)", "Censos demográficos IBGE (1991–2022)", "Google Open Buildings"]
tools: ["Python (GeoPandas, Matplotlib)", "Análise de mudança de cobertura do solo", "Pipeline reproduzível"]
---

{{< lead >}}
Como a urbanização impulsionada pelo turismo está transformando o Litoral Norte do Rio Grande do Sul, e qual o efeito sobre ecossistemas costeiros sensíveis?
{{< /lead >}}

{{< facts >}}

## O desafio

O Litoral Norte é uma das regiões que mais crescem no estado. Turismo sazonal, segundas residências e migração permanente formaram uma faixa urbana quase contínua ao longo da costa. A pergunta não era só *quanto* as cidades cresceram, mas *sobre o quê*: dunas, restingas e banhados que protegem a costa e são difíceis de recuperar depois de ocupados.

## Abordagem

Processei 39 anos de mapas anuais de cobertura do solo para três municípios vizinhos, cada um com um papel diferente: Osório (polo regional), Tramandaí (principal centro turístico) e Imbé (crescimento sazonal). A mudança de cobertura foi combinada com a evolução populacional dos censos.

{{< flow title="Da série temporal de satélite à evidência para o planejamento" >}}
{{< step label="Série temporal" >}}
MapBiomas, cobertura anual do solo, 1985–2023
{{< /step >}}
{{< step label="Processamento" >}}
Pipeline em Python: reclassificação, recorte por município, área por classe e ano
{{< /step >}}
{{< step label="Análise de mudança" >}}
Mapas de 1985 e 2023, tendências por classe, crescimento populacional (IBGE)
{{< /step >}}
{{< step label="Achados" accent="true" >}}
Onde e como a urbanização avançou sobre ecossistemas sensíveis
{{< /step >}}
{{< /flow >}}

## Resultados

- A área urbanizada da aglomeração urbana do Litoral Norte cresceu **60%**, de 112 km² (1985) para 180 km² (2023).
- A população da região cresceu **25,8%** entre 2010 e 2022; a de Imbé se multiplicou por **3,6** entre 1991 e 2022.
- Três padrões distintos: **espraiamento disperso e fragmentado** em Osório (+79%); crescimento contínuo e **adensamento** em Tramandaí (+26%); crescimento **sazonal** e rápido em Imbé (+17%), avançando sobre dunas e restinga (a cobertura de praia e duna caiu 40% em Imbé e 30% em Tramandaí).
- Ao sobrepor a área urbana de 2023 à cobertura do solo de 1985, vê-se o que ela substituiu: **51% da nova área urbana da AULINOR era praia, duna, restinga ou banhado, chegando a 85% em Tramandaí e 76% em Imbé**.

## Por que importa

Os resultados são um alerta para o planejamento costeiro: a urbanização avança sobre áreas de alta sensibilidade ambiental, e a conurbação faz com que as escolhas de um município afetem os vizinhos. O artigo defende uma gestão territorial e ambiental integrada, com soluções regionalizadas.

Depois, reconstruí os cálculos em um pipeline aberto e reproduzível em Python, que confere seus resultados com os números publicados no artigo: [código e dados no GitHub](https://github.com/carolinafaccin/coastal).

[Leia o artigo](https://seer.ufrgs.br/index.php/paraonde/article/view/150243): Faccin, Souza & Dalcin (2026), *Padrões de transformação urbana e de uso e cobertura da terra no litoral norte: o caso de Osório, Tramandaí e Imbé*.

## Figuras

Produzidas pelo pipeline aberto acima (legendas internas em inglês).

{{< fig src="/img/projects/coastal/map_urban_expansion.webp" alt="Mapa de Osório, Tramandaí e Imbé: área urbana em 1985 em ferrugem escuro, concentrada no litoral e no centro de Osório, e nova área urbana até 2023 em laranja, espalhada ao redor de Osório e ao longo da costa" caption="Área urbana em 1985 e nova área urbana até 2023." >}}

{{< fig src="/img/projects/coastal/urban_timeline.webp" alt="Gráfico de linhas da área urbana de 1985 a 2023: Tramandaí de 18,0 a 22,7 km² (+26%), Imbé de 15,5 a 18,1 km² (+17%) e Osório de 9,7 a 17,3 km² (+79%)" caption="Área urbana, 1985–2023 (km²)." >}}

{{< fig src="/img/projects/coastal/urban_growth.webp" alt="Gráfico de halteres da área urbana em 1985 e 2023 nos municípios da AULINOR, de Capão da Canoa e Tramandaí no topo a Capivari do Sul na base, com o crescimento percentual de cada um" caption="Onde a área urbana cresceu nos 20 municípios da AULINOR." >}}

{{< fig src="/img/projects/coastal/land_replaced.webp" alt="Barras empilhadas com a cobertura do solo em 1985 da nova área urbana: praia, duna e banhado dominam em Imbé (76% sensíveis) e Tramandaí (85%), e pastagem e lavouras na AULINOR como um todo" caption="O que a nova área urbana substituiu (cobertura do solo em 1985)." >}}

{{< fig src="/img/projects/coastal/landcover_change.webp" alt="Três gráficos de área empilhada da cobertura do solo por grupo de 1985 a 2023 em Osório, Tramandaí e Imbé, com a classe urbana crescendo no topo enquanto praia e duna, restinga e banhado diminuem" caption="Cobertura do solo por grupo, 1985–2023." >}}

{{< fig src="/img/projects/coastal/map_landcover.webp" alt="Mapas de cobertura do solo de Osório, Tramandaí e Imbé em 1985 e 2023, com área urbana em laranja ao longo da costa, silvicultura em ferrugem avançando para o interior e uma faixa de praia e duna em amarelo no sul" caption="Cobertura do solo em 1985 e 2023." >}}
