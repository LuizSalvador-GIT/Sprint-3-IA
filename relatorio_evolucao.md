# Relatório de evolução — Sprint 03

> Rascunho para conversão em PDF. Limite final: cinco páginas.

## 1. Resumo da evolução

O código das Sprints 1 e 2 foi localizado no repositório público do grupo. A versão
anterior usava Streamlit, SDK do Ollama, Llama 3 8B e histórico manual limitado por
quantidade de mensagens. Na Sprint 03, o núcleo passa a usar LangChain LCEL, memória
por sessão limitada por tokens, saída estruturada Pydantic v2, XML tagging e guardrails.

## 2. Refatoração e decisões técnicas

Descrever a chain `prompt | llm | parser`, a memória limitada por tokens e os trade-offs
observados depois dos testes.

## 3. Comparativo antes/depois

Preencher somente com resultados medidos pelo mesmo eval set:

| Métrica | Sprints 1/2 — versão manual | Sprint 03 — LCEL |
|---|---:|---:|
| Qualidade das respostas | Pendente | Pendente |
| Tokens por turno | Pendente | Pendente |
| Latência média | Pendente | Pendente |
| Acurácia do structured output | Pendente | Pendente |

## 4. Problemas encontrados e soluções

1. O repositório anterior não estava inicialmente disponível; ele foi localizado e usado como fonte verificável da baseline.
2. O modelo obrigatório de 120B não cabe no computador de desenvolvimento com 16 GB; será necessário um servidor Ollama remoto para a execução final.

## 5. Equipe e divisão de trabalho

| Nome | RM | Tarefa principal |
|---|---|---|
| Victor Manzini | 572123 | Preencher atividade na Sprint 03 |
| Guilherme de Oliveira Santos | 572195 | Preencher atividade na Sprint 03 |
| Caio Marinho Pereira | 572873 | Preencher atividade na Sprint 03 |
| Ricardo Tunes | 555919 | Preencher atividade na Sprint 03 |
| Luiz Cesar Conti Salvador | 571305 | Refatoração LangChain e integração |
