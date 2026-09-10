# Relatório de modelos e parâmetros

## Configuração comum

- `temperature`: 0.2
- `top_p`: 0.9
- `max_tokens` / `num_predict`: 512
- limite da memória: 1.800 tokens

## Modelos a comparar

### gpt-oss:120b

Modelo principal exigido no enunciado, executado por `ChatOllama`. Registrar aqui
latência média, qualidade, consumo de memória e observações após o eval.

### qwen3:4b-instruct

Modelo menor para comparação e desenvolvimento no Mac Intel. Executar o mesmo eval
com `--model qwen3:4b-instruct` e registrar
os resultados. Não preencher métricas sem executar os modelos.

## Limitação atual

O repositório das Sprints 1 e 2 registra Llama 3 8B, temperature 0.3, top_p 0.9 e
num_predict 512. Os 11 testes foram classificados como adequados, mas sem medição de
tokens e latência. Essas métricas serão geradas novamente sob as mesmas condições.
