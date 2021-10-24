## About TaskManager

TaskManager is an application that allows you to create lists and add tasks to that list which you can then mark as done when it's done. It is written primarily for demonstrating microservice architecture and kubernetes. It can be used as a _sample or reference_ project for building similar projects. The backend is written in *Python* using the *Flask* lightweight web framework. It uses *Flask-SQLAlchemy* for the ORM and it uses *Alembic* migration tool which is built on top of SQLAlchemy. The UI is written in *Vue.js* and the state management is handled using *Vuex*. The router is handled using *vue-router*. 

## Screenshots

- Creating a list

[![create_list.gif](https://s1.gifyu.com/images/create_list.gif)](https://gifyu.com/image/eIPA)

- Deleting a list

[![delete_list.gif](https://s1.gifyu.com/images/delete_list.gif)](https://gifyu.com/image/eIXI)

## Installation

- Install docker if you don't already have it.
- Install minikube if you don't already have it.
- run ```minikube start``` to start the cluster
- run ```minikube ip``` to get the node's IP address
- open `/etc/hosts` file and add an entry ```{minikube_ip} taskmanagerbackend```. Replace `{minikube_ip}` with the ip we found with ```minikube ip``` command
- clone the repository
- run ```sh deploy.sh``` and it should deploy the application to minikube
- to access the application, go to `http://taskmanagerbackend:8080`

## If the installation steps didn't work

Please create an issue on the repository
