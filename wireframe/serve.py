#!/usr/bin/env python3
"""
Servidor para o protótipo: arquivos em wireframe/ na raiz da URL
e design-system/ disponível em /design-system/ (pasta irmã no disco).

Uso: python serve.py
      http://localhost:3456/index.html
"""
from __future__ import annotations

import argparse
import http.server
import socketserver
from pathlib import Path

WIREFRAME_DIR = Path(__file__).resolve().parent
DESIGN_SYSTEM_DIR = WIREFRAME_DIR.parent / "design-system"
DEFAULT_PORT = 3456


class WireframeHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(WIREFRAME_DIR), **kwargs)

    def do_GET(self) -> None:
        path = self.path.split("?", 1)[0].split("#", 1)[0]
        if path in ("", "/"):
            self.send_response(302)
            self.send_header("Location", "/index.html")
            self.end_headers()
            return
        super().do_GET()

    def translate_path(self, path: str) -> str:
        path = path.split("?", 1)[0].split("#", 1)[0]
        if path.startswith("/design-system/"):
            rel = path[len("/design-system/") :].lstrip("/")
            if rel:
                target = DESIGN_SYSTEM_DIR.joinpath(*rel.split("/"))
                if target.is_file():
                    return str(target)
        return super().translate_path(path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Serve wireframe em localhost")
    parser.add_argument("-p", "--port", type=int, default=DEFAULT_PORT)
    args = parser.parse_args()

    if not DESIGN_SYSTEM_DIR.is_dir():
        raise SystemExit(f"Design system não encontrado: {DESIGN_SYSTEM_DIR}")

    socketserver.TCPServer.allow_reuse_address = True
    try:
        httpd = socketserver.TCPServer(("", args.port), WireframeHandler)
    except OSError as err:
        raise SystemExit(
            f"Porta {args.port} em uso. Encerre outros servidores "
            f"(ex.: python -m http.server {args.port}) e tente de novo.\n{err}"
        ) from err

    with httpd:
        print(f"Protótipo:  http://localhost:{args.port}/index.html")
        print(f"Showcase:   http://localhost:{args.port}/design-system/showcase.html")
        print("Ctrl+C para encerrar")
        httpd.serve_forever()


if __name__ == "__main__":
    main()
