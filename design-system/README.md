# Design System — Assistente CMDPII

Paleta e componentes tokenizados para o assistente de integração do Colégio Militar Dom Pedro II.

## Origem das cores

As cores de marca seguem as **cores heráldicas do CBMDF/CMDPII**: vermelho, azul ultramar, branco e ouro. Referência: [Heráldica CMDPII (PDF)](https://cmdpii.com.br/wp-content/uploads/2021/06/heraldicadocmdpii.pdf).

| Cor | Significado (heráldica) | Uso na UI |
|-----|-------------------------|-----------|
| Vermelho | Coragem, força | Botões primários, CTAs |
| Azul ultramar | Lealdade, justiça | Header, links, bolha do assistente |
| Branco | Equilíbrio, pureza | Superfícies, texto sobre marca |
| Ouro | Tradição, destaque | Badges, card selecionado (uso parcial) |

## Camadas de tokens

1. **`tokens/primitives.css`** — Valores brutos (hex, rem, px).
2. **`tokens/semantic.css`** — Significado (`--color-bg-page`, `--color-text-primary`).
3. **`tokens/components.css`** — Por componente (`--button-primary-bg`, `--header-bg`).

Estilos visuais ficam em `components.css` (raiz) e usam **apenas** `var(--token)`.

## Como importar

No wireframe (com `serve.py` na pasta `wireframe/`):

```html
<link rel="stylesheet" href="design-system/index.css">
```

Em outros projetos na raiz do repositório:

```html
<link rel="stylesheet" href="design-system/index.css">
```

## Componente → tokens principais

| Componente | Tokens |
|------------|--------|
| `.btn` / `.btn-primary` | `--button-*` |
| `.header` | `--header-*` |
| `.personality` | `--badge-*` |
| `.bubble-user` | `--chat-bubble-user-*` |
| `.bubble-bot` | `--chat-bubble-bot-*` |
| `.input-bar` | `--input-bar-*`, `--input-field-*` |
| `.card` | `--card-*` |
| `.feedback-block` | `--feedback-*` |
| `.disclaimer` | `--disclaimer-*` |

## Regras de uso

- **Vermelho**: ações e CTAs; evite blocos grandes de texto vermelho.
- **Ouro**: detalhes (badge, borda selecionada); não use como fundo dominante.
- **Azul escuro**: header e títulos; garanta texto claro sobre fundo azul.

## Vitrine

Abra `showcase.html` no navegador (via servidor local) para ver paleta e componentes.

Vitrine e protótipo (recomendado — porta 3456):

```bash
cd wireframe
python serve.py
```

- Protótipo: `http://localhost:3456/index.html`
- Showcase: `http://localhost:3456/design-system/showcase.html`

No Windows, dê duplo clique em `wireframe/iniciar.bat`.

## Protótipo

O wireframe em `../wireframe/` importa este design system e mantém a mesma navegação entre telas. Use sempre `wireframe/serve.py`; `python -m http.server` só na pasta `wireframe` **não** carrega o CSS.
