echo "deploy frontend? yes/no "
read deploy_frontend
echo "deploy backend? yes/no "
read deploy_backend

if [ "$deploy_backend" = "yes" ]; then
	echo "deploying backend"
	kubectl delete deployment taskmanager-deployment
	minikube image rm taskmanager
	sudo docker build . -t taskmanager
	minikube image load taskmanager
fi

if [ "$deploy_frontend" = "yes" ]; then
	echo "deploying frontend"
	kubectl delete deployment frontend-deployment
	minikube image rm frontend-taskmanager
	sudo docker build frontend/taskmanager -t frontend-taskmanager
	minikube image load frontend-taskmanager
fi

kubectl apply -f mysql-deployment.yaml

sleep 25

if [ "$deploy_backend" = "yes" ]; then
	kubectl apply -f taskmanager-deployment.yaml
fi

if [ "$deploy_frontend" = "yes" ]; then
	kubectl apply -f frontend/taskmanager/frontend-deployment.yaml
fi

