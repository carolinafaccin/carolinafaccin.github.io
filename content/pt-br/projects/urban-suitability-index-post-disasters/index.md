---
title: "Índice de Aptidão Urbana Pós-Desastres"
date: 2025-07-08T09:00:00+00:00
featured: 1
categories:
  - "Clima e Ambiente"
draft: false
summary: "Depois das enchentes de 2023–2024, onde sete cidades devastadas do Vale do Taquari podem se reconstruir com segurança? Um modelo multicritério de aptidão que transformou mapas de risco em diretrizes de ocupação prioritária para o Governo do Estado."
period: "2024–2025"
location: "Vale do Taquari, RS: Arroio do Meio, Colinas, Cruzeiro do Sul, Encantado, Estrela, Muçum e Roca Sales"
partners: "SEDUR/RS (Secretaria de Desenvolvimento Urbano e Metropolitano), Univates, prefeituras municipais"
role: "Analista geoespacial da equipe de georreferenciamento: processamento de dados espaciais, modelagem multicritério de aptidão e produção de mapas para os relatórios municipais."
data: ["MapBiomas (2022)", "Áreas urbanizadas IBGE (2019)", "Base cartográfica FEPAM/SEMA", "Modelo de terreno ANADEM", "Cicatrizes de movimentos de massa UFRGS (maio 2024)", "Dados hidráulicos IPH/UFRGS"]
tools: ["QGIS", "Python", "Análise multicritério", "Álgebra de mapas raster (10 m)"]
---

{{< lead >}}
Como definir onde reconstruir depois de um desastre, de forma segura, rápida e com baixo custo?
{{< /lead >}}

{{< facts >}}

## O desafio

As enchentes de setembro e novembro de 2023 e de maio de 2024 arrasaram bairros inteiros no Vale do Taquari. Em Muçum, **79% da população** foi atingida; em Roca Sales, 55%; em Arroio do Meio e Colinas, quase metade. Em Cruzeiro do Sul, 600 das 850 casas do bairro Passo de Estrela foram destruídas.

Famílias precisavam ser reassentadas, e os municípios precisavam de respostas rápidas: quais áreas são seguras, quais já têm infraestrutura e onde priorizar novas moradias, equipamentos públicos e serviços? O Governo do Estado contratou um estudo técnico para apoiar essas decisões enquanto os planos diretores eram revisados.

## Abordagem

Combinamos o zoneamento de risco de cada município (inundação, zonas de arraste e suscetibilidade a movimentos de massa) com um **modelo multicritério de aptidão**. Cada célula de 10 m do território recebeu uma nota de 1 a 100 indicando o quanto é adequada para nova ocupação urbana.

{{< flow title="Como funciona o índice de aptidão" >}}
{{< step label="Restrições" >}}
- Áreas de Preservação Permanente (Código Florestal)
- Zonas de risco: alto (0,1), médio (0,4), baixo (0,8), sem risco (1)
{{< /step >}}
{{< step label="Fatores" >}}
- Uso do solo: urbano 100, agropecuária 80, natural 40
- Distância à sede urbana (faixas de 1 km)
- Distância a rodovias (faixas de 250 m)
- Declividade: acima de 30% excluída por lei
{{< /step >}}
{{< step label="Álgebra de mapas" >}}
Média ponderada dos quatro fatores × restrição de risco → superfície de aptidão (muito baixa a alta)
{{< /step >}}
{{< step label="Diretrizes" accent="true" >}}
Sobreposição com projetos em andamento, tendências de crescimento e contribuições dos técnicos municipais → áreas de ocupação prioritária
{{< /step >}}
{{< /flow >}}

A lógica de pesos favorece o **crescimento compacto**: áreas já urbanizadas ou próximas da infraestrutura existente recebem notas maiores, a vegetação nativa é protegida e declividades acima de 30% são excluídas, conforme a Lei de Parcelamento do Solo (Lei 6.766/79).

## Resultados

- Um mapa de aptidão para cada um dos sete municípios, com quatro níveis (muito baixa, baixa, média, alta) e áreas não aptas à urbanização.
- **Diretrizes preliminares de ocupação prioritária** para habitação, equipamentos públicos, comércio e serviços, discutidas com o grupo de apoio de cada prefeitura.
- Recomendações para áreas já consolidadas em zonas de alto e médio risco: planos de contingência, monitoramento contínuo, melhorias de drenagem e engajamento da comunidade.

