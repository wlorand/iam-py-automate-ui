# iam-py-automate-ui

**Python Selenium scripts that perform browser automation tasks for the DG2 / mydata project.**<br />
While these scripts are designed to be deployed to AppDyanmics, <br />
please follow the instructions below to get the scripts running locally from the command line

## Running Scripts Locally

These instructions assume you have [Homebrew](https://brew.sh/) running on a Mac.

1. Install Python3 & PIP3 package manager via Homebrew (or use Anaconda PY distribution)
<pre><code>$ brew install python</code></pre>
2. Use PIP or conda to install the Selenium package
<pre>
<code>$ pip install selenium</code>
<code>$ conda install selenium</code>
</pre>

3. Download Browser Drivers and make them accessible to your $PATH<br />
    3.1- Download and unzip [geckodriver](https://github.com/mozilla/geckodriver/releases/tag/v0.26.0)  
    3.2- Download and unzip [chromedriver](https://chromedriver.chromium.org/downloads) based on your chrome version<br />
    3.3- place the unix .exe files in /usr/local/bin and confirm this dir in your $PATH via
   <pre><code>$ echo $PATH</code></pre>
4. Run any of the available scripts here via the command line (with only one driver uncommented)
   <pre><code>\$ python3 iam_auth_login_prod.py</code></pre>

## AppDyanmics Deployment Note

AppDynamics includes its own browser drivers, so the browser driver code in these scripts
should be commented out before deployment
