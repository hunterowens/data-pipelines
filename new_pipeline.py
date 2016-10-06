import pandas as pd 

YEARS = {2012: 'http://opendata.dc.gov/datasets/5f4ea2f25c9a45b29e15e53072126739_7.csv',
         2013: 'http://opendata.dc.gov/datasets/4911fcf3527246ae9bf81b5553a48c4d_6.csv',
         2014: 'http://opendata.dc.gov/datasets/d4891ca6951947538f6707a6b07ae225_5.csv',
         2015: 'http://opendata.dc.gov/datasets/981c105beef74af38cc4090992661264_25.csv',
         2016: 'http://opendata.dc.gov/datasets/5d14ae7dcd1544878c54e61edda489c3_24.csv'}

class DownloadTask(luigi.ExternalTask):
    """
    downloads data from the portal.
    """

    url = luigi.Parameter()

    def run(self):
        pass

    def output(self):
        pass


class cleanCSV(luigi.Task):
    """
    cleans a CSV into the format we'd like for analysis. 
    """
    def requires(self):
        pass

    def run(self):
        pass

    def output(self):
        pass


class mergeDatasets(luigi.Task):
    """
    merges the datasets
    """
    def requires(self):
        pass

    def run(self):
        pass

    def output(self):
        pass

class importIntoPandasDF(luigi.Task):
    """
    converts the CSVs into pandas dataframes, saves as pickle file. 
    """
    def requires(self):
        pass

    def run(self):
        pass

    def output(self):
        pass

class computeWards(luigi.Task):
    """
    compute the development by ward per year and save. 
    """
    
    def requires(self):
        pass

    def run(self):
        pass

    def output(self):
        pass

class makeMap(luigi.Task):
    """
    make a map of development
    """
    
    def requires(self):
        pass

    def run(self):
        pass

    def output(self):
        pass

class MakePredictions(luigi.Task):
    """Make predictions for given"""

    def requires(self):
        pass

    def run(self):
        pass

    def output(self):
        pass

class makeReport(luigi.Task):
    """
    Gathers info and saves to report 
    """

    def requires(self):
        pass

    def run(self):
        pass

    def output(self):
        pass

if __name__ == '__main__':
    luigi.run(['task_name', '--local-scheduler']
              )
