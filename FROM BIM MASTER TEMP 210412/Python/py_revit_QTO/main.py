

#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
import pandas as pd
from search_match import *
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
def main():
    source_path = r"C:\Users\tvpduy\py_revit_QTO\source\Lookup.xlsx"
    sheet_name = "Lookup"

    print(f"{'-'*10}Source_path:{'-'*10}\n{source_path}")

    # 1. TẠO DỮ LIỆU TỪ ĐIỂN TRA CỨU
    source_df = pd.read_excel(source_path, sheet_name = sheet_name)
    print(f"{'-'*10}Source_DataFrame:{'-'*10}\n{source_df.shape}")
    # print(f"{'-'*10}Source_DataFrame_describe:{'-'*10}\n{source_df.describe()}")

    source_dict = source_df.to_dict()
    # print(f"{'-'*10}Source_Dictionary:{'-'*10}\n{source_dict}")

    source_json_path = f"{source_path[:-len(source_path.split('.')[-1])-1]}.json"
    source_json = source_df.to_json(source_json_path,orient='records',indent = 4)

    # 2. TẢI DỮ LIỆU REVIT
    revit_data_path = r"C:\Users\tvpduy\py_revit_QTO\data\ACR-QTO-ZZ-ZZ-ZZ-combine-210705.json"
    revit_data_df = pd.read_json(revit_data_path)
    # print(f"{'-'*10}Revit_data_df:{'-'*10}\n{revit_data_df}")

    # PARAMETER  COFICO
    cof_parameter_heads = sorted([c for c in revit_data_df.columns.tolist() if 'cof_' in c.lower()])
    print(f"{'-'*10}Revit_data_df_columns_cof_parameter_heads:{'-'*10}\n{cof_parameter_heads}")

    # PARAMETER NOT COFICO
    parameter_heads = sorted([c for c in revit_data_df.columns.tolist() if not 'cof_' in c.lower()])
    print(f"{'-'*10}Revit_data_df_columns_parameter_heads:{'-'*10}\n{parameter_heads}")

    # 2.1 ClEAN revit_data_df
    column_names = ['COF_GEN__ProjectNumber',
                'COF_GEN__BuildingNumber',
                'COF_GEN__Category',
                'COF_GEN__Level',
                'Volume',
                'Category',
                'Type']

    revit_data_df_small = revit_data_df[column_names]
    print(f"{'-'*10}Revit_data_df:{'-'*10}\n{revit_data_df_small}")

    # json.loads()

if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        quit()
