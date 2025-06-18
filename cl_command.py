from mapepire_python.client.sql_job import SQLJob
from mapepire_python.data_types import QueryOptions


with SQLJob("./mapepire.ini") as sql_job:
    opts = QueryOptions(isClCommand=True)
    with sql_job.query("WRKACTJOB", opts=opts) as query:
        result = query.run(rows_to_fetch=1)
        print(result)
