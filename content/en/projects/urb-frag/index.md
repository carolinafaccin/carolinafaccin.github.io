---
title: "Sociospatial Fragmentation in Santa Cruz do Sul-RS, Brazil"
date: 2025-06-16T14:00:00+00:00
categories:
  - "Housing & Inequality"
  - "Urban Form & Land Use"
draft: false
aliases: ["/projects/sociospatial-fragmentation/"]
summary: "My PhD research: a composite index, built from environmental, social, housing and infrastructure indicators, that measures 50 years of sociospatial fragmentation in a medium-sized Brazilian city."
period: "2021–2025"
location: "Santa Cruz do Sul, Rio Grande do Sul, Brazil"
partners: "PROPUR/UFRGS (PhD in Urban and Regional Planning)"
role: "Independent doctoral research: research design, data collection and database, indicators and index, spatial analysis, interviews and writing."
data: ["IBGE censuses", "Municipal databases", "MapBiomas", "Google Open Buildings", "OpenStreetMap", "FEPAM/RS", "DAER", "Public policy documents", "Semi-structured interviews"]
tools: ["Python", "QGIS", "PostgreSQL/PostGIS", "Composite index", "Mixed methods"]
---

{{< lead >}}
How can sociospatial fragmentation be measured over five decades, and linked to the public policies and market dynamics that produced it?
{{< /lead >}}

{{< facts >}}

## The challenge

Segregation is usually studied in large metropolises. Medium-sized cities, which are growing fast in Brazil, often reproduce the same patterns with less scrutiny. Santa Cruz do Sul, a tobacco-industry hub of about 130,000 people, offered a chance to trace how a city became divided, from its agro-industrial boom to today.

## Approach

The research combined a historical reading of the city with a quantitative spatial model. I identified three phases of urban development, built a database of indicators and synthesized them into a single fragmentation index.

{{< flow title="Measuring fragmentation" >}}
{{< step label="Periodization" >}}
Documents and interviews define three phases: 1970–1993, 1993–2013, 2013–2022
{{< /step >}}
{{< step label="Indicators" >}}
Four families: environmental, social, housing and infrastructure
{{< /step >}}
{{< step label="Synthesis" >}}
Quantitative spatial synthesis into a fragmentation index (high, medium, low)
{{< /step >}}
{{< step label="Interpretation" accent="true" >}}
Barriers, gated communities and social housing read together with policies and market
{{< /step >}}
{{< /flow >}}

## Results

- Three phases of fragmentation: **agro-industrial rise and migration** (1970–1993), **economic diversification and segregation** (1993–2013), and **consolidation of fragmentation** (2013–2022).
- Physical and symbolic **barriers** (highways, industrial zones, natural features) that deepen inequality and limit urban integration.
- A sharp **north–south divide**: the north concentrates gated communities and high-quality infrastructure for high-income residents; the south concentrates low-income housing developments with precarious public services.
- The index splits the 144 urban census tracts into **70 of low, 54 of medium and 20 of high fragmentation**: the center is the most integrated; the gated communities of the north and the social housing of the south and west are the most fragmented.
- The city urbanized fast and extensively: from 12.5 km² in 1985 to 35 km² in 2022 (MapBiomas), with 22 gated communities and 37 social housing subdivisions approved by the City, most of them between 1993 and 2013.
- Segregation persisted for five decades, **reinforced by public policies and real estate dynamics**, reproducing in a medium-sized city the exclusion typical of metropolises.

## Why it matters

The index and the database offer a diagnosis that can be updated and reused to inform zoning, housing policy and infrastructure investment, and the method can be transferred to other medium-sized cities.

- [Thesis (PT)](https://lume.ufrgs.br/handle/10183/294929)
- [Open dataset on Zenodo](https://doi.org/10.5281/zenodo.16423545)
- [Faccin (2025)](https://editorarealize.com.br/artigo/visualizar/122487) (PT): paper presented at XXI ENANPUR.

I later rebuilt the index and the figures as an open, reproducible Python pipeline from the thesis dataset, checked against the numbers in the thesis: [code and figures on GitHub](https://github.com/carolinafaccin/urb-frag).

## Figures

Produced by the open pipeline above.

{{< fig src="/img/projects/urb-frag/map_index.webp" alt="Map of Santa Cruz do Sul's census tracts shaded by fragmentation index: low in the center, high in the north around the gated communities and in the west and south around the social housing subdivisions, with highways, industrial zone and Green Belt" caption="Sociospatial fragmentation index, with gated communities, social housing subdivisions and urban barriers." >}}

{{< fig src="/img/projects/urb-frag/index_profile.webp" alt="Histogram of the fragmentation index across 144 census tracts with thresholds at 50 and 55, and bars of the mean environmental, social, housing and infrastructure scores by class" caption="How the index is built: distribution and dimensions by class." >}}

{{< fig src="/img/projects/urb-frag/map_indicators.webp" alt="Six small maps of census tracts: high-income households and gated communities in the north; low-income households, special social-interest zones and social housing in the south and west; landslide-prone areas around the Green Belt" caption="Six of the 23 variables of the index." >}}

{{< fig src="/img/projects/urb-frag/map_expansion.webp" alt="Map of the urbanized area of Santa Cruz do Sul by period: a compact core urbanized by 1985 and growth toward the north, east and south up to 2022" caption="Urbanized area by period, 1985–2022." >}}

{{< fig src="/img/projects/urb-frag/growth_and_developments.webp" alt="Bar chart of urbanized area from 12.5 km² in 1985 to 35 km² in 2022, and step lines of the cumulative area of gated communities and social housing subdivisions, rising mostly between 1993 and 2013" caption="Urban growth and the two housing products that drove it." >}}

{{< fig src="/img/projects/urb-frag/map_location.webp" alt="Two location maps: Santa Cruz do Sul highlighted in Rio Grande do Sul, and the urbanized area in the south of the municipality" caption="Location of Santa Cruz do Sul." >}}
