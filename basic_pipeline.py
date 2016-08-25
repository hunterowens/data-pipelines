import luigi
import requests


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

if __name__ == '__main__':
    luigi.run()
