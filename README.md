# Container Meetup Guestbook

Make sure you are in a clean state
```bash
kubectl get pods
kubectl get services
kubectl get ds
```
Should return nothing but the `kubernetes` service

Create the guestbook app
```bash
kubectl create -f guestbook/redis-master-controller.yaml
kubectl create -f guestbook/redis-master-service.yaml
kubectl create -f guestbook/frontend-controller.yaml
kubectl create -f guestbook/frontend-service.yaml
```

Install the agent as a DaemonSet
```bash
kubectl create -f ddagent.yaml
```

By now the frontend service should have acquired it's public ip
You can try the guestbook.

You can also "stress test" it by running `python guestbook/guestbookpy/stress.py http://$PUBLIC_IP_OF_THE_FRONTEND_LOAD_BALANCER`
(requires the `requests` library)

Dashboard:
https://app.datadoghq.com/screen/63047/guestbook-monitoring
(org name: remi)
