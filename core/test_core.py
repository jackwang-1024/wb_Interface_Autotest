import openpyxl,pytest,requests
from tools.handle_excel import ReadExcel

caselist = ReadExcel.read_excel(r"C:\learning\python\wb_Interface_Autotest\data\testcase.xlsx")
print(caselist)

@pytest.mark.parametrize("case",caselist)
def test_case_exec(case):
    print(case)
    response = requests.request(
        url=case[2],
        method=case[3],
        params=case[4]
    )
    print(response.json())
    assert 'ok' == response.json()['state']
