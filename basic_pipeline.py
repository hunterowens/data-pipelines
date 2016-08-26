import luigi
import requests
import pandas as pd 
import geocoder 
class DownloadTask(luigi.ExternalTask):
    """
    Downloads Permit Data from the Portal
    """

    def run(self):
        url = "https://data.cityofchicago.org/api/views/ydr8-5enu/rows.csv?accessType=DOWNLOAD"
        response  = requests.get(url)
        with self.output().open('w') as out_file:
            out_file.write(response.text)
    
    def output(self):
        return luigi.LocalTarget("data/permits.csv") 

class cleanCSV(luigi.Task):
    """This is our cleaning step"""

    def requires(self):
        return DownloadTask


## TODO ## 
class ReverseGeocode(luigi.Task):
    "Pandas integration because we real cool"
    def requires(self):
        return DownloadTask()

    def run(self):
        df = pd.read_csv(self.input().open('r'))
        def reverse 
    
    def output(self):
        pass

## TODO ## 
class MakeWards(luigi.Task):
    pass

## TODO ## 
class MakeMaps(luigi.Task):
    pass

## TODO ## 
class MakePredictions(luigi.Task):
    pass

## TODO ##
class UploadPredictions(luigi.Task):
    pass

## TODO ## 
class LoadCensus(luigi.Task):
    pass


if __name__ == '__main__':
    luigi.run()
