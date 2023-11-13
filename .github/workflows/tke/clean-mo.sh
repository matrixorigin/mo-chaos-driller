#!/bin/sh
set -e
ls
uuid=$(cat uuid)
NAMESPACE=chaos-$uuid
# remove mo clusterr
echo "kubectl delete -f mo-cluster.yaml -n $NAMESPACE"
kubectl delete matrixoneclusters.core.matrixorigin.io chaos -n $NAMESPACE
# delete namespace
echo "kubectl delete ns $NAMESPACE"
kubectl delete ns $NAMESPACE