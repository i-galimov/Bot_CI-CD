#!/bin/bash
minikube start
kubectl create deployment resume-bot --image phella/resume_bot
kubectl expose deployment resume-bot --type=NodePort --port=8080

kubectl create deployment translate-bot --image phella/translate_bot
kubectl expose deployment translate-bot --type=NodePort --port=8081

kubectl get pod