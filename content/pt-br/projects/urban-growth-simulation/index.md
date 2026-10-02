---
title: "Simulando o Crescimento Urbano na Região Metropolitana de Porto Alegre"
date: 2026-10-01T10:00:00+00:00
featured: false
categories:
  - "Forma Urbana e Uso do Solo"
  - "Desenvolvimento Regional"
draft: true
summary: "Um modelo de cadeias de Markov e autômatos celulares, treinado com cobertura do solo do MapBiomas de 1985 a 2015 e validado contra 2023, projeta onde a Região Metropolitana de Porto Alegre pode se urbanizar até 2040."
period: "2026"
location: "Região Metropolitana de Porto Alegre, RS"
role: "Autoria única: desenho do modelo, implementação em Python, validação e mapas."
data: ["MapBiomas uso e cobertura da terra (1985–2023)", "Principais vias do OpenStreetMap", "Limites municipais do IBGE"]
tools: ["Python", "Cadeias de Markov", "Autômatos celulares", "Análise espacial"]
---

{{< lead >}}
Onde a Região Metropolitana de Porto Alegre deve se urbanizar nos próximos anos, e até onde um modelo simples e transparente consegue chegar?
{{< /lead >}}

{{< facts >}}

## O desafio

<!-- TODO: 2-3 frases sobre por que projetar na escala metropolitana importa (planejamento, enchentes, habitação) e por que um modelo simples e replicável. -->

## Abordagem

O modelo separa duas perguntas: *quanto* solo vai se urbanizar e *onde*.

{{< flow title="Da cobertura do solo por satélite à projeção para 2040" >}}
{{< step label="Dados" >}}
Cobertura anual do MapBiomas (30 m), reclassificada em 5 classes
{{< /step >}}
{{< step label="Cadeia de Markov" >}}
A matriz de transição 1985–2015 define quanta área urbana nova esperar
{{< /step >}}
{{< step label="Aptidão + autômato" >}}
Distância à área urbana e às vias principais, mais regras de vizinhança, definem onde ela se localiza
{{< /step >}}
{{< step label="Validação" accent="true" >}}
Simula 2015–2023 e compara com o mapa observado de 2023
{{< /step >}}
{{< /flow >}}

A aptidão não usa pesos escolhidos à mão: para cada fator, o modelo mede que parcela das células realmente se urbanizou entre 1985 e 2015 em cada faixa de distância e usa isso como pontuação.

## Validação

<!-- TODO após `mccast validate`: figura de mérito, kappa, acertos/omissões/falsos alarmes e a leitura em linguagem simples. Um modelo de "nenhuma mudança" pontua 0. -->

## Resultados

<!-- TODO após `mccast project`: área urbana em 1985, 2015, 2023 e 2040 (km²), quais municípios/corredores mais crescem, que uso do solo é substituído. -->

## Limitações

- Apenas a expansão urbana é alocada no espaço; as demais classes mudam somente onde o urbano as substitui.
- As vias são a rede atual, aplicada ao passado.
- Ainda sem restrições de áreas protegidas, declividade ou risco de inundação.

## Mapas

<!-- TODO após `mccast export --site-dir ...`:
{{< fig src="/img/projects/urban-growth-simulation/maps_land_cover.png" alt="..." caption="Cobertura do solo em 1985, 2015, 2023 e projeção para 2040." >}}
{{< fig src="/img/projects/urban-growth-simulation/map_validation.png" alt="..." caption="Validação 2015–2023: acertos, omissões e falsos alarmes." >}}
-->
