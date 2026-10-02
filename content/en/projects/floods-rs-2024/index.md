---
title: "2024 Floods of Small Cities in RS, Brazil"
date: 2024-09-23T11:00:00+00:00
featured: 3
categories:
  - "Climate & Environment"
draft: false
aliases: ["/projects/floods-in-small-cities/"]
summary: "A rapid geospatial diagnosis, built by a volunteer research task force, of which buildings the May 2024 floods reached in small cities of the Rio Pardo and Taquari valleys, delivered to regional decision-makers."
period: "2024"
location: "Rio Pardo Valley and Taquari Valley, Rio Grande do Sul, Brazil"
partners: "Volunteer task force of researchers; report delivered to public managers through COREDE Vale do Rio Pardo"
role: "Co-author of the technical report and the paper; responsible for the geospatial analysis that identified the urban areas and buildings reached by the flood."
data: ["IPH/UFRGS flood extent (6 May 2024)", "Google Open Buildings", "IBGE census tracts (2010)", "DAER-RS highways"]
tools: ["QGIS", "Python", "Spatial overlay analysis", "Documentary analysis of planning instruments"]
---

{{< lead >}}
In the weeks after the 2024 floods, how could researchers provide small municipalities with a fast, reliable picture of what was hit?
{{< /lead >}}

{{< facts >}}

## The challenge

In May 2024, Rio Grande do Sul faced the worst climate disaster in its history. Small cities in the Rio Pardo and Taquari valleys, many with limited technical staff, had to make emergency decisions without an overview of which neighborhoods and buildings had been reached by the water.

## Approach

A volunteer task force of researchers came together to produce a technical report in a few weeks. I led the geospatial analysis, crossing the observed flood extent with building footprints, and the team reviewed the municipalities' existing planning instruments.

{{< flow title="Rapid flood-impact diagnosis" >}}
{{< step label="Flood extent" >}}
Observed flood area of 6 May 2024 (IPH/UFRGS)
{{< /step >}}
{{< step label="Exposure" >}}
Building footprints (Google Open Buildings) and 2010 census tracts (urban or rural)
{{< /step >}}
{{< step label="Overlay" >}}
Buildings inside the flood extent, mapped city by city
{{< /step >}}
{{< step label="Report" accent="true" >}}
Diagnosis and recommendations for public managers
{{< /step >}}
{{< /flow >}}

## Results

- **43,600 buildings** were reached by the floods in the two valleys: 26,633 in the Taquari valley and 16,967 in the Rio Pardo valley, 8.7% of all buildings and 11.6% of those in urban census tracts.
- **Small towns were hit hardest**: the flood reached about half the urban buildings of Marques de Souza (54%) and Muçum (51%), and more than 40% in Roca Sales, Cruzeiro do Sul and Estrela.
- City-scale maps for urban areas in both valleys (including Santa Cruz do Sul, Rio Pardo, Candelária, Lajeado, Estrela, Encantado, Muçum and Roca Sales) showing where flooded buildings concentrate.
- The analysis exposed fragile infrastructure (blocked roads, damaged bridges) and planning instruments that did not account for flood risk.

## Impact

The technical report was delivered directly to public managers through COREDE Vale do Rio Pardo, supporting emergency decision-making and the discussion on climate adaptation. The work was later published as a peer-reviewed article, which stresses that small cities need institutional support from state and federal governments and multi-scale policy coordination.

[Read the paper (EN/PT)](https://www.rbgdr.net/revista/index.php/rbgdr/article/view/8020): Detoni, Faccin, Silveira, Rorato & Machado (2025), *Extreme weather events and their socio-spatial impacts on small cities in Rio Grande do Sul, Brazil*.

I later rebuilt the analysis as an open, reproducible Python pipeline that reproduces the counts published in the paper: [code and figures on GitHub](https://github.com/carolinafaccin/floods-rs-2024).

## Figures

Produced by the open pipeline above.

{{< fig src="/img/projects/floods-rs-2024/map_region.webp" alt="Map of the Rio Pardo and Taquari valleys with the flood extent of 6 May 2024 along the rivers, flooded buildings in orange and boxes marking the seven town maps" caption="The flood in the two valleys, with the extent of the town maps." >}}

{{< fig src="/img/projects/floods-rs-2024/flooded_by_municipality.webp" alt="Two bar charts of flooded buildings per municipality, split into urban and rural census tracts: Estrela leads the Taquari valley with 6,495 and Venâncio Aires the Rio Pardo valley with 7,502" caption="Flooded buildings by municipality, urban and rural." >}}

{{< fig src="/img/projects/floods-rs-2024/share_flooded.webp" alt="Dot chart of the share of buildings flooded in urban and rural census tracts per municipality, with Marques de Souza, Muçum, Roca Sales, Cruzeiro do Sul and Estrela above 40% urban" caption="Share of buildings flooded, urban and rural census tracts." >}}

{{< fig src="/img/projects/floods-rs-2024/map_lajeado_estrela.webp" alt="Map of Lajeado, Estrela, Arroio do Meio and Cruzeiro do Sul with a wide flood area along the Taquari River and flooded buildings in orange in the riverside cores" caption="Lajeado, Estrela, Arroio do Meio and Cruzeiro do Sul." >}}

{{< fig src="/img/projects/floods-rs-2024/map_encantado_mucum.webp" alt="Map of Encantado, Roca Sales and Muçum with the flood following the Taquari River and flooded buildings concentrated in the riverside cores of the three towns" caption="Encantado, Roca Sales and Muçum." >}}

{{< fig src="/img/projects/floods-rs-2024/map_santa_cruz.webp" alt="Map of Santa Cruz do Sul and Vera Cruz with the flood along the Pardinho River west of the city and flooded buildings on its western edge" caption="Santa Cruz do Sul and Vera Cruz." >}}

{{< fig src="/img/projects/floods-rs-2024/map_rio_pardo.webp" alt="Map of Rio Pardo surrounded by the flood of the Jacuí and Pardo rivers, with flooded buildings in the southwest of the town" caption="Rio Pardo." >}}

{{< fig src="/img/projects/floods-rs-2024/map_candelaria.webp" alt="Map of Candelária with the flood along the Pardo River east of the town and flooded buildings along the river" caption="Candelária." >}}

{{< fig src="/img/projects/floods-rs-2024/map_marques_de_souza.webp" alt="Map of Marques de Souza and Travesseiro with the flood along the Forqueta River and flooded buildings in both towns" caption="Marques de Souza and Travesseiro." >}}

{{< fig src="/img/projects/floods-rs-2024/map_sinimbu.webp" alt="Map of Sinimbu with a narrow flood area along the Pardinho River and flooded buildings along the main street in the town center" caption="Sinimbu." >}}
