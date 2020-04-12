#!/usr/bin/env python
# coding: utf-8

# $$\Large \textbf{Query Table Information With SQL}$$
# 
# $$\textbf{Phuong Van Nguyen}$$
# 
# This notebook will show how to query the number of tables and a table'columns given a database using the **SQL**

# # Loading SQL magic

# In[1]:


get_ipython().run_line_magic('load_ext', 'sql')


# # Connecting to the given database of demo.db3

# In[2]:


get_ipython().run_line_magic('sql', 'sqlite:///C:/Users/Phuong_1/Documents/SQL/SQLite/Practice-SQL-with-SQLite-and-Jupyter-Notebook-master/demo.db3')


# # Exploring a Database
# ## List  tables in a database
# 
# Table and index names can be list by doing a **SELECT** on a special table named "***SQLITE_MASTER***". Every SQLite database has an SQLITE_MASTER table that defines the schema for the database. For tables, the ***type*** field will always be '***table***' and the name field will be the name of the table. So to get a list of all tables in the database, use the following SELECT command:
# 
# See more at https://www.sqlite.org/faq.html#q7.

# In[5]:


get_ipython().run_line_magic('sql', "SELECT name FROM sqlite_master WHERE type='table'")


# ## Selecting a specific Table in Database
# ### Listing the name of columns in a table
# 
# We take the table of rch as an example

# In[55]:


get_ipython().run_cell_magic('sql', 'sqlite://', '    SELECT * \n    FROM rch \n    WHERE 1=0')


# ### Counting the number of rows in a Table
# This can be done with the SQLite ***COUNT*** function. We will touch other SQLite function over the next few notebooks.

# In[53]:


get_ipython().run_line_magic('sql', 'SELECT COUNT(*) as Number_of_Rows FROM rch')


# ### Listing the first number of all columns in Table
# 
# Often it is not convenient to show all rows on screen as you have to scroll. We can use use SQLite ***LIMIT*** clause to constrain the number of rows returned by a query. This can be used for testing or to prevent consuming excessive resources if the query returns more information than expected.
# 
# The following illustrates the syntax of the LIMIT clause:
# - SELECT column_list FROM table_name LIMIT row_count;
# 
# We list the first 10 observations

# In[34]:


get_ipython().run_line_magic('sql', 'SELECT * FROM rch LIMIT 10')


# ### Listing a specific sample of Table with a specific condition (WHERE)
# 
# ometimes, you’ll want to only check the rows returned by a query, where one or more columns meet certain criteria. This can be done with a WHERE statement. The WHERE clause is an optional clause of the SELECT statement. It appears after the FROM clause as the following statement:
# 
# >SELECT column_list FROM table_name WHERE search_condition;
# 
# In the WHERE statement, we can the combinations of ***NOT, IN, <>, !=, >=, >, <, <=, AND, OR, ()*** and even some of math operators (such as %, *, /, +, -)to retrieve the data we want easily and efficiently. 

# In[36]:


get_ipython().run_line_magic('sql', 'SELECT * FROM rch WHERE RCH==1 and YR==1981 LIMIT 10')


# ***Warning***! This table contains too many records. It'd better not query all of them.

# ### Listing the  specific number of columns  in Table

# In[38]:


get_ipython().run_line_magic('sql', 'SELECT RCH, YR, FLOW_INcms,FLOW_OUTcms,EVAPcms FROM rch LIMIT 5')


# ### Renaming a column
# the exmpression is presented as a new column name. It is not that beautiful.
# ***It is quite easy for us to give it a new name using an AS statement (this is known as an alias).***
# 
# ***However, keep in mind that such an operatation does not affect the real data or change the name in the table.It only change the way you see it on your screen.***

# In[41]:


get_ipython().run_line_magic('sql', 'SELECT RCH, YR, FLOW_INcms,FLOW_OUTcms,EVAPcms as EVAP FROM rch LIMIT 5')


# ### Doing some calculations
# Sometimes, we are also intersted in the relationship between columns. 

# #### Math algebra operations
# This can be done with expressions in SELECT Statements. For example, I'd like to see the difference between ***FLOW_OUTcms*** and ***FLOW_INcms*** columns (using the minus operator **-**). You can also try other operators such as +, *, / or %.

# In[44]:


get_ipython().run_cell_magic('sql', 'sqlite://', 'SELECT RCH, YR, FLOW_INcms,FLOW_OUTcms, FLOW_INcms-FLOW_OUTcms \nFROM rch \nWHERE RCH<=5 and YR==1981 \nLIMIT 5')


# #### Taking the round

# In[47]:


get_ipython().run_cell_magic('sql', 'sqlite://', '    SELECT round(FLOW_INcms,2) , round(FLOW_OUTcms,2),  round(FLOW_INcms-FLOW_OUTcms,2)\n    FROM rch\n    LIMIT 5')


# #### Do some statistics 
# Two of the most-used aggregate functions in data analysis are avg() and sum().

# ##### Average

# In[49]:


get_ipython().run_cell_magic('sql', 'sqlite://', '    SELECT round(avg(FLOW_INcms),2), round(avg(FLOW_OUTcms),2) \n    FROM rch')


# ##### Sum

# In[50]:


get_ipython().run_cell_magic('sql', 'sqlite://', '    SELECT round(sum(FLOW_INcms),2), round(sum(FLOW_OUTcms),2)\n    FROM rch')


# ##### Min and Max

# In[51]:


get_ipython().run_cell_magic('sql', 'sqlite://', '    SELECT max(FLOW_INcms), min(FLOW_INcms)\n    FROM rch')


# ### Checking the unique values
# We can use the ***DISTINCT*** keyword in conjunction with SELECT statement to eliminate all the duplicate records and fetching only the unique records.

# In[63]:


get_ipython().run_cell_magic('sql', 'sqlite://', '    SELECT DISTINCT YR\n    FROM rch')


# In[65]:


get_ipython().run_line_magic('sql', 'SELECT COUNT(DISTINCT YR) as Num_years FROM rch')


# ### Grouping by a specific column
# The ***GROUP BY*** clause is an optional clause of the SELECT statement. The GROUP BY clause a selected group of rows into summary rows by values of one or more columns. 
# 
# The GROUP BY clause returns one row for each group. For each group, you can apply an aggregate function such as ***MIN, MAX, SUM, COUNT, or AVG*** to provide more information about each group.
# 
# In the follwing code, we will group all data according to ***YR*** (Year) and ***MO*** (month)

# In[68]:


get_ipython().run_cell_magic('sql', 'sqlite://', '    SELECT YR, MO,FLOW_INcms,FLOW_OUTcms,EVAPcms,TLOSScms\n    FROM rch\n    GROUP BY YR, MO\n    LIMIT 12')


# ### Ording data in Table

# In[73]:


get_ipython().run_cell_magic('sql', 'sqlite://', '    SELECT YR, FLOW_INcms,FLOW_OUTcms,EVAPcms,TLOSScms\n    FROM rch\n    ORDER BY YR\n    LIMIT 5')


# # Exporting a Table in Database to Pandas DataFrame

# In[16]:


df_rch = get_ipython().run_line_magic('sql', 'SELECT * FROM rch')
df_rch=df_rch.DataFrame()
display(df_rch.head(5))


# # EDA with Pandas Profiling

# In[17]:


from pandas_profiling import ProfileReport


# In[24]:


rch_prof=ProfileReport(df_rch)
rch_prof


# In[ ]:




