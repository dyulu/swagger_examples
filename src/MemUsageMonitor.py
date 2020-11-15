import psutil

class MemUsageMonitor:
    MEM_USAGE_THRESHOLD = 80

    def __init__(self):
        self._mem_usage = psutil.virtual_memory().percent
        self._mem_usage_threshold = MemUsageMonitor.MEM_USAGE_THRESHOLD

    def getMemUsage(self):
        mem_usage = {}
        mem_usage['Mem Usage'] = psutil.virtual_memory().percent
        mem_usage['Mem Usage Threshold'] = self._mem_usage_threshold
        if psutil.virtual_memory().percent >= self._mem_usage_threshold:
            mem_usage['Mem Usage Fault'] = True
        else:
            mem_usage['Mem Usage Fault'] = False
        return mem_usage

    def setMemUsageThreshold(self, threshold):
        self._mem_usage_threshold = threshold

    def __str__(self):
        output = "_mem_usage : {}, _mem_usage_threshold : {}".format(self._mem_usage, self._mem_usage_threshold)
        return output

    def __repr__(self):
        return 'MemUsageMonitor'

# pip3 install psutil
if __name__ == '__main__':
    mum = MemUsageMonitor()
    print(mum.getMemUsage())

