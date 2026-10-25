---
title: "Datasets"
description: "Open geospatial datasets by Carolina Faccin on population, disaster susceptibility, gated communities and urban fragmentation in Brazil."
showTableOfContents: false
---

Datasets I built or co-authored, published with a DOI and an open license so they can be cited and reused. Each one comes with documentation of its sources and methods, and most with the code that produced it.

## Brazil

### BrazilPop: population and address grids

Raster grids (GeoTIFF) covering all of Brazil with population estimates and address counts for the 2010 and 2022 censuses, derived from the national address register (CNEFE/IBGE). Population is allocated to addresses by dasymetric disaggregation of census tract totals. Layers come in three groups: population, address type and household subtype.

{{< dataset authors="Possantti, I.; **Faccin, C. R.** (2026)" coverage="Brazil" years="2010, 2022" format="GeoTIFF; 30 m, 100 m and 1 km grids" license="CC BY 4.0" doi="10.5281/zenodo.22918300" code="https://github.com/iporepos/build-brazilpop" >}}

### SGB susceptibility maps: a harmonized national base

The municipal susceptibility maps for landslides, mass flows and floods published by the Geological Survey of Brazil (SGB/CPRM), gathered into a single harmonized base: 839 municipalities in 27 states and 2.57 million polygons, with the IBGE municipality code on every polygon, normalized classes and the original geometry. Susceptibility maps show the terrain's propensity to each process; they are not risk maps.

{{< dataset authors="**Faccin, C. R.** (2026)" coverage="Brazil (839 municipalities, 27 states)" years="Maps published up to October 2026" format="GeoParquet, one file per process group and state; SIRGAS 2000" license="CC BY 4.0" access="Data restricted on Zenodo for now. The code (catalog collection, download, harmonization and checks) is open." doi="10.5281/zenodo.23417168" code="https://github.com/carolinafaccin/cartas-suscetibilidade-sgb" >}}

## Rio Grande do Sul

### Gated communities in Porto Alegre

The boundaries and attributes of the 1,024 gated residential communities mapped in Porto Alegre in 2022, identified on satellite imagery, delimited with the City's fence-and-wall layer and confirmed on Street View, with a data dictionary and the neighborhood and permanent preservation area layers used in the analysis.

{{< dataset authors="**Faccin, C. R.** (2025)" coverage="Porto Alegre, RS" years="2022" format="GeoPackage, CSV" license="CC BY 4.0" doi="10.5281/zenodo.17023731" code="https://github.com/carolinafaccin/housing-poa" project="/projects/housing-poa" paper="[Faccin, Almeida & Campos (2024)](https://doi.org/10.11606/issn.2317-2762.posfauusp.2024.226515)" >}}

### Urban fragmentation in Santa Cruz do Sul

The database of my PhD thesis: census, municipal, MapBiomas, OpenStreetMap and Google Open Buildings layers for the city of Santa Cruz do Sul, used to build the sociospatial fragmentation index, along with the thesis text and its annexes.

{{< dataset authors="**Faccin, C. R.** (2025)" coverage="Santa Cruz do Sul, RS" years="1970–2022" format="GeoPackage, PDF" license="CC BY 4.0" doi="10.5281/zenodo.16423545" code="https://github.com/carolinafaccin/urb-frag" project="/projects/urb-frag" paper="[Thesis (PT)](https://lume.ufrgs.br/handle/10183/294929)" >}}
