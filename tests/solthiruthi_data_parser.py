# -*- coding: utf-8 -*-
# (C) 2015 Muthiah Annamalai

# setup the paths
from opentamiltests import *
from solthiruthi.data_parser import *
from solthiruthi.solthiruthi import Solthiruthi
import sys

class CmdLineIO(unittest.TestCase):
    def test_CLI_interface_help(self):
        return
        # find a way to run this test which exits the suite
        _,parser = Solthiruthi.get_CLI_options(do_parse=False)
        args = parser.parse_args(['--help'])
        self.assertEqual(args.help,True)
    def test_CLI_defaults(self):
        _,parser = Solthiruthi.get_CLI_options(do_parse=False)
        args = parser.parse_args( ['-stdin'])
        self.assertEqual(args.files,'')
        self.assertEqual(args.help,False)
        self.assertEqual(args.nalt,10)
        self.assertEqual(args.Dictionary,['std'])
        self.assertEqual(args.dialects,['std'])
        
    def test_CLI_files(self):
        ips = ['-files','poonga','vanam','sethu','ezhuthu']
        _,parser = Solthiruthi.get_CLI_options(do_parse=False)
        args = parser.parse_args( ips )
        self.assertEqual(args.files,ips[1:])

    def test_CLI_dicts(self):
        ips = ['-Dict','std','wikipedia','madurai']
        _,parser = Solthiruthi.get_CLI_options(do_parse=False)
        args = parser.parse_args( ips )
        self.assertEqual(args.Dictionary,ips[1:])

class DataParserTest(unittest.TestCase):
    def test_worlists(self):
        obj = DataParser.run(["data/maligaiporul.txt",\
                              "data/vilangugal.txt"])
        r = obj.analysis()
        self.assertEqual(r['catlen'],5)
        #self.assertEqual(r['total'],141)
        self.assertEqual(sorted(list(map(len,r['dict'].values()))),sorted([56,28,15,8,3]))

if __name__ == "__main__":
    unittest.main()
