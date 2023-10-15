#!/bin/bash
kubectl delete services translate-bot resume-bot exxxusebot
kubectl delete deployment translate-bot resume-bot exxxusebot
minikube stop