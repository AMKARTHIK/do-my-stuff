#!/usr/bin/env python

import requests
import urlparse
from bs4 import BeautifulSoup as bs
from pprint import pprint as pp
import getpass
import readline
import os
from dotenv import load_dotenv

load_dotenv()

readline.set_completer_delims(' \t\n;')
readline.parse_and_bind("tab: complete")
# above line are inspired from
# https://stackoverflow.com/questions/5637124/tab-completion-in-pythons-raw-input

username = 'data'
password = os.environ.get('OLD_LOG_PWD') or getpass.getpass('Please enter the password:')
url = 'https://{0}:{1}@data.sodexis.com/oldlogs'.format(username,password)

def get_available_links(req, url_list):
    return_list = []
    for url in url_list:
        res = req.get(url)
        soup = bs(res.text, 'html.parser')
        # print soup.prettify()
        soup_links = soup.find_all('a')
        available_links = [lnks.get_text() for lnks in soup_links if lnks.get_text() not in ['Parent Directory','modern browsers','powered by h5ai']]
        return_list = return_list + available_links
    return return_list

def get_url(base,new):
    return urlparse.urljoin('{0}/'.format(base), new)


with requests.Session() as req:
    available_servers = get_available_links(req, [url])
    print "\nAvailable server logs\n"
    for index, servers in enumerate(available_servers):
        print "{0}. {1}".format(index + 1, servers)

    server_choosen = int(raw_input("\n\nChoose the server to download the log files: "))
    choosen_server_url = [get_url(url ,available_servers[server_choosen-1])]
    available_log_dir = get_available_links(req, choosen_server_url)
    print "\n\n Available log folders\n"
    for index, log_dir in enumerate(available_log_dir):
        print "{0}. {1}".format(index + 1, log_dir)

    log_folder_choosen = int(raw_input("\n\nChoose the log folder to download the log files: "))
    choosen_log_folder_url = [get_url(choosen_server_url[0], available_log_dir[log_folder_choosen-1])]
    available_log_files = get_available_links(req, choosen_log_folder_url)
    print "\n\nThe list of available logs\n\n"
    for index, files in enumerate(available_log_files):
        print "{0}. {1}".format(index+1, files)

    print "\n\nEnter the range of log files to download."
    start = int(raw_input("\nStart: ")) - 1
    end = int(raw_input("\nEnd: "))
    log_files_to_download = available_log_files[start:end]
    print "\n\nFiles to be downloaded: \n"
    for index, f in enumerate(log_files_to_download):
        print '{0}. {1}'.format(index+1, f)
    print "\n\n"

    folder = raw_input("Enter the path to downlod the files: ")
    if not os.path.isdir(folder):
        os.mkdir(os.path.abspath(folder))

    for file_to_download in log_files_to_download:
        # log_file_download_url = urlparse.urljoin(choosen_log_folder_url[0], file_to_download)
        log_file_download_url = '/'.join((choosen_log_folder_url[0], file_to_download))
        log_file_downloaded = req.get(log_file_download_url)
        with open(os.path.join(os.path.abspath(folder),file_to_download), 'wb') as new_log_file:
            new_log_file.write(log_file_downloaded.content)
