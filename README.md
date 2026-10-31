# Lab — Build Automatizado e Integração Contínua

Laboratório prático da disciplina **Integração Contínua de Software** (Engenharia de Software — 7º período, UniEVANGÉLICA).

Demonstra um pipeline de CI com **GitHub Actions** que executa build e testes automatizados a cada `push` ou `pull request` na branch `main`.

## Estrutura

```
lab-build-automatizado/
├── .github/
│   └── workflows/
│       └── build.yml      # pipeline de CI
├── app.py                 # aplicação (soma e subtrai)
├── test_app.py            # suíte de testes (unittest)
├── .gitignore
└── README.md
```

## Rodando os testes localmente

```bash
python -m unittest test_app.py
```

Saída esperada: `OK` — indicando que o build local passou.

## Pipeline

O workflow `Python CI` é disparado por:

- `push` na branch `main`
- `pull_request` com destino à branch `main`

Etapas: checkout do código → configuração do Python 3.x → atualização do pip → execução da suíte de testes.

Se qualquer teste falhar, o `unittest` retorna código de saída diferente de zero e o GitHub Actions marca a execução como falha, sinalizando o **build quebrado**.
