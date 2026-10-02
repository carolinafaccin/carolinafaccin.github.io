---
title: "Urban Suitability Index Post-Disasters"
date: 2025-07-08T09:00:00+00:00
featured: 1
categories:
  - "Climate & Environment"
draft: false
summary: "After the 2023–2024 floods, where can seven devastated towns in the Taquari Valley safely rebuild? A multicriteria suitability model that turned risk maps into priority-occupation guidelines for the State Government."
period: "2024–2025"
location: "Taquari Valley, Rio Grande do Sul, Brazil: Arroio do Meio, Colinas, Cruzeiro do Sul, Encantado, Estrela, Muçum and Roca Sales"
partners: "SEDUR/RS (State Secretariat of Urban and Metropolitan Development), Univates, municipal governments"
role: "Geospatial analyst on the georeferencing team: spatial data processing, multicriteria suitability modeling and map production for the municipal reports."
data: ["MapBiomas land cover (2022)", "IBGE urbanized areas (2019)", "FEPAM/SEMA cartographic base", "ANADEM terrain model", "UFRGS landslide-scar mapping (May 2024)", "IPH/UFRGS hydraulic data"]
tools: ["QGIS", "Python", "Multicriteria analysis", "Raster map algebra (10 m)"]
---

{{< lead >}}
How can we define where to rebuild after a disaster — safely, quickly and on a tight budget?
{{< /lead >}}

{{< facts >}}

## The challenge

The floods of September and November 2023 and May 2024 wiped out entire neighborhoods in the Taquari Valley. In Muçum, **79% of the population** was affected; in Roca Sales, 55%; in Arroio do Meio and Colinas, nearly half. In Cruzeiro do Sul, 600 of the 850 homes in the Passo de Estrela neighborhood were destroyed.

Families needed to be resettled, and municipalities needed answers fast: which land is safe, which is already served by infrastructure, and where should new housing, public facilities and services go first? The State Government commissioned a technical study to support those decisions while the municipal master plans were being revised.

## Approach

We combined the risk zoning produced for each municipality (flood, flash-flood drag zones and landslide susceptibility) with a **multicriteria suitability model**. Every 10 m cell of each municipality received a score from 1 to 100 indicating how suitable it is for new urban occupation.

{{< flow title="How the suitability index works" >}}
{{< step label="Restrictions" >}}
- Permanent Preservation Areas (Forest Code)
- Risk zones: high (0.1), medium (0.4), low (0.8), none (1)
{{< /step >}}
{{< step label="Factors" >}}
- Land cover: urban 100, agriculture 80, natural 40
- Distance to the urban core (1 km bands)
- Distance to roads (250 m bands)
- Slope: >30% excluded by law
{{< /step >}}
{{< step label="Map algebra" >}}
Weighted mean of the four factors × risk restriction → suitability surface (very low to high)
{{< /step >}}
{{< step label="Guidelines" accent="true" >}}
Overlay with ongoing projects, growth trends and input from municipal technicians → priority occupation areas
{{< /step >}}
{{< /flow >}}

The weighting logic favors **compact growth**: land that is already urbanized or close to existing infrastructure scores higher, natural vegetation is protected, and slopes above 30% are excluded in line with the federal land subdivision law (Law 6.766/79).

## Results

- A suitability map for each of the seven municipalities, classifying land into four levels (very low, low, medium, high) plus areas not suitable for urbanization.
- **Preliminary priority-occupation guidelines** for housing, public facilities, commerce and services, discussed with each municipality's support group.
- Recommendations for areas already consolidated in high and medium risk zones: contingency plans, continuous monitoring, drainage upgrades and community engagement.

## Impact

The study gave municipalities an **emergency decision-support tool** during reconstruction and a technical basis for their new master plans. All maps were published on the State's spatial data infrastructure, so planners and the public can explore them interactively.

A peer-reviewed paper on the method is forthcoming.

