import subprocess
from subprocess import Popen, PIPE
import json


json_file = 'webhook_tag.json'
pipeline_name = "CP-permissions-test0"
# Get webhooks list
cmd_get_webhook = 'aws codepipeline list-webhooks --region eu-west-2'

cmd = Popen(cmd_get_webhook, shell=True, stdout=PIPE)
output = cmd.communicate()[0]

webhooks = json.loads(output)

cmd_set_webhook = 'aws codepipeline put-webhook --webhook {} --region eu-west-2'

# Read filter definition to be set
with open('webhook_tag.json', 'r') as fr:
    filters = fr.read()

# Find Pipeline name
data = None
for hook in webhooks['webhooks']:
    if hook['definition']['targetPipeline'] == pipeline_name:
        hook['definition']['filters'] = json.loads(filters)
        data = hook['definition']
        break

assert data!=None, 'Pipeline name was not found'

# Set the new filter
cmd_set_webhook = cmd_set_webhook.
                  format( '"' + str(data)[1:-1].
                  replace("'","").
                  replace(':','=') + '"') # Delete spaces and quotation mark
cmd = Popen(cmd_set_webhook, shell=True, stdout=PIPE)
output = cmd.communicate()[0]
response = json.loads(output)
print('*'*30)
print('RESULTS:')
print('*'*30)
print('Expected filters:')
print(json.loads(filters))
print('Read filters:')
print(response['webhook']['definition']['filters'])

# Validate that filters were set correctly
assert response['webhook']['definition']['filters']==json.loads(filters), 'Filters don not match'
print('Token:',response['webhook']['definition']['authenticationConfiguration']['SecretToken'])
print('URL:',response['webhook']['url'])
print('*'*30)
