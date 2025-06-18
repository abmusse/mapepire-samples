import asyncio
from mapepire_python.pool.pool_job import PoolJob

async def main():
    async with PoolJob("./mapepire.ini") as pool_job:
        async with pool_job.query('select * from SAMPLES.employee') as query:
          res = await query.run(rows_to_fetch=1)

if __name__ == '__main__':
    asyncio.run(main())
