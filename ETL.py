import pandas as pd
import pandera as pa

## Validações: ##

if __name__ == '__main__':
    df = pd.read_csv('ocorrencia.csv', sep=';', parse_dates=['ocorrencia_dia'], dayfirst=True)
    print(df)

    schema = pa.DataFrameSchema(
        columns={"codigo" : pa.Column(pa.Int, required=False),
                 "codigo_ocorrencia": pa.Column(pa.Int),
                 "codigo_ocorrencia2" : pa.Column(pa.Int),
                 "ocorrencia_classificacao" : pa.Column(pa.String),
                 "ocorrencia_cidade" : pa.Column(pa.String),
                 "ocorrencia_uf" : pa.Column(pa.String, pa.Check.str_length(2, 2), nullable=True),
                 "ocorrencia_aerodromo" : pa.Column(pa.String, nullable=True),
                 "ocorrencia_dia" : pa.Column(pa.DateTime),
                 "ocorrencia_hora" : pa.Column(pa.String, pa.Check.str_matches(r'^([0-1]?[0-9]|[2][0-3]):([0-5][0-9])(:[0-5][0-9])?$'),
                                               nullable=True),
                 "total_recomendacoes" : pa.Column(pa.Int)
                 })
    schema.validate(df)
    print(df.dtypes)
    print('-' * 50)

## Limpeza: ##

    #print(df.loc[1:3, 'ocorrencia_cidade']) -- é possível usar iloc, que aí a busca é por índice, podendo buscar posição negativa ou entre periodos [10:15]
    #print(df.loc[[10, 27, 13]])
    print(df.codigo_ocorrencia.is_unique)
    #df.set_index('codigo_ocorrencia', inplace=True)
    #df.reset_index(drop=True, inplace=True)
    df.loc[0, 'ocorrencia_aerodromo'] = '<NA>'
    print(df.loc[0, 'ocorrencia_aerodromo'])

    df.loc[df.ocorrencia_aerodromo == '****', ['ocorrencia_aerodromo']] = pd.NA
    df.replace(['**', '###!', '####', '*****', 'NULL'], pd.NA, inplace=True)

    print(df.loc[:, 'ocorrencia_aerodromo'])
    print(df.isna().sum())
    # df.fillna('A', inplace=True) -- altera todos os dados NA
    # df.dropna() -- tira a linha inteira que tenha um elemento NA
    # df.dropduplicates() -- tira linhas duplicadas

    print('-' * 50)

## transformação ##

    print(df.loc[df.ocorrencia_uf.isnull()])
    # print(df.count()) # conta os valores não nulos

    filtro = df.total_recomendacoes > 10
    print(df.loc[filtro, 'ocorrencia_cidade'])
