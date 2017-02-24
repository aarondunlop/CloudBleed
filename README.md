This project is in response to the silly-named, but quite scary CloudFront CDN breach currently unfolding. While it is very possible that your data is secure and you are not affected the sites listed here: https://github.com/pirate/sites-using-cloudflare were verified to have exposed sensitive data including passwords, logins, personal information, etc.

As always when something like this comes about, change your passwords. This one is difficult because CloudFront is a massive player in this space so many, many sites were affected. To do a quick sweep I exported my Chrome password file, then wrote this script to dump out anything I had affected. 

To export Chrome passwords:

1. Open Chrome://flags in your Chrome.
2. Find Password Import and Export option, select Enabled from the drop-down box, and then restart the Chrome browser.
3. Now, open Chrome://settings/passwords page.
4. Click on Export button to export/backup saved passwords.' 

Steps from: www.intowindows.com/how-to-backup-saved-passwords-in-google-chrome-browser/

Requirements:

1. OSX, or Linux environments.
2. Python 2.7 or later.
3. Existing /tmp/password.csv from the above steps.
4. check.py from this project existing in /tmp/check.py

Download check.py from here, and run it. It will download, unzip, and compare only the website name (with a little formatting) against the affected list. This password file should be *deleted* as soon as you are done, and if in doubt - change extra passwords. Don't trust that the master list is valid, or that my novice attempts to deal with this didn't miss something important.
