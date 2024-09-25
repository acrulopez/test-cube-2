# Cube configuration options: https://cube.dev/docs/config

from cube import config

@config('context_to_app_id')
def context_to_app_id(ctx: dict) -> str:
  return f"CUBE_APP_{ctx['securityContext'].get('tenant_id','null')}"
 
@config('context_to_orchestrator_id')
def context_to_orchestrator_id(ctx: dict) -> str:
  return f"CUBE_APP_{ctx['securityContext'].get('tenant_id','null')}"

@config('driver_factory')
def driver_factory(ctx: dict) -> None:
  context = ctx['securityContext']
  data_source = ctx['dataSource']


  print(ctx)

  if ctx['securityContext']['tenant_id'] == '1':
    return {
      'type': 'bigquery',
      'projectId': 'ornate-magnet-376615',
      'location': 'EU',
      'database': data_source
    }
  else:
    return {
      'type': 'bigquery',
      'projectId': 'learn-terraform-378516',
      'location': 'EU',
      'database': data_source
    }
