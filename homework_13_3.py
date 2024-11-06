import xml.etree.ElementTree as ET
import logging

# Логер
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def find_group_number(xml_file, group_number):
    try:
        # Парсинг XML файлу
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # Пошук group в number i timing_exbytes в incoming
        for group in root.findall("group"):
            number = group.find("number")
            if number is not None and number.text == str(group_number):
                timing_exbytes = group.find("timingExbytes")
                if timing_exbytes is not None:
                    incoming = timing_exbytes.find("incoming")
                    if incoming is not None:
                        logging.info(f"Group number {group_number}, 'timingExbytes > incoming': {incoming.text}")
                        return incoming.text
        logging.info(f"There is no 'timingExbytes > incoming' for group number {group_number}")

    except Exception as e:
        logging.error(f"No info found: {e}")

find_group_number('groups.xml', '0')
find_group_number('groups.xml', '1')
find_group_number('groups.xml', '2')
find_group_number('groups.xml', '3')
find_group_number('groups.xml', '4')
find_group_number('groups.xml', '5')
