# Cube configuration options: https://cube.dev/docs/config

from cube import config
import os

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

  if ctx['securityContext'].get('tenant_id','null') == '1':
    os.environ["CUBEJS_DB_BQ_CREDENTIALS"] = "ewogICJ0eXBlIjogInNlcnZpY2VfYWNjb3VudCIsCiAgInByb2plY3RfaWQiOiAibGVhcm4tdGVycmFmb3JtLTM3ODUxNiIsCiAgInByaXZhdGVfa2V5X2lkIjogIjBkZmM3OWJmMzU0YmZmYzJiYzJiN2MxZDZmZWRkOWU2MTZmOGY4OTYiLAogICJwcml2YXRlX2tleSI6ICItLS0tLUJFR0lOIFBSSVZBVEUgS0VZLS0tLS1cbk1JSUV2Z0lCQURBTkJna3Foa2lHOXcwQkFRRUZBQVNDQktnd2dnU2tBZ0VBQW9JQkFRREsvaXFYZTlhVW1qL0lcbkdHazFBVHo1RHRWQ05qSnlmN01weEJpQmZ1cHZSM3RrUTVrcjJnWUJxaEI4KzFuNkNpajNuVVpRV1hRc1gwdWpcbnZFWVZsT002Yzl3TTdaaW8wMU9Mc3lUaDRDRzFpTDJtY2hpL0ZVYkpmcWxxZmlNeDBYN1VDdjVMd1FKZmN3c3lcbm9ZQ0FYdHZBOG0rVmxRV1NqTHZpSTJlTWI2QTBZaUs2a3hyaVVOZElJS0J4Vm4wN3JuTnJFR2FVM3FnOVM2RzRcbitXMmxXZnIrbVphSEVkWWRobVpvbEJFcnNEVFZFUWRpTlY2MnVTRTJielVBSjRDR2FCRGpxVDhsdXVCQm9oYzhcbjJWZTkvWkZtVzVrQWRaTDhBVlRXa2hxWDBWL010UzZUZGZ3RC83NXVGMEgwUG9pSnR5SG5hQmplWXFoNjcxejZcbnpML282MjQzQWdNQkFBRUNnZ0VBTHVXN3AxWElCSHNDZzFNSWMyTisxN2VTazRKNzh6SUhqWDJ0ZjdWM3FnL2tcbnRReGRCZUdRQTdCcnNNUk5URlF1bE01MElUb1plZXJtU2NURW1GWFdqWG1ZL0Mra1ZsVEVkNEVDNDJCcHlVdjNcbkxNNHRZM0FoODRsYzBLcWxyT3ZPbG1TWHpaNmcwclo4ZnMwTEtCMUNQZmlFeVJVdHZXYmdQV1dhbGJwd1U4bHlcbjRncFp5ZVdmS2lVNVVUaG5iZXdhb0xKK0NHTkt3ajNmRGIwWVpuM2Y3aUFZZVZ3RkVVeUVvaTNvWnk5eVpaZVVcbkNHbVh6RTlIbVhWaVJYamdlTjFKQ0txTEM5dWVuVnAvbTlRQUU5UXdxbzJQNnVjOVhzNzFwN3pQczFCcC9wTU9cbnNzSEJhVmg4WXJXZlhLcTl3UFRBc3VQR2lnZVExdS9GT2hITHJkd3IrUUtCZ1FEeDNIMXd6RXAvK0htWlYxYlZcbnZ6YldJQko1aUN1ejd2VDdSNmNZUGNobmhxRzNmRXlMN0w0WlBKTEpXYUJxNTdHWnNVZnA0d2VyeXFVeUlJNHJcbnNodDBncE41ZDFSK1RDZnd0Zy9sZkZQcTl0dDczMFp0dHhBN2lraWFDZWpZMUt2dHdOdEZFektJaTZKZ0p1ODlcbnBXNEtLQldwUjhRNHV0c2RPa0RodmNKMDh3S0JnUURXM0FCREdNcHJSQ1lNTjVNeWNnSmQ3UldWbnlwTnRJQlNcbm51Y0FQMDZEU2JWUDhialNVNFNXVFk3Rmd0V21iKzlKSzZySkhSYWVndUttZmZSTHdSUksvSGxxRVlCMm1vdWlcblBDRURXRHJoRTI4WXZoNThvWGprMXFLZGpJbHUweWpWRGxDV21DeEpoekJBbVVocnY2Tk5KZVNwNDdkbEFXSWpcbjVCR3lZaVdDclFLQmdRQ0M0Y2U4SjhGVkdSaHNvN2ZvK1kzcU4vYm5iNG4rMkJ3WWN3RDRmRTZidjE1NkZiaXlcbnE4MS9pS2tDYnc4QmF4cFB5b0RaRDdPU0FwcDgwdU04d0NoZFYyQUpCa3RpQVVKSDM2NGdpTFE4M1pPT3FCZkxcbnZabjZMbTMxZGRGY3JWSFEybUdPTXNKUTVBZGRzeFFhTHhDcVRHRFVkM0szSkY3NHBSS0JWcGdKZ3dLQmdRQ0ZcbkZxTm03RzArQW1tYStiWEk4b3Y2eUVldGRYa0x4dm9SczNJZFdobDFBMnczQitEWEQzcTZhM0k3Yis2TmVScDhcbmRYc0Z0bW56WjltakRiUU1WSjRRVU5HWVhSejQyb1FSeXpNYjBrUXVkUTVGQWtiNkpqOHZhTEF6N1FDWVVGNGpcbmt3bGlMd0tIelNDYmN4ZEQvdUhWZ05waVRiYWs3elZ1Uy9DV1VXc3d4UUtCZ0c4dU41YVk4VzdWNUlqYWdPeG5cblJ5VTNjMEJCMlRvWkVoeFozU1F2RWlsQ3VYMThKcEZENmZFcVp0VVlINkk1Y3d3c0FhVDV0bmI2N1lPYVNxK3dcblRxV3pZV0svRDNJd2E2K0lQaElCbFczNmpYV0p0Y2tEWUVkWkRIVjh1QzNPL2JOdm9DTWEwY213bGVtdzBIQlJcblV0d2x0Y2VTTUEveDdnK202Rk03RTZIMlxuLS0tLS1FTkQgUFJJVkFURSBLRVktLS0tLVxuIiwKICAiY2xpZW50X2VtYWlsIjogImN1YmUtdGVzdEBsZWFybi10ZXJyYWZvcm0tMzc4NTE2LmlhbS5nc2VydmljZWFjY291bnQuY29tIiwKICAiY2xpZW50X2lkIjogIjExMTQ3MzM0NzU0NDU4NDIzMzE5NiIsCiAgImF1dGhfdXJpIjogImh0dHBzOi8vYWNjb3VudHMuZ29vZ2xlLmNvbS9vL29hdXRoMi9hdXRoIiwKICAidG9rZW5fdXJpIjogImh0dHBzOi8vb2F1dGgyLmdvb2dsZWFwaXMuY29tL3Rva2VuIiwKICAiYXV0aF9wcm92aWRlcl94NTA5X2NlcnRfdXJsIjogImh0dHBzOi8vd3d3Lmdvb2dsZWFwaXMuY29tL29hdXRoMi92MS9jZXJ0cyIsCiAgImNsaWVudF94NTA5X2NlcnRfdXJsIjogImh0dHBzOi8vd3d3Lmdvb2dsZWFwaXMuY29tL3JvYm90L3YxL21ldGFkYXRhL3g1MDkvY3ViZS10ZXN0JTQwbGVhcm4tdGVycmFmb3JtLTM3ODUxNi5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSIsCiAgInVuaXZlcnNlX2RvbWFpbiI6ICJnb29nbGVhcGlzLmNvbSIKfQo="
    return {
      'type': 'bigquery',
      'projectId': 'ornate-magnet-376615',
      'location': 'EU',
    }
  else: 
    os.environ["CUBEJS_DB_BQ_CREDENTIALS"] = "ewogICJ0eXBlIjogInNlcnZpY2VfYWNjb3VudCIsCiAgInByb2plY3RfaWQiOiAib3JuYXRlLW1hZ25ldC0zNzY2MTUiLAogICJwcml2YXRlX2tleV9pZCI6ICIzYTY3NmI4MTlkYmZkMGQ4ZjA1OGVjMjdjZDNhNjQ2YjIxZjY3NGE5IiwKICAicHJpdmF0ZV9rZXkiOiAiLS0tLS1CRUdJTiBQUklWQVRFIEtFWS0tLS0tXG5NSUlFdmdJQkFEQU5CZ2txaGtpRzl3MEJBUUVGQUFTQ0JLZ3dnZ1NrQWdFQUFvSUJBUURSV0MxMGVnd21KOFIyXG5FQnBWYkdIamcxWTRXTm9aejkwMXp5V3NsSHRaRm52S00xRXhCTENSblRBMDdoNWlZRXlUQml1VVozWUpZeG5DXG5FV1JKZlhPU3R5VzVCNGtsTG5jd1FBaE5yUHUyUlBnQkJzWWs4MEl5aFNUWUg1VmJMclhtVnNYRzdaNjQ2NmRVXG5ySDE1cmdwM20rZzd3MmpUZXRHdXB4UmNpeDI2OFczVi9LOXQrZ0p6Yjg4d05QWTQvalRja0FIK0RoZVo3ajYvXG5MN0VGcnU5RW9CTm4yNFFvcmlRREZoT1NBcUliZ3o4RzdLZHVZYjNSN2xoQnB4VW0rdkI4Sy9CWFNLb2JMSlhaXG5samhxek5YUUhLVlB4dVQ2MDNDdmM3b25rVURnejVLSzZiSXNDWUhTcW5VUEx4dlZPSGQwMVFWWjArSGhCUkZBXG43THlqKzJsTEFnTUJBQUVDZ2dFQURnVjNhZTFBd2c5NHo2V05kZm8vNWpLbVJEampSc1pPM1N0R0xUUjJ2SVZPXG5ma0VJcDUxV1RESjRoNXNKU3ZLRFBuZXoxSWxIZFNKL2w2bDlpNVNNK0o4dXRpRmtsS3B6ampaRHVCd2xjZFJWXG52Zy9ibHA3NmFKTFZZR3BoSVEzVVhoeWl1NHV2elZmdlNiTVI1bVA3VEg2VFErbDNMRzcxKzFveWVXNVI2L0xmXG5ybHZhekp5K0M0dUVtR0hBby8zZTNSRXhzWHRPT3ZrTXMxZlFlNnc2YmRicDJ2a0QwRTNsRDdmeTJXVFQrT2h3XG4rV0laYVlWVmtET3NGZUlRS3VjaEY1ZXlGWTlxMGlkdFFBV2kreEhFMFVvRlFURnBaVlo1RSt3Yi9HNDNHMUpXXG52Y3FaUjZoMkJHUHhOdDU5blExZHVDSE00ZFl2SVJ5N2UvYWtWSlUwaFFLQmdRRHZwY3FvWFA4OTZreDZGNk92XG52U3pVeVlBMXJNREx0SE9jVXdiTlRIbVZLZWJQWXlTR3N4cnZRYWgyTTc0bzBrVnlkcm9ISjhnbmlqR1NwamhzXG5ueXZDS2NJMlQvTEo4VER0Q0dTb0Z5Q0dVYmRnT2l2TGYyVTJHYXUxVnpUSFJXRmFjSGZpU2lOa1haL2hTRjZuXG40NTlJbE1JSzhPYjB2b0ZOTFExYWpMeVd2d0tCZ1FEZm9RdGhkejQwN3NJNFF4ZWxSU3VpcmtBaGl5Q1V3Sk1lXG5nYlZkcE8zMkRQK1BieUVIdElVM2hPdG92aU1JMUZlTi9yMnMzYmwwWFUxcm5Wa2lpajNRNytSZGk3bFpXZElyXG5iaFZzZWdFc2xkSW5FTmZPZDRCbW1DbGNwSnZXcjNBVTdacmxJQjBEbWJwRFhPdXBJVWJuejY5T2g2Z2pnSHBYXG5hZ2pWRHJwOGRRS0JnUUNqV0FBQUxoTVRvcVdwK243cGhDb1FoNS9KOWd3YlRNNFlXVWNqbStLclZ6b3BWVXhLXG5PNzQ2SWlpdkdLbWVyV1FFbHdSSmFFWTNIU3lZNW85RENtTUxIdWR2bWFMRkhvN1lvWVhxUklrNHhHNFhPczhyXG5ENVJ2QWFSV0lEQ3JPcEVXMGQ0RThiK1o0MjdjWVRXVGZjVE45Z2NrNmZxaUMwK2F5UUIzSGNKVmhRS0JnQWE1XG52akRoT0RLNVY0Zi9wSTlvNUNZUlhZWmt1OGNkZjQ4MFVYTU9pY1dUb0gvODFKNTV0R1AyRUdwbkJZQzNlaWFnXG5HYTVBUU5xYUQ4RUR5M0Y1Zk9CeXhvaDFzazVZb0RTRUxBckdKSkRsdEp0T0sxOWZRckpUTXpOQkZCckJ6Zm9qXG5KenhxMmRTSTVBd3dtRG5POFdYNVhnbGJsUmYwUGptd3k3RTByekVkQW9HQkFJNGZJRmRiSS9ZWWdTbHhNM2kvXG5HWGxEQmR6a0FLR0lPb0x4Y0w1MTlGVzZkVGF3OEVHclplVHZaSVZ0NU8rOVUxWWNveGZ6Tko4T3BrRzltZ2JjXG5oK1RPQWljbURCRkVYS3NTL0hyN3ZSNTFNN1IveWU3dHN4VUNvTVhJRHM4T05xZzN6T2twUHlzRlMzWlhIUjg1XG5wTVpyeWRaWFZhRzVKNEp3Z0tRdEtYYVRcbi0tLS0tRU5EIFBSSVZBVEUgS0VZLS0tLS1cbiIsCiAgImNsaWVudF9lbWFpbCI6ICJjdWJlLXRlc3RAb3JuYXRlLW1hZ25ldC0zNzY2MTUuaWFtLmdzZXJ2aWNlYWNjb3VudC5jb20iLAogICJjbGllbnRfaWQiOiAiMTE4NDA0NzE0MzE4NDA4NzkzMzY2IiwKICAiYXV0aF91cmkiOiAiaHR0cHM6Ly9hY2NvdW50cy5nb29nbGUuY29tL28vb2F1dGgyL2F1dGgiLAogICJ0b2tlbl91cmkiOiAiaHR0cHM6Ly9vYXV0aDIuZ29vZ2xlYXBpcy5jb20vdG9rZW4iLAogICJhdXRoX3Byb3ZpZGVyX3g1MDlfY2VydF91cmwiOiAiaHR0cHM6Ly93d3cuZ29vZ2xlYXBpcy5jb20vb2F1dGgyL3YxL2NlcnRzIiwKICAiY2xpZW50X3g1MDlfY2VydF91cmwiOiAiaHR0cHM6Ly93d3cuZ29vZ2xlYXBpcy5jb20vcm9ib3QvdjEvbWV0YWRhdGEveDUwOS9jdWJlLXRlc3QlNDBvcm5hdGUtbWFnbmV0LTM3NjYxNS5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSIsCiAgInVuaXZlcnNlX2RvbWFpbiI6ICJnb29nbGVhcGlzLmNvbSIKfQo=="
    return {
      'type': 'bigquery',
      'projectId': 'learn-terraform-378516',
      'location': 'EU',
      'database': data_source
    }
