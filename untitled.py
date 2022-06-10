import pandas as pd
import snowflake.connector
conn = snowflake.connector.connect(user='INNOKENTYVOLOSHIN',password='1Q2w3e4r',account='iwb20380.us-east-1')

sql = """
-- auto-generated definition
insert into JENKINSTEST.PUBLIC.TEST_EXECUTION_RESULTS (EXECUTION_ID, PROCESS_NAME, CATEGORY, STATUS)
select 'absce','Usage - Fetch Data from Bob','Integration (BI)','SUCCESS'
union
select 'absce','Usage - Import Data into Netsuite','Integration','FAILED';
"""

query = conn.cursor().execute(sql).fetchall()

sql2 = """
SELECT * FROM JENKINSTEST.PUBLIC.TEST_EXECUTION_RESULTS;
"""

query2 = conn.cursor().execute(sql2).fetchall()


df = pd.DataFrame(query2)
df.style