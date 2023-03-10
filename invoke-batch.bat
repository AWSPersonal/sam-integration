
call docker run --name sns-stepfunctions -d -p 8083:8083 --env-file local-credentials.env amazon/aws-stepfunctions-local

call aws stepfunctions create-state-machine --endpoint-url http://localhost:8083 --definition file://dispatcher.asl.json --name "SNS-Dispatcher" --role-arn "arn:aws:iam::012345678901:role/DummyRole"

call aws stepfunctions start-execution --endpoint-url http://localhost:8083 --state-machine arn:aws:states:ap-south-1:123456789012:stateMachine:SNS-Dispatcher --name test

call sam local invoke -e test-event.json -t dispatcher-template.yaml --docker-network sam
