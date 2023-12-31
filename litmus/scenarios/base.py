import os


class Base:
    def __init__(self):
        self.duration = os.getenv('DURATION') or '60'
        self.namespace = os.getenv('NAMESPACE') or open(
            '/var/run/secrets/kubernetes.io/serviceaccount/namespace').read()
        self.label = os.getenv('LABEL') or 'matrixorigin.io/component=CNSet'
        self.all_pods = bool(os.getenv('ALL_PODS')) or False
        self.interval = os.getenv('INTERVAL') or '10'