## Impacto

O estudo deu aos municípios uma **ferramenta emergencial de apoio à decisão** durante a reconstrução e uma base técnica para os novos planos diretores. Todos os mapas foram publicados na infraestrutura de dados espaciais do Estado, para que técnicos e população possam explorá-los de forma interativa.

Um artigo científico sobre o método será publicado em breve.

## Mapas

{{< figs cols="2" >}}
{{< fig src="/img/projects/urban-suitability-index-post-disasters/urban-suitability_01.webp" alt="Mapas de localização com os sete municípios estudados destacados em cinza escuro no Vale do Taquari, no Rio Grande do Sul e na bacia Taquari-Antas" caption="Área de estudo: sete municípios do Vale do Taquari." >}}
{{< fig src="/img/projects/urban-suitability-index-post-disasters/urban-suitability_02.webp" alt="Mapa regional de aptidão à urbanização, com grandes áreas em vermelho e laranja nas encostas íngremes e áreas verdes e amarelas em terrenos planos próximos às cidades" caption="Aptidão à urbanização na área de estudo, de não apta (vermelho) a alta (verde)." >}}
{{< /figs >}}

{{< fig src="/img/projects/urban-suitability-index-post-disasters/urban-suitability_06.webp" alt="Seis pequenos mapas de Muçum em tons de rosa e roxo, um para cada camada de entrada: uso do solo, distância à sede, distância a rodovias, declividade, suscetibilidade a inundação e a movimentos de massa" caption="As seis camadas de entrada para Muçum, cada uma convertida para uma escala comum de aptidão." >}}

{{< figs cols="2" >}}
{{< fig src="/img/projects/urban-suitability-index-post-disasters/urban-suitability_07.webp" alt="Mapa de aptidão de Muçum em roxo e laranja, com áreas de alta aptidão em laranja nas encostas mais suaves e áreas não aptas ao longo do Rio Taquari" caption="Muçum: aptidão à urbanização em quatro classes." >}}
{{< fig src="/img/projects/urban-suitability-index-post-disasters/urban-suitability_08.webp" alt="Detalhe da área urbana de Muçum sobre imagem de satélite, com áreas de alta aptidão contornadas em laranja e de baixa aptidão em roxo" caption="Muçum: detalhe das áreas de alta aptidão em torno da sede." >}}
{{< /figs >}}

## Relatórios

