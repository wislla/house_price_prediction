# Previsão de Preços de Imóveis

Este projeto é uma solução completa para a previsão de preços de imóveis, abrangendo desde a coleta de dados até a disponibilização de um modelo preditivo via uma API. O projeto é dividido em várias partes principais: coleta de dados, análise exploratória, treinamento de modelos e implementação de uma API.

## Estrutura do Projeto

A estrutura do projeto é a seguinte:
```
├── src/
│ ├── init.py
│ ├── data/
│ │ ├── init.py
│ │ └── load_data.py
│ ├── features/
│ │ ├── init.py
│ │ └── build_features.py
│ ├── models/
│ │ ├── init.py
│ │ └── train_model.py
│ ├── utils/
│ │ ├── init.py
│ │ └── helpers.py
│ └── app.py
├── data/
│ └── (diretório para armazenar dados baixados)
├── model/
│ └── linear_regression.pkl (modelo treinado)
├── requirements.txt
├── .gitignore
└── README.md
```

## Funcionalidades

1. **Coleta de Dados:**
   - Utiliza a API do Kaggle para baixar conjuntos de dados de imóveis.

2. **Análise Exploratória de Dados:**
   - Processa e analisa os dados para entender melhor as características e a distribuição dos dados.

3. **Treinamento de Modelos:**
   - Treina um modelo de regressão linear para prever os preços dos imóveis usando o Scikit-learn.

4. **API Flask:**
   - Implementa uma API RESTful usando Flask para disponibilizar o modelo preditivo. A API aceita dados em formato JSON e retorna as previsões dos preços dos imóveis.

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu_usuario/previsao_precos_imoveis.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd previsao_precos_imoveis
    ```

3. Crie e ative um ambiente virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

4. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. **Coletar Dados:**

    Execute o script `data_collection.py` para baixar os dados:

    ```bash
    python src/data/data_collection.py
    ```

2. **Treinar o Modelo:**

    Execute o script `train_model.py` para treinar o modelo e salvar o modelo treinado:

    ```bash
    python src/models/train_model.py
    ```

3. **Executar a API:**

    Inicie o servidor Flask para disponibilizar a API:

    ```bash
    python src/app.py
    ```

4. **Fazer Previsões:**

    Envie uma solicitação POST para `http://127.0.0.1:5000/predict` com um payload JSON contendo os dados dos imóveis para obter as previsões.

    Exemplo de payload JSON:

    ```json
    [
        {"feature1": value1, "feature2": value2, ...},
        {"feature1": value1, "feature2": value2, ...}
    ]
    ```

## Contribuições

Contribuições são bem-vindas! Se você tiver sugestões ou melhorias, sinta-se à vontade para abrir uma issue ou um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).