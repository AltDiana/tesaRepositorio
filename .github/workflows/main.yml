name: Prueba Python

on:
  workflow_dispatch:

jobs:
  ejecutar-script:
    runs-on: ubuntu-latest

    steps:
      - name: Clonar repositorio
        uses: actions/checkout@v4

      - name: Instalar Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Ejecutar calculadora.py
        run: python calculadora.py