Relatórios técnicos entregues à [SEDUR](https://www.sedur.rs.gov.br/cidades). Explore os [mapas interativos](https://iede.rs.gov.br/portal/apps/webappviewer/index.html?id=34e8fb12b1284b9f88685f561f2c1e0b) no portal de dados espaciais do Estado.

**1. Zoneamento de risco** — suscetibilidade a inundação e a movimentos de massa, zonas de arraste:
[Arroio do Meio](/pdf/projects/urban-suitability-index-post-disasters/1a-zoneamento-de-risco-arroio-do-meio.pdf) ·
[Colinas](/pdf/projects/urban-suitability-index-post-disasters/1a-zoneamento-de-risco-colinas.pdf) ·
[Cruzeiro do Sul](/pdf/projects/urban-suitability-index-post-disasters/1a-zoneamento-de-risco-cruzeiro-do-sul.pdf) ·
[Encantado](/pdf/projects/urban-suitability-index-post-disasters/1a-zoneamento-de-risco-encantado.pdf) ·
[Estrela](/pdf/projects/urban-suitability-index-post-disasters/1a-zoneamento-de-risco-estrela.pdf) ·
[Muçum](/pdf/projects/urban-suitability-index-post-disasters/1a-zoneamento-de-risco-mucum.pdf) ·
[Roca Sales](/pdf/projects/urban-suitability-index-post-disasters/1a-zoneamento-de-risco-roca-sales.pdf)

{{< figs cols="3" >}}
{{< fig src="/img/projects/urban-suitability-index-post-disasters/urban-suitability_03.webp" alt="Mapa de zoneamento de risco de Arroio do Meio com alto risco em vermelho ao longo dos rios e encostas, médio em laranja, baixo em verde e sem risco em amarelo" caption="Arroio do Meio: zoneamento de risco." >}}
{{< fig src="/img/projects/urban-suitability-index-post-disasters/urban-suitability_04.webp" alt="Mapa de Arroio do Meio com áreas suscetíveis a inundação em laranja claro ao longo dos rios Taquari e Forqueta e a área urbana atingida em laranja escuro" caption="Arroio do Meio: suscetibilidade a inundação e áreas urbanas atingidas em 2024." >}}
{{< fig src="/img/projects/urban-suitability-index-post-disasters/urban-suitability_05.webp" alt="Detalhe da área central de Arroio do Meio sobre imagem de satélite, com classes de risco e pontos de referência numerados como a prefeitura e a ponte de ferro" caption="Arroio do Meio: classes de risco na sede urbana." >}}
{{< /figs >}}

**2. Diretrizes preliminares de ocupação prioritária:**
[Arroio do Meio](/pdf/projects/urban-suitability-index-post-disasters/1b-diretrizes-preliminares-de-ocupacao-prioritaria-arroio-do-meio.pdf) ·
[Colinas](/pdf/projects/urban-suitability-index-post-disasters/1b-diretrizes-preliminares-de-ocupacao-prioritaria-colinas.pdf) ·
[Cruzeiro do Sul](/pdf/projects/urban-suitability-index-post-disasters/1b-diretrizes-preliminares-de-ocupacao-prioritaria-cruzeiro-do-sul.pdf) ·
[Encantado](/pdf/projects/urban-suitability-index-post-disasters/1b-diretrizes-preliminares-de-ocupacao-prioritaria-encantado.pdf) ·
[Estrela](/pdf/projects/urban-suitability-index-post-disasters/1b-diretrizes-preliminares-de-ocupacao-prioritaria-estrela.pdf) ·
[Muçum](/pdf/projects/urban-suitability-index-post-disasters/1b-diretrizes-preliminares-de-ocupacao-prioritaria-mucum.pdf) ·
[Roca Sales](/pdf/projects/urban-suitability-index-post-disasters/1b-diretrizes-preliminares-de-ocupacao-prioritaria-roca-sales.pdf)

**3. Diagnóstico e leitura técnica** — aspectos físicos, sociais, econômicos, infraestrutura, mobilidade e legislação:
[Arroio do Meio](/pdf/projects/urban-suitability-index-post-disasters/2b-1-diagnostico-tecnico-e-leitura-tecnica-arroio-do-meio.pdf) ·
[Colinas](/pdf/projects/urban-suitability-index-post-disasters/2b-1-diagnostico-tecnico-e-leitura-tecnica-colinas.pdf) ·
[Cruzeiro do Sul](/pdf/projects/urban-suitability-index-post-disasters/2b-1-diagnostico-tecnico-e-leitura-tecnica-cruzeiro-do-sul.pdf) ·
[Encantado](/pdf/projects/urban-suitability-index-post-disasters/2b-1-diagnostico-tecnico-e-leitura-tecnica-encantado.pdf) ·
[Estrela](/pdf/projects/urban-suitability-index-post-disasters/2b-1-diagnostico-tecnico-e-leitura-tecnica-estrela.pdf) ·
[Muçum](/pdf/projects/urban-suitability-index-post-disasters/2b-1-diagnostico-tecnico-e-leitura-tecnica-mucum.pdf) ·
[Roca Sales](/pdf/projects/urban-suitability-index-post-disasters/2b-1-diagnostico-tecnico-e-leitura-tecnica-roca-sales.pdf)

{{< figs cols="3" >}}
{{< fig src="/img/projects/urban-suitability-index-post-disasters/urban-suitability_09.webp" alt="Mapa de uso rural de Roca Sales com soja, lavouras temporárias, pastagem e silvicultura em cores diferentes" caption="Roca Sales: produção rural (MapBiomas 2023)." >}}
{{< fig src="/img/projects/urban-suitability-index-post-disasters/urban-suitability_10.webp" alt="Mapa da área urbana de Roca Sales com a evolução urbana em 2004, 2014 e 2024 em amarelo, laranja e vermelho, zonas de alto risco e loteamentos numerados" caption="Roca Sales: evolução urbana 2004–2024 e novos loteamentos." >}}
{{< fig src="/img/projects/urban-suitability-index-post-disasters/urban-suitability_11.webp" alt="Mapa coroplético dos setores censitários de Roca Sales em tons de azul com o percentual de domicílios abastecidos por poço, mais escuro no centro rural do município" caption="Roca Sales: domicílios abastecidos por poço (Censo 2022)." >}}
{{< /figs >}}
