#!/usr/bin/env python3
import psycopg2

DATABASE = "news"

# Um - Quais sao os tres artigos mais populares de todos os tempos?
query_t1 = ("Quais sao os tres artigos mais populares de todos os tempos?")
query_1 = (
    "select articles.title, count(*) as v "
    "from articles inner join log on log.path "
    "like concat('%', articles.slug, '%') "
    "where log.status like '%200%' group by "
    "articles.title, log.path order by v desc limit 3")

# Dois - Quem sao os autores de artigos mais populares de todos os tempos
query_t2 = ("Autores de artigos mais populares de todos os tempos?")
query_2 = (
    "select authors.name, count(*) as v from articles inner "
    "join authors on articles.author = authors.id inner join log "
    "on log.path like concat('%', articles.slug, '%') where "
    "log.status like '%200%' group "
    "by authors.name order by v desc")

# Tres - Em quais dias mais de 1% das requisicoes resultaram em erros?
query_t3 = ("Em quais dias mais de 1% das requisicoes resultaram em erros?")
query_3 = (
    "select day, perc from ("
    "select day, round((sum(requests)/(select count(*) from log where "
    "substring(cast(log.time as text), 0, 11) = day) * 100), 2) as "
    "perc from (select substring(cast(log.time as text), 0, 11) as day, "
    "count(*) as requests from log where status like '%404%' group by day)"
    "as log_percentage group by day order by perc desc) as final_query "
    "where perc >= 1")


def get_results(query):
    # Receber a query
    db = psycopg2.connect(database=DATABASE)
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()
    db.close()


def print_results(query_results):
    print(query_results[1])
    for index, results in enumerate(query_results[0]):
        print(
            "Resultado", index+1, results[0],
            str(results[1]), "visualizacoes")


def print_results_erro(query_results):
    print(query_results[1])
    for results in query_results[0]:
        print("Data", results[0], "Porcentagem", str(results[1]) + "% erros")


if __name__ == '__main__':
    # Guardar resultados das querys
    result_popular = get_results(query_1), query_t1
    result_autor = get_results(query_2), query_t2
    result_erro = get_results(query_3), query_t3

    # Imprimir query
    print_results(result_popular)
    print_results(result_autor)
    print_results_erro(result_erro)