## Maps

{{< figs cols="2" >}}
{{< fig src="/img/projects/urban-suitability-index-post-disasters/urban-suitability_01.webp" alt="Location maps showing the seven study municipalities highlighted in dark grey within the Taquari Valley, Rio Grande do Sul and the Taquari-Antas river basin" caption="Study area: seven municipalities in the Taquari Valley." >}}
{{< fig src="/img/projects/urban-suitability-index-post-disasters/urban-suitability_02.webp" alt="Regional map of urban suitability, with large areas in red and orange on steep valley slopes and green and yellow areas on flatter land near towns" caption="Urban suitability across the study area, from not suitable (red) to high suitability (green)." >}}
{{< /figs >}}

{{< fig src="/img/projects/urban-suitability-index-post-disasters/urban-suitability_06.webp" alt="Six small maps of Muçum in shades of pink and purple, one for each input layer: land cover, distance to urban core, distance to roads, slope, flood susceptibility and landslide susceptibility" caption="The six input layers for Muçum, each rescaled to a common suitability score." >}}

{{< figs cols="2" >}}
{{< fig src="/img/projects/urban-suitability-index-post-disasters/urban-suitability_07.webp" alt="Suitability map of Muçum in purple and orange, with high-suitability areas in orange along gentler slopes and non-suitable areas along the Taquari River" caption="Muçum: suitability for urbanization in four classes." >}}
{{< fig src="/img/projects/urban-suitability-index-post-disasters/urban-suitability_08.webp" alt="Detail of Muçum's urban area over satellite imagery, highlighting high-suitability land in orange outline and low-suitability land in purple" caption="Muçum: detail of high-suitability land around the urban core." >}}
{{< /figs >}}

## Reports

