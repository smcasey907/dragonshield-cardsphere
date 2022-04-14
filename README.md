<p align="center">
  <a href="" rel="noopener">
 <img width=110px height=70px src="https://www.dragonshield.com/storage/2021/04/DS-Logo.png" alt="Dragonshield logo">
 <img width=70px height=70px src="https://www.cardsphere.com/static/img/logo-color-small.svg" alt="Cardsphere logo"></a>
</p>

<h3 align="center">Dragon Shield MTG Card Manager Export => Cardsphere Collection Import</h3>

<div align="center">

</div>

---

<p align="center"> A scripting tool created to import card collections from Dragon Shield Card Manager to Cardsphere's "Haves"
    <br> 
</p>

## Table of Contents

- [This Project](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## This Project <a name = "about"></a>

I really like Dragon Shield's Card Manager and scanner. The insights provided by Dragon Shield are super helpful as well. If you are not familiar with the Dragon Shield App, check out [Dragon Shield Scanner](https://www.dragonshield.com/digital-card-manager/).

I also have been a huge fan of Cardsphere once I've discovered it. I don't get the chance to go to my LGS and trade frequently, and sometimes we just end up with cards that we really have a hard time trading away. Cardsphere is a web platform that allows users to post their collection for trade while also allowing me to create a wants list to receive cards from other users. Check out [Cardsphere](https://www.cardsphere.com/).

Recently, I revamped a lot of my decks, created several new decks, and totally disrupted my collection on Cardsphere. So I now have to start over. I used Dragon Shield to scan my binders, but I found that Cardsphere didn't like the CSV format that Dragon Shield exported. With the help of the Cardsphere devs and community, and a useful API tool at [Multiverse Bridge](https://www.multiversebridge.com/), I was able to convert Dragon Shield's export CSV files to a format that Cardsphere liked. 

<br>

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

You'll need to do a little setup in order to get this project running for the first time. I hope to have executable files in a future update, but I'm not there yet and I want to get this out for people to use.

You'll need Python 3: 
Click [here](https://www.python.org/downloads/) and download the latest version for your OS. Once downloaded, double-click the installation package.

#### <u>For Windows:</u>
A window will pop up asking to install Python 3. <b>Make sure you click []Add Python 3.x to PATH</b>, or else you will not be able to run the script.
<center><img height="300px" src="https://miro.medium.com/max/1344/0*7nOyowsPsGI19pZT.png"></center>

Once installation is done, open command prompt by typing `ctrl + R` and type `cmd`.

You'll need to add a Python Library for making requests to the API. To add the library, type:
```
python -m pip install requests
```

This will install the required library so that the converter tool will work.

<br>

#### <u>For MacOS</u>
A window will pop up and walk you through the installation of Python. Once installation is complete, Finder will pop up within the Python 3.x folder. If it doesn't you can simply navigate to your Python 3 folder within the Applications Folder. Here, you will find a fill that will set Python to your PATH. Double-click the file labeled `Update Shell Profile.command`. A Command Shell will pop up and run the script, setting Python to your PATH.

Once installation is complete, you'll need to add a Python Library for making requests to the API. To add the Library, open a terminal session and type:
```
pip install requests
```
This will install the required library so that the converter tool will work.

<br>

### Installing
- Navigate to the [github repository](https://github.com/smcasey907/dragonshield-cardsphere) for this project (if you're not already here).
- Click the dropdown under <i>Code</i>.
- Select `Download ZIP` from the options (see image, instructions continue after image):
<center><img height="300px" src="https://i.imgur.com/zlOfoo7.png"></center>

- Extract the zip file to a location you'll remember.
- Navigate to your collection in [Dragon Shield Web Portal](https://mtg.dragonshield.com/). Make sure you're logged in.
- In the folders tab, you'll see a list of your folder collection. Click the download icon to the right of the folder you'd like to download or the Export button at the top of the list. Your .csv file will be saved in your Downloads folder. 
- <span style="color:red"><b>Important!</span> Do not edit your .csv file. The output from Dragon Shield is very specific, and many csv readers will create their own formating on save as there is no universal format rules for csv files.</b>
- Move the csv file (or files...the tool can process many csv files at once) into the `dragonshield-cardsphere-main` (not the `app` folder or `import-to-cardsphere` folder within that folder)

You are now ready to run the converter.

#### <u>For Windows</u>
- In the `dragonshield-cardsphere-main` folder, right click on the file labeled `win_ds-cs` or `win_ds-cs.ps1` (if your file manager is showing file extensions).
- Select `Run With PowerShell` from the dropdown options.
- A PowerShell window will pop up and begin running the converter. When completed, you will find the Cardsphere .csv files in the `import-to-cardsphere` folder. If this is the case, [go to this step](#import_to_cardsphere)...otherwise, continue reading.

If you get a message like this:
```
.\win_ds-cs.ps1 : File C:\dragonshield-cardsphere-main\win_ds-cs.ps1 cannot be loaded 
because running scripts is disabled on this system. For more information, see 
about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:1
+ .\win_ds-cs.ps1
+ ~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```
...you have two options. Option one is to change the execution policy on your computer or run the command in a command shell.

To change the execution policy, hit the windows key and type `PowerShell`. Select `Run as Administrator`. Type this command in the prompt:
```
Set-ExecutionPolicy -ExectutionPolicy RemoteSigned -Scope LocalMachine
```
Run the script again and it should work.

The other option is to hit `ctrl+r` and type `cmd`. This will open a command prompt. Navigate to the extracted folder `dragonshield-cardsphere-main` and type the command `./win_ds-cs.ps1`. This should work as well.

<br>

#### <u>For MacOS</u>


<br>

### <b>Importing to Cardsphere</b> <a name="import_to_cardsphere"></a>
## Usage <a name="usage"></a>

Add notes about how to use the system.

## Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/) - Scripting Language
- [Multiverse Bridge](https://expressjs.com/) - API
- [Dragon Shield Digital Card Manager](https://www.dragonshield.com/digital-card-manager/) - Digital Card Manager
- [Cardsphere](https://www.cardsphere.com) - MTG Card Trading Platform
- [Google](https://google.com/) - Endless Knowledge Database and random rabbit holes

##  Author <a name = "authors"></a>

- [@smcasey907](https://github.com/smcasey907) - Idea & Initial work <br>
<a href="https://www.buymeacoffee.com/smcasey907" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

## Acknowledgements <a name = "acknowledgement"></a>

- @gunhoe86 - Discord User and Contributor to Multiverse Bridge...reached out with the API information I needed for my project
- @Bodey & @Michael ʕ •ᴥ•ʔ on the Cardsphere Discord channel who helped with some of the Cardsphere functionality under the hood
