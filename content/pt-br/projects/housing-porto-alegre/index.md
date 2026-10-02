---
title: "Habitação e Condomínios Fechados em Porto Alegre"
date: 2024-07-11T10:00:00+00:00
featured: true
categories:
  - "Habitação e Desigualdade"
  - "Forma Urbana e Uso do Solo"
draft: false
summary: "Uma base aberta com todos os condomínios fechados de Porto Alegre, classificados em nove tipologias de forma construída, revela como produtos imobiliários para diferentes classes sociais moldam a segregação na metrópole."
period: "2021–2024"
location: "Porto Alegre, RS"
partners: "PROPUR/UFRGS; Observatório das Metrópoles (Núcleo Porto Alegre)"
role: "Autora principal: levantamento e georreferenciamento, construção da tipologia, análise espacial e estatística, mapas e base de dados aberta."
data: ["Imagens Google Earth (2022)", "Censo IBGE 2010 (renda por setor censitário)", "Google Open Buildings", "OpenStreetMap"]
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

- **Nove tipologias** de condomínios fechados, cada uma associada a um segmento social.
- Uma clara **segregação morfológica**: condomínios horizontais de pequena escala (sobrados e casas) predominam na Zona Sul, enquanto torres de alto padrão se concentram na Zona Centro-Leste.
- Comparações detalhadas entre bairros contrastantes: Boa Vista e Jardim Europa, ao norte; Tristeza e Camaquã, ao sul.

## Por que importa

A base transforma um fenômeno muito debatido em algo mensurável. Ela está disponível para técnicos, pesquisadores e jornalistas que queiram estudar habitação, segregação ou dinâmica imobiliária em Porto Alegre.

- [Base de dados aberta no Zenodo](https://doi.org/10.5281/zenodo.17023731)
- [Faccin, Almeida & Campos (2024)](https://www.revistas.usp.br/posfau/article/view/226515): *Morfologia urbana e tipologia de condomínios fechados na metrópole de Porto Alegre–RS*.
- [Lahorgue *et al.* (2022)](https://www.observatoriodasmetropoles.net.br/reforma-urbana-e-direito-a-cidade-porto-alegre/): situação e perspectivas da habitação em Porto Alegre.

**Pesquisas relacionadas sobre produção imobiliária:**

- [Almeida, Faccin & Campos (2025)](https://www.researchgate.net/publication/394435940_Financeirizacao_do_espaco_urbano_e_capitalismo_de_plataforma_producao_imobiliaria_em_Porto_Alegre-RS): studios e apartamentos compactos concebidos como ativos financeiros para renda.
- [Almeida, Morlin Filho & Faccin (2025)](https://editorarealize.com.br/artigo/visualizar/122479): produção imobiliária em Porto Alegre e os agentes envolvidos.

## Mapas

{{< figs cols="2" >}}
{{< fig src="/img/projects/housing-porto-alegre/housing-poa_01.webp" alt="Dois mapas de Porto Alegre: condomínios fechados como pontos sobre bairros coloridos pela quantidade, e gráficos de pizza por bairro com a proporção de condomínios horizontais, verticais baixos e altos" caption="Distribuição dos condomínios fechados por bairro e a proporção de formas horizontais e verticais." >}}
{{< fig src="/img/projects/housing-porto-alegre/housing-poa_02.webp" alt="Dois mapas de Porto Alegre: condomínios coloridos por período de construção, e coloridos pela renda média do setor censitário" caption="Período de construção e renda média do responsável pelo domicílio (Censo 2010)." >}}
{{< /figs >}}

{{< figs cols="2" >}}
{{< fig src="/img/projects/housing-porto-alegre/housing-poa_06.webp" alt="Oito pequenos mapas de Porto Alegre, um por tipologia, mostrando onde cada tipo de condomínio se localiza" caption="Onde está cada tipologia." >}}
{{< fig src="/img/projects/housing-porto-alegre/housing-poa_03.webp" alt="Mapa de Porto Alegre com condomínios fechados em vermelho, condomínios do Minha Casa Minha Vida como círculos amarelos e vias radiais e perimetrais" caption="Condomínios fechados, empreendimentos do MCMV e a estrutura viária principal." >}}
{{< /figs >}}

{{< figs cols="2" >}}
{{< fig src="/img/projects/housing-porto-alegre/housing-poa_04.webp" alt="Três mapas empilhados de Boa Vista e Jardim Europa com os condomínios por tipologia, renda e período de construção" caption="Zona norte: Boa Vista e Jardim Europa." >}}
{{< fig src="/img/projects/housing-porto-alegre/housing-poa_05.webp" alt="Três mapas empilhados de Tristeza e Camaquã com os condomínios por tipologia, renda e período de construção" caption="Zona sul: Tristeza e Camaquã." >}}
{{< /figs >}}
