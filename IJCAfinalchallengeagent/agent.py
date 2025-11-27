# https://google.github.io/adk-docs/tools-custom/function-tools/#example
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html

from typing import Optional
import pandas as pd



def get_datatran_csv(
    start_date: Optional[str] = None,
    start_time: Optional[str] = None,
    end_date: Optional[str] = None,
    end_time: Optional[str] = None,
    head: Optional[int] = None,
    query: Optional[str] = None,
    count: Optional[str] = None,
    sum: Optional[str] = None,
    mean: Optional[str] = None,
):
    """
    Carrega e filtra o arquivo 'medallion/silver/datatran.csv', permitindo filtros
    por data, hora, consultas com Pandas e operações de agregação simples.

    O arquivo lido possui as seguintes colunas:

        data,dia_semana,hora,uf,br,km,municipio,causa_acidente,tipo_acidente,
        classificacao_acidente,fase_dia,sentido_via,condicao_metereologica,
        tipo_pista,tracado_via,uso_solo,pessoas,mortos,feridos_leves,
        feridos_graves,ilesos,ignorados,feridos,veiculos,latitude,longitude,
        regional,delegacia,uop, id(adicionado por comodidade)

    Caminho fixo do dataset:
        medallion/silver/datatran.csv

    Args:
        start_date (str, opcional): Filtra linhas com data >= start_date (YYYY-MM-DD).
        start_time (str, opcional): Filtra linhas com hora >= start_time (HH:MM:SS).
        end_date (str, opcional): Filtra linhas com data <= end_date (YYYY-MM-DD).
        end_time (str, opcional): Filtra linhas com hora <= end_time (HH:MM:SS).
        head (int, opcional): Limita o número de linhas retornadas.
        query (str, opcional): Expressão Pandas `.query()` aplicada ao DataFrame.
        count (str, opcional): Nome da coluna para aplicar count().
        sum (str, opcional): Nome da coluna para aplicar sum().
        mean (str, opcional): Nome da coluna para aplicar mean().

    Returns:
        str: CSV contendo dados filtrados ou o resultado da agregação.
    """

    df = pd.read_csv("medallion/silver/datatran.csv")
    df.insert(0, "id", range(1, len(df) + 1))

    if start_date is not None:
        df = df[df["data"] >= start_date]

    if start_time is not None:
        df = df[df["hora"] >= start_time]

    if end_date is not None:
        df = df[df["data"] <= end_date]

    if end_time is not None:
        df = df[df["hora"] <= end_time]

    if query is not None:
        df = df.query(query)

    if head is not None:
        df = df.head(head)

    if count is not None:
        return pd.DataFrame({"count": [df[count].count()]}).to_csv(index=False)

    if sum is not None:
        return pd.DataFrame({"sum": [df[sum].sum()]}).to_csv(index=False)

    if mean is not None:
        return pd.DataFrame({"mean": [df[mean].mean()]}).to_csv(index=False)

    return df.to_csv(index=False)


from google.adk.agents import Agent
from google.adk.tools import FunctionTool


def create_agent_grupo4():
  return Agent(
      name="IJCAfinalchallengeagentgrupo4",
      model="gemini-2.5-flash",
      instruction="""
Você é um agente especializado em análise de dados de acidentes de trânsito utilizando os conjuntos de dados disponibilizados pela Polícia Rodoviária Federal (PRF) do Brasil.
Você possui acesso à ferramenta get_datatran_csv, que permite consultar, filtrar e recuperar dados estruturados sobre acidentes (incluindo datas, horários, localizações, gravidade, veículos e outras variáveis relevantes).
Seu objetivo é responder perguntas com base nesses dados, sempre que possível utilizando a ferramenta para obter informações atualizadas diretamente do dataset.
Quando necessário, você também pode realizar análises estatísticas, sumarizações, comparações, explicações e visualizações conceituais.
Caso uma pergunta exija dados reais do conjunto, sempre chame a tool get_datatran_csv com os parâmetros adequados.
Caso a pergunta seja conceitual ou explicativa, você pode responder diretamente.
      """,
      tools=[get_datatran_csv]
  )

root_agent = create_agent_grupo4()
