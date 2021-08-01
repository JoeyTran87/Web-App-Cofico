import pandas as pd

tonkho_excel_path = "data_ton_kho\\TỒN KHO LA KỲ 20.06.2021.xlsx"

# tonkho_data = pd.read_excel(tonkho_excel_path,sheet_name = None)
# print(tonkho_data)


def show_excel_sheet(excel_path) -> list:
    """Show danh sách tên các sheet trong file Excel"""
    xl = pd.ExcelFile(excel_path)
    sheets = xl.sheet_names
    for i,shn in enumerate(sheets):
        print(f"\t[{i}]\t{shn}")  # see all sheet names
    return sheets

# xl.parse(sheet_name)  # read a specific sheet to DataFrame