from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from random import choice

from . import util

import markdown2


class SearchForm(forms.Form):
    search_query = forms.CharField(label="",required=False, widget=forms.TextInput (attrs={'placeholder':'Search Encyclopedia'}))


def index(request):
    form = SearchForm()

    entries = util.list_entries()
    return render(request, "encyclopedia/index.html", {
        "entries": entries,
        "form": form
    })


def get_entrypage(request, entry):
    form = SearchForm()

    display = util.get_entry(entry)

    if display == None:
        return render(request, "encyclopedia/error-page.html", {
            "message":"This page does not exist..",
            "form": form
        })
    else:
        return render(request, "encyclopedia/entrypage.html", {
            "title": entry,
            "display": markdown2.markdown(display),
            "form": form
        })


def search_entry(request):

    if request.method == "POST":

        form = SearchForm(request.POST)

        if form.is_valid():

            search_query = form.cleaned_data["search_query"]
            entry_list = util.get_entry(search_query)

            if entry_list is not None:
                return get_entrypage(request, search_query)
            else:
                search_results = []
                for entry in util.list_entries():
                    if search_query.lower() in entry.lower():
                        search_results.append(entry)
                if search_results:
                    return render(request, "encyclopedia/search_results.html", {
                        "search_results": search_results,
                        "form": form
                    })
                else:
                    return render(request, "encyclopedia/error-page.html", {
                        "message": "No search results found..",
                        "form": form
                    })


def new_page(request):
    form = SearchForm()

    if request.method == "GET":
        return render(request, "encyclopedia/newpage.html", {
            "form": form
        })
    else:
        entry = request.POST['title']
        display = request.POST['md_content']
        if util.get_entry(entry) is not None:
            return render(request, "encyclopedia/error-page.html", {
                "message":"This entry already exists..",
                "form": form
            })
        else:
            util.save_entry(entry, display)
            return get_entrypage(request, entry)

def edit_page(request):
    form = SearchForm()

    if request.method == "POST":
        entry = request.POST['title']
        display = util.get_entry(entry)
        return render(request, "encyclopedia/editpage.html", {
            "title": entry,
            "content": display,
            "form": form
        })

def save_page(request):
    form = SearchForm()

    if request.method == "POST":
        entry = request.POST['title']
        display = request.POST['md_content']
        util.save_entry(entry, display)
        return get_entrypage(request, entry)

def random_page(request):
    form = SearchForm()

    entries = util.list_entries()
    entry = choice(entries)
    display = util.get_entry(entry)
    return get_entrypage(request, entry)
