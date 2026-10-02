---
title: "Habitação e Condomínios Fechados em Porto Alegre"
date: 2024-07-11T10:00:00+00:00
featured: true
categories:
  - "Habitação e Desigualdade"
  - "Forma Urbana e Uso do Solo"
draft: false
aliases: ["/projects/housing-porto-alegre/"]
summary: "Uma base aberta com todos os condomínios fechados de Porto Alegre, classificados em nove tipologias de forma construída, revela como produtos imobiliários para diferentes classes sociais moldam a segregação na metrópole."
period: "2021–2024"
location: "Porto Alegre, RS"
partners: "PROPUR/UFRGS; Observatório das Metrópoles (Núcleo Porto Alegre)"
role: "Autora principal: levantamento e georreferenciamento, construção da tipologia, análise espacial e estatística, mapas e base de dados aberta."
data: ["Imagens Google Earth (2022)", "Censo IBGE 2010 (renda por setor censitário)", "Prefeitura de Porto Alegre (empreendimentos do MCMV)", "OpenStreetMap"]
tools: ["QGIS", "Python", "Construção de tipologias", "Estatística espacial"]
---

{{< lead >}}
Onde estão os condomínios fechados de Porto Alegre, como eles são e o que sua distribuição diz sobre a segregação na cidade?
{{< /lead >}}

{{< facts >}}

## O desafio

Os condomínios fechados se tornaram um produto imobiliário dominante nas cidades brasileiras, mas não havia um mapeamento consistente de toda Porto Alegre, muito menos um que distinguisse um conjunto de torres de um grupo de sobrados ou de um condomínio de habitação social. Sem isso, é difícil discutir como o mercado e as políticas públicas moldam a cidade.

## Abordagem

Construí a base do zero, georreferenciando cada condomínio fechado visível nas imagens de satélite e registrando sua forma construída e período de construção. Os condomínios foram então agrupados em uma tipologia e analisados em relação à renda dos bairros.

{{< flow title="Das imagens a uma base de dados aberta" >}}
{{< step label="Mapeamento" >}}
Digitalização de cada condomínio fechado em imagens de satélite (2022)
{{< /step >}}
{{< step label="Atributos" >}}
Horizontal ou vertical, número de pavimentos, período de construção
{{< /step >}}
{{< step label="Tipologia" >}}
Nove tipos de forma construída (A1 a E)
{{< /step >}}
{{< step label="Análise" >}}
Cruzamento com renda censitária, bairros, estrutura viária e empreendimentos do MCMV
{{< /step >}}
{{< step label="Produtos" accent="true" >}}
Base aberta (Zenodo) e artigo científico
{{< /step >}}
{{< /flow >}}

## Resultados

- **1.024 condomínios fechados** em 77 dos 94 bairros da cidade: 459 horizontais (casas), 560 verticais (blocos e torres) e 5 mistos.
- **Nove tipologias** de condomínios fechados, cada uma associada a um segmento social. Os condomínios com equipamentos de lazer tendem ao topo: 60% das torres com equipamentos (B2) e 68% dos conjuntos de casas com equipamentos (C2) estão em setores censitários das duas classes de renda mais altas.
- Uma clara **segregação morfológica**: condomínios horizontais de pequena escala (sobrados e casas) predominam na Zona Sul, enquanto torres de alto padrão se concentram na Zona Centro-Leste.
- Comparações detalhadas entre bairros contrastantes: Boa Vista e Jardim Europa, ao norte; Tristeza e Camaquã, ao sul.

## Por que importa

A base transforma um fenômeno muito debatido em algo mensurável. Ela está disponível para técnicos, pesquisadores e jornalistas que queiram estudar habitação, segregação ou dinâmica imobiliária em Porto Alegre.

