Travesty – A directory and file enumeration tool (post directory traversal exploitation)

This tool assists security analysts in identifying interesting directories and files once a directory traversal has been found.

Blog post at: https://blog.telspace.co.za/2019/11/travesty-directory-and-file-enumeration.html

usage: travesty-v1.0.py [-h] -t TRAVERSAL -o OUTPUT

This is a public release Travesty script - Telspace Systems

optional arguments:
  -h, --help            show this help message and exit
  -t TRAVERSAL, --traversal TRAVERSAL
                        Traversal URL - in full - i.e.
                        https://www.domain.com/../../../../
  -o OUTPUT, --output OUTPUT
                        Output file name
