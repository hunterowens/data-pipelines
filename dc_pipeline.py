import pandas as pd
import requests
import folium
import luigi

YEARS = {2012: 'http://opendata.dc.gov/datasets/5f4ea2f25c9a45b29e15e53072126739_7.csv',
         2013: 'http://opendata.dc.gov/datasets/4911fcf3527246ae9bf81b5553a48c4d_6.csv',
         2014: 'http://opendata.dc.gov/datasets/d4891ca6951947538f6707a6b07ae225_5.csv',
         2015: 'http://opendata.dc.gov/datasets/981c105beef74af38cc4090992661264_25.csv',
         2016: 'http://opendata.dc.gov/datasets/5d14ae7dcd1544878c54e61edda489c3_24.csv'}

class DownloadTask(luigi.ExternalTask):
    """
    downloads data from the portal.
    """
    
    year = luigi.IntParameter(default=2012)

    def run(self):
        pass

    def output(self):
        return luigi.LocalTarget('./data/permits-dc-%s.csv' % str(self.year))


class cleanCSV(luigi.Task):
    """
    cleans a CSV into the format we'd like for analysis.

    you'll want to grab the Ward, Fees, Permit, and Geospacial fees. 
    """
    def requires(self):
        return DownloadTask(self.param)

    def run(self):
        pass

    def output(self):
        pass


class mergeDatasets(luigi.Task):
    """
    merges the datasets
    """
    def requires(self):
        return [cleanCSV(year) for year in range(2012,2017)]

    def run(self):
        pass

    def output(self):
        pass

class importIntoPandasDF(luigi.Task):
    """
    converts the CSVs into pandas dataframes, saves as pickle file. 
    """
    def requires(self):
        return mergeDatasets

    def run(self):
        pass

    def output(self):
        pass

class computeWards(luigi.Task):
    """
    compute the development by ward per year and save. 

    Basically, you'll want to value_counts() on the ward field.

    How many permits per ward were issued
    """
    
    def requires(self):
        return importIntoPandasDF()

    def run(self):
        pass

    def output(self):
        pass

class makeMap(luigi.Task):
    """
    make a map of development
    """
    
    def requires(self):
        return importIntoPandasDF()

    def run(self):
        """
        We're gonna use Folium to make a map. 
        I'm giving you some basic code here to get a map object and show you 
        how to plot a marker. 
        """
        # make a map
        map= folium.Map(location=[38.9072, -77.0369],
                           zoom_start=12)
        # add a marker
        folium.Marker([45.3288, -121.6625], popup='Mt. Hood Meadows').add_to(map)
        pass

    def output(self):
        pass

class makePredictions(luigi.Task):
    """
    Make predictions for given next years number of ward development, 
    Given the ward sums, predict the values using a simple regression.

    NB: This is not good modeling, but I'm trying to demostrate plumbing here. 
    """

    def requires(self):
        return computeWards()

    def run(self):
        ## Here's the basic skeleton of how do do a linear regression
        from sklearn.linear_model import LinearRegression
        data = np.asarray(df)
        lr = LinearRegression()
        X, y = data[:, 1], data[:, 0] ## THIS DEPENDS ON HOW YOU SHAPE YOUR DATA - X should be years, y should be counts
        lr.fit(X, y)
        lr.predict(2017)

        pass

    def output(self):
        pass

class makeReport(luigi.Task):
    """
    Gathers info and saves to report 
    """

    def requires(self):
        return makePredictions(), makeMap() 

    def run(self):
        pass

    def output(self):
        pass

if __name__ == '__main__':
    luigi.run(['DownloadTask', '--local-scheduler'])
