import os
import random

import constants
import pandas as pd
import openpyxl


class LogicCreator(object):

    def __init__(self):
        self.filelocation = os.getcwd()
        self.excelfile = os.path.join(self.filelocation, constants.EXCEL_FILENAME)

    def compute_excel_logic(self):
        random_sheet_number = self.generate_random_sheet()
        sheet_name_selected = "Sheet" + str(random_sheet_number)
        # header=None in order to also use the first row of the excel
        dataframe = pd.read_excel(self.excelfile, sheet_name=sheet_name_selected, header=None)
        print(dataframe)
        dict_index_value = {}
        index_dict = 1
        columns = dataframe.columns
        for index, row in dataframe.iterrows():
            for column in columns:
                value = row[column]
                dict_index_value.update({index_dict: value})
                index_dict += 1
        return dict_index_value

    def generate_random_sheet(self):
        try:
            wb = openpyxl.load_workbook(self.excelfile)
            number_sheets = len(wb.worksheets)
            # get a random sheet for the game
            random_sheet = random.randint(1, number_sheets)
            return random_sheet
        except:
            raise Exception("Please close excel file")

    def extract_entry_number(self, entry_string):
        list_string = entry_string.split("entry")
        print(list_string)
        if list_string[1] == '':
            return "1"
        return "".join(list_string[1])
