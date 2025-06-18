from mapepire_python import connect

with connect("./mapepire.ini") as conn:
    with conn.execute("SELECT * FROM SAMPLES.employee WHERE first_name = ? AND department = ?", ("Alice", "Engineering") ) as cursor:
        results = cursor.fetchall()
        print(results)
