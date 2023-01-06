import xlrd

def read_locator(sheetname):
    d = {}
    wb = xlrd.open_workbook("../Excel/Locators.xlsx")
    sh = wb.sheet_by_name(sheetname)
    rows = sh.get_rows()
    next(rows)
    for row in rows:
        d[row[0].value] = (row[1].value, row[2].value)
    return d

