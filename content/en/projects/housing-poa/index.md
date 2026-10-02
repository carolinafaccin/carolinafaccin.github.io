---
title: "Housing and Gated Communities in Porto Alegre"
date: 2024-07-11T10:00:00+00:00
featured: 2
categories:
  - "Housing & Inequality"
  - "Urban Form & Land Use"
draft: false
aliases: ["/projects/housing-porto-alegre/"]
summary: "A city-wide open dataset of gated communities in Porto Alegre, classified into nine built-form types, reveals how housing products for different social classes shape segregation in the metropolis."
period: "2021–2024"
location: "Porto Alegre, Rio Grande do Sul, Brazil"
partners: "PROPUR/UFRGS; Observatório das Metrópoles (Porto Alegre core)"
role: "Lead author: data collection and georeferencing, typology design, spatial and statistical analysis, maps and open dataset."
data: ["Google Earth imagery (2022)", "IBGE Census 2010 (income by census tract)", "City of Porto Alegre (federal housing program sites)", "OpenStreetMap"]
tools: ["QGIS", "Python", "Typology building", "Spatial statistics"]
---

{{< lead >}}
Where are Porto Alegre's gated communities, what do they look like, and what does their distribution say about segregation in the city?
{{< /lead >}}

{{< facts >}}

## The challenge

Gated communities have become a dominant housing product in Brazilian cities, but there was no consistent, city-wide map of them in Porto Alegre, let alone one that distinguished a high-rise tower complex from a cluster of townhouses or a social housing condominium. Without that, it is hard to discuss how housing markets and public programs shape the city.

## Approach

I built the dataset from scratch, georeferencing every gated community visible in satellite imagery and recording its built form and period of construction. Communities were then grouped into a typology and analyzed against neighborhood income.

{{< flow title="From imagery to an open dataset" >}}
{{< step label="Mapping" >}}
Digitize every gated community from satellite imagery (2022)
{{< /step >}}
{{< step label="Attributes" >}}
Horizontal vs. vertical, number of floors, period of construction
{{< /step >}}
{{< step label="Typology" >}}
Nine built-form types (A1 to E)
{{< /step >}}
{{< step label="Analysis" >}}
Overlay with census income, neighborhoods, road structure and federal housing program sites
{{< /step >}}
{{< step label="Outputs" accent="true" >}}
Open dataset (Zenodo) and peer-reviewed paper
{{< /step >}}
{{< /flow >}}

## Results

- **1,024 gated communities** in 77 of the city's 94 neighborhoods: 459 horizontal (houses), 560 vertical (apartment blocks and towers) and 5 mixed.
- **Nine typologies** of gated communities, each associated with a different social segment. Communities with shared amenities lean to the top: 60% of the towers with amenities (B2) and 68% of the house clusters with amenities (C2) sit in census tracts of the two highest income classes.
- A clear **morphological segregation**: small-scale horizontal condominiums (townhouses and single-family homes) predominate in the South Zone, while high-rise towers for high-income households concentrate in the Center-East Zone.
- Detailed comparisons of contrasting neighborhoods: Boa Vista and Jardim Europa in the north, Tristeza and Camaquã in the south.

## Why it matters

The dataset turns a much-debated phenomenon into something that can be measured. It is openly available for planners, researchers and journalists who want to study housing, segregation or real estate dynamics in Porto Alegre.

I later rebuilt the analysis as an open, reproducible Python pipeline that checks its results against the numbers published in the paper: [code and figures on GitHub](https://github.com/carolinafaccin/housing-poa).

- [Open dataset on Zenodo](https://doi.org/10.5281/zenodo.17023731)
- [Faccin, Almeida & Campos (2024)](https://www.revistas.usp.br/posfau/article/view/226515) (PT): *Urban morphology and typology of gated communities in the Porto Alegre metropolis*.
- [Lahorgue *et al.* (2022)](https://www.observatoriodasmetropoles.net.br/reforma-urbana-e-direito-a-cidade-porto-alegre/) (PT): housing situation and perspectives in Porto Alegre.

**Related research on real estate production:**

- [Almeida, Faccin & Campos (2025)](https://www.researchgate.net/publication/394435940_Financeirizacao_do_espaco_urbano_e_capitalismo_de_plataforma_producao_imobiliaria_em_Porto_Alegre-RS) (PT): studios and compact apartments conceived as financial assets for rental income.
- [Almeida, Morlin Filho & Faccin (2025)](https://editorarealize.com.br/artigo/visualizar/122479) (PT): real estate production in Porto Alegre and the agents involved.

## Figures

Produced by the open pipeline above.

{{< fig src="/img/projects/housing-poa/map_neighborhoods.webp" alt="Map of Porto Alegre neighborhoods shaded by number of gated communities, darkest in Tristeza, Ipanema, Camaquã and Cristal in the south zone, with each gated community as a dot" caption="Gated communities by neighborhood." >}}

{{< fig src="/img/projects/housing-poa/map_form.webp" alt="Map of Porto Alegre with gated communities as dots sized by gated area and colored by building form: light orange horizontal clusters in the south zone, dark high-rise towers in the center-east" caption="Building form: houses in the south, towers in the center-east." >}}

{{< fig src="/img/projects/housing-poa/form_by_neighborhood.webp" alt="Stacked bars of the 20 neighborhoods with most gated communities, led by Tristeza with 94, split into horizontal, low-rise, high-rise and mixed forms" caption="The 20 neighborhoods with most gated communities, by building form." >}}

{{< fig src="/img/projects/housing-poa/map_period_income.webp" alt="Two maps of Porto Alegre: gated communities colored by period of construction, with the newest toward the eastern and southern edges, and by household income class of their census tract" caption="Period of construction and household income of the census tract (2010)." >}}

{{< fig src="/img/projects/housing-poa/map_typology.webp" alt="Nine small maps of Porto Alegre, one per gated-community type, each highlighting where that type is located over grey dots for all others" caption="Where each of the nine types is located." >}}

{{< fig src="/img/projects/housing-poa/typology_profile.webp" alt="Two stacked bar charts per type: share by period of construction, and share by household income class of the census tract, with B2 and C2 leaning to classes A and B" caption="Period of construction and income class by type." >}}

{{< fig src="/img/projects/housing-poa/map_mcmv.webp" alt="Map of Porto Alegre with gated communities as orange dots along the radial roads and the south shore, federal housing program developments as dark red diamonds at the eastern and southern edges, and the main roads" caption="Gated communities, federal housing program (MCMV) developments and the main roads." >}}

{{< fig src="/img/projects/housing-poa/map_case_studies.webp" alt="Two maps of gated-community footprints colored by type family: Tristeza and Camaquã, dominated by small house clusters, and Boa Vista and Jardim Europa, dominated by towers with amenities" caption="South zone (Tristeza and Camaquã) and center-east (Boa Vista and Jardim Europa)." >}}
