import psycopg2
import sys

#Define our connection string
conn_string = "host='localhost' dbname='postgres' user='ranxu' password='123456'"

# print the connection string we will use to connect
print "Connecting to database\n	->%s" % (conn_string)

# get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(conn_string)

# conn.cursor will return a cursor object, you can use this cursor to perform queries
cur = conn.cursor()
print "Connected!\n"

cur.execute("""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'""")
conn.commit()
tnames = []
for tname in cur.fetchall():
	tnames.append(tname[0])
print tnames

# Constructing commands
commands = []
prefix = 'drop table '
for tname in tnames:
	commands.append(prefix + tname)

# Drop all existing tables
print "\nStart dropping all tables"
for command in commands:
	print '\nExecuting commands......'	
	print command
	cur.execute(command)
	conn.commit()




commands = ('''
	CREATE TABLE H1B_16(
		CASE_NUMBER varchar(20), 
		CASE_STATUS varchar(20), 
		VISA_CLASS varchar(200),
		EMPLOYER_NAME varchar(200), 
		JOB_TITLE varchar(200),
		TOTAL_WORKERS integer,
		WORKSITE_CITY varchar(200),
		WORKSITE_COUNTY varchar(50),
		WORKSITE_STATE varchar(20),
		PREVAILING_WAGE money
		);
	''',
	'''
	CREATE TABLE temp(
		CASE_NUMBER varchar(20), 
		CASE_STATUS varchar(20), 
		CASE_SUBMITTED date,
		DECISION_DATA date,
		VISA_CLASS varchar(200),
		EMPLOYMENT_START_DATA date,
		EMPLOYMENT_END_DATE date,
		EMPLOYER_NAME varchar(200),
		EMPLOYER_ADDRESS varchar(200),
		EMPLOYER_CITY varchar(200),
		EMPLOYER_STATE varchar(200),
		EMPLOYER_POSTAL_CODE varchar(20),
		EMPLOYER_COUNTRY varchar(200),
		EMPLOYER_PROVINCE varchar(200),
		EMPLOYER_PHONE varchar(50),
		EMPLOYER_PHONE_EXT varchar(20),
		AGENT_ATTORNEY_NAME varchar(200),
		AGENT_ATTORNEY_CITY varchar(200),
		AGENT_ATTORNEY_STATE varchar(50),
		JOB_TITLE varchar(200),
		SOC_CODE varchar(20),
		SOC_NAME varchar(200),
		NAIC_CODE integer,
		TOTAL_WORKERS integer,
		FULL_TIME_POSITION varchar(20),
		PREVAILING_WAGE money,
		PW_UNIT_OF_PAY varchar(50),
		PW_WAGE_SOURCE varchar(50),
		PW_SOURCE_YEAR integer,
		PW_SOURCE_OTHER varchar(200),
		WAGE_RATE_OF_PAY_FROM money,
		WAGE_RATE_OF_PAY_TO money,
		WAGE_UNIT_OF_PAY varchar(20),
		H1B_DEPENDENT varchar(20),
		WILLFUL_VOILATOR varchar(50),
		WORKSITE_CITY varchar(200),
		WORKSITE_COUNTY varchar(50),
		WORKSITE_STATE varchar(20),
		WORKSITE_POSTAL_CODE varchar(20),
		ORIGINAL_CERT_DATE date
		);
	''')
for command in commands:
	print '\nExecuting commands......'	
	print command
	cur.execute(command)
	conn.commit()

with open('/Users/ranxu/Documents/GradStudy/CS263/Final_Project/postgres_h1b/H-1B_FY16.csv') as f:
	cur.copy_expert('''COPY temp FROM STDIN DELIMITER ',' CSV HEADER encoding 'windows-1251';''',f)
f.close()


