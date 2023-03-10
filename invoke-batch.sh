
exec sam local start-lambda -t handler-template.yaml --host 0.0.0.0 --port 3001

exec aws stepfunctions create-state-machine --endpoint-url http://localhost:8083 --definition file://dispatcher.asl.json --name "SNS-Dispatcher" --role-arn "arn:aws:iam::012345678901:role/DummyRole" \

exec aws stepfunctions start-execution --endpoint-url http://localhost:8083 --state-machine arn:aws:states:ap-south-1:123456789012:stateMachine:SNS-Dispatcher --name test \

exec sam local invoke -e test-event.json -t dispatcher-template.yaml
