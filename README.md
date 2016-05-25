# Container Meetup Guestbook


Requirements:
- A kubernetes cluster up and running and kubectl set up


Create the guestbook app
```bash
kubectl create -f guestbook/redis-master-controller.yaml
kubectl create -f guestbook/redis-master-service.yaml
kubectl create -f guestbook/frontend-controller.yaml
kubectl create -f guestbook/frontend-service.yaml
```

Edit ddagent.yaml and set your API Key.
Install the agent as a DaemonSet
```bash
kubectl create -f ddagent.yaml
```

By now the frontend service should have acquired it's public ip
```bash
kubectl get services
```
You can try the guestbook.

You can also "stress test" it by running `python guestbook/guestbookpy/stress.py http://$PUBLIC_IP_OF_THE_FRONTEND_LOAD_BALANCER`
(requires the `requests` library)

Dashboard:
https://app.datadoghq.com/screen/63047/guestbook-monitoring
(org name: remi)
