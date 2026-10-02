---
title: "Urban Transformation Patterns in Coastal Cities"
date: 2025-08-14T10:00:00+00:00
featured: true
categories:
  - "Climate & Environment"
  - "Urban Form & Land Use"
draft: false
summary: "Four decades of satellite-based land-cover data show how tourism-driven growth on Rio Grande do Sul's North Coast expanded the urbanized area by 60% and advanced over dunes, wetlands and coastal vegetation."
period: "2025–2026"
location: "Osório, Tramandaí and Imbé, North Coast of Rio Grande do Sul, Brazil"
partners: "Co-authors Juliana Lombard de Souza and Guilherme Kruger Dalcin"
role: "Lead author: research design, data processing in Python, spatial analysis and maps."
data: ["MapBiomas land use and land cover (1985–2023)", "IBGE demographic censuses (1991–2022)", "Google Open Buildings"]
tools: ["Python (Jupyter)", "QGIS", "Land-cover change analysis"]
---

{{< lead >}}
How is tourism-driven urbanization reshaping the North Coast of Rio Grande do Sul, and what is it doing to sensitive coastal ecosystems?
{{< /lead >}}

{{< facts >}}

## The challenge

The North Coast is one of the fastest-growing parts of the state. Seasonal tourism, second homes and permanent migration have pushed cities into a near-continuous strip along the shoreline. The question was not just *how much* the cities grew, but *over what*: dunes, beach vegetation (restinga) and wetlands that protect the coast and are hard to recover once built over.

## Approach

I processed 39 years of annual land-cover maps for three neighboring municipalities, each with a different role: Osório (regional hub), Tramandaí (main tourist center) and Imbé (seasonal growth). Land-cover change was combined with census population trends.

{{< flow title="From satellite time series to planning evidence" >}}
{{< step label="Time series" >}}
MapBiomas annual land cover, 1985–2023
{{< /step >}}
{{< step label="Processing" >}}
Python pipeline: reclassify, clip by municipality, compute area per class and year
{{< /step >}}
{{< step label="Change analysis" >}}
1985 vs. 2023 maps, class-by-class trends, population growth (IBGE)
{{< /step >}}
{{< step label="Findings" accent="true" >}}
Where and how urban growth advanced over sensitive ecosystems
{{< /step >}}
{{< /flow >}}

## Results

- The coastal urban agglomeration's urbanized area grew by **60%**, from 112 km² (1985) to 180 km² (2023).
- The region's population grew **25.8%** between 2010 and 2022; Imbé's population multiplied **3.6 times** between 1991 and 2022.
- Three distinct patterns: **dispersed, fragmented sprawl** in Osório; continuous growth and **densification** in Tramandaí (+26% urbanized area); fast, **seasonal growth** in Imbé (+17%), encroaching on dunes and coastal vegetation (beach and dune cover fell by about 40%).

## Why it matters

The results are a warning for coastal planning: urbanization is advancing over areas of high environmental sensitivity, and conurbation means one municipality's choices affect its neighbors. The paper argues for integrated territorial and environmental management with regional solutions.

[Read the paper (PT)](https://seer.ufrgs.br/index.php/paraonde/article/view/150243): Faccin, Souza & Dalcin (2026), *Patterns of urban transformation and land use and land cover on the North Coast: Osório, Tramandaí and Imbé*.

## Maps

{{< fig src="/img/projects/coastal/coastal_03.webp" alt="Land-cover maps of Osório, Tramandaí and Imbé in 1985 and 2023 next to stacked area charts per municipality, showing urban area growing while beach, dune and grassland classes shrink" caption="Land use and land cover in 1985 and 2023, with change by class for each municipality (MapBiomas)." >}}

{{< figs cols="2" >}}
{{< fig src="/img/projects/coastal/coastal_02.webp" alt="Map of the three municipalities showing urbanized area in 1985 in red and in 2023 in light orange, with labels of +2.6 km² (+17.1%) for Imbé and +4.7 km² (+26.2%) for Tramandaí" caption="Urbanized area in 1985 and 2023." >}}
{{< fig src="/img/projects/coastal/coastal_01.webp" alt="Two maps of Rio Grande do Sul: annual population growth by regional council, highest on the coast, and the coastal urban hierarchy with links to Porto Alegre" caption="Regional context: population growth by region and the coastal urban hierarchy." >}}
{{< /figs >}}
