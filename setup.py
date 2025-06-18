from mapepire_python.client.sql_job import SQLJob


with SQLJob("./mapepire.ini") as sql_job:
    create_schema_sql = "CREATE SCHEMA SAMPLES"

    create_table_sql = """
      CREATE TABLE SAMPLES.employee (
      id INT PRIMARY KEY,
      first_name VARCHAR(50),
      last_name VARCHAR(50),
      email VARCHAR(100),
      department VARCHAR(50),
      salary DECIMAL(10, 2),
      hire_date DATE)
      """

    insert_sql = """
     INSERT INTO SAMPLES.employee (id, first_name, last_name, email, department, salary, hire_date)
     VALUES 
     (1, 'Alice', 'Johnson', 'alice.johnson@example.com', 'Engineering', 85000.00, '2022-03-01'),
     (2, 'Bob', 'Smith', 'bob.smith@example.com', 'Marketing', 65000.00, '2021-06-15'),
     (3, 'Clara', 'Davis', 'clara.davis@example.com', 'HR', 60000.00, '2020-09-20'),
     (4, 'Daniel', 'Lee', 'daniel.lee@example.com', 'Engineering', 90000.00, '2019-01-10'),
     (5, 'Eva', 'Martinez', 'eva.martinez@example.com', 'Finance', 72000.00, '2023-05-12')
     """

    create_schema_results = sql_job.query_and_run(create_schema_sql)
    print(create_schema_results)
    
    create_table_results = sql_job.query_and_run(create_table_sql)
    print(create_table_results)

    insert_results = sql_job.query_and_run(insert_sql)
    print(insert_results)
    
