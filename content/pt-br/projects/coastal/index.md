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
tools: ["Python (Jupyter)", "QGIS", "Análise de mudança de cobertura do solo"]
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
- Três padrões distintos: **espraiamento disperso e fragmentado** em Osório; crescimento contínuo e **adensamento** em Tramandaí (+26% de área urbanizada); crescimento **sazonal** e rápido em Imbé (+17%), avançando sobre dunas e restinga (a cobertura de praia e duna caiu cerca de 40%).

## Por que importa

Os resultados são um alerta para o planejamento costeiro: a urbanização avança sobre áreas de alta sensibilidade ambiental, e a conurbação faz com que as escolhas de um município afetem os vizinhos. O artigo defende uma gestão territorial e ambiental integrada, com soluções regionalizadas.

[Leia o artigo](https://seer.ufrgs.br/index.php/paraonde/article/view/150243): Faccin, Souza & Dalcin (2026), *Padrões de transformação urbana e de uso e cobertura da terra no litoral norte: o caso de Osório, Tramandaí e Imbé*.

## Mapas

{{< fig src="/img/projects/coastal/coastal_03.webp" alt="Mapas de cobertura do solo de Osório, Tramandaí e Imbé em 1985 e 2023 ao lado de gráficos de área por município, mostrando o crescimento da área urbana e a redução de praias, dunas e campos" caption="Uso e cobertura da terra em 1985 e 2023, com a variação de cada classe por município (MapBiomas)." >}}

{{< figs cols="2" >}}
{{< fig src="/img/projects/coastal/coastal_02.webp" alt="Mapa dos três municípios com a área urbanizada em 1985 em vermelho e em 2023 em laranja claro, com rótulos de +2,6 km² (+17,1%) para Imbé e +4,7 km² (+26,2%) para Tramandaí" caption="Área urbanizada em 1985 e 2023." >}}
{{< fig src="/img/projects/coastal/coastal_01.webp" alt="Dois mapas do Rio Grande do Sul: crescimento populacional anual por COREDE, maior no litoral, e a hierarquia urbana do litoral com ligações a Porto Alegre" caption="Contexto regional: crescimento populacional e hierarquia urbana do litoral." >}}
{{< /figs >}}
