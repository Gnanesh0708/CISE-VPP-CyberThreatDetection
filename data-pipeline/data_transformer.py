import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):
    
    df.columns=(df.columns
        .str.replace(" ","_")
        .str.lower())

    df['source_ip']=df['ip_address_ports'].apply(lambda x: x.split(',')[0][1:])
    df['source_port']=df['ip_address_ports'].apply(lambda x: x.split(',')[1]).astype('int64')
    df['destination_ip']=df['ip_address_ports'].apply(lambda x: x.split(',')[2])
    df['destination_port']=df['ip_address_ports'].apply(lambda x: x.split(',')[3][:-1]).astype('int64')
    df['timestamp']=pd.to_datetime(df['timestamp'])
    df=df.drop(['unnamed:_0','ip_address_ports'],axis=1)
    print(df.info())
    
    df['extraction_date']=df['timestamp'].dt.date
    df=df.drop_duplicates()
    df=df.dropna()
    return df
    df.to_csv('sample_mqtt.csv')


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert 'pv_voltage' in output.columns and "extraction_date" in output.columns 