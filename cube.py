# Cube configuration options: https://cube.dev/docs/config

from cube import config

@config('driver_factory')
def driver_factory(ctx: dict) -> None:
  context = ctx['securityContext']
  data_source = ctx['dataSource']

  return {
    'type': 'bigquery',
    'BQ_PROJECT_ID': 'demo-db-examples.cube.dev',
    'user': 'cube',
    'password': '12345',
    'database': data_source
  }
 
  return {
    'type': 'postgres',
    'host': 'demo-db-examples.cube.dev',
    'user': 'cube',
    'password': '12345',
    'database': data_source
  }