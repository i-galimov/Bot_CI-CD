#!/bin/bash
kubectl delete services translate-bot resume-bot
kubectl delete deployment translate-bot resume-bot
minikube stop