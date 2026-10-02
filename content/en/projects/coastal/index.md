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
tools: ["Python (GeoPandas, Matplotlib)", "Land-cover change analysis", "Reproducible pipeline"]
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
- Three distinct patterns: **dispersed, fragmented sprawl** in Osório (+79%); continuous growth and **densification** in Tramandaí (+26%); fast, **seasonal growth** in Imbé (+17%), encroaching on dunes and coastal vegetation (beach and dune cover fell by 40% in Imbé and 30% in Tramandaí).
- Overlaying the 2023 urban area on the 1985 land cover shows what it replaced: **51% of the new urban land in AULINOR was beach, dune, restinga or wetland, rising to 85% in Tramandaí and 76% in Imbé**.

## Why it matters

The results are a warning for coastal planning: urbanization is advancing over areas of high environmental sensitivity, and conurbation means one municipality's choices affect its neighbors. The paper argues for integrated territorial and environmental management with regional solutions.

I later rebuilt the calculations as an open, reproducible Python pipeline that checks its results against the numbers published in the paper: [code and data on GitHub](https://github.com/carolinafaccin/coastal).

[Read the paper (PT)](https://seer.ufrgs.br/index.php/paraonde/article/view/150243): Faccin, Souza & Dalcin (2026), *Patterns of urban transformation and land use and land cover on the North Coast: Osório, Tramandaí and Imbé*.

## Figures

Produced by the open pipeline above.

{{< fig src="/img/projects/coastal/map_urban_expansion.webp" alt="Map of Osório, Tramandaí and Imbé: urban area in 1985 in dark rust, concentrated along the shoreline and in Osório's center, and new urban area by 2023 in orange, spreading around Osório and along the coast" caption="Urban area in 1985 and new urban area by 2023." >}}

{{< fig src="/img/projects/coastal/urban_timeline.webp" alt="Line chart of urban area from 1985 to 2023: Tramandaí from 18.0 to 22.7 km² (+26%), Imbé from 15.5 to 18.1 km² (+17%) and Osório from 9.7 to 17.3 km² (+79%)" caption="Urban area, 1985–2023 (km²)." >}}

{{< fig src="/img/projects/coastal/urban_growth.webp" alt="Dumbbell chart of urban area in 1985 and 2023 for the AULINOR municipalities, from Capão da Canoa and Tramandaí at the top to Capivari do Sul at the bottom, with the percentage growth of each" caption="Where the urban area grew across the 20 AULINOR municipalities." >}}

{{< fig src="/img/projects/coastal/land_replaced.webp" alt="Stacked bars with the 1985 land cover of the new urban area: beach, dune and wetland classes dominate in Imbé (76% sensitive) and Tramandaí (85%), and pasture and crops in AULINOR overall" caption="What the new urban land replaced (1985 land cover)." >}}

{{< fig src="/img/projects/coastal/landcover_change.webp" alt="Three stacked area charts of land cover by group from 1985 to 2023 for Osório, Tramandaí and Imbé, with the urban class growing at the top while beach and dune, restinga and wetland shrink" caption="Land cover by group, 1985–2023." >}}

{{< fig src="/img/projects/coastal/map_landcover.webp" alt="Land-cover maps of Osório, Tramandaí and Imbé in 1985 and 2023, with urban area in orange along the coast, forestry plantations in dark rust spreading inland and a beach and dune strip in yellow in the south" caption="Land cover in 1985 and 2023." >}}
