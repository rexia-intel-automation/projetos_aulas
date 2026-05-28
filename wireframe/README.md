# Protótipo — Assistente CMDPII

Protótipo navegável com o **design system institucional** (cores heráldicas CMDPII/CBMDF).

## Rodar em localhost (porta 3456)

Na pasta `wireframe/`, use o servidor incluído (ele expõe também `/design-system/`):

```bash
python serve.py
```

Abra **http://localhost:3456/index.html**

> `python -m http.server` **nesta pasta** não serve o design system e a landing fica sem layout. Use sempre `serve.py`.

Outra porta:

```bash
python serve.py -p 8080
```

## Design system

Código-fonte em `../design-system/`. Vitrine: suba o mesmo `serve.py` e abra `http://localhost:3456/design-system/showcase.html`.

## Fluxo

`index.html` → chat → resposta / sem resposta / inadequada → config → sobre