Technical reports delivered to [SEDUR](https://www.sedur.rs.gov.br/cidades), in Portuguese. Explore the [interactive maps](https://iede.rs.gov.br/portal/apps/webappviewer/index.html?id=34e8fb12b1284b9f88685f561f2c1e0b) on the State's spatial data portal.

**1. Risk zoning** — flood and landslide susceptibility, drag zones:
[Arroio do Meio](/pdf/projects/urban-suitability-index-post-disasters/1a-zoneamento-de-risco-arroio-do-meio.pdf) ·
[Colinas](/pdf/projects/urban-suitability-index-post-disasters/1a-zoneamento-de-risco-colinas.pdf) ·
[Cruzeiro do Sul](/pdf/projects/urban-suitability-index-post-disasters/1a-zoneamento-de-risco-cruzeiro-do-sul.pdf) ·
[Encantado](/pdf/projects/urban-suitability-index-post-disasters/1a-zoneamento-de-risco-encantado.pdf) ·
[Estrela](/pdf/projects/urban-suitability-index-post-disasters/1a-zoneamento-de-risco-estrela.pdf) ·
[Muçum](/pdf/projects/urban-suitability-index-post-disasters/1a-zoneamento-de-risco-mucum.pdf) ·
[Roca Sales](/pdf/projects/urban-suitability-index-post-disasters/1a-zoneamento-de-risco-roca-sales.pdf)

{{< figs cols="3" >}}
{{< fig src="/img/projects/urban-suitability-index-post-disasters/urban-suitability_03.webp" alt="Risk zoning map of Arroio do Meio with high risk in red along rivers and steep slopes, medium in orange, low in green and no risk in yellow" caption="Arroio do Meio: risk zoning." >}}
{{< fig src="/img/projects/urban-suitability-index-post-disasters/urban-suitability_04.webp" alt="Map of Arroio do Meio showing flood-susceptible land in light orange along the Taquari and Forqueta rivers and the urbanized area hit by the flood in darker orange" caption="Arroio do Meio: flood susceptibility and urban areas hit in 2024." >}}
{{< fig src="/img/projects/urban-suitability-index-post-disasters/urban-suitability_05.webp" alt="Detail of Arroio do Meio's urban core over satellite imagery, with risk classes overlaid and numbered landmarks such as the city hall and the iron bridge" caption="Arroio do Meio: risk classes in the urban core." >}}
{{< /figs >}}

**2. Preliminary guidelines for priority occupation:**
[Arroio do Meio](/pdf/projects/urban-suitability-index-post-disasters/1b-diretrizes-preliminares-de-ocupacao-prioritaria-arroio-do-meio.pdf) ·
[Colinas](/pdf/projects/urban-suitability-index-post-disasters/1b-diretrizes-preliminares-de-ocupacao-prioritaria-colinas.pdf) ·
[Cruzeiro do Sul](/pdf/projects/urban-suitability-index-post-disasters/1b-diretrizes-preliminares-de-ocupacao-prioritaria-cruzeiro-do-sul.pdf) ·
[Encantado](/pdf/projects/urban-suitability-index-post-disasters/1b-diretrizes-preliminares-de-ocupacao-prioritaria-encantado.pdf) ·
[Estrela](/pdf/projects/urban-suitability-index-post-disasters/1b-diretrizes-preliminares-de-ocupacao-prioritaria-estrela.pdf) ·
[Muçum](/pdf/projects/urban-suitability-index-post-disasters/1b-diretrizes-preliminares-de-ocupacao-prioritaria-mucum.pdf) ·
[Roca Sales](/pdf/projects/urban-suitability-index-post-disasters/1b-diretrizes-preliminares-de-ocupacao-prioritaria-roca-sales.pdf)

**3. Technical diagnosis** — physical, social, economic, infrastructure, mobility and legislation:
[Arroio do Meio](/pdf/projects/urban-suitability-index-post-disasters/2b-1-diagnostico-tecnico-e-leitura-tecnica-arroio-do-meio.pdf) ·
[Colinas](/pdf/projects/urban-suitability-index-post-disasters/2b-1-diagnostico-tecnico-e-leitura-tecnica-colinas.pdf) ·
[Cruzeiro do Sul](/pdf/projects/urban-suitability-index-post-disasters/2b-1-diagnostico-tecnico-e-leitura-tecnica-cruzeiro-do-sul.pdf) ·
[Encantado](/pdf/projects/urban-suitability-index-post-disasters/2b-1-diagnostico-tecnico-e-leitura-tecnica-encantado.pdf) ·
[Estrela](/pdf/projects/urban-suitability-index-post-disasters/2b-1-diagnostico-tecnico-e-leitura-tecnica-estrela.pdf) ·
[Muçum](/pdf/projects/urban-suitability-index-post-disasters/2b-1-diagnostico-tecnico-e-leitura-tecnica-mucum.pdf) ·
[Roca Sales](/pdf/projects/urban-suitability-index-post-disasters/2b-1-diagnostico-tecnico-e-leitura-tecnica-roca-sales.pdf)

{{< figs cols="3" >}}
{{< fig src="/img/projects/urban-suitability-index-post-disasters/urban-suitability_09.webp" alt="Rural land use map of Roca Sales showing soy, temporary crops, pasture and forestry plantations in different colors" caption="Roca Sales: rural production (MapBiomas 2023)." >}}
{{< fig src="/img/projects/urban-suitability-index-post-disasters/urban-suitability_10.webp" alt="Map of Roca Sales' urban area showing urban growth in 2004, 2014 and 2024 in yellow, orange and red, high-risk zones and numbered residential subdivisions" caption="Roca Sales: urban growth 2004–2024 and new subdivisions." >}}
{{< fig src="/img/projects/urban-suitability-index-post-disasters/urban-suitability_11.webp" alt="Choropleth map of Roca Sales census tracts in shades of blue showing the share of households supplied by wells, darker in the rural center of the municipality" caption="Roca Sales: share of households relying on wells (Census 2022)." >}}
{{< /figs >}}
