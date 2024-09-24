# Cube configuration options: https://cube.dev/docs/config

from cube import config

@config('driver_factory')
def driver_factory(ctx: dict) -> None:
  context = ctx['securityContext']
  data_source = ctx['dataSource']

  return {
    'type': 'bigquery',
    'project_id': 'ornate-magnet-376615',
    'key_file': 'wogICJ0eXBlIjogInNlcnZpY2VfYWNjb3VudCIsCiAgInByb2plY3RfaWQiOiAib3JuYXRlLW1hZ25ldC0zNzY2MTUiLAogICJwcml2YXRlX2tleV9pZCI6ICIzYTY3NmI4MTlkYmZkMGQ4ZjA1OGVjMjdjZDNhNjQ2YjIxZjY3NGE5IiwKICAicHJpdmF0ZV9rZXkiOiAiLS0tLS1CRUdJTiBQUklWQVRFIEtFWS0tLS0tXG5NSUlFdmdJQkFEQU5CZ2txaGtpRzl3MEJBUUVGQUFTQ0JLZ3dnZ1NrQWdFQUFvSUJBUURSV0MxMGVnd21KOFIyXG5FQnBWYkdIamcxWTRXTm9aejkwMXp5V3NsSHRaRm52S00xRXhCTENSblRBMDdoNWlZRXlUQml1VVozWUpZeG5DXG5FV1JKZlhPU3R5VzVCNGtsTG5jd1FBaE5yUHUyUlBnQkJzWWs4MEl5aFNUWUg1VmJMclhtVnNYRzdaNjQ2NmRVXG5ySDE1cmdwM20rZzd3MmpUZXRHdXB4UmNpeDI2OFczVi9LOXQrZ0p6Yjg4d05QWTQvalRja0FIK0RoZVo3ajYvXG5MN0VGcnU5RW9CTm4yNFFvcmlRREZoT1NBcUliZ3o4RzdLZHVZYjNSN2xoQnB4VW0rdkI4Sy9CWFNLb2JMSlhaXG5samhxek5YUUhLVlB4dVQ2MDNDdmM3b25rVURnejVLSzZiSXNDWUhTcW5VUEx4dlZPSGQwMVFWWjArSGhCUkZBXG43THlqKzJsTEFnTUJBQUVDZ2dFQURnVjNhZTFBd2c5NHo2V05kZm8vNWpLbVJEampSc1pPM1N0R0xUUjJ2SVZPXG5ma0VJcDUxV1RESjRoNXNKU3ZLRFBuZXoxSWxIZFNKL2w2bDlpNVNNK0o4dXRpRmtsS3B6ampaRHVCd2xjZFJWXG52Zy9ibHA3NmFKTFZZR3BoSVEzVVhoeWl1NHV2elZmdlNiTVI1bVA3VEg2VFErbDNMRzcxKzFveWVXNVI2L0xmXG5ybHZhekp5K0M0dUVtR0hBby8zZTNSRXhzWHRPT3ZrTXMxZlFlNnc2YmRicDJ2a0QwRTNsRDdmeTJXVFQrT2h3XG4rV0laYVlWVmtET3NGZUlRS3VjaEY1ZXlGWTlxMGlkdFFBV2kreEhFMFVvRlFURnBaVlo1RSt3Yi9HNDNHMUpXXG52Y3FaUjZoMkJHUHhOdDU5blExZHVDSE00ZFl2SVJ5N2UvYWtWSlUwaFFLQmdRRHZwY3FvWFA4OTZreDZGNk92XG52U3pVeVlBMXJNREx0SE9jVXdiTlRIbVZLZWJQWXlTR3N4cnZRYWgyTTc0bzBrVnlkcm9ISjhnbmlqR1NwamhzXG5ueXZDS2NJMlQvTEo4VER0Q0dTb0Z5Q0dVYmRnT2l2TGYyVTJHYXUxVnpUSFJXRmFjSGZpU2lOa1haL2hTRjZuXG40NTlJbE1JSzhPYjB2b0ZOTFExYWpMeVd2d0tCZ1FEZm9RdGhkejQwN3NJNFF4ZWxSU3VpcmtBaGl5Q1V3Sk1lXG5nYlZkcE8zMkRQK1BieUVIdElVM2hPdG92aU1JMUZlTi9yMnMzYmwwWFUxcm5Wa2lpajNRNytSZGk3bFpXZElyXG5iaFZzZWdFc2xkSW5FTmZPZDRCbW1DbGNwSnZXcjNBVTdacmxJQjBEbWJwRFhPdXBJVWJuejY5T2g2Z2pnSHBYXG5hZ2pWRHJwOGRRS0JnUUNqV0FBQUxoTVRvcVdwK243cGhDb1FoNS9KOWd3YlRNNFlXVWNqbStLclZ6b3BWVXhLXG5PNzQ2SWlpdkdLbWVyV1FFbHdSSmFFWTNIU3lZNW85RENtTUxIdWR2bWFMRkhvN1lvWVhxUklrNHhHNFhPczhyXG5ENVJ2QWFSV0lEQ3JPcEVXMGQ0RThiK1o0MjdjWVRXVGZjVE45Z2NrNmZxaUMwK2F5UUIzSGNKVmhRS0JnQWE1XG52akRoT0RLNVY0Zi9wSTlvNUNZUlhZWmt1OGNkZjQ4MFVYTU9pY1dUb0gvODFKNTV0R1AyRUdwbkJZQzNlaWFnXG5HYTVBUU5xYUQ4RUR5M0Y1Zk9CeXhvaDFzazVZb0RTRUxBckdKSkRsdEp0T0sxOWZRckpUTXpOQkZCckJ6Zm9qXG5KenhxMmRTSTVBd3dtRG5POFdYNVhnbGJsUmYwUGptd3k3RTByekVkQW9HQkFJNGZJRmRiSS9ZWWdTbHhNM2kvXG5HWGxEQmR6a0FLR0lPb0x4Y0w1MTlGVzZkVGF3OEVHclplVHZaSVZ0NU8rOVUxWWNveGZ6Tko4T3BrRzltZ2JjXG5oK1RPQWljbURCRkVYS3NTL0hyN3ZSNTFNN1IveWU3dHN4VUNvTVhJRHM4T05xZzN6T2twUHlzRlMzWlhIUjg1XG5wTVpyeWRaWFZhRzVKNEp3Z0tRdEtYYVRcbi0tLS0tRU5EIFBSSVZBVEUgS0VZLS0tLS1cbiIsCiAgImNsaWVudF9lbWFpbCI6ICJjdWJlLXRlc3RAb3JuYXRlLW1hZ25ldC0zNzY2MTUuaWFtLmdzZXJ2aWNlYWNjb3VudC5jb20iLAogICJjbGllbnRfaWQiOiAiMTE4NDA0NzE0MzE4NDA4NzkzMzY2IiwKICAiYXV0aF91cmkiOiAiaHR0cHM6Ly9hY2NvdW50cy5nb29nbGUuY29tL28vb2F1dGgyL2F1dGgiLAogICJ0b2tlbl91cmkiOiAiaHR0cHM6Ly9vYXV0aDIuZ29vZ2xlYXBpcy5jb20vdG9rZW4iLAogICJhdXRoX3Byb3ZpZGVyX3g1MDlfY2VydF91cmwiOiAiaHR0cHM6Ly93d3cuZ29vZ2xlYXBpcy5jb20vb2F1dGgyL3YxL2NlcnRzIiwKICAiY2xpZW50X3g1MDlfY2VydF91cmwiOiAiaHR0cHM6Ly93d3cuZ29vZ2xlYXBpcy5jb20vcm9ib3QvdjEvbWV0YWRhdGEveDUwOS9jdWJlLXRlc3QlNDBvcm5hdGUtbWFnbmV0LTM3NjYxNS5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSIsCiAgInVuaXZlcnNlX2RvbWFpbiI6ICJnb29nbGVhcGlzLmNvbSIKfQo',
    'location': 'EU',
    'database': "bigquery_datasource"
  }
 
 
  return {
    'type': 'postgres',
    'host': 'demo-db-examples.cube.dev',
    'user': 'cube',
    'password': '12345',
    'database': data_source
  }