commands2=(
	#'''
	#COPY temp FROM '/Users/ranxu/Documents/GradStudy/CS263/Final_Project/postgres_h1b/H-1B_FY16.csv' DELIMITER ',' CSV HEADER encoding 'windows-1251';
	#''',
	#only select certain columns that we care most.
	'''
	INSERT INTO H1B_16(CASE_NUMBER,CASE_STATUS,VISA_CLASS,EMPLOYER_NAME,JOB_TITLE,TOTAL_WORKERS,WORKSITE_CITY,WORKSITE_COUNTY,WORKSITE_STATE,PREVAILING_WAGE)
	SELECT CASE_NUMBER,CASE_STATUS,VISA_CLASS,EMPLOYER_NAME,JOB_TITLE,TOTAL_WORKERS,WORKSITE_CITY,WORKSITE_COUNTY,WORKSITE_STATE,PREVAILING_WAGE FROM  temp;
	''',
	'''
	DELETE FROM H1B_16
	WHERE VISA_CLASS!='H-1B'; 
	''',
	#get the status of the case_status: there are four case statuses, which are withdrawn, certified-withdrawn, denied, certified.
	'''
	CREATE TABLE STATUS_ALL_CASE AS 
	SELECT CASE_STATUS, COUNT(CASE_NUMBER) 
	FROM H1B_16
	GROUP BY CASE_STATUS;
	''',
	#SAVE THE RESULT TO A FILE
	#'''
	#COPY STATUS_ALL_CASE TO '/Users/ranxu/Documents/GradStudy/CS263/Final_Project/postgres_h1b/STATUS_ALL_CASE.csv' DELIMITER ',' CSV HEADER
	#''',
	#ANALYSIS OF THE STATUS IN EACH EMPLOYER, BY JOINNING OF TWO FOLLOWING TABLES, WE CAN GET THE RATIO OF CERTIFIED H1B IN EACH EMPLOYER
	'''
	CREATE TABLE STATUS_EMPLOYER AS 
	SELECT EMPLOYER_NAME, COUNT(CASE_NUMBER),SUM(TOTAL_WORKERS) AS SUM_OF_TOTAL_WORKERS
	FROM H1B_16
	GROUP BY EMPLOYER_NAME ORDER BY COUNT(CASE_NUMBER) DESC;
	''',
#
	'''
	CREATE TABLE STATUS_EMPLOYER_CERTIFIED AS SELECT EMPLOYER_NAME , COUNT(CASE_NUMBER) AS CERTIFIED_NUMBER, SUM(TOTAL_WORKERS) AS CERTIFIED_TOTAL_WORKERS FROM H1B_16 WHERE CASE_STATUS = 'CERTIFIED' GROUP BY EMPLOYER_NAME;
	''',
	'''
	ALTER TABLE STATUS_EMPLOYER_CERTIFIED RENAME EMPLOYER_NAME TO E_NAME;
	''',
	'''
	CREATE TABLE EMPLOYER_RATIO_STATUS AS SELECT * FROM STATUS_EMPLOYER LEFT OUTER JOIN STATUS_EMPLOYER_CERTIFIED ON STATUS_EMPLOYER.EMPLOYER_NAME=STATUS_EMPLOYER_CERTIFIED.E_NAME ORDER BY CERTIFIED_NUMBER DESC;
	''',
	'''
	CREATE TABLE STATUS_JOB_TITLE AS SELECT JOB_TITLE,COUNT(CASE_NUMBER) FROM H1B_16 WHERE CASE_STATUS = 'CERTIFIED' GROUP BY JOB_TITLE ORDER BY COUNT(CASE_NUMBER) DESC;
	'''
	#COPY EMPLOYER_RATIO_STATUS TO '/Users/ranxu/Documents/GradStudy/CS263/Final_Project/postgres_h1b/EMPLOYER_RATIO_STATUS.csv' DELIMITER ',' CSV HEADER;
	#'''

)
for command in commands2:
	print '\nExecuting commands......'	
	print command
	cur.execute(command)
	conn.commit()

with open('/Users/ranxu/Documents/GradStudy/CS263/Final_Project/postgres_h1b/STATUS_ALL_CASE.csv','w') as f1:
	cur.copy_expert('''COPY STATUS_ALL_CASE to STDOUT DELIMITER ',' CSV HEADER encoding 'windows-1251';''',f1)
f1.close()


with open('/Users/ranxu/Documents/GradStudy/CS263/Final_Project/postgres_h1b/EMPLOYER_RATIO_STATUS.csv','w') as f2:
	cur.copy_expert('''COPY EMPLOYER_RATIO_STATUS to STDOUT DELIMITER ',' CSV HEADER encoding 'windows-1251';''',f2)
f2.close()

with open('/Users/ranxu/Documents/GradStudy/CS263/Final_Project/postgres_h1b/STATUS_JOB_TITLE.csv','w') as f3:
	cur.copy_expert('''COPY STATUS_JOB_TITLE to STDOUT DELIMITER ',' CSV HEADER encoding 'windows-1251';''',f3)
f3.close()

print '\nAll commands executed'

conn.close()
print '\nClosed connection to databsed'


# with open('/Users/ranxu/Documents/GradStudy/CS263/Final_Project/postgres_h1b/EMPLOYER_RATIO_STATUS.csv','wr') as f4:

	
# f4.close()

