from . import community_bp
from flask import render_template, request, abort

@community_bp.route('/')
def show_index():
    if request.method == 'GET':
        title = 'Community'
        # return render_template('community/index.html', title=title)
        return render_template('under-construction.html', title=title)

    else:
        return abort(404)
    
@community_bp.route('/youth')
def show_youth():
    title = 'Youth'
    # return render_template('community/youth.html', title=title)
    return render_template('under-construction.html', title=title)


@community_bp.route('/news')
def show_news():
    title = 'News'
    # return render_template('community/news.html', title=title)
    return render_template('under-construction.html', title=title)


@community_bp.route('/schedule')
def show_schedule():
    title = 'Schedule'
    # return render_template('community/2023.html', title=title)
    return render_template('under-construction.html', title=title)

