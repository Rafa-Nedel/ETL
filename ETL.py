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
                 "ocorrencia_uf" : pa.Column(pa.String, pa.Check.str_length(2, 2)),
                 "ocorrencia_aerodromo" : pa.Column(pa.String),
                 "ocorrencia_dia" : pa.Column(pa.DateTime),
                 "ocorrencia_hora" : pa.Column(pa.String, pa.Check.str_matches(r'^([0-1]?[0-9]|[2][0-3]):([0-5][0-9])(:[0-5][0-9])?$'),
                                               nullable=True),
                 "total_recomendacoes" : pa.Column(pa.Int)
                 })
    schema.validate(df)
    print(df.dtypes)
    print('-' * 50)
## Limpeza: ##
    #print(df.loc[1:3, 'ocorrencia_cidade'])
    #print(df.loc[[10, 27, 13]])
    print(df.codigo_ocorrencia.is_unique)
    #df.set_index('codigo_ocorrencia', inplace=True)
    #df.reset_index(drop=True, inplace=True)
    df.loc[0, 'ocorrencia_aerodromo'] = 'N/D'
    print(df.loc[0, 'ocorrencia_aerodromo'])