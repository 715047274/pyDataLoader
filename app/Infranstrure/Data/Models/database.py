from sqlalchemy import create_engine, MetaData
#from sqlalchemy.ext.declarative import declarative_base
import urllib

SERVER_NAME03='torrdperfdb03'
DB_NAME03='large_perftest_851'
SERVER_NAME02='ncdbqa06'
DB_NAME02='851payroll102'
SERVER_NAME01 ='CANWS326\sql2012'
DB_NAME01='DFLocal01'

#Base = declarative_base()
quoted = urllib.parse.quote_plus('DRIVER={SQL Server Native Client 11.0};'
                                 'SERVER=torrdperfdb03;'
                                 'DATABASE=large_perftest_851;'
                                 'UID=wbpoc;'
                                 'PWD=sql@tfs2008;')


quotedLocal = urllib.parse.quote_plus('DRIVER={SQL Server Native Client 11.0};'
                                 'SERVER=CANWS194\sql2012;'
                                 'DATABASE=DFLocal01;'
                                 'UID=wbpoc;'
                                 'PWD=sql@tfs2008;')

Banfield850 = urllib.parse.quote_plus('DRIVER={SQL Server Native Client 11.0};'
                                 'SERVER=ncdbqa09;'
                                 'DATABASE=850qa412;'
                                 'UID=wbpoc;'
                                 'PWD=sql@tfs2008;')

Banfield852 = urllib.parse.quote_plus('DRIVER={SQL Server Native Client 11.0};'
                                 'SERVER=ncdbqa09;'
                                 'DATABASE=852qa412;'
                                 'UID=wbpoc;'
                                 'PWD=sql@tfs2008;')

Stantec852 = urllib.parse.quote_plus('DRIVER={SQL Server Native Client 11.0};'
                                 'SERVER=ncdbqa14;'
                                 'DATABASE=852qa34775;'
                                 'UID=wbpoc;'
                                 'PWD=sql@tfs2008;')

Perf52_10000 = urllib.parse.quote_plus('DRIVER={SQL Server Native Client 11.0};'
                                 'SERVER=torrdperfdb05;'
                                 'DATABASE=prperftest52_10000;'
                                 'UID=wbpoc;'
                                 'PWD=sql@tfs2008;')

Perf52_10001 = urllib.parse.quote_plus('DRIVER={SQL Server Native Client 11.0};'
                                 'SERVER=torrdperfdb05;'
                                 'DATABASE=prperftest52_10001;'
                                 'UID=wbpoc;'
                                 'PWD=sql@tfs2008;')

Perf52_10002 = urllib.parse.quote_plus('DRIVER={SQL Server Native Client 11.0};'
                                 'SERVER=torrdperfdb05;'
                                 'DATABASE=prperftest52_10002;'
                                 'UID=wbpoc;'
                                 'PWD=sql@tfs2008;')

Perf53_10000 = urllib.parse.quote_plus('DRIVER={SQL Server Native Client 11.0};'
                                 'SERVER=torrdperfdb05;'
                                 'DATABASE=prperftest53_10000;'
                                 'UID=wbpoc;'
                                 'PWD=sql@tfs2008;')

Perf53_10002 = urllib.parse.quote_plus('DRIVER={SQL Server Native Client 11.0};'
                                 'SERVER=torrdperfdb05;'
                                 'DATABASE=prperftest53_10002;'
                                 'UID=wbpoc;'
                                 'PWD=sql@tfs2008;')


Perf54_10000 = urllib.parse.quote_plus('DRIVER={SQL Server Native Client 11.0};'
                                 'SERVER=torrdperfdb04;'
                                 'DATABASE=prperftest2_10000;'
                                 'UID=wbpoc;'
                                 'PWD=sql@tfs2008;')

Perf54_10002 = urllib.parse.quote_plus('DRIVER={SQL Server Native Client 11.0};'
                                 'SERVER=torrdperfdb04;'
                                 'DATABASE=prperftest2_10002;'
                                 'UID=wbpoc;'
                                 'PWD=sql@tfs2008;')

Perf58_10000 = urllib.parse.quote_plus('DRIVER={SQL Server Native Client 11.0};'
                                 'SERVER=torrdperfdb04;'
                                 'DATABASE=prperftest3_10000;'
                                 'UID=wbpoc;'
                                 'PWD=sql@tfs2008;')

