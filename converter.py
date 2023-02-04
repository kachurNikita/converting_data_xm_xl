import xml.dom.minidom as md
# import xlwt
# from xlwt import Workbook
xml_path = 'xml_data.xml'
user = {}


def parse_file(xml_file_path):
    docs = md.parse(xml_file_path)
    profession = docs.createElement('profession')
    profession.appendChild(docs.createTextNode('Software Engineer'))
    docs.firstChild.appendChild(profession)
    with open('xml_data.xml', "w") as fs:
        fs.write(docs.toxml())
        fs.close()
    modyfied_docs = md.parse(xml_file_path)
    name = docs.getElementsByTagName('fname')
    lastName = docs.getElementsByTagName('lname')
    age = docs.getElementsByTagName('age')
    new_value = modyfied_docs.getElementsByTagName('profession')
    user['user'] = {
                'fname': name[0].firstChild.nodeValue,
                'lname': lastName[0].firstChild.nodeValue,
                'age': age[0].firstChild.nodeValue,
                'profession': new_value[0].firstChild.nodeValue
            }
    return user

test = parse_file(xml_path)
print(test)


# def write_to_excel(data_object):
#     work_book = xlwt.Workbook()
#     sheet = work_book.add_sheet('Sheet name')
#     style = xlwt.easyxf('font: bold 1')
#     sheet.write(0, 0, 'user name', style)
#     sheet.write(1, 0, data_object['user']['fname'])
#     sheet.write(0, 1, 'user surname', style)
#     sheet.write(1, 1, data_object['user']['lname'], style)
#     sheet.write(0, 2, 'user age', style)
#     sheet.write(1, 2, data_object['user']['age'], style)
#     sheet.write(0, 3, 'user profession', style)
#     sheet.write(1, 3, data_object['user']['profession'], style)
#     work_book.save('sample.xls')

# Pandas implementation









