import os.path
from RepoFilter import RepoFilter
import platform
import xml.etree.ElementTree as et

class RepoAnalyzerJavaNcss(RepoFilter):
    def __init__(self):
        super().__init__()
        self.source = 'javancss'

    def execute_impl(self):
        folder = f'../tmp/{self.name}'
        s = os.sep
        ncss_exec = f'.{s}..{s}bin{s}javancss{s}bin{s}'
        if platform.system() == 'Linux':
            ncss_exec += 'javancss'
        else:
            ncss_exec += 'javancss.bat'

        cmd = f'{ncss_exec} -package -xml -out ../data/ncss/{self.name}.xml {folder}'
        print(cmd)
        os.system(cmd)

    def getMetricResults(self):
        outfile = f'../data/ncss/{self.name}.xml'
        # create element tree object
        tree = et.parse(outfile)

        # get root element
        root = tree.getroot()
        # create empty list for news items
        totals = {}

        # iterate news items
        for item in root.findall('./packages/total'):
            for child in item:
                totals[child.tag] = child.text

        # return news items list
        return totals
