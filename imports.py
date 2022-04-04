from flask import Flask, render_template
from flask_ngrok import run_with_ngrok
import requests
from bs4 import BeautifulSoup
import sqlite3