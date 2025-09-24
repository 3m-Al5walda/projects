
import csv
import os
import enum
import dataclasses as dc
import typing 
import uuid
'''
files csv
# a list of contacts
# data format:
contact_id,name,gender,contact_number

'''

class Gender(str, enum.Enum):
    '''enum to store =gender '''
    """enum to store values of genders"""

    MALE= enum.auto()
    FEMALE= enum.auto()

@dc.dataclass
class Contact:
    '''a dataclass to store a single contact'''
    contact_id: str = '0000'
    name: str = 'John Doe'
    contact_number: str = '0000000000'
    gender : Gender = Gender.MALE


@dc.dataclass
class Contacts:
    '''a list of contacts'''
    contacts: typing.List[Contact] = dc.field(default_factory=list)


class Field(str,enum.Enum):
    Gender = enum.auto()
    NAME = enum.auto()
    CONTACT_NUMBER = enum.auto()


class csvDb:
    '''a class to handle csv database operations'''

    def __init__(self):
        self.contacts :Contacts = []
    ####    '''=======================   We need CRUD Operation =========================='''

    def create_contact(self, name:str,gender : Gender, contact_number:str) -> Contact:

        '''create a new contact'''
        truncated_uuid = str(uuid.uuid4())[::-1][:4].upper()
        # create a new contact
        try :
            if self.valid_number(contact_number):
                contact  = Contact(
                    contact_id=truncated_uuid, 
                    name=name,
                    contact_number=contact_number, gender=gender
                )
                self.contacts.append(contact)
                print(f'Great Mr {name}!!\n\n create successfully with {truncated_uuid} ') 
            return contact
        
        except Exception as ex :
            raise ex
        
    
    def valid_number(self,number) ->bool:
        lenOfNumber = len(number)
        firs_dig = number[:2]
        therd_dig = number[2]
        if (lenOfNumber == 10) and firs_dig=='07' and (('7'in therd_dig) or ('8'in therd_dig) or ('9'in therd_dig)) :
            return True
        
        raise ValueError(f'Incorrect Number Entered: {number}.\nNumber should be formatted as 07XXXXXXXX and should start with 079 or 078 or 077')

    def read_contact(self,contact_id:str) ->Contact:
        '''return user contact if found'''
        for i in self.contacts:
            if i.contact_id == contact_id:
                return i
        
        raise f'the contact {contact_id} not found 404'
        
    
    def get_contact(self,contact_id:str) ->Contact:
        '''return user contact if found'''
        for i in self.contacts:
            if i.contact_id == contact_id:
                return i

    def update_contact(self,contact_id : str,update_filed : Field, update_params : typing.Union[Gender,str])->Contact:
        '''update parameters like name , gender and contact_number ...'''
        match update_filed :
            case Field.NAME :
                contact = self.get_contact(contact_id)
                contact.name = update_params
                return contact
            
            case Field.Gender:
                contact = self.get_contact(contact_id)
                contact.gender = update_params
                return contact
            
            case Field.CONTACT_NUMBER :
                try :
                    if self.valid_number(update_params):
                        contact = self.get_contact(contact_id)
                        contact.contact_number = update_params
                        return contact
                except Exception as ex:
                    raise ex
                
        def delete_contact(self, contact_id: str):
            '''delet contact number if can found ...'''
            for idx, contact in enumerate(self.contacts):
                if contact.contact_id == contact_id:
                    del self.contacts[idx]
                    print(f"Contact ID {contact_id} deleted successfully")
                    return

            raise ValueError(f"Contact ID {contact_id} does not exist.")


    def save_data(self,name_file : str):
        '''save data to csv file'''
        cont = [f'{i.contact_id},{i.name},{i.gender},{i.contact_number}' for i in self.contacts]
        if os.path.exists(name_file):
            print(f'the path is found {name_file}')

        with open(f'{name_file} .csv', 'w', newline='',encoding='utf-8') as f:
            file_write = csv.writer(f)
            file_write.writerow(cont)


cs = csvDb()
cs.create_contact('abdulla','MALE','0796070317')
#cs.update_contact('EA58',Field.NAME,'abdulla_mohamad')

cs.save_data('abdulla')
a = csvDb()
a.create_contact('hamza','MALE','0794662620')
a.save_data('messe')
print()

