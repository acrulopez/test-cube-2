# Cube configuration options: https://cube.dev/docs/config

from cube import config

@config('driver_factory')
def driver_factory(ctx: dict) -> None:
  context = ctx['securityContext']
  data_source = ctx['dataSource']

  print(ctx)

  if ctx['securityContext'].get('merchant_id') == 1:
    return {
      'type': 'bigquery',
      'projectId': 'ornate-magnet-376615',
      'database': data_source
    }
  else:
    return {
      'type': 'bigquery',
      'projectId': 'learn-terraform-378516',
      'location': 'EU',
      'database': data_source
    }

 
 
  return {
    'type': 'postgres',
    'host': 'demo-db-examples.cube.dev',
    'user': 'cube',
    'password': '12345',
    'database': 'bigquery'
  }