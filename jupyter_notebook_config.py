# Kernel config
c.IPKernelApp.pylab = 'inline'  # if you want plotting support always in your notebook
c = get_config()
c.NotebookApp.ip = '*'
c.NotebookApp.port = 8888
c.NotebookApp.open_browser = False
# password is: demo , see https://ipython.org/ipython-doc/3/notebook/public_server.html 
c.NotebookApp.password = u'sha1:66069c6ecdc5:0b41b8cbdcc98a1876054568b1381bc6da99a1a8'