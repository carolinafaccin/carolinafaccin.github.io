---
title: "Financeirização da Moradia em Porto Alegre"
date: 2026-10-14T10:00:00+00:00
categories:
  - "Habitação e Desigualdade"
draft: false
summary: "Studios e apartamentos compactos vendidos como investimento, domicílios vazios e população em queda: um olhar reprodutível sobre a produção imobiliária de Porto Alegre de 2007 a 2024."
period: "2024–atual"
location: "Porto Alegre, RS"
partners: "PROPUR/UFRGS; Nicole Leal de Almeida (autora principal); Heleniza Ávila Campos"
role: "Coautora: organização dos dados, análise espacial e mapas; pipeline reprodutível que refaz as figuras do artigo a partir dos dados originais e do Censo."
data: ["Censo do Mercado Imobiliário (2007–2018) e Panorama do Mercado Imobiliário (set. 2024), Sinduscon-RS", "Censos IBGE 2000, 2010 e 2022 e CNEFE (2010, 2022)", "Sites das incorporadoras (Melnick, Cyrela Goldsztein)", "Anúncios do ZAP Imóveis (out. 2026)"]
tools: ["Python", "GeoPandas", "QGIS", "Dados censitários"]
---

{{< lead >}}
Para quem se constrói moradia em Porto Alegre, se a cidade continua ganhando domicílios enquanto perde moradores?
{{< /lead >}}

{{< facts >}}

## O desafio

Desde 2020 as incorporadoras de Porto Alegre lançam studios e apartamentos compactos anunciados como investimento: unidades para alugar em plataformas de curta temporada, vendidas em frações ou administradas por proptechs. Ao mesmo tempo, o Censo 2022 encontrou uma cidade com menos moradores do que em 2010 e quase um domicílio em cada cinco vazio. Relacionar as duas coisas exige juntar dados que estão espalhados entre o sindicato da construção, os sites das incorporadoras e o Censo, e que raramente usam a mesma geografia.

## Abordagem

