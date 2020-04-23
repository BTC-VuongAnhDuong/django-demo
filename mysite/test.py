import pandas as pd
data_list = [{
              'sample_code': '140F001A',
            'sample_size' : '110',
              'url_colorway': 'C26275711',
              'sample_pattern': 'A-1',
              'spec': 'US/EU',
              'destination_selected': 'HI',
              },
{
              'sample_code': '140F001A',
            'sample_size' : '120',
              'url_colorway': 'C26275711',
              'sample_pattern': 'A-1',
              'spec': 'US/EU',
              'destination_selected': 'HI',
              },
{
              'sample_code': '140F001A',
            'sample_size' : '130',
              'url_colorway': 'C26275711',
              'sample_pattern': 'A-1',
              'spec': 'US/EU',
              'destination_selected': 'HI',
              },
{
              'sample_code': '140F001A',
            'sample_size' : '140',
              'url_colorway': 'C26275711',
              'sample_pattern': 'A-1',
              'spec': 'US/EU',
              'destination_selected': 'HI',
              }
]
df = pd.DataFrame.from_records(data_list)

rfid_df = [{
              'SAMPLE_CODE': '140F001A',
            'SAMPLE_SIZE' : '110',
              'CENTRIC_ID': 'C26275711',
              'SAMPLE_PATTERN': 'A-1',
              'SPEC': 'US/EU',
              'DESTINATION_A': 'HI',
              },
{
              'SAMPLE_CODE': '140F001A',
            'SAMPLE_SIZE' : '110',
              'CENTRIC_ID': 'C26275711',
              'SAMPLE_PATTERN': 'A-1',
              'SPEC': 'US/EU',
              'DESTINATION_A': 'HI',
              },
{
              'SAMPLE_CODE': '140F001A',
            'SAMPLE_SIZE' : '110',
              'CENTRIC_ID': 'C26275711',
              'SAMPLE_PATTERN': 'A-1',
              'SPEC': 'US/EU',
              'DESTINATION_A': 'HI',
              },
{
              'SAMPLE_CODE': '140F001A',
            'SAMPLE_SIZE' : '110',
              'CENTRIC_ID': 'C26275711',
              'SAMPLE_PATTERN': 'A-1',
              'SPEC': 'US/EU',
              'DESTINATION_A': 'HI',
              },
]
rfid_df = pd.DataFrame.from_records(rfid_df)

df = pd.merge(df, rfid_df
                              , how='left'
                              , left_on=['sample_code', 'sample_size', 'url_colorway',
                                         'sample_pattern', 'spec', 'destination_selected']
                              , right_on=['SAMPLE_CODE', 'SAMPLE_SIZE', 'CENTRIC_ID',
                                          'SAMPLE_PATTERN', 'SPEC', 'DESTINATION_A'])

print(df)