---
title: "Housing and Gated Communities in Porto Alegre"
date: 2024-07-11T10:00:00+00:00
featured: true
categories:
  - "Housing & Inequality"
  - "Urban Form & Land Use"
draft: false
summary: "A city-wide open dataset of gated communities in Porto Alegre, classified into nine built-form types, reveals how housing products for different social classes shape segregation in the metropolis."
period: "2021–2024"
location: "Porto Alegre, Rio Grande do Sul, Brazil"
partners: "PROPUR/UFRGS; Observatório das Metrópoles (Porto Alegre core)"
role: "Lead author: data collection and georeferencing, typology design, spatial and statistical analysis, maps and open dataset."
data: ["Google Earth imagery (2022)", "IBGE Census 2010 (income by census tract)", "Google Open Buildings", "OpenStreetMap"]
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

- **Nine typologies** of gated communities, each associated with a different social segment.
- A clear **morphological segregation**: small-scale horizontal condominiums (townhouses and single-family homes) predominate in the South Zone, while high-rise towers for high-income households concentrate in the Center-East Zone.
- Detailed comparisons of contrasting neighborhoods: Boa Vista and Jardim Europa in the north, Tristeza and Camaquã in the south.

## Why it matters

The dataset turns a much-debated phenomenon into something that can be measured. It is openly available for planners, researchers and journalists who want to study housing, segregation or real estate dynamics in Porto Alegre.

- [Open dataset on Zenodo](https://doi.org/10.5281/zenodo.17023731)
- [Faccin, Almeida & Campos (2024)](https://www.revistas.usp.br/posfau/article/view/226515) (PT): *Urban morphology and typology of gated communities in the Porto Alegre metropolis*.
- [Lahorgue *et al.* (2022)](https://www.observatoriodasmetropoles.net.br/reforma-urbana-e-direito-a-cidade-porto-alegre/) (PT): housing situation and perspectives in Porto Alegre.

**Related research on real estate production:**

- [Almeida, Faccin & Campos (2025)](https://www.researchgate.net/publication/394435940_Financeirizacao_do_espaco_urbano_e_capitalismo_de_plataforma_producao_imobiliaria_em_Porto_Alegre-RS) (PT): studios and compact apartments conceived as financial assets for rental income.
- [Almeida, Morlin Filho & Faccin (2025)](https://editorarealize.com.br/artigo/visualizar/122479) (PT): real estate production in Porto Alegre and the agents involved.

## Maps

{{< figs cols="2" >}}
{{< fig src="/img/projects/housing-porto-alegre/housing-poa_01.webp" alt="Two maps of Porto Alegre: gated communities as dots over neighborhoods shaded by count, and pie charts per neighborhood showing the share of horizontal, low-rise and high-rise communities" caption="Distribution of gated communities by neighborhood, and the mix of horizontal and vertical forms." >}}
{{< fig src="/img/projects/housing-porto-alegre/housing-poa_02.webp" alt="Two maps of Porto Alegre: gated communities colored by period of construction, and colored by average household income of the surrounding census tract" caption="Period of construction and average household income (Census 2010)." >}}
{{< /figs >}}

{{< figs cols="2" >}}
{{< fig src="/img/projects/housing-porto-alegre/housing-poa_06.webp" alt="Eight small maps of Porto Alegre, one per typology, showing where each type of gated community is located" caption="Where each typology is located." >}}
{{< fig src="/img/projects/housing-porto-alegre/housing-poa_03.webp" alt="Map of Porto Alegre showing gated communities in red, condominiums built under the federal housing program as yellow circles, and radial and perimeter roads" caption="Gated communities, federal housing program condominiums and the main road structure." >}}
{{< /figs >}}

{{< figs cols="2" >}}
{{< fig src="/img/projects/housing-porto-alegre/housing-poa_04.webp" alt="Three stacked maps of Boa Vista and Jardim Europa showing gated communities by typology, household income and period of construction" caption="North zone: Boa Vista and Jardim Europa." >}}
{{< fig src="/img/projects/housing-porto-alegre/housing-poa_05.webp" alt="Three stacked maps of Tristeza and Camaquã showing gated communities by typology, household income and period of construction" caption="South zone: Tristeza and Camaquã." >}}
{{< /figs >}}
