---
title: "Dispersion of Covid-19"
date: 2022-03-15T10:00:00+00:00
categories:
  - "Regional Development"
draft: false
summary: "A PostGIS database and maps tracking how Covid-19 spread across Rio Grande do Sul's 497 municipalities, following commuting corridors, meatpacking plants and the urban network."
period: "2020–2022"
location: "Rio Grande do Sul and the Porto Alegre Metropolitan Region, Brazil"
partners: "ObservaDR/COVID-19 project (more than 20 researchers); PROPUR/UFRGS"
role: "Built and maintained the spatial database for the 497 municipalities, ran the analyses and produced the maps; lead author of the metropolitan study."
data: ["State and municipal health secretariats", "Brasil.io open data", "IBGE (Census 2010, REGIC 2018)", "RAIS (2018)", "MAPA establishment registry", "FEPAM"]
tools: ["PostgreSQL/PostGIS", "SQL", "QGIS", "Python", "Excel", "Adobe Illustrator"]
---

{{< lead >}}
When the pandemic arrived, how could we track the spread of Covid-19 across a territory as large as Rio Grande do Sul, and explain it to the public?
{{< /lead >}}

{{< facts >}}

## The challenge

In 2020, case counts were published daily for each of the state's 497 municipalities, but raw numbers did not explain *why* the virus moved the way it did. Researchers suspected the answer lay in how cities are connected: commuting, access to hospitals and the location of large workplaces.

## Approach

As part of the **ObservaDR/COVID-19** project, I built a spatial database that joined daily epidemiological data to the structure of the urban network. We then applied the same approach in more detail to the Porto Alegre Metropolitan Region, the state's most populated area.

{{< flow title="From daily counts to territorial patterns" >}}
{{< step label="Case data" >}}
Daily confirmed cases and deaths (state health secretariat, Brasil.io)
{{< /step >}}
{{< step label="Database" >}}
PostGIS database covering all 497 municipalities
{{< /step >}}
{{< step label="Context layers" >}}
Commuting, urban hierarchy, hospital access, meatpacking plants, housing conditions
{{< /step >}}
{{< step label="Public output" accent="true" >}}
Maps for the public and peer-reviewed articles
{{< /step >}}
{{< /flow >}}

## Results

- In the metropolitan region, Porto Alegre, Canoas and Novo Hamburgo concentrated **56.3% of confirmed cases** by April 2021. The virus spread along the **BR-116 highway and the Trensurb rail corridor**, the main commuting axes.
- Mortality was higher in shoe-manufacturing municipalities, and municipalities with inadequate household infrastructure had higher transmission.
- In the interior, cases concentrated in **medium-sized cities**, which are also regional health hubs, and vaccination clearly reduced deaths over the two years analyzed.
- In Santa Cruz do Sul, the state's **controlled-distancing model** reduced circulation and cases until December 2020, but did not prevent exponential growth in 2021.

## Why it matters

The project showed that pandemic response depends on urban planning: mobility, regional health networks and infrastructure inequality shaped who got sick. It also showed that open data and a well-structured spatial database can inform the public quickly during a crisis.

**Publications (PT):**

- [Faccin *et al.* (2022)](https://www.scielo.br/j/urbe/a/LSrfgjKMGvr9qds4KYLjFYy/): one year of the pandemic in the Porto Alegre Metropolitan Region.
- [Silveira, Cazarotto, Faccin & Vogt (2020)](https://www.rbgdr.net/revista/index.php/rbgdr/article/view/5984): Covid-19 dispersion in the Vales Region and the medium-sized cities of Santa Cruz do Sul and Lajeado.
- [Stavizki Junior, Faccin & Silva (2022)](https://periodicos.utfpr.edu.br/rbpd/article/view/15296): the controlled-distancing model in Santa Cruz do Sul.
- [Giacometti & Faccin (2024)](https://periodicos.uem.br/ojs/index.php/BolGeogr/article/view/69370): two years of the pandemic in the Vales Region.

## Maps

{{< figs cols="2" >}}
{{< fig src="/img/projects/dispersion-of-covid-19/covid19_01.webp" alt="Map of the Porto Alegre Metropolitan Region with municipalities shaded by population, population density grid, the road network and the Trensurb rail line" caption="Porto Alegre Metropolitan Region: population, density, highways and Trensurb." >}}
{{< fig src="/img/projects/dispersion-of-covid-19/covid19_02.webp" alt="Map of commuting flows in the Porto Alegre Metropolitan Region, with thick red arrows converging on Porto Alegre from neighboring municipalities" caption="Commuting flows for work in the metropolitan region." >}}
{{< /figs >}}

{{< fig src="/img/projects/dispersion-of-covid-19/covid19_03.webp" alt="Map of Rio Grande do Sul with circles sized by confirmed Covid-19 cases per municipality, over the urban network structure, with the largest circles around Porto Alegre" caption="Confirmed cases by municipality and the urban network (September 2021)." >}}

{{< figs cols="3" >}}
{{< fig src="/img/projects/dispersion-of-covid-19/covid19_04.webp" alt="Map of poultry slaughter employment and meatpacking plants in Rio Grande do Sul with confirmed Covid-19 cases in May 2020, showing overlap in the north and Taquari Valley" caption="Poultry slaughter jobs, plants and early cases (May 2020)." >}}
{{< fig src="/img/projects/dispersion-of-covid-19/covid19_05.webp" alt="Map of pork slaughter employment and meatpacking plants with confirmed Covid-19 cases in May 2020" caption="Pork slaughter jobs, plants and early cases (May 2020)." >}}
{{< fig src="/img/projects/dispersion-of-covid-19/covid19_06.webp" alt="Map of patient travel for high-complexity health care, with blue lines converging on Porto Alegre and regional hubs, and hospitals with intensive care units" caption="Travel for high-complexity health care (REGIC 2018) and ICU hospitals." >}}
{{< /figs >}}