Depois, reconstruí a análise em um pipeline aberto e reproduzível em Python, que confere seus resultados com os números publicados no artigo: [código e figuras no GitHub](https://github.com/carolinafaccin/housing-poa).

- [Base de dados aberta no Zenodo](https://doi.org/10.5281/zenodo.17023731)
- [Faccin, Almeida & Campos (2024)](https://www.revistas.usp.br/posfau/article/view/226515): *Morfologia urbana e tipologia de condomínios fechados na metrópole de Porto Alegre–RS*.
- [Lahorgue *et al.* (2022)](https://www.observatoriodasmetropoles.net.br/reforma-urbana-e-direito-a-cidade-porto-alegre/): situação e perspectivas da habitação em Porto Alegre.

**Pesquisas relacionadas sobre produção imobiliária:**

- [Almeida, Faccin & Campos (2025)](https://www.researchgate.net/publication/394435940_Financeirizacao_do_espaco_urbano_e_capitalismo_de_plataforma_producao_imobiliaria_em_Porto_Alegre-RS): studios e apartamentos compactos concebidos como ativos financeiros para renda.
- [Almeida, Morlin Filho & Faccin (2025)](https://editorarealize.com.br/artigo/visualizar/122479): produção imobiliária em Porto Alegre e os agentes envolvidos.

## Figuras

Produzidas pelo pipeline aberto acima (legendas internas em inglês).

{{< fig src="/img/projects/housing-poa/map_neighborhoods.webp" alt="Mapa dos bairros de Porto Alegre coloridos pela quantidade de condomínios fechados, mais escuros em Tristeza, Ipanema, Camaquã e Cristal, na Zona Sul, com cada condomínio como um ponto" caption="Condomínios fechados por bairro." >}}

{{< fig src="/img/projects/housing-poa/map_form.webp" alt="Mapa de Porto Alegre com os condomínios como pontos dimensionados pela área fechada e coloridos pela forma construída: conjuntos horizontais em laranja claro na Zona Sul e torres em tom escuro na Zona Centro-Leste" caption="Forma construída: casas no sul, torres no centro-leste." >}}

{{< fig src="/img/projects/housing-poa/form_by_neighborhood.webp" alt="Barras empilhadas dos 20 bairros com mais condomínios fechados, liderados pela Tristeza com 94, divididas em formas horizontal, vertical baixa, vertical alta e mista" caption="Os 20 bairros com mais condomínios, por forma construída." >}}

{{< fig src="/img/projects/housing-poa/map_period_income.webp" alt="Dois mapas de Porto Alegre: condomínios coloridos pelo período de construção, com os mais novos nas bordas leste e sul, e pela classe de renda do setor censitário" caption="Período de construção e renda do setor censitário (2010)." >}}

{{< fig src="/img/projects/housing-poa/map_typology.webp" alt="Nove pequenos mapas de Porto Alegre, um por tipo de condomínio, cada um destacando onde aquele tipo se localiza sobre pontos cinza com todos os demais" caption="Onde está cada um dos nove tipos." >}}

{{< fig src="/img/projects/housing-poa/typology_profile.webp" alt="Dois gráficos de barras empilhadas por tipo: proporção por período de construção e por classe de renda do setor censitário, com B2 e C2 concentrados nas classes A e B" caption="Período de construção e classe de renda por tipo." >}}

{{< fig src="/img/projects/housing-poa/map_mcmv.webp" alt="Mapa de Porto Alegre com os condomínios fechados como pontos laranja ao longo das radiais e da orla sul, os empreendimentos do Minha Casa Minha Vida como losangos ferrugem nas bordas leste e sul, e as vias principais" caption="Condomínios fechados, empreendimentos do MCMV e as vias principais." >}}

{{< fig src="/img/projects/housing-poa/map_case_studies.webp" alt="Dois mapas com os polígonos dos condomínios coloridos por grupo de tipos: Tristeza e Camaquã, com predomínio de conjuntos de casas pequenos, e Boa Vista e Jardim Europa, com predomínio de torres com equipamentos" caption="Zona Sul (Tristeza e Camaquã) e Centro-Leste (Boa Vista e Jardim Europa)." >}}
