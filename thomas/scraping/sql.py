import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.sql import select

import logging

class ScrapingDB():

    def __init__(self):
        # in memory db
        self.logFile = ''
        self.connectionString = 'sqlite:///:memory:'
    
    def create(self, dbFile=None, logFile=None):
        if logFile != None and logFile != '' :
            self.logFile = logFile
            handler = logging.FileHandler(self.logFile)
            handler.setLevel(logging.DEBUG)
            logging.getLogger('sqlalchemy').addHandler(handler)

        if dbFile != None and dbFile != '':
            self.connectionString = 'sqlite:///{0}'.format(dbFile)

        self.engine = create_engine(self.connectionString, echo=True)

        metadata = MetaData()
        self.columnSetName = Column('setName', String)
        self.columnPartName = Column('partName', String)
        self.partsToSets = Table('PartsToSets', metadata,
            self.columnSetName,
            self.columnPartName
        )
        metadata.create_all(self.engine)

    def _insert(self,setNumber, partNumber):
        ins = self.partsToSets.insert().values(setName=setNumber, partName=partNumber)
        ins.compile().params
        conn = self.engine.connect()
        result = conn.execute(ins)
        ins.bind = self.engine
        return result

    # insert if not exists
    def insertAssociation(self, setNumber, partNumber):
        
        query = select([self.partsToSets]).where(self.columnSetName == setNumber).where(self.columnPartName == partNumber)
        conn = self.engine.connect()
        result = conn.execute(query)
        rows = result.fetchall()

        if len(rows) == 0 :
            ins = self.partsToSets.insert().values(setName=setNumber, partName=partNumber)
            ins.compile().params
            conn = self.engine.connect()
            result = conn.execute(ins)
            ins.bind = self.engine
            print("\n [SQL].insertAssociation: partNumber={0} to setNumber={1}".format(partNumber,setNumber))
            return result
        else :
            print("\n [SQL].insertAssociation: partNumber={0} to setNumber={1} already exists".format(partNumber,setNumber))

    def selectAllAssociations(self):
        query = select([self.partsToSets])
        conn = self.engine.connect()
        result = conn.execute(query)
        return result

    def info(self):
        print("logging version: {0}; logging into '{1}' ".format(logging.__version__, self.logFile))
        print("SQLAlchemy version: {0}; db connection string: '{1}'".format(sqlalchemy.__version__, self.connectionString))