O artigo de [Almeida, Faccin e Campos (2025)](http://dx.doi.org/10.1590/2236-9996.2025-6469490-pt) combinou essas fontes com uma leitura qualitativa das estratégias das incorporadoras. Depois, refiz as figuras do artigo em um pipeline em Python que lê os dados originais, liga cada contagem aos bairros da lei de 2016 e confere cada número do texto com a sua fonte.

{{< flow title="De fontes dispersas a bairros comparáveis" >}}
{{< step label="Lançamentos" >}}
Unidades e empreendimentos lançados por ano, tipologia e bairro (Sinduscon-RS, 2007–2018)
{{< /step >}}
{{< step label="Domicílios" >}}
Todos os endereços de domicílios particulares dos Censos 2010 e 2022 (CNEFE), ocupados ou não
{{< /step >}}
{{< step label="Incorporadoras" >}}
Empreendimentos compactos da Melnick e da Cyrela Goldsztein (2020–2024), com a localização conferida
{{< /step >}}
{{< step label="Preços" >}}
Mediana do preço anunciado por m² por bairro (ZAP Imóveis)
{{< /step >}}
{{< step label="Resultados" accent="true" >}}
Artigo revisado por pares e figuras reprodutíveis
{{< /step >}}
{{< /flow >}}

## Resultados

- **Menos empreendimentos, e maiores.** De 2007 a 2015 foram lançadas 59.872 unidades em 3.305 empreendimentos. As unidades chegaram ao pico de 8.423 em 2012, enquanto o número de empreendimentos caiu de 452 em 2007 para 321 em 2015: o empreendimento médio passou de 12 para 20 unidades.
- **A virada para as unidades pequenas.** Entre 2016 e 2018 os lançamentos de um dormitório cresceram 65% e os de JK mais que triplicaram, enquanto os de três dormitórios caíram 12%. Nos doze meses até setembro de 2024, os studios foram 42% das 2.761 unidades verticais lançadas, mas só 19% do valor de vendas; os de três dormitórios foram 27% das unidades e 51% do valor.
- **Mais domicílios, menos gente.** Entre 2010 e 2022 Porto Alegre ganhou 112.807 domicílios particulares e perdeu 76.506 moradores (−5,4%). Os domicílios não ocupados, vagos ou de uso ocasional, praticamente dobraram, de 65.226 (11% do estoque) para 128.239 (19%). O crescimento foi maior na periferia (Restinga, Mário Quintana, Lomba do Pinheiro); o percentual de domicílios vazios é maior no centro (Centro Histórico, 30%).
- **Unidades de investimento no centro mais valorizado.** Os 17 empreendimentos compactos que a Melnick e a Cyrela Goldsztein lançaram de 2020 a 2024 (4.107 unidades) estão todos em 11 bairros centrais e do centro-leste, do Rio Branco e Petrópolis à Cidade Baixa, onde o preço anunciado por m² é mais alto. A linha GO da Melnick tem em média 48 m² por unidade; os compactos da Cyrela, 34 m². O Vista Praia de Belas, com 419 unidades de 18 a 21 m², foi vendido em 14 dias em 2024, num bairro inundado em maio daquele ano.

## Por que importa

A produção de moradia em Porto Alegre responde mais a investidores em busca de renda de aluguel do que às famílias que precisam de casa. As unidades compactas se concentram onde a terra é mais valorizada, enquanto o estoque de domicílios vazios cresce e a habitação de menor renda é empurrada para as bordas. O pipeline reprodutível permite atualizar esses números a cada novo Censo ou relatório de mercado.

Este projeto continua a pesquisa sobre produção imobiliária de [Condomínios Fechados em Porto Alegre]({{< ref "/projects/housing-poa" >}}). Está em andamento um capítulo de livro sobre as unidades compactas de investimento e a inundação de maio de 2024 (Almeida e Faccin, 2027); o código será publicado com ele.

- [Almeida, Faccin e Campos (2025)](http://dx.doi.org/10.1590/2236-9996.2025-6469490-pt): *Financeirização do espaço urbano e capitalismo de plataforma: produção imobiliária em Porto Alegre-RS*, Cadernos Metrópole 27(64).
- [Almeida, Morlin Filho e Faccin (2025)](https://editorarealize.com.br/artigo/visualizar/122479): produção imobiliária em Porto Alegre e os agentes envolvidos.

## Figuras

Refeitas com os dados do artigo e do Censo. As contagens de domicílios usam todos os endereços dos dois Censos e a localização dos empreendimentos foi conferida um a um, por isso alguns valores diferem um pouco das figuras publicadas.

{{< fig src="/img/projects/financialization-poa/a25_graficos_1_3_lancamentos.webp" alt="Quatro gráficos dos lançamentos residenciais em Porto Alegre: unidades por ano de 2007 a 2015, com pico de cerca de 8.400 em 2012; empreendimentos caindo de cerca de 450 para 320; unidades de 2 e 3 dormitórios com pico em 2012 e 2013; e unidades de 1 dormitório subindo forte de 2016 a 2018" caption="Lançamentos residenciais, 2007–2018 (Gráficos 1 a 3 do artigo)." >}}

{{< fig src="/img/projects/financialization-poa/a25_figura_1_lancamentos_bairros.webp" alt="Dois mapas dos bairros de Porto Alegre: unidades lançadas de 2007 a 2015, mais escuro no Sarandi, ao norte, e em Petrópolis, no centro-leste, e empreendimentos lançados, mais escuro em Petrópolis, quase nada no sul" caption="Unidades e empreendimentos lançados por bairro, 2007–2015 (Figura 1)." >}}

{{< fig src="/img/projects/financialization-poa/a25_figura_2_nao_ocupados_crescimento.webp" alt="Dois mapas dos bairros de Porto Alegre: percentual de domicílios não ocupados em 2022, maior no Centro Histórico, Praia de Belas e Floresta, e crescimento dos domicílios particulares de 2010 a 2022, maior na Restinga, Lomba do Pinheiro e Mário Quintana, na periferia, com alguns bairros perdendo domicílios" caption="Domicílios não ocupados (2022) e crescimento dos domicílios (2010–2022) por bairro (Figura 2)." >}}

{{< fig src="/img/projects/financialization-poa/a25_figura_3_preco_studios.webp" alt="Dois mapas dos bairros de Porto Alegre: mediana do preço anunciado por metro quadrado dos apartamentos à venda, maior no centro-leste, e número de empreendimentos de studios e 1 dormitório da Melnick e da Cyrela Goldsztein de 2020 a 2024, todos num conjunto de bairros centrais e do centro-leste" caption="Preço do m² (out. 2026) e empreendimentos compactos da Melnick e da Cyrela Goldsztein, 2020–2024 (Figura 3)." >}}
