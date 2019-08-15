class AbstractEtl:
    def extract(self):
        pass
    def transfer(self, data):
        pass
    def load(self, data):
        pass


    def execute(self):
        extactData = self.extract()
        transferData = self.transfer(extactData)
        loadData = self.load(transferData)