Deploying Machine Learning Model as Web Services using FLASK
-------------------------------------------------------------------
# Author: Arvind Kumar
# Email: arvind.cse@gmail.com
----------------------------------------------

1. Install ANACONDA for python dev. environment
			https://www.anaconda.com/distribution/

2. Open Anaconda command prompt and Install FLASK:
		conda install -c anaconda flask

3. Setup folder structure and prepare your Python code and HTML.
			Main Folder (contains python source files)
			|
			|--> static:   contains HTML pages
			|--> test-images: contains images to identified

4. Open Anaconda command prompt and run following to start web service:
		# Enable Debug mode
		set FLASK_DEBUG=1

		# set main python file containing the code
		set FLASK_APP=akg-sample.py

		# Run FLASK servers
		flask run --host=0.0.0.0
================================================================
Youtube Tutorial video is available as following:

	https://youtu.be/0FM2T6kswY8
	
