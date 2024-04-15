import openpyxl

class ReadExcel:

    @staticmethod
    def read_excel(casePath):
        # wb = openpyxl.load_workbook(r"C:\learning\python\wbseleniumProject\testdata\新建 XLSX 工作表.xlsx")
        wb = openpyxl.load_workbook(casePath)
        sheet = wb['Sheet1']
        all_values = list(sheet.values)
        all_values.pop(0)
        return  all_values


if __name__ == '__main__':
    ReadExcel.read_excel(r"C:\learning\python\wb_Interface_Autotest\data\testcase.xlsx")