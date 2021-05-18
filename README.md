# prostate_cancer_classifier
Prostate Cancer classification using KNN and Scikit-Learn.

## Use it [here](http://prostatecancerclassifier.herokuapp.com/).

The model uses the K-Nearest-Neighbours algorithm to classify the features array into Benign or Malignant tumours. <br>
The optimum value for neighbours was found to be <b>3</b>, which gave a testing accuracy of <b>93%</b>.

## Test app on your local system
#### Clone the repository<br>
```shell
git clone https://github.com/DeagleOfficial/prostate_cancer_classifier.git
```
#### Create a new virtual environment and activate it
```shell
virtualenv env
.\env\Scripts\activate
```

#### Install the required libraries
```shell
pip install requirements.txt
```

#### Run development server
```shell
flask run
```

#### Run production server
```shell
gunicorn app:app
```
## Note 
This project uses Gunicorn for its production server which supports Unix systems and does not run on Windows. However, you can run the development server on Windows using <code>flask run</code>.
