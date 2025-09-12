# Controle de Scripts de Sistemas Embarcados

Pequeno projeto com frontend e backend para listar e executar scripts Python didáticos sobre sistemas embarcados.

Estrutura:
- `app.py` - servidor Flask que lista e executa scripts em `scripts/`
- `index.html` - frontend que consome `/scripts` e `/run`
- `scripts/` - 10 scripts de exemplo
- `requirements.txt` - dependências

Como usar (Windows cmd):

1. Criar um ambiente virtual (opcional, recomendado):

```cmd
python -m venv .venv
.\.venv\Scripts\activate
```

2. Instalar dependências:

```cmd
pip install -r requirements.txt
```

3. Rodar o servidor:

```cmd
python app.py
```

4. Abrir `http://127.0.0.1:5000/` no navegador e executar scripts.

Segurança: O servidor só executa arquivos `.py` dentro da pasta `scripts/` e usa um timeout de 10s.
