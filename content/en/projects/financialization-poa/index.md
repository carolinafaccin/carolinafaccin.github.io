---
title: "Financialization of Housing in Porto Alegre"
date: 2026-10-14T10:00:00+00:00
categories:
  - "Housing & Inequality"
draft: false
summary: "Studios and compact apartments sold as investments, empty dwellings and a shrinking population: a reproducible look at real estate production in Porto Alegre from 2007 to 2024."
period: "2024–present"
location: "Porto Alegre, Rio Grande do Sul, Brazil"
partners: "PROPUR/UFRGS; Nicole Leal de Almeida (lead author); Heleniza Ávila Campos"
role: "Co-author: data organization, spatial analysis and maps; reproducible pipeline that rebuilds the paper's figures from the original data and the census."
data: ["Sinduscon-RS real estate census (2007–2018) and market report (Sept 2024)", "IBGE Census 2000, 2010 and 2022 and CNEFE address files (2010, 2022)", "Developers' websites (Melnick, Cyrela Goldsztein)", "ZAP Imóveis listings (Oct 2026)"]
tools: ["Python", "GeoPandas", "QGIS", "Census data"]
---

{{< lead >}}
Who is the housing being built in Porto Alegre for, if the city keeps adding dwellings while it loses residents?
{{< /lead >}}

{{< facts >}}

## The challenge

Since 2020 Porto Alegre's developers have launched studios and compact apartments marketed as investments: units to rent on short-stay platforms, sold in fractions or managed by proptechs. At the same time the 2022 Census found a city with fewer residents than in 2010 and almost one dwelling in five empty. Connecting the two requires putting together data that are scattered across the builders' association, developers' websites and the census, and that rarely use the same geography.

## Approach

The paper by [Almeida, Faccin & Campos (2025)](http://dx.doi.org/10.1590/2236-9996.2025-6469490-pt) combined these sources with a qualitative reading of the developers' strategies. I then rebuilt its figures as a Python pipeline that reads the original data, links every count to the neighborhoods of the 2016 municipal law and checks each number of the text against its source.

{{< flow title="From scattered sources to comparable neighborhoods" >}}
{{< step label="Launches" >}}
Units and developments launched per year, typology and neighborhood (Sinduscon-RS, 2007–2018)
{{< /step >}}
{{< step label="Dwellings" >}}
Every private dwelling address of the 2010 and 2022 censuses (CNEFE), occupied or not
{{< /step >}}
{{< step label="Developers" >}}
Compact developments of Melnick and Cyrela Goldsztein (2020–2024), with location checked
{{< /step >}}
{{< step label="Prices" >}}
Median asking price per m² by neighborhood (ZAP Imóveis)
{{< /step >}}
{{< step label="Outputs" accent="true" >}}
Peer-reviewed paper and reproducible figures
{{< /step >}}
{{< /flow >}}

## Results

- **Fewer, larger developments.** From 2007 to 2015 the city saw 59,872 units launched in 3,305 developments. Units peaked at 8,423 in 2012, while the number of developments fell from 452 in 2007 to 321 in 2015: the average development grew from 12 to 20 units.
- **The turn to small units.** Between 2016 and 2018 one-bedroom launches grew 65% and studios (JK) more than tripled, while three-bedroom launches fell 12%. In the twelve months to September 2024, studios were 42% of the 2,761 vertical units launched but only 19% of their sales value; three-bedroom units were 27% of the units and 51% of the value.
- **More dwellings, fewer people.** Between 2010 and 2022 Porto Alegre gained 112,807 private dwellings and lost 76,506 residents (−5.4%). Dwellings not occupied, vacant or for occasional use, doubled from 65,226 (11% of the stock) to 128,239 (19%). Growth was largest at the periphery (Restinga, Mário Quintana, Lomba do Pinheiro); the share of empty dwellings is highest in the center (Centro Histórico, 30%).
- **Investment units in the most valued center.** The 17 compact developments that Melnick and Cyrela Goldsztein launched from 2020 to 2024 (4,107 units) are all in 11 central and east-central neighborhoods, from Rio Branco and Petrópolis to Cidade Baixa, where asking prices per m² are highest. Melnick's GO line averages 48 m² per unit; Cyrela's compacts, 34 m². Vista Praia de Belas, 419 units of 18 to 21 m², sold out in 14 days in 2024, in a neighborhood flooded that May.

## Why it matters

Housing production in Porto Alegre answers to investors looking for rental income more than to the households that need a home. Compact units concentrate where land is most valued, while the stock of empty dwellings grows and lower-income housing is pushed to the edges. The reproducible pipeline makes these numbers easy to update with each new census or market report.

This project continues the research on real estate production in [Gated Communities in Porto Alegre]({{< ref "/projects/housing-poa" >}}). A book chapter on compact investment units and the May 2024 flood (Almeida & Faccin, 2027) is in progress; the code will be published with it.

- [Almeida, Faccin & Campos (2025)](http://dx.doi.org/10.1590/2236-9996.2025-6469490-pt) (PT): *Financialization of urban space and platform capitalism: real estate production in Porto Alegre*, Cadernos Metrópole 27(64).
- [Almeida, Morlin Filho & Faccin (2025)](https://editorarealize.com.br/artigo/visualizar/122479) (PT): real estate production in Porto Alegre and the agents involved.

## Figures

Rebuilt from the paper's data and the census (text in Portuguese). The dwelling counts use every address of both censuses and the developments' locations were checked one by one, so some values differ slightly from the published figures.

{{< fig src="/img/projects/financialization-poa/a25_graficos_1_3_lancamentos.webp" alt="Four charts of residential launches in Porto Alegre: units per year from 2007 to 2015, peaking at about 8,400 in 2012; developments falling from about 450 to 320; two- and three-bedroom units peaking in 2012 and 2013; and one-bedroom units rising sharply from 2016 to 2018" caption="Residential launches, 2007–2018 (Graphs 1 to 3 of the paper)." >}}

{{< fig src="/img/projects/financialization-poa/a25_figura_1_lancamentos_bairros.webp" alt="Two maps of Porto Alegre neighborhoods: units launched from 2007 to 2015, darkest in Sarandi in the north and Petrópolis in the center-east, and developments launched, darkest in Petrópolis, with almost nothing in the south" caption="Units and developments launched by neighborhood, 2007–2015 (Figure 1)." >}}

{{< fig src="/img/projects/financialization-poa/a25_figura_2_nao_ocupados_crescimento.webp" alt="Two maps of Porto Alegre neighborhoods: the share of dwellings not occupied in 2022, highest in Centro Histórico, Praia de Belas and Floresta, and the growth of private dwellings from 2010 to 2022, highest in Restinga, Lomba do Pinheiro and Mário Quintana at the periphery, with a few neighborhoods losing dwellings" caption="Dwellings not occupied (2022) and growth of dwellings (2010–2022) by neighborhood (Figure 2)." >}}

{{< fig src="/img/projects/financialization-poa/a25_figura_3_preco_studios.webp" alt="Two maps of Porto Alegre neighborhoods: median asking price per square meter of apartments for sale, highest in the center-east, and the number of studio and one-bedroom developments by Melnick and Cyrela Goldsztein from 2020 to 2024, all in a cluster of central and east-central neighborhoods" caption="Price per m² (Oct 2026) and compact developments of Melnick and Cyrela Goldsztein, 2020–2024 (Figure 3)." >}}
