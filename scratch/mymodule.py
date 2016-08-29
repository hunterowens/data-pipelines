import luigi

class MyTask(luigi.ExternalTask):

    def run(self):
        f = self.output().open('w')
        print >> f, "Hello World! This is a Luigi Job"
        f.close()

    def output(self):
        return luigi.LocalTarget('/tmp/foo/output.txt')

if __name__ == '__main__':
    luigi.run(MyTask)
