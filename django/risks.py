import openpyxl
wb = openpyxl.load_workbook('employees.xlsx')
sheet=wb["abc"]
data=[]
for row_data in sheet.iter_rows():
    values={}
    values['name']=row_data[0].value
    values['gender']=row_data[1].value
    values['date']=row_data[2].value
    data.append(values)
print(data)