---
title: "Simulating Urban Growth in the Porto Alegre Metropolitan Region"
date: 2026-10-01T10:00:00+00:00
featured: false
categories:
  - "Urban Form & Land Use"
  - "Regional Development"
draft: true
summary: "A Markov chain and cellular automata model, trained on MapBiomas land cover from 1985 to 2015 and validated against 2023, projects where the Porto Alegre Metropolitan Region may urbanize by 2040."
period: "2026"
location: "Porto Alegre Metropolitan Region, Rio Grande do Sul, Brazil"
role: "Sole author: model design, Python implementation, validation and maps."
data: ["MapBiomas land use and land cover (1985–2023)", "OpenStreetMap main roads", "IBGE municipal boundaries"]
tools: ["Python", "Markov chains", "Cellular automata", "Spatial analysis"]
---

{{< lead >}}
Where is the Porto Alegre Metropolitan Region likely to urbanize next, and how far can a simple, transparent model get us?
{{< /lead >}}

{{< facts >}}

## The challenge

<!-- TODO: 2-3 sentences on why metropolitan-scale projection matters (planning, floods, housing) and why a simple replicable model. -->

## Approach

The model separates two questions: *how much* land will urbanize, and *where*.

{{< flow title="From satellite land cover to a 2040 projection" >}}
{{< step label="Data" >}}
MapBiomas annual land cover (30 m), reclassified into 5 classes
{{< /step >}}
{{< step label="Markov chain" >}}
Transition matrix 1985–2015 sets how much new urban area to expect
{{< /step >}}
{{< step label="Suitability + automaton" >}}
Distance to urban area and to main roads, plus neighborhood rules, decide where it goes
{{< /step >}}
{{< step label="Validation" accent="true" >}}
Simulate 2015–2023 and compare with the observed 2023 map
{{< /step >}}
{{< /flow >}}

Suitability is not hand-weighted: for each factor, the model measures what share of cells actually urbanized in 1985–2015 at each distance, and uses that as the score.

## Validation

<!-- TODO after `mccast validate`: figure of merit, kappa, hits/misses/false alarms, and the plain-language reading. A "no change" model scores 0. -->

## Results

<!-- TODO after `mccast project`: urban area 1985, 2015, 2023, 2040 (km²), which municipalities/corridors grow most, what land it replaces. -->

## Limitations

- Only urban expansion is allocated spatially; other classes change only where urban replaces them.
- Roads are today's network, applied to the past.
- No protected areas, slope or flood-risk restrictions yet.

## Maps

<!-- TODO after `mccast export --site-dir ...`:
{{< fig src="/img/projects/urban-growth-simulation/maps_land_cover.png" alt="..." caption="Land cover in 1985, 2015, 2023 and projected 2040." >}}
{{< fig src="/img/projects/urban-growth-simulation/map_validation.png" alt="..." caption="Validation 2015–2023: hits, misses and false alarms." >}}
-->