Perf58_10002 = urllib.parse.quote_plus('DRIVER={SQL Server Native Client 11.0};'
                                 'SERVER=torrdperfdb04;'
                                 'DATABASE=prperftest3_10002;'
                                 'UID=wbpoc;'
                                 'PWD=sql@tfs2008;')

Perf56_10000 = urllib.parse.quote_plus('DRIVER={SQL Server Native Client 11.0};'
                                 'SERVER=torrdperfdb03;'
                                 'DATABASE=prperftest1_10000;'
                                 'UID=wbpoc;'
                                 'PWD=sql@tfs2008;')

Perf56_10002 = urllib.parse.quote_plus('DRIVER={SQL Server Native Client 11.0};'
                                 'SERVER=torrdperfdb03;'
                                 'DATABASE=prperftest1_10002;'
                                 'UID=wbpoc;'
                                 'PWD=sql@tfs2008;')

Perf61_10000 = urllib.parse.quote_plus('DRIVER={SQL Server Native Client 11.0};'
                                 'SERVER=torrdperfdb03;'
                                 'DATABASE=prperftestx2_10000;'
                                 'UID=wbpoc;'
                                 'PWD=sql@tfs2008;')

Perf61_10002 = urllib.parse.quote_plus('DRIVER={SQL Server Native Client 11.0};'
                                 'SERVER=torrdperfdb03;'
                                 'DATABASE=prperftestx2_10002;'
                                 'UID=wbpoc;'
                                 'PWD=sql@tfs2008;')

Perf57_10002 = urllib.parse.quote_plus('DRIVER={SQL Server Native Client 11.0};'
                                 'SERVER=torrdperfdb04;'
                                 'DATABASE=prperftest2_10002;'
                                 'UID=wbpoc;'
                                 'PWD=sql@tfs2008;')

atpr57_16 = urllib.parse.quote_plus('DRIVER={SQL Server Native Client 11.0};'
                                 'SERVER=nan4auto1sql02;'
                                 'DATABASE=atpr57_16;'
                                 'UID=wbpoc;'
                                 'PWD=sql@tfs2008;')

perfausr57 = urllib.parse.quote_plus('DRIVER={SQL Server Native Client 11.0};'
                                 'SERVER=TDC9PERF1SQL01;'
                                 'DATABASE=perfausr57;'
                                 'UID=wbpoc;'
                                 'PWD=sql@tfs2008;')

pay860roll190 = urllib.parse.quote_plus('DRIVER={SQL Server Native Client 11.0};'
                                 'SERVER=nan4dfc1sql903;'
                                 'DATABASE=860payroll190;'
                                 'UID=wbpoc;'
                                 'PWD=sql@tfs2008;')

pay859roll190 = urllib.parse.quote_plus('DRIVER={SQL Server Native Client 11.0};'
                                 'SERVER=nan4dfc1sql28;'
                                 'DATABASE=859payroll190;'
                                 'UID=wbpoc;'
                                 'PWD=sql@tfs2008;')

perfx2_56865 = urllib.parse.quote_plus('DRIVER={SQL Server Native Client 11.0};'
                                 'SERVER=torrdperfdb03;'
                                 'DATABASE=prperftestx2_56865;'
                                 'UID=wbpoc;'
                                 'PWD=sql@tfs2008;')

#   Client Instance: intodp_700140 (cadmin/1)
#   DB Server: ncintdb01
intodp700140 = urllib.parse.quote_plus('DRIVER={SQL Server Native Client 11.0};'
                                 'SERVER=ncintdb01;'
                                 'DATABASE=intodp_700140;'
                                 'UID=wbpoc;'
                                 'PWD=sql@tfs2008;')

ecksso25 = urllib.parse.quote_plus('DRIVER={SQL Server Native Client 11.0};'
                                 'SERVER=azg5perfsql02a;'
                                 'DATABASE=ecksso25_jupiter;'
                                 'UID=wbpoc;'
                                 'PWD=sql@tfs2008;')

localhost = urllib.parse.quote_plus('DRIVER={SQL Server Native Client 11.0};'
                                 'SERVER=localhost;'
                                 'DATABASE=dflocal;'
                                 'UID=wbpoc;'
                                 'PWD=sql@tfs2008;')


connect_args = {'autocommit': True}
engine = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(localhost), connect_args=connect_args)

def start():
    return engine
metadata = MetaData(bind=engine)


if __name__=='__main__':
    start()