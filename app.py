import subprocess
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html')

@app.route('/update', methods=['POST'])
def update_website():
    try:
        # List of Python scripts to run
        scripts_to_run = ['Asperion.py', 'appfoundery.py', 'aimms.py', 'aexus.py', 'adveronline.py', '4vision.py', '6gorrials.py', '4itgroup.py', '5miles.py', 'admisol.py', 'acco_group.py', 'agisko.py','apixa.py', 'apptweak.py', 'wiseman.py','arcadis.py', 'askphil.py', 'asperion.py','atomikos.py','avinity.py', 'regnology.py','bastion.py','bcs.py','craftzing.py','benetworks.py','mediabrands.py','billink.py','kubus.py','birdsai.py']
        
        # Run each Python script using subprocess
        for script in scripts_to_run:
            subprocess.run(['python', script], check=True)
        
        return 'Website updated successfully'
    except subprocess.CalledProcessError:
        return 'Error updating the website'

@app.route('/selenium', methods=['POST'])
def run_selenium_script():
    try:
        subprocess.run(['python', 'test.py'], check=True)
        return 'Selenium script executed successfully'
    except subprocess.CalledProcessError:
        return 'Error running the selenium script'

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)



