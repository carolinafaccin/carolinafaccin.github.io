---
title: "Dispersão da Covid-19"
date: 2022-03-15T10:00:00+00:00
categories:
  - "Desenvolvimento Regional"
draft: false
summary: "Um banco de dados PostGIS e mapas acompanhando como a Covid-19 se espalhou pelos 497 municípios do Rio Grande do Sul, seguindo eixos de deslocamento, frigoríficos e a rede urbana."
period: "2020–2022"
location: "Rio Grande do Sul e Região Metropolitana de Porto Alegre"
partners: "Projeto ObservaDR/COVID-19 (mais de 20 pesquisadores); PROPUR/UFRGS"
role: "Construí e mantive o banco de dados espacial dos 497 municípios, conduzi as análises e produzi os mapas; autora principal do estudo metropolitano."
data: ["Secretarias de saúde estadual e municipais", "Dados abertos Brasil.io", "IBGE (Censo 2010, REGIC 2018)", "RAIS (2018)", "Registro de estabelecimentos MAPA", "FEPAM"]
tools: ["PostgreSQL/PostGIS", "SQL", "QGIS", "Python", "Excel", "Adobe Illustrator"]
---

{{< lead >}}
Quando a pandemia chegou, como acompanhar a dispersão da Covid-19 em um território tão grande quanto o Rio Grande do Sul, e explicá-la à população?
{{< /lead >}}

{{< facts >}}

## O desafio

Em 2020, os casos eram divulgados diariamente para cada um dos 497 municípios do estado, mas os números brutos não explicavam *por que* o vírus se movia como se movia. Os pesquisadores suspeitavam que a resposta estava na forma como as cidades se conectam: deslocamentos pendulares, acesso a hospitais e a localização de grandes locais de trabalho.

## Abordagem

No projeto **ObservaDR/COVID-19**, construí um banco de dados espacial que unia os dados epidemiológicos diários à estrutura da rede urbana. Depois aplicamos a mesma abordagem, com mais detalhe, à Região Metropolitana de Porto Alegre, a área mais populosa do estado.

{{< flow title="Dos números diários aos padrões territoriais" >}}
{{< step label="Casos" >}}
Casos confirmados e óbitos diários (SES-RS, Brasil.io)
{{< /step >}}
{{< step label="Banco de dados" >}}
Banco PostGIS cobrindo os 497 municípios
{{< /step >}}
{{< step label="Camadas de contexto" >}}
Pendularidade, hierarquia urbana, acesso a hospitais, frigoríficos, condições de moradia
{{< /step >}}
{{< step label="Divulgação" accent="true" >}}
Mapas para o público e artigos científicos
{{< /step >}}
{{< /flow >}}

## Resultados

- Na região metropolitana, Porto Alegre, Canoas e Novo Hamburgo concentravam **56,3% dos casos confirmados** em abril de 2021. O vírus se espalhou ao longo da **BR-116 e do eixo do Trensurb**, os principais corredores de deslocamento.
- A mortalidade foi maior nos municípios calçadistas, e municípios com infraestrutura domiciliar inadequada tiveram maior transmissão.
- No interior, os casos se concentraram nas **cidades médias**, que também são polos regionais de saúde, e a vacinação reduziu claramente os óbitos nos dois anos analisados.
- Em Santa Cruz do Sul, o **Modelo de Distanciamento Controlado** do estado reduziu a circulação e os casos até dezembro de 2020, mas não evitou o crescimento exponencial em 2021.

## Por que importa

O projeto mostrou que a resposta a uma pandemia depende do planejamento urbano: mobilidade, redes regionais de saúde e desigualdade de infraestrutura definiram quem adoeceu. Também mostrou que dados abertos e um banco de dados espacial bem estruturado podem informar a população rapidamente durante uma crise.

**Publicações:**

- [Faccin *et al.* (2022)](https://www.scielo.br/j/urbe/a/LSrfgjKMGvr9qds4KYLjFYy/): um ano de pandemia na Região Metropolitana de Porto Alegre.
- [Silveira, Cazarotto, Faccin & Vogt (2020)](https://www.rbgdr.net/revista/index.php/rbgdr/article/view/5984): dispersão da Covid-19 na Região dos Vales e nas cidades médias de Santa Cruz do Sul e Lajeado.
- [Stavizki Junior, Faccin & Silva (2022)](https://periodicos.utfpr.edu.br/rbpd/article/view/15296): o Modelo de Distanciamento Controlado em Santa Cruz do Sul.
- [Giacometti & Faccin (2024)](https://periodicos.uem.br/ojs/index.php/BolGeogr/article/view/69370): dois anos de pandemia na Região dos Vales.

## Mapas

{{< figs cols="2" >}}
{{< fig src="/img/projects/dispersion-of-covid-19/covid19_01.webp" alt="Mapa da Região Metropolitana de Porto Alegre com municípios coloridos pela população, grade de densidade populacional, rede rodoviária e a linha do Trensurb" caption="Região Metropolitana de Porto Alegre: população, densidade, rodovias e Trensurb." >}}
{{< fig src="/img/projects/dispersion-of-covid-19/covid19_02.webp" alt="Mapa de deslocamentos pendulares na Região Metropolitana de Porto Alegre, com setas vermelhas grossas convergindo para Porto Alegre a partir dos municípios vizinhos" caption="Deslocamentos pendulares para trabalho na região metropolitana." >}}
{{< /figs >}}

{{< fig src="/img/projects/dispersion-of-covid-19/covid19_03.webp" alt="Mapa do Rio Grande do Sul com círculos proporcionais aos casos confirmados de Covid-19 por município, sobre a estrutura da rede urbana, com os maiores círculos em torno de Porto Alegre" caption="Casos confirmados por município e a rede urbana (setembro de 2021)." >}}

{{< figs cols="3" >}}
{{< fig src="/img/projects/dispersion-of-covid-19/covid19_04.webp" alt="Mapa de empregos no abate de aves e frigoríficos no Rio Grande do Sul com casos confirmados de Covid-19 em maio de 2020, mostrando sobreposição no norte e no Vale do Taquari" caption="Empregos no abate de aves, frigoríficos e primeiros casos (maio de 2020)." >}}
{{< fig src="/img/projects/dispersion-of-covid-19/covid19_05.webp" alt="Mapa de empregos no abate de suínos e frigoríficos com casos confirmados de Covid-19 em maio de 2020" caption="Empregos no abate de suínos, frigoríficos e primeiros casos (maio de 2020)." >}}
{{< fig src="/img/projects/dispersion-of-covid-19/covid19_06.webp" alt="Mapa de deslocamentos para serviços de saúde de alta complexidade, com linhas azuis convergindo para Porto Alegre e polos regionais, e hospitais com UTI" caption="Deslocamentos para saúde de alta complexidade (REGIC 2018) e hospitais com UTI." >}}
{{< /figs >}}
