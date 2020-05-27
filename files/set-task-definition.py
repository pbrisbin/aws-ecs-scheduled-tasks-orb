import sys
import json
targets = json.loads(sys.stdin.read())
targets['Targets'][0]['EcsParameters']['TaskDefinitionArn'] = '$td_arn'
targets['Rule'] = '$rule'
print(json.dumps(targets))
