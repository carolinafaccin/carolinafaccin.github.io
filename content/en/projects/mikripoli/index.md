---
title: "Dynamics and Morphology of Small Cities"
date: 2024-12-15T09:00:00+00:00
categories:
  - "Regional Development"
  - "Urban Form & Land Use"
draft: false
aliases: ["/projects/small-cities-dynamics/"]
summary: "Typologies, half a century of urban network change and comparative morphology studies of the small cities that make up most of Rio Grande do Sul's urban network, yet are often overlooked."
period: "2021–2024"
location: "Vales Region, Rio Grande do Sul, Brazil (case studies: Sobradinho, Rio Pardo and Encantado)"
partners: "Mikripoli research network on small cities"
role: "Network member: statistical and spatial data analysis, typologies, comparative case studies, maps and co-authoring; also teaching and workshops."
data: ["IBGE REGIC (1966–2018)", "IBGE censuses (2010, 2022)", "DEE-RS", "RAIS and CAGED", "Landsat imagery", "Google Earth", "OpenStreetMap", "Municipal data", "Fieldwork"]
tools: ["QGIS", "Statistical analysis", "Typology building", "Morphological analysis"]
---

{{< lead >}}
What role do small cities play in the regional urban network, and what are their own sociospatial and morphological dynamics?
{{< /lead >}}

{{< facts >}}

## The challenge

Small cities are the majority of urban centers in Rio Grande do Sul, but urban research and planning tools are designed for large cities. Many small municipalities were created by successive emancipations and have little technical capacity. As part of the **Mikripoli** research network, I worked on describing them with data rather than assumptions.

## Approach

The work moved between three scales: the regional network over time, a typology of small cities, and the urban form of individual towns.

{{< flow title="Three scales of analysis" >}}
{{< step label="Network over time" >}}
Regions of influence of cities, 1966 to 2018 (IBGE REGIC)
{{< /step >}}
{{< step label="Typology" >}}
Small cities grouped by population, economy, services and centrality (IBGE, DEE-RS)
{{< /step >}}
{{< step label="Morphology" >}}
Census tracts, satellite imagery and fieldwork in three towns
{{< /step >}}
{{< step label="Synthesis" accent="true" >}}
Inputs for planning adapted to small cities
{{< /step >}}
{{< /flow >}}

## Results

- **Small cities form most of the regional network**, providing basic services locally, while Santa Cruz do Sul and Lajeado gained centrality through public management and specialized services, supported by tobacco and poultry/pork agro-industry.
- A **typology of small cities** based on how they take part in the regional division of labor.
- A comparative morphology of **Sobradinho** (compact), **Rio Pardo** (dispersed growth, agricultural economy) and **Encantado** (fragmented expansion, diversified economy), with a clear center–periphery inequality in all three.
- In 2024–2025, the same team analyzed the [impacts of the floods on small cities](../floods-rs-2024/).

## Why it matters

The work provides a baseline for planning in places that usually lack one, and brings small cities into debates on regional development and climate adaptation.

I later rebuilt the census maps of the three towns as an open, reproducible Python pipeline: [code and figures on GitHub](https://github.com/carolinafaccin/mikripoli).

**Publications:**

- [Detoni, Faccin, Silveira, Rorato & Machado (2025)](https://www.rbgdr.net/revista/index.php/rbgdr/article/view/8020) (EN): extreme climate events and their sociospatial impacts on small cities.
- [Silveira, Faccin & Detoni (2023)](https://online.unisc.br/seer/index.php/redes/article/view/18531) (EN): small cities and changes in the regional urban network.
- [Silveira, Faccin, Detoni & Silva (2024)](https://online.unisc.br/seer/index.php/redes/article/view/19899) (PT): comparative morphology of three small cities.
- [Silveira, Faccin, Detoni, Menezes & Haas (2022)](https://revistas.planejamento.rs.gov.br/index.php/boletim-geografico-rs/article/view/4488) (PT): a typology of small cities in the Vales Region.
- [Rorato, Detoni & Faccin (2022)](https://www.researchgate.net/publication/373975584_Cidades_pequenas_no_contexto_do_ensino_superior_relato_de_experiencia_da_disciplina_de_Sistemas_de_Informacoes_Geograficas_em_Urbanismo) (PT): teaching small cities in a GIS course at UFRGS.
- [Detoni, Faccin & Rorato (2023)](https://periodicos.ufpel.edu.br/index.php/pixo/article/view/26495) (PT): the "Architectures of a Small City" collage workshop.

## Figures

The census and neighborhood maps are produced by the open pipeline above.

{{< fig src="/img/projects/mikripoli/map_tracts.webp" alt="Grid of nine maps: census tracts of Sobradinho, Rio Pardo and Encantado colored by residents per tract, residents per dwelling and mean income of the household head in 2010, with the highest incomes in the town centers" caption="Population, household size and income by census tract (2010)." >}}

{{< fig src="/img/projects/mikripoli/map_neighborhoods.webp" alt="Three maps of the urban neighborhoods of Sobradinho, Rio Pardo and Encantado, shaded by number of residents and labeled by name, with main roads and rivers" caption="Neighborhoods of the three case-study towns." >}}
