from django.shortcuts import render

from datetime import date

all_posts = [
    {
        "slug":"bottomless-pit",
        "image":"pit.jpg",
        "author":"A.M. Jamal Shengor",
        "date": date(2021,7,21),
        "title":"Bottomless Pit",
        "excerpt":""" 
        Whenever I argue with Mr. Ortaylı, I always learn something new from him. 
        Ortaylı is like a bottomless pit in terms of scientific knowledge.""",
        "content":"""
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
        Aliquam ab vero quibusdam quod ullam itaque dolor, eos vitae excepturi veritatis, 
        aperiam temporibus culpa veniam beatae animi inventore voluptas necessitatibus a.
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
        Aliquam ab vero quibusdam quod ullam itaque dolor, eos vitae excepturi veritatis, 
        aperiam temporibus culpa veniam beatae animi inventore voluptas necessitatibus a.
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
        Aliquam ab vero quibusdam quod ullam itaque dolor, eos vitae excepturi veritatis, 
        aperiam temporibus culpa veniam beatae animi inventore voluptas necessitatibus a.
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
        Aliquam ab vero quibusdam quod ullam itaque dolor, eos vitae excepturi veritatis, 
        aperiam temporibus culpa veniam beatae animi inventore voluptas necessitatibus a.
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
        Aliquam ab vero quibusdam quod ullam itaque dolor, eos vitae excepturi veritatis, 
        aperiam temporibus culpa veniam beatae animi inventore voluptas necessitatibus a."""
    },
    {
        "slug":"conscience-and-fear",
        "image":"fear.jpg",
        "author":"A.M. Jamal Shengor",
        "date": date(2022,6,30),
        "title":"Conscience and Fear",
        "excerpt":""" 
        If you do not do evil because you fear God, it means you are not conscientious but a coward.""",
        "content":"""
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
        Aliquam ab vero quibusdam quod ullam itaque dolor, eos vitae excepturi veritatis, 
        aperiam temporibus culpa veniam beatae animi inventore voluptas necessitatibus a.
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
        Aliquam ab vero quibusdam quod ullam itaque dolor, eos vitae excepturi veritatis, 
        aperiam temporibus culpa veniam beatae animi inventore voluptas necessitatibus a.
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
        Aliquam ab vero quibusdam quod ullam itaque dolor, eos vitae excepturi veritatis, 
        aperiam temporibus culpa veniam beatae animi inventore voluptas necessitatibus a.
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
        Aliquam ab vero quibusdam quod ullam itaque dolor, eos vitae excepturi veritatis, 
        aperiam temporibus culpa veniam beatae animi inventore voluptas necessitatibus a.
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
        Aliquam ab vero quibusdam quod ullam itaque dolor, eos vitae excepturi veritatis, 
        aperiam temporibus culpa veniam beatae animi inventore voluptas necessitatibus a."""
    },
    {
        "slug":"nescience-of-you",
        "image":"education.jpg",
        "author":"A.M. Jamal Shengor",
        "date": date(2023,5,10),
        "title":"Nescience of You!",
        "excerpt":""" 
        You will make education metasori because your nescience is affecting my life.""",
        "content":"""
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
        Aliquam ab vero quibusdam quod ullam itaque dolor, eos vitae excepturi veritatis, 
        aperiam temporibus culpa veniam beatae animi inventore voluptas necessitatibus a.
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
        Aliquam ab vero quibusdam quod ullam itaque dolor, eos vitae excepturi veritatis, 
        aperiam temporibus culpa veniam beatae animi inventore voluptas necessitatibus a.
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
        Aliquam ab vero quibusdam quod ullam itaque dolor, eos vitae excepturi veritatis, 
        aperiam temporibus culpa veniam beatae animi inventore voluptas necessitatibus a.
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
        Aliquam ab vero quibusdam quod ullam itaque dolor, eos vitae excepturi veritatis, 
        aperiam temporibus culpa veniam beatae animi inventore voluptas necessitatibus a.
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
        Aliquam ab vero quibusdam quod ullam itaque dolor, eos vitae excepturi veritatis, 
        aperiam temporibus culpa veniam beatae animi inventore voluptas necessitatibus a."""
    }
]


def get_date(post):
    return post['date']

def starting_page(request):
    sorted_posts = sorted(all_posts,key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html",{
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts" : all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post":identified_post
    })