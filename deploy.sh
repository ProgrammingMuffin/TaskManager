kubectl delete deployments taskmanager-deployment mysql-deployment

minikube image rm taskmanager

sudo docker build . -t taskmanager

minikube image load taskmanager

kubectl apply -f mysql-deployment.yaml

sleep 25

kubectl apply -f taskmanager-deployment.yaml
