from copy import error
from pymongo import MongoClient
import inspect

from pymongo.message import insert


class mongoORM:
    _hraw_to_hname_data ={
    "data-dencom" : "Denumire comercială",
    "data-dci" : "DCI",
    "data-formafarm" : "Forma farmaceutică",
    "data-conc" : "Concentrația",
    "data-codatc" : "Cod ATC",
    "data-actter" : "Acțiune terapeutică",
    "data-prescript" : "Prescripție",
    "data-ambalaj" : "Ambalaj",
    "data-volumamb" : "Volum ambalaj",
    "data-valabamb" : "Valabilitate ambalaj",
    "data-cim" : "Cod CIM",
    "data-firmtarp" : "Firma / țara producătoare APP",
    "data-firmtard" : "Firma / țara deținătoare APP",
    "data-nrdtamb" : "Nr. / data ambalaj APP",
    "data-linkrcp" : "Rezumat caracteristici produs",
    "data-linkpro" : "Prospect",
    "data-linkamb" : "Ambalaj",
    }

    __url__ = 'localhost'
    __port__ = 27017
    conn = None
    def createConnection(self):
        self.conn = MongoClient(host=self.__url__, port=self.__port__)
        self.conn = self.conn["app"]

    def __init__(self) -> None:
        self.createConnection()
    
    def connectToPDFDb(self):
        retr_prm = None
        if self.conn != None:
            retr_prm = self.conn["pdf"]
        else:
            self.__init__
            retr_prm = self.conn["pdf"]
        return retr_prm

    def connectToMedDb(self):
        retr_prm = None
        if self.conn != None:
            retr_prm = self.conn["med"]
        else:
            self.__init__
            retr_prm = self.conn["med"]
        return retr_prm
    
    def insertMedicament(self,_row:dict):
        #TODO: prefiltering/check if row exists
        connMed = None
        try:
            connMed = self.connectToMedDb()
        except Exception as e:
            print("Error on slecting collection in function {fct_name} !\n{err}".format(fct_name = inspect.__name__, err = str(e)))
        try:
            connMed.insert_one(_row)
        except Exception as e:
            print("Error on insertion in function {fct_name} !\n{err}".format(fct_name = inspect.__name__, err = str(e)))

    def searchMedAfterField(self,_field):
        retr_prm = None
        if _field not in self._hraw_to_hname_data.keys():
            print("Error: parameter \"{prm}\" in function {fct_name} is not supported, please see mongoORM._hraw_to_hname_data for supported parameteres".format(
                prm = _field,
                fct_name = inspect.__name__
            ))
        else:
            try:
                connMed = None
                try:
                    connMed = self.connectToMedDb()
                except Exception as e:
                    print("Error on slecting collection in function {fct_name} !\n{err}".format(fct_name = inspect.__name__, err = str(e)))
                
                try:
                    retr_prm = connMed.find({_field:1})
                except Exception as e:
                    print("Error trying to get data from collection in function {fct_name} on field {fld}!\n{err}".format(
                        fct_name=inspect.__name__,
                        fld=_field,
                        err=str(e)
                    ))
            except Exception as e:
                pass
        return retr_prm
