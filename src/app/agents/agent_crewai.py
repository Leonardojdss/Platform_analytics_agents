from crewai import Agent, Task

def create_crew_agents():
    cientista_de_dados = Agent(
        role="cientista de dados",
        goal="Realizar uma análise dos dados fornecido pelo agente do langchain",
        backstory=(
            "Você é um Analista de Dados experiente, especializado em coletar, \
            processar e analisar grandes volumes de dados para extrair insights\
            valiosos. Sua comunicação é clara, objetiva e baseada em fatos.\
            Você utiliza ferramentas e técnicas avançadas de análise de dados para\
            apoiar a tomada de decisões estratégicas. "
        ),
        allow_delegation=False,
        verbose=True,
        llm="azure/gpt-4o-mini"
        )

    analista_de_geracao_recomendacoes = Agent(
        role="Analista de Geração de Recomendações",
        goal="Fornecer recomendações com base em análises de dados, otimizando estratégias de venda, marketing e atendimento ao cliente.",
        backstory=(
            "Este agente é responsável por transformar dados complexos em recomendações acionáveis, "
            "focando no aumento da eficiência dos serviços e na melhoria da experiência dos clientes. "
            "Ele colabora diretamente com cientistas de dados para interpretar modelos preditivos e fornecer recomendações estratégicas."
        ),
        allow_delegation=False,
        verbose=True,
        llm="azure/gpt-4o"
        )

    # revisao_de_texto = Agent(
    #     role="Analista de Geração de Texto em Markdown",
    #     goal="Transformar as recomendações e análises técnicas em relatórios claros e organizados, formatados em Markdown para fácil compartilhamento.",
    #     backstory=(
    #         "Este agente é especializado em redigir e revisar documentos técnicos e relatórios estratégicos "
    #         "em linguagem Markdown. Ele é responsável por traduzir dados técnicos e recomendações em um formato acessível, "
    #         "garantindo que as informações sejam bem estruturadas e fáceis de entender para tomadores de decisão."
    #     ),
    #     allow_delegation=False,
    #     verbose=True,
    #     llm=llm_openai_gpt4o
    # )

    return [cientista_de_dados, analista_de_geracao_recomendacoes]

def create_crew_tasks(output, agents):
    tarefa_cientista_de_dados = Task(
        description=(f"1. Analisar o retorno da query do agente da langChain, Realizar uma análise como um cientista de dados,\
                     segue retorno\n: {output}"),
        expected_output=("Análise detalhada do retorno da query do agente da langChain"),
        agent=agents[0]
    )

    tarefa_de_recomendacoes = Task(
        description=(
            "Receber a análise prescritiva ou descritiva do cientista de dados sobre os dados analisados"
        ),
        expected_output=(
            "Relatório contendo recomendações estratégicas sobre os dados analisados, Texto precisa estar formatado com markdown"
        ),
        agent=agents[1]
    )

    # tarefa_revisao_de_texto = Task(
    #     description=(
    #         "Receber as recomendações geradas pelo Analista de Geração de Recomendações e transformá-las em um relatório em markdown."
    #         "estruturado em Markdown, garantindo clareza e precisão nas informações apresentadas."
    #     ),
    #     expected_output=(
    #         "Documento em Markdown contendo as recomendações bem organizadas, com seções claras e objetivas, "
    #         "de forma sucinta e objetiva."
    #     ),
    #     agent=agents[2]
    # )

    return [tarefa_cientista_de_dados, tarefa_de_recomendacoes]