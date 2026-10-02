---
title: "Dinâmicas e Morfologia de Cidades Pequenas"
date: 2024-12-15T09:00:00+00:00
categories:
  - "Desenvolvimento Regional"
  - "Forma Urbana e Uso do Solo"
draft: false
aliases: ["/projects/small-cities-dynamics/"]
summary: "Tipologias, meio século de mudanças na rede urbana e estudos comparativos de morfologia das cidades pequenas, que formam a maior parte da rede urbana gaúcha, mas costumam ficar de fora dos estudos urbanos."
period: "2021–2024"
location: "Região dos Vales, RS (estudos de caso: Sobradinho, Rio Pardo e Encantado)"
partners: "Rede de pesquisa Mikripoli sobre cidades pequenas"
role: "Integrante da rede: análise estatística e espacial, tipologias, estudos de caso comparativos, mapas e coautoria; também ensino e oficinas."
data: ["IBGE REGIC (1966–2018)", "Censos IBGE (2010, 2022)", "DEE-RS", "RAIS e CAGED", "Imagens Landsat", "Google Earth", "OpenStreetMap", "Dados municipais", "Trabalho de campo"]
tools: ["QGIS", "Análise estatística", "Construção de tipologias", "Análise morfológica"]
---

{{< lead >}}
Qual o papel das cidades pequenas na rede urbana regional, e quais são suas dinâmicas socioespaciais e morfológicas próprias?
{{< /lead >}}

{{< facts >}}

## O desafio

As cidades pequenas são a maioria dos centros urbanos do Rio Grande do Sul, mas a pesquisa e os instrumentos de planejamento urbano são pensados para cidades grandes. Muitos pequenos municípios surgiram de sucessivas emancipações e têm pouca capacidade técnica. Como parte da rede de pesquisa **Mikripoli**, trabalhei para descrevê-las com dados, e não com suposições.

## Abordagem

O trabalho transitou por três escalas: a rede regional ao longo do tempo, uma tipologia de cidades pequenas e a forma urbana de cidades específicas.

{{< flow title="Três escalas de análise" >}}
{{< step label="Rede no tempo" >}}
Regiões de influência das cidades, de 1966 a 2018 (IBGE REGIC)
{{< /step >}}
{{< step label="Tipologia" >}}
Cidades pequenas agrupadas por população, economia, serviços e centralidade (IBGE, DEE-RS)
{{< /step >}}
{{< step label="Morfologia" >}}
Setores censitários, imagens de satélite e campo em três cidades
{{< /step >}}
{{< step label="Síntese" accent="true" >}}
Subsídios para um planejamento adaptado às cidades pequenas
{{< /step >}}
{{< /flow >}}

## Resultados

- **As cidades pequenas formam a maior parte da rede regional**, oferecendo serviços básicos localmente, enquanto Santa Cruz do Sul e Lajeado ganharam centralidade pela gestão pública e por serviços especializados, sustentados pela agroindústria do tabaco e de aves e suínos.
- Uma **tipologia de cidades pequenas** baseada em como participam da divisão regional do trabalho.
- Uma morfologia comparada de **Sobradinho** (compacta), **Rio Pardo** (crescimento disperso, economia agrícola) e **Encantado** (expansão fragmentada, economia diversificada), com clara desigualdade centro–periferia nas três.
- Em 2024–2025, a mesma equipe analisou os [impactos das enchentes nas cidades pequenas](../floods-rs-2024/).

## Por que importa

O trabalho oferece uma linha de base para o planejamento em lugares que costumam não ter uma, e traz as cidades pequenas para os debates sobre desenvolvimento regional e adaptação climática.

Depois, reconstruí os mapas censitários das três cidades em um pipeline aberto e reproduzível em Python: [código e figuras no GitHub](https://github.com/carolinafaccin/mikripoli).

**Publicações:**

- [Detoni, Faccin, Silveira, Rorato & Machado (2025)](https://www.rbgdr.net/revista/index.php/rbgdr/article/view/8020): eventos climáticos extremos e seus impactos socioespaciais em cidades pequenas.
- [Silveira, Faccin & Detoni (2023)](https://online.unisc.br/seer/index.php/redes/article/view/18531): cidades pequenas e mudanças na rede urbana regional.
- [Silveira, Faccin, Detoni & Silva (2024)](https://online.unisc.br/seer/index.php/redes/article/view/19899): morfologia comparada de três cidades pequenas.
- [Silveira, Faccin, Detoni, Menezes & Haas (2022)](https://revistas.planejamento.rs.gov.br/index.php/boletim-geografico-rs/article/view/4488): uma tipologia de cidades pequenas na Região dos Vales.
- [Rorato, Detoni & Faccin (2022)](https://www.researchgate.net/publication/373975584_Cidades_pequenas_no_contexto_do_ensino_superior_relato_de_experiencia_da_disciplina_de_Sistemas_de_Informacoes_Geograficas_em_Urbanismo): cidades pequenas na disciplina de SIG em Urbanismo da UFRGS.
- [Detoni, Faccin & Rorato (2023)](https://periodicos.ufpel.edu.br/index.php/pixo/article/view/26495): a oficina de colagem "Arquiteturas de uma Cidade Pequena".

## Figuras

Os mapas censitários e de bairros são produzidos pelo pipeline aberto acima (legendas internas em inglês).

{{< fig src="/img/projects/mikripoli/map_tracts.webp" alt="Grade de nove mapas: setores censitários de Sobradinho, Rio Pardo e Encantado coloridos por moradores por setor, moradores por domicílio e renda média do responsável em 2010, com as rendas mais altas nos centros" caption="População, moradores por domicílio e renda por setor censitário (2010)." >}}

{{< fig src="/img/projects/mikripoli/map_neighborhoods.webp" alt="Três mapas dos bairros urbanos de Sobradinho, Rio Pardo e Encantado, coloridos pelo número de moradores e identificados pelo nome, com as vias principais e os rios" caption="Bairros das três cidades estudadas." >}}

A rede urbana regional ao longo do tempo (IBGE REGIC):

{{< figs cols="2" >}}
{{< fig src="/img/projects/mikripoli/small-cities_03.webp" alt="Mapa da rede urbana da Região dos Vales em 1966, com poucos níveis hierárquicos e linhas de influência apontando para Porto Alegre" caption="Rede urbana em 1966." >}}
{{< fig src="/img/projects/mikripoli/small-cities_04.webp" alt="Mapa da rede urbana da Região dos Vales em 1978, com centros sub-regionais e linhas de influência" caption="1978." >}}
{{< fig src="/img/projects/mikripoli/small-cities_05.webp" alt="Mapa da rede urbana da Região dos Vales em 1993, com níveis de centralidade de muito fraco a máximo" caption="1993." >}}
{{< fig src="/img/projects/mikripoli/small-cities_06.webp" alt="Mapa da rede urbana da Região dos Vales em 2007, com capitais regionais, centros sub-regionais e muito mais centros locais e ligações" caption="2007." >}}
{{< /figs >}}
