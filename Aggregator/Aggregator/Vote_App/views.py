# WEB3 IMPORT REQUIRED
import json
from web3 import Web3

#DJANGO IMPORT REQUIRED
from .render import Render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect,  HttpResponse
from django.contrib.auth.decorators import login_required


#ROPSTEN ACCOUNT
public_key = "0x4604F4045bb2b2d998dEd660081eb6ebC19C9f1e"
private_key = "5aefce0a2d473f59578fa7dee6a122d6509af1e0f79fcbee700dfcfeddabe4cc"

#CONNECTING TO INFURA
# url = 'https://ropsten.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161'

#CONNECTING TO INFURA
url = 'https://rinkeby.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161'

#INITIATING WEB3
web3 = Web3(Web3.HTTPProvider(url))

#CONTRACT'S ADDRESS AND ABI
address = web3.toChecksumAddress("0x51e8e2F594191ab64db6B9C85cF49800328DEB05")
abi = json.loads('Ballot')

#CREATING A CONTRACT INSTANCE
contract = web3.eth.contract(address=address, abi=abi)

# Create your views here.
