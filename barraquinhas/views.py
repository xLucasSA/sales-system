from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .models import Produtos
from .forms import *
from django.utils.timezone import now as dateNow
import datetime
from django.db.models import Q
