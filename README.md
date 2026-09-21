# carolinafaccin.github.io

Site profissional da Carolina Faccin — portfólio de projetos em análise
geoespacial e planejamento urbano. Site estático construído com
[Hugo](https://gohugo.io/) e o tema [Blowfish](https://blowfish.page/),
publicado no GitHub Pages.

🔗 **https://carolinafaccin.github.io**

Bilíngue: inglês (padrão) e português do Brasil.

## Requisitos

- [Hugo extended](https://gohugo.io/installation/) **v0.161.1 ou superior**
  (a versão *extended* é obrigatória)
- Git

## Rodando localmente

```bash
git clone --recurse-submodules --shallow-submodules https://github.com/carolinafaccin/carolinafaccin.github.io.git
cd carolinafaccin.github.io

hugo server -D    # http://localhost:1313 com live reload
```

O tema Blowfish é um submódulo Git — sem ele o build não funciona.
`--shallow-submodules` baixa só o commit atual do tema, não o histórico
inteiro dele (economiza uns 500 MB).

Se clonar pela interface do VSCode (ou qualquer outro jeito que não seja o
comando acima), os submódulos não vêm junto. Rode depois:

```bash
git submodule update --init --depth 1
```

### Recriando o ambiente Python (scripts de migração, opcional)

Só necessário se for usar os scripts de migração do WordPress (histórico do
repo). Não é preciso para rodar o site:

```bash
python3 -m venv venv
venv/bin/pip install -r requirements.txt
```

## Estrutura

```bash
config/_default/   configuração do Hugo (dividida em vários .toml)
content/en/        conteúdo em inglês
content/pt-br/     conteúdo em português
layouts/           overrides de templates do tema
assets/            CSS custom, esquema de cores "carolina", imagens
static/            arquivos servidos como estão (favicon etc.)
themes/blowfish/   tema (submódulo Git)
```

As duas árvores de idioma (`content/en/` e `content/pt-br/`) são espelhadas —
ao adicionar uma página, crie a versão nos dois idiomas.

## Adicionando um projeto

Cada projeto é um *page bundle* com a página em Markdown e a imagem de capa:

```bash
hugo new content/en/projects/meu-projeto/index.md
# crie também content/pt-br/projects/meu-projeto/index.md
# adicione a capa feature.png em cada pasta
```

No *front matter*, use `categories` (alimenta o filtro de categorias) e
`summary` (resumo exibido nos cards).

## Deploy

Automático: qualquer `push` na branch `main` dispara o workflow
[`.github/workflows/deploy.yml`](.github/workflows/deploy.yml), que compila o
site com `hugo --minify` e publica no GitHub Pages. Não há passo manual.

## Mais detalhes

Veja [CLAUDE.md](CLAUDE.md) para a arquitetura completa do projeto